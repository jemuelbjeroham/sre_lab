**Top 50 DHCP Interview Questions and Answers**

---

**1. What is DHCP?**
Dynamic Host Configuration Protocol (DHCP) is a network management protocol used to dynamically assign IP addresses and other network configuration parameters to devices.

**2. What are the advantages of using DHCP?**
Automatic IP assignment, reduced manual errors, centralized IP management, and efficient handling of IP changes.

**3. What are the main components of DHCP?**
DHCP Server, DHCP Client, DHCP Relay Agent.

**4. What ports does DHCP use?**
UDP Port 67 (server) and UDP Port 68 (client).

**5. What is the DORA process in DHCP?**
Discover, Offer, Request, Acknowledge – the four-step handshake to assign an IP address.

**6. What is a DHCP lease?**
A DHCP lease is a temporary assignment of an IP address to a client for a specific period.

**7. What happens when a DHCP lease expires?**
The client must renew the lease or request a new IP from the DHCP server.

**8. Can a DHCP server assign a static IP?**
Yes, through DHCP reservation using MAC address mapping.

**9. What is DHCP relay?**
A device that forwards DHCP requests from clients in different subnets to a DHCP server.

**10. What is the purpose of DHCP reservation?**
To assign the same IP to a specific device every time based on its MAC address.

**11. What is the difference between DHCP and static IP addressing?**
DHCP is automatic; static IPs are manually configured.

**12. What is the DHCPDECLINE message?**
Sent by the client if the offered IP address is already in use.

**13. What is the DHCPNAK message?**
Sent by the server if it cannot fulfill the client’s request.

**14. How can IP conflicts be avoided in DHCP?**
By using IP address exclusion ranges and proper reservations.

**15. What is DHCP snooping?**
A security feature that filters untrusted DHCP messages.

**16. What is the role of Option 82 in DHCP?**
Used by relay agents to add additional information for security and tracking.

**17. What is the use of DHCP Option 3?**
Specifies the default gateway for the client.

**18. What is the use of DHCP Option 6?**
Specifies DNS servers for the client.

**19. Can multiple DHCP servers exist in a network?**
Yes, for redundancy or load balancing, but care must be taken to avoid IP conflicts.

**20. What is the DHCPINFORM message?**
Used by a client to obtain configuration parameters without an IP address.

**21. How does a client renew its DHCP lease?**
It sends a DHCPREQUEST to the server before lease expiry.

**22. What is T1 and T2 in DHCP?**
T1 is the time to renew the lease with the original server; T2 is to rebroadcast if the original server is unreachable.

**23. What is the default lease time in DHCP?**
Typically 24 hours, but it can be configured.

**24. Can DHCP assign IPv6 addresses?**
Yes, using DHCPv6.

**25. What is DHCP starvation attack?**
An attack that floods the DHCP server with requests to exhaust IP addresses.

**26. How do you secure a DHCP server?**
Enable DHCP snooping, use MAC filtering, monitor logs, use firewalls.

**27. What is APIPA?**
Automatic Private IP Addressing assigns a 169.254.x.x IP if no DHCP server is found.

**28. What happens if a DHCP server is down?**
Clients will retain their current IP until lease expiry or fall back to APIPA.

**29. How to configure DHCP on a Cisco router?**
Using `ip dhcp pool`, `network`, `default-router`, `dns-server` commands in global config.

**30. How do clients find the DHCP server?**
Clients broadcast a DHCPDISCOVER message on the network.

**31. What are DHCP scopes?**
A range of IP addresses defined for lease assignment.

**32. What is an exclusion range?**
Specific IPs within the DHCP scope that are not assigned to clients.

**33. What is a split-scope DHCP configuration?**
DHCP scope split between two servers to provide high availability.

**34. What is DHCP failover?**
A mechanism to ensure DHCP service availability in case of server failure.

**35. How does DHCP handle VLANs?**
Via DHCP relay or separate scopes for each VLAN.

**36. What is the purpose of the 255.255.255.255 address in DHCP?**
Used by the client to broadcast DHCPDISCOVER.

**37. What is the role of MAC address in DHCP?**
Used to uniquely identify clients for reservations or tracking.

**38. What is the significance of Option 66 and 67?**
Used for PXE booting – option 66 is TFTP server name, 67 is boot file name.

**39. Can DHCP be used for VoIP phones?**
Yes, with proper options like 150 (TFTP server IP) for configuration files.

**40. What is the difference between DHCPv4 and DHCPv6?**
DHCPv6 supports IPv6 addressing and has different message types and options.

**41. What is the function of Option 15?**
Specifies the domain name for the client.

**42. How to release and renew DHCP lease on Windows?**
Use `ipconfig /release` and `ipconfig /renew` commands.

**43. How to check DHCP leases on a Cisco device?**
Use `show ip dhcp binding` command.

**44. Can you assign multiple gateways via DHCP?**
No, DHCP usually assigns only one default gateway.

**45. What happens if two DHCP servers offer IPs to the same client?**
The client accepts the first offer it receives.

**46. How is DHCP different from BOOTP?**
BOOTP is static and older; DHCP is dynamic and more flexible.

**47. What is the use of Option 121?**
Specifies static routes.

**48. Can a DHCP client request a specific IP address?**
Yes, during the REQUEST stage, but the server may or may not honor it.

**49. What is the effect of a DHCP server with overlapping scopes?**
Can lead to IP conflicts unless scopes are coordinated.

**50. What is DHCP fingerprinting?**
Technique to identify device types based on their DHCP requests.
