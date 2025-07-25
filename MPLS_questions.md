**Most Frequently Asked MPLS Interview Questions and Answers (50 Q\&A)**

1. **What is MPLS?**

   * MPLS (Multiprotocol Label Switching) is a data forwarding technology that uses labels to make data forwarding decisions, increasing speed and efficiency in a network.

2. **What are the key components of MPLS?**

   * Label Edge Router (LER), Label Switch Router (LSR), Labels, Label Distribution Protocol (LDP).

3. **What is a label in MPLS?**

   * A short, fixed-length identifier used by routers to forward packets without inspecting the IP header.

4. **How many bits are in an MPLS label?**

   * 20 bits.

5. **What is the MPLS header size?**

   * 32 bits (4 bytes).

6. **What are the fields in an MPLS header?**

   * Label (20 bits), Experimental bits (3 bits), Bottom of Stack (1 bit), and TTL (8 bits).

7. **What is the role of LER in MPLS?**

   * Label Edge Routers sit at the edge of an MPLS network and assign (ingress) or remove (egress) labels from packets.

8. **What is an LSR?**

   * Label Switch Routers forward packets based on the MPLS label.

9. **What is the purpose of LDP?**

   * Label Distribution Protocol is used to distribute label mappings between routers.

10. **What are FECs in MPLS?**

    * Forwarding Equivalence Classes: a group of IP packets forwarded in the same manner.

11. **How does MPLS differ from traditional IP routing?**

    * Traditional IP routing uses destination-based lookups; MPLS uses labels, enabling faster and more predictable forwarding.

12. **What is Penultimate Hop Popping (PHP)?**

    * The second-to-last router removes the MPLS label before forwarding to the egress router.

13. **What is a label stack?**

    * Multiple MPLS labels can be stacked, useful in VPNs and Traffic Engineering.

14. **What is Traffic Engineering (TE) in MPLS?**

    * It allows optimal use of network resources by directing traffic through pre-defined paths.

15. **What protocols are used for MPLS Traffic Engineering?**

    * RSVP-TE (Resource Reservation Protocol with Traffic Engineering extensions).

16. **What is MPLS VPN?**

    * An MPLS-based VPN uses label switching to provide isolated and secure network segments for customers.

17. **What is the difference between Layer 2 and Layer 3 MPLS VPN?**

    * Layer 2 VPN emulates a point-to-point circuit, Layer 3 VPN routes packets between sites using VRFs.

18. **What is a VRF?**

    * Virtual Routing and Forwarding: a virtual instance of a routing table.

19. **What is the role of Route Distinguisher in MPLS VPN?**

    * It makes overlapping IP prefixes unique in MPLS VPNs.

20. **What is Route Target in MPLS VPN?**

    * It is a BGP extended community used for route import/export policies in VRFs.

21. **What are the advantages of MPLS?**

    * Scalability, QoS support, VPN support, traffic engineering, reduced latency.

22. **What is the function of the Bottom of Stack bit?**

    * Indicates whether the current label is the last in the label stack.

23. **Can MPLS work over Ethernet?**

    * Yes, MPLS can encapsulate packets over Ethernet links.

24. **What is the default MPLS label range?**

    * 16 to 1048575.

25. **What labels are reserved in MPLS?**

    * 0 (IPv4 Explicit NULL), 1 (Router Alert), 2 (IPv6 Explicit NULL), 3 (Implicit NULL), etc.

26. **What is Explicit NULL label?**

    * A reserved label (0 or 2) that forces the egress router to see the IP header.

27. **What is Implicit NULL label?**

    * A label (3) that tells the upstream router to pop the label (used in PHP).

28. **How is QoS implemented in MPLS?**

    * Through the EXP bits (3-bit field in the MPLS header) for traffic classification.

29. **Is MPLS a Layer 2 or Layer 3 protocol?**

    * MPLS operates between Layer 2 and Layer 3 (often called Layer 2.5).

30. **Can MPLS be used in data centers?**

    * Yes, though its use is more common in large service provider networks.

31. **What is the significance of TTL in MPLS?**

    * Time-To-Live helps prevent loops, similar to IP TTL.

32. **How does MPLS support redundancy?**

    * By allowing multiple label-switched paths (LSPs) and fast reroute mechanisms.

33. **What is Fast Reroute (FRR)?**

    * A mechanism that provides near-instant failover in MPLS networks.

34. **What is an LSP?**

    * Label Switched Path: the path through the MPLS network established by labels.

35. **How is an LSP established?**

    * Either dynamically via LDP or statically via configuration or RSVP-TE.

36. **What is MPLS OAM?**

    * Operations, Administration, and Maintenance: tools and protocols for troubleshooting MPLS.

37. **What is BGP’s role in MPLS VPNs?**

    * BGP distributes VPN routes across the MPLS core using extended communities.

38. **What is the main difference between LDP and RSVP-TE?**

    * LDP is for best-effort label distribution; RSVP-TE is for traffic engineering.

39. **What is an E-LSP and L-LSP?**

    * E-LSP: EXP-Inferred LSP (uses EXP bits for QoS), L-LSP: Label-Only-Inferred LSP.

40. **How does MPLS scale better than traditional IP routing?**

    * It reduces routing table lookups by using labels.

41. **What is a P router in MPLS VPN?**

    * Provider router that does not hold VPN routing information.

42. **What is a PE router in MPLS VPN?**

    * Provider Edge router that connects to customer sites and handles label operations.

43. **What is a CE router in MPLS VPN?**

    * Customer Edge router that connects to the provider network.

44. **What is label imposition?**

    * Process of adding an MPLS label to a packet.

45. **What is label swapping?**

    * Process where LSR replaces the incoming label with a new label before forwarding.

46. **What is label disposition?**

    * Process of removing the label (usually at the egress).

47. **What is a Martini Tunnel?**

    * An early method of Layer 2 VPN over MPLS using LDP.

48. **What is VPLS?**

    * Virtual Private LAN Service: Layer 2 VPN that emulates a LAN across MPLS.

49. **What is the control plane and data plane in MPLS?**

    * Control plane manages label distribution; data plane forwards packets using labels.

50. **Can you run MPLS over IPv6?**

    * Yes, MPLS can support IPv6, though with additional considerations.
