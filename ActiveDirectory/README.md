## Install the required Ansible Module ##
- pip install --upgrade ansible
- ansible-galaxy collection install ansible.windows --force
- ansible-galaxy collection list | grep ansible.windows
