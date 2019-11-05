SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE IF NOT EXISTS `servers` (
  `sn` int(10) NOT NULL AUTO_INCREMENT,
  `servname` varchar(255) NOT NULL,
  `ip` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `env` varchar(255) NOT NULL,
  `remarks` varchar(255) NOT NULL,
  PRIMARY KEY (`sn`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;


--
-- Dumping data for table `servers`
--

INSERT INTO `servers` (`sn`, `servname`, `ip`, `location`, `env`, `remarks`) VALUES
(1, 'ansible-master.techarkit.local', '192.168.2.200', 'India', 'Development', 'Ansible Development Master'),
(2, 'node2.techarkit.local', '192.168.2.201', 'India', 'Development', 'Ansible Node'),
(3, 'node3.techarkit.local', '192.168.2.202', 'India', 'Development', 'Ansible Node');
