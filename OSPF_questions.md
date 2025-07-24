Here are **50 frequently asked OSPF (Open Shortest Path First) interview questions and answers**, optimized for network reliability roles. Feel free to save them as a local document.

---

## 🔹 1–10: OSPF Fundamentals

1. **What is OSPF?**
   A link-state IGP for IP routing within an AS. It uses Dijkstra’s SPF algorithm to build a loop-free topology.

2. **What are OSPF areas?**
   Logical divisions within an OSPF domain to reduce SPF computation and control LSA flooding (e.g., Area 0 is the backbone).

3. **Why must all areas connect to Area 0?**
   It prevents routing loops and ensures consistent routing between areas.

4. **What is a Router ID (RID)?**
   A 32-bit value (often an IP) uniquely identifying each router in an OSPF domain.

5. **Explain OSPF cost.**
   A metric based on interface bandwidth (reference 100 Mbps). Lower cost paths are preferred.

6. **How is cost calculated by default?**
   Cost = Reference bandwidth / interface bandwidth (e.g., 100,000,000 bps / 1,000,000,000 bps = cost 1).

7. **What is an LSA?**
   Link-State Advertisement — describes routing topology. There are multiple types (Type 1–5, 7).

8. **What types of LSAs are there?**
   Type 1 (Router), Type 2 (Network), Type 3 (Summary), Type 4 (ASBR summary), Type 5 (External), Type 7 (NSSA).

9. **What is an ABR?**
   Area Border Router — connects an area to Area 0 and generates Type 3 LSAs.

10. **What is an ASBR?**
    Autonomous System Boundary Router — injects external routes (e.g., redistributed from BGP), generating Type 5 LSAs.

---

## 🔹 11–20: Neighbor and Adjacency

11. **How is an OSPF neighbor formed?**
    Through Hello packets. Routers exchange hello messages on matching Router IDs, areas, and network types.

12. **What matching criteria must neighbors have?**
    Area ID, subnet mask, Hello/Dead timers, authentication, and network type.

13. **Explain OSPF Hello/Dead intervals.**
    Default hello is 10s (1s on NBMA/networks); dead is typically 4× hello (40s or 4s).

14. **What are OSPF neighbor states?**
    Down → Init → 2-Way → ExStart → Exchange → Loading → Full.

15. **What is the DR and BDR?**
    Designated and Backup Designated Router — elected on broadcast/multi-access networks to reduce adjacencies.

16. **When is DR/BDR election used?**
    On broadcast and NBMA networks, not on point-to-point links.

17. **What triggers adjacency?**
    DR for broadcast networks; full mesh for point-to-point and point-to-multipoint.

18. **What is the DBD packet?**
    Database Description — summary of LSDB contents exchanged between neighbors.

19. **What is the LSR packet?**
    Link-State Request — used after DBD to get missing or outdated LSAs.

20. **What is the LSU packet?**
    Link-State Update — contains requested LSAs or unsolicited LSA updates.

---

## 🔹 21–30: LSDB and SPF

21. **What is the LSDB?**
    Link-State Database — a router’s complete topology map for its area.

22. **What is SPF calculation?**
    Dijkstra’s algorithm used on LSDB to compute best paths.

23. **When does OSPF recalc SPF?**
    On LSDB changes, interface flaps, or periodic LSRefresh (30 minutes).

24. **What are LSRefresh and MaxAge timers?**
    LSRefresh: re-originates LSAs every 30 minutes; MaxAge: after 60 minutes, invalidates stale LSA.

25. **What is Type 3 LSA?**
    Summary LSA – advertises a route from another area across ABRs.

26. **What is Type 4 LSA?**
    ASBR summary – advertises route to an ASBR in another area.

27. **What is Type 5 LSA?**
    External LSA – carries routes redistributed into OSPF (e.g., from BGP).

28. **What is Type 7 LSA?**
    NSSA external LSA – used in Not-So-Stubby Areas to carry external routes.

29. **What is an NSSA?**
    A Not-So-Stubby Area that allows external route injection via Type 7 LSAs.

30. **How does Type 7 become Type 5?**
    ABR translates Type 7 LSAs to Type 5 before flooding into backbone.

---

## 🔹 31–40: Area Types and Summarization

31. **What is a Stub Area?**
    Prevents Type 5 LSAs and uses a default route to reach external networks.

32. **What is Totally Stubby Area?**
    Blocks Type 3, 4, 5 LSAs; only default route injected by ABR.

33. **What is NSSA?**
    Similar to stub, but allows external route injection with Type 7 LSAs intact.

34. **What is Totally NSSA?**
    Blocks summary LSAs (3, 4) and external LSAs (5); ABR injects default.

35. **What is LSA summarization?**
    Reduces LSDB size by aggregating networks at ABRs (summary LSAs) and ASBRs (external LSAs).

36. **How do you configure summarization?**
    On ABR: `area X range A.B.C.D/N`
    On ASBR: `summary-address A.B.C.D/N`

37. **Why use area summarization?**
    Reduces routing overhead and isolates instability between areas.

38. **What is an opaque LSA?**
    Used to carry additional info like TE, traffic engineering, or MPLS-TE.

39. **What is virtual link?**
    Connects discontiguous OSPF areas through transit Area 0 via another ABR.

40. **When use virtual link?**
    When an area isn’t directly attached to Area 0 but needs connectivity.

---

## 🔹 41–50: Advanced and Troubleshooting

41. **What is OSPF cost adjustment best practice?**
    Adjust reference bandwidth to reflect high-speed links (e.g., 10Gbps).

42. **What is route redistribution?**
    Importing routes from other protocols into OSPF (e.g., RIP, BGP) with care to avoid loops.

43. **How to prevent feedback loops?**
    Use route maps, filters, metrics and limit redistribution scope.

44. **How do you fix OSPF neighbor stuck in Init state?**
    Check area IDs, hello/dead timers, subnet mask mismatches, authentication, and MTU.

45. **What causes OSPF flapping?**
    Interface instability, CPU overload, LSDB convergence issues.

46. **What is SPF throttling?**
    Rate limit SPF recalculations to prevent resource exhaustion from frequent topology changes.

47. **What is OSPF authentication?**
    Plaintext or MD5 to secure routing updates — all routers in area need matching keys.

48. **Why use MD5 over plaintext?**
    MD5 prevents route hijacking or spoofing by validating authenticity.

49. **What does “full adjacency” mean?**
    LSDB fully synchronized; routers can exchange complete routing info.

50. **Troubleshooting: OSPF routes missing in routing table**
    Use: `show ip ospf database`, `show ip ospf neighbor`, check timers, authentication, MTU, network statements.

---

Copy, save, and review these for a solid OSPF prep session. Let me know if you’d like labs, CLI examples, or packet-level breakdowns next!
