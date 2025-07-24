**50 Most Frequently Asked DNS Interview Questions and Answers**

1. **What is DNS?**
   DNS (Domain Name System) translates domain names into IP addresses so browsers can load Internet resources.

2. **What are the components of DNS?**
   DNS components include DNS Resolver, DNS Server (Authoritative, Recursive), and DNS Records.

3. **What is a DNS Resolver?**
   A DNS Resolver is a server that receives DNS queries from clients and resolves them by querying other DNS servers.

4. **What is an Authoritative DNS Server?**
   It holds the actual DNS records for a domain and provides answers to queries about those domains.

5. **What is a Recursive DNS Server?**
   It queries other DNS servers on behalf of the client to resolve a domain name.

6. **What is a DNS Zone?**
   A DNS Zone is a portion of the DNS namespace managed by a specific organization or administrator.

7. **What is a DNS Record?**
   DNS records are entries in DNS databases that provide information about a domain, such as its IP address.

8. **What are A and AAAA records?**
   "A" maps a domain to an IPv4 address; "AAAA" maps a domain to an IPv6 address.

9. **What is a CNAME record?**
   A CNAME (Canonical Name) record maps one domain to another domain.

10. **What is an MX record?**
    MX (Mail Exchange) record directs email to a mail server.

11. **What is an NS record?**
    NS (Name Server) record indicates which DNS server is authoritative for a domain.

12. **What is a TXT record?**
    TXT records hold text information for external sources to read, often used for verification and SPF.

13. **What is an SOA record?**
    SOA (Start of Authority) record provides information about the domain, including the primary DNS server.

14. **What is TTL in DNS?**
    TTL (Time To Live) is the duration that a DNS record is cached by DNS servers and clients.

15. **What is DNS propagation?**
    The time it takes for DNS changes to be updated across all servers on the Internet.

16. **What causes DNS propagation delay?**
    Primarily TTL settings and caching by ISPs or intermediate resolvers.

17. **What is reverse DNS (rDNS)?**
    rDNS maps an IP address to a domain name using a PTR record.

18. **What is a PTR record?**
    PTR (Pointer) record provides the domain name associated with an IP address.

19. **What is a DNS forwarder?**
    A DNS forwarder is a server configured to forward queries it cannot resolve to another DNS server.

20. **What is DNS caching?**
    Temporarily storing DNS query results to speed up subsequent queries.

21. **What is a Root DNS Server?**
    A Root DNS server is the first step in translating human-readable domain names into IP addresses.

22. **How many root DNS servers exist?**
    There are 13 sets of root DNS servers labeled A to M.

23. **What is DNS Spoofing?**
    A type of attack where false DNS results are provided, redirecting traffic to malicious sites.

24. **What is DNSSEC?**
    DNSSEC (DNS Security Extensions) adds security by enabling DNS responses to be verified.

25. **What are the benefits of DNS?**
    Ease of use, scalability, redundancy, load distribution, and decentralized management.

26. **What is split DNS?**
    Split DNS provides different DNS answers based on whether the client is internal or external.

27. **What are common DNS troubleshooting tools?**
    dig, nslookup, host, ping, traceroute.

28. **What is the purpose of the dig command?**
    To query DNS servers and troubleshoot DNS problems.

29. **What is the difference between dig and nslookup?**
    dig is more flexible and preferred for scripting; nslookup is simpler for quick queries.

30. **What is dynamic DNS?**
    Automatically updates DNS records when an IP address changes.

31. **How does DNS work?**
    Client sends a query → Resolver → Root → TLD → Authoritative → IP returned to client.

32. **What is DNS poisoning?**
    Injecting false DNS data into a resolver's cache.

33. **What are TLDs in DNS?**
    Top Level Domains like .com, .net, .org that are right after the root in DNS hierarchy.

34. **What is a DNS hierarchy?**
    Root → TLD → Second-Level Domain → Subdomain.

35. **Can a domain have multiple A records?**
    Yes, this is used for load balancing and redundancy.

36. **What happens when a DNS query fails?**
    An error is returned to the client, like NXDOMAIN or SERVFAIL.

37. **What is NXDOMAIN?**
    A DNS response meaning the domain name does not exist.

38. **What is SERVFAIL?**
    The DNS server failed to complete the query due to an internal error.

39. **What is a wildcard DNS record?**
    A record that matches all subdomains not explicitly defined.

40. **What is a DNS zone transfer?**
    Copying zone data from a master DNS server to a slave.

41. **What is AXFR and IXFR?**
    AXFR is full zone transfer, IXFR is incremental zone transfer.

42. **What is a primary vs secondary DNS server?**
    Primary holds the master copy; secondary holds a replicated copy.

43. **How to secure DNS infrastructure?**
    Use DNSSEC, rate limiting, access controls, monitoring.

44. **What is Anycast in DNS?**
    Technique where multiple DNS servers share the same IP for faster and redundant response.

45. **What is EDNS?**
    Extension Mechanisms for DNS to support larger message sizes and additional features.

46. **What is a negative caching TTL?**
    Time a DNS resolver caches a failed lookup.

47. **Can DNS work over TCP?**
    Yes, usually for large responses or zone transfers (TCP port 53).

48. **What port does DNS use?**
    UDP port 53 (TCP port 53 for larger payloads).

49. **What is DNS Amplification Attack?**
    An attack that uses DNS servers to flood a target with large amounts of data.

50. **Why is DNS important?**
    It’s the backbone of the Internet, enabling user-friendly access to services by resolving names to IPs.
