Check the current config and back it up.

```
show running-conifg all
copy running-config tftp://192.168.1.100/backup-config

# View specific sections
show running-config interfaces
show running-config bgp
show running-config vlan
```

Copy and Install EOS Image
```
copy tftp://<TFTP-IP>/EOS-4.x.x.swi flash:
verify /md5 flash:EOS-4.x.x.swi
install source flash:EOS-4.x.x.swi
```

Here's a sample output of `show boot-config` from an Arista switch:
```
Software image: flash:/EOS-4.31.2F.swi 
Console speed: (not set) 
Aboot password (encrypted): (not set) 
Memory test iterations: (not set)
```
The key piece here is the "Software image" line which shows which EOS image will be used on the next boot. This is particularly important during upgrades to verify you're pointing to the correct image.

If you'd like to verify the available images on flash, you can use:
```
switch# dir flash: 
Directory of flash:/ 
-rwx 419329159 Nov 15 14:22 EOS-4.31.2F.swi 
-rwx 398274523 Aug 10 09:15 EOS-4.30.4M.swi
```

If your switch supports **ISSU (In-Service Software Upgrade)**, use this:
```
install source flash:EOS-4.x.x.swi
```

After reboot, check the EOS version
```
show version
show boot-config
show log last 20
```

-------
```
show chassis 
show chassis detail 
show chassis environment

show environment all
show environment cooling
show environment power
show environment temperature

show modules
show modules status
show modules detail
```

-------
## Layer 2
```
show lldp neighbors
show lldp neighbors detail

show cdp neighbors
show cdp neihbors detail
```
-----
ARP
```
show arp
show ip arp
show arp vlan <id>
clear arp cache

# check if MAC is in ARP table
show arp | include <ip-address>
show arp | include <mac-address>
show mac address-table>
```
-----
```
show redundancy status
show redundancy states
show redundancy protocol
```


