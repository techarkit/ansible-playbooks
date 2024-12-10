#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl


def connect_to_vcenter(vcenter_ip, username, password):
    """Connect to vCenter"""
    context = ssl._create_unverified_context()
    si = SmartConnect(host=vcenter_ip, user=username, pwd=password, sslContext=context)
    return si


def find_vm(si, vm_name):
    """Find VM by name"""
    content = si.RetrieveContent()
    container = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    for vm in container.view:
        if vm.name == vm_name:
            return vm
    return None


def execute_script_on_vm(si, vm, guest_username, guest_password, script_path):
    """Execute script on VM using Guest Operations"""
    guest_ops_manager = si.content.guestOperationsManager

    creds = vim.vm.guest.NamePasswordAuthentication(
        username=guest_username,
        password=guest_password
    )

    spec = vim.vm.guest.ProcessManager.ProgramSpec(
        programPath="C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
        arguments=f"-ExecutionPolicy Bypass -File {script_path}"
    )

    process_manager = guest_ops_manager.processManager
    pid = process_manager.StartProgramInGuest(vm, creds, spec)
    return pid


def main():
    # Define module arguments
    module_args = dict(
        vcenter_ip=dict(type='str', required=False),  # Accept vcenter_ip
        vcenter_hostname=dict(type='str', required=False),  # Accept vcenter_hostname as an alternative
        vcenter_username=dict(type='str', required=True),
        vcenter_password=dict(type='str', required=True, no_log=True),
        vm_name=dict(type='str', required=True),
        guest_username=dict(type='str', required=True),
        guest_password=dict(type='str', required=True, no_log=True),
        script_path=dict(type='str', required=True)
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    # Extract parameters
    vcenter_ip = module.params.get('vcenter_ip') or module.params.get('vcenter_hostname')
    vcenter_username = module.params['vcenter_username']
    vcenter_password = module.params['vcenter_password']
    vm_name = module.params['vm_name']
    guest_username = module.params['guest_username']
    guest_password = module.params['guest_password']
    script_path = module.params['script_path']

    if not vcenter_ip:
        module.fail_json(msg="Either 'vcenter_ip' or 'vcenter_hostname' must be provided.")

    try:
        # Connect to vCenter
        si = connect_to_vcenter(vcenter_ip, vcenter_username, vcenter_password)

        # Find VM
        vm = find_vm(si, vm_name)
        if not vm:
            module.fail_json(msg=f"VM '{vm_name}' not found in vCenter.")

        # Execute script on VM
        pid = execute_script_on_vm(si, vm, guest_username, guest_password, script_path)

        # Success
        module.exit_json(changed=True, msg=f"Script executed successfully with PID: {pid}")

    except Exception as e:
        module.fail_json(msg=f"Failed to execute script: {str(e)}")

    finally:
        if 'si' in locals():
            Disconnect(si)


if __name__ == '__main__':
    main()
