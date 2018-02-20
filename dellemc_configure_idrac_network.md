# dellemc_configure_idrac_network
Configures the iDRAC network attributes

  * [Synopsis](#Synopsis)
  * [Options](#Options)
  * [Examples](#Examples)
  * [Return Values](#Return-Values)

## <a name="Synopsis"></a>Synopsis
This module is responsible for configuring the iDRAC network attributes

## <a name="Options"></a>Options

| Parameter             | required      | default   | choices                                                                                         | comments                                                                               |
| -------------         | ------------- | --------- | -----------                                                                                     | ---------                                                                              |
| idrac_ip              | Yes           | NA        | NA                                                                                              | iDRAC IP Address                                                                       |
| idrac_user            | Yes           | NA        | NA                                                                                              | iDRAC user name                                                                        |
| idrac_pwd             | Yes           | NA        | NA                                                                                              | iDRAC user password                                                                    |
| idrac_port            | No            | 443       | NA                                                                                              | iDRAC port                                                                             |
| share_name            | Yes           | NA        | NA                                                                                              | CIFS or NFS Network share                                                              |
| share_user            | Yes           | NA        | NA                                                                                              | Network share user in the format 'user@domain' if user is part of a domain else 'user' |
| share_pwd             | Yes           | NA        | NA                                                                                              | Network share user password                                                            |
| share_mnt             | Yes           | NA        | NA                                                                                              | Local mount path of the network share with read-write permission for ansible user      |
| setup_idrac_nic_vlan  | No            | NA        | NA                                                                                              | Configuring the VLAN-related setting for iDRAC                                         |
| register_idrac_on_dns | No            | NA        | <ul> <li>Enabled</li> <li>Disabled</li> </ul>                                                   | Registering Domain Name System for iDRAC                                               |
| dns_idrac_name        | No            | NA        | NA                                                                                              | DNS Name for iDRAC                                                                     |
| auto_config           | No            | NA        | <ul> <li>Enabled</li> <li>Disabled</li> </ul>                                                   | Automatically creates the records for DNS                                              |
| static_dns            | No            | NA        | NA                                                                                              | Static configuration for DNS                                                           |
| vlan_id               | No            | None      | NA                                                                                              | Configuring the VLAN id for iDRAC                                                      |
| vlan_priority         | No            | None      | NA                                                                                              | Configuring the VLAN priority for iDRAC                                                |
| enable_nic            | No            | None      | <ul> <li>Enabled</li> <li>Disabled</li> </ul>                                                   | Whether to Enable or Disable Network Interface Controller for iDRAC                    |
| nic_selection         | No            | NA        | <ul> <li>Dedicated</li> <li>LOM1</li> <li>LOM2</li> <li>LOM3</li> <li>LOM4</li> </ul>           | Selecting Network Interface Controller types for iDRAC                                 |
| failover_network      | No            | NA        | <ul> <li>ALL</li> <li>LOM1</li> <li>LOM2</li> <li>LOM3</li> <li>LOM4</li> <li>T_None</li> </ul> | Failover Network Interface Controller types for iDRAC                                  |
| auto_detect           | No            | NA        | <ul> <li>Enabled</li> <li>Disabled</li> </ul>                                                   | Auto detect Network Interface Controller types for iDRAC                               |
| auto_negotiation      | No            | NA        | <ul> <li>Enabled</li> <li>Disabled</li> </ul>                                                   | Auto negotiation of Network Interface Controller for iDRAC                             |
| network_speed         | No            | NA        | <ul> <li>T_10</li> <li>T_100</li> <li>T_1000</li> </ul>                                         | Network speed for Network Interface Controller types for iDRAC                         |
| duplex_mode           | No            | NA        | <ul> <li>Full</li> <li>Half</li> </ul>                                                          | Transmission of data Network Interface Controller types for iDRAC                      |
| nic_mtu               | No            | None      | NA                                                                                              | NIC Maximum Transmission Unit                                                          |
| ip_address            | No            | NA        | NA                                                                                              | IP Address needs to be defined                                                         |
| enable_dhcp           | No            | NA        | NA                                                                                              | Whether to Enable or Disable DHCP Protocol for iDRAC                                   |
| dns_1                 | No            | NA        | NA                                                                                              | Needs to specify Domain Name Server Configuration                                      |
| dns_2                 | No            | NA        | NA                                                                                              | Needs to specify Domain Name Server Configuration                                      |
| dns_from_dhcp         | No            | NA        | <ul> <li>Enabled</li> <li>Disabled</li> </ul>                                                   | Specifying Domain Name Server from Dynamic Host Configuration Protocol                 |
| enable_ipv4           | No            | NA        | <ul> <li>Enabled</li> <li>Disabled</li> </ul>                                                   | Whether to Enable or Disable IPv4 configuration                                        |
| gateway               | No            | None      | NA                                                                                              | iDRAC network gateway address                                                          |
| net_mask              | No            | None      | NA                                                                                              | iDRAC network netmask details                                                          |
| static_dns_from_dhcp  | No            | None      | <ul> <li>Enabled</li> <li>Disabled</li> </ul>                                                   | Specifying Domain Name Server from Dynamic Host Configuration Protocol                 |
| static_dns_1          | No            | NA        | NA                                                                                              | Specify Domain Name Server Configuration                                               |
| static_dns_2          | No            | NA        | NA                                                                                              | Specify Domain Name Server Configuration                                               |
| static_gateway        | No            | None      | NA                                                                                              | Interfacing the network with another protocol                                          |
| static_net_mask       | No            | None      | NA                                                                                              | Determine whether IP address belongs to host                                          |



## <a name="Examples"></a>Examples

```
# Configure the iDRAC network attributes
- name: Configure the iDRAC network attributes
    dellemc_configure_idrac_network:	
      idrac_ip:   "xx.xx.xx.xx"
	  idrac_user: "xxxx"
	  idrac_pwd:  "xxxxxxxx"
	  share_name: "\\\\xx.xx.xx.xx\\share"
	  share_pwd:  "xxxxxxxx"
	  share_user: "xxxx"
	  share_mnt: "/mnt/share"
	  register_idrac_on_dns: Enabled
	  dns_idrac_name: None
	  auto_config: None
	  static_dns: None
	  setup_idrac_nic_vlan: Enabled
	  vlan_id: 0
	  vlan_priority: 1
	  enable_nic: Enabled
	  nic_selection: Dedicated
	  failover_network: T_None
	  auto_detect: Disabled
	  auto_negotiation: Enabled
	  network_speed: T_1000
	  duplex_mode: Full
	  nic_mtu: 1500
	  ip_address: "x.x.x.x"
	  enable_dhcp: Enabled
	  dns_1: "x.x.x.x"
	  dns_2: "x.x.x.x"
	  dns_from_dhcp: Enabled
	  enable_ipv4: Enabled
	  gateway: None
	  net_mask: None
	  static_dns_1: "x.x.x.x"
	  static_dns_2: "x.x.x.x"
	  static_dns_from_dhcp: Enabled
	  static_gateway: None
      static_net_mask: None

```
## <a name="Return-Values"></a>Return Values

Common return values are documented here [Return Values](http://docs.ansible.com/ansible/latest/common_return_values.html), the following are the fields unique to this module:

| name           | description                              | returned | type   | sample                                                             |
|----------------|------------------------------------------|----------|--------|--------------------------------------------------------------------|
| iDRAC Network | Configures the iDRAC network attributes | Success  | String | [Refer](https://github.com/dell/Dell-EMC-AnsibleModules-for-iDRAC) |

---

Copyright © 2017 Dell Inc. or its subsidiaries. All rights reserved. Dell, EMC, and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other trademarks may be trademarks of their respective owners.
