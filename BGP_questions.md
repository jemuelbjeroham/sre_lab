Here are **50 frequently asked BGP interview questions and answers**, ideal for saving as a local document. They cover everything from foundational knowledge to advanced scenarios and troubleshooting.

---

## 📘 Basics

1. **What is BGP?**
   Border Gateway Protocol – the main protocol for routing between autonomous systems (AS) on the Internet. It uses a path-vector mechanism over TCP port 179.

2. **What’s the difference between eBGP and iBGP?**

   * **eBGP**: between routers in different ASes (directly connected).
   * **iBGP**: between routers in the same AS (can be multihop). (<strong>10‍</strong>)

3. **Why use BGP instead of OSPF or RIP?**
   BGP handles routing **between** ASes (inter-domain), supports policy-based routing, and scales globally.

4. **What is an AS (Autonomous System)?**
   A group of IP networks under single admin with a common routing policy, identified by an ASN.

5. **Which transport and port does BGP use?**
   BGP uses **TCP port 179** for establishing reliable peer sessions. ([mindmajix][1], [Wikipedia][2], [PyNet Labs][3], [Hack The Forum][4], [Verve Copilot][5])

6. **What are the BGP message types?**

   * **OPEN**: Establishes session
   * **UPDATE**: Shares route info
   * **KEEPALIVE**: Maintains session
   * **NOTIFICATION**: Reports errors ([PyNet Labs][3])

7. **What are BGP timers?**

   * **Hold Timer**: default 180s
   * **Keepalive Timer**: default 60s
     These ensure session liveness and detect failures.

8. **What is BGP convergence?**
   Time it takes after a change (link down/up) for BGP to settle on new best paths across peers.

9. **What is split-horizon in BGP?**
   Mechanism preventing re-advertisement of routes back to the neighbor they were learned from—prevents loops. ([PyNet Labs][3], [Hack The Forum][4], [Wikipedia][2], [mindmajix][1])

10. **What is the administrative distance of BGP?**

    * **eBGP**: 20
    * **iBGP**: 200

---

## ⚙️ BGP Attributes & Path Selection

11. **List the main BGP path attributes in selection order.**
    Weight, Local Preference, Locally Originated, AS‑Path length, Origin type, MED, eBGP over iBGP, IGP metric to next‑hop, oldest path, Router ID ([InterviewBit][6])

12. **What is Weight?**
    Cisco-specific attribute; highest weight is preferred; local to the router.

13. **What is Local Preference (LOCAL\_PREF)?**
    Preferred route within AS; higher LOCAL\_PREF is preferred.

14. **What is AS-Path?**
    The list of ASes a route has traversed; used to prevent loops (longer paths are less preferred).

15. **What is Origin type?**
    Indicates route origin: IGP (most preferred), EGP, or Incomplete (least preferred).

16. **What is MED?**
    Multi-Exit Discriminator—signals preference for entry points into AS; lower MED is preferred.

17. **Why is eBGP favored over iBGP?**
    Because external routes are typically more direct and trusted.

18. **What is the role of NEXT\_HOP?**
    Identifies the router to reach the destination network—must be reachable.

19. **What is the AIGP attribute?**
    IGP metric carried in BGP (RFC 7311), used in Cisco to influence path selection. ([Hack The Forum][4], [Wikipedia][2], [mindmajix][1], [Verve Copilot][5])

20. **What influence does Router ID have?**
    Tie-breaker: lowest router ID preferred if all else is equal.

---

## 🛠️ BGP Configuration & Operations

21. **How do you define a neighbor in Cisco IOS?**

    ```
    router bgp <ASN>
     neighbor x.x.x.x remote-as <ASN>
    ```

22. **Can iBGP peers be formed across subnets?**
    Yes, with the `neighbor ... ebgp-multihop` command. ([PyNet Labs][3], [arXiv][7])

23. **What is a route reflector?**
    Router that allows iBGP neighbors to peer through it, avoiding full mesh.

24. **What are BGP confederations?**
    Method to divide a large AS into sub-ASes to reduce iBGP sessions. ([InterviewBit][6], [PyNet Labs][3], [Wikipedia][2])

25. **What is BGP route dampening?**
    Suppresses flapping routes to increase stability by penalizing unstable prefixes.

26. **What is AS\_PATH prepending?**
    Adding extra ASNs to AS\_PATH to make route less preferred.

27. **What are BGP communities?**
    Tags applied to prefixes to manage routing policies. Common ones include `NO_EXPORT`. ([Hack The Forum][4], [arXiv][8], [PyNet Labs][3], [Wikipedia][2])

28. **Explain TTL Security for eBGP.**
    Protects sessions from spoofed packets by enforcing strict TTL values. ([InterviewBit][6])

29. **What is BGP synchronization?**
    Old mechanism requiring route in IGP before advertising via iBGP (now often disabled).

30. **Describe hard vs soft reset in BGP.**

    * **Hard**: drops TCP session and clears table
    * **Soft**: refresh only UPDATEs without session drop ([PyNet Labs][3])

---

## 🔁 BGP Troubleshooting

31. **How to check BGP neighbor status?**
    `show ip bgp summary`

32. **How to view BGP table entries?**
    `show ip bgp` or `show ip bgp x.x.x.x`

33. **How to verify the next-hop?**
    Check `show ip bgp x.x.x.x` and use traceroute to validate reachability.

34. **What causes session issues in BGP?**
    Mismatched AS, authentication failure, incorrect next-hop, TTL/security, ACLs, route filters.

35. **How do you trace route selection?**
    Use `show ip bgp x.x.x.x detail` to see why a path was preferred.

36. **How to troubleshoot route flapping?**
    Check `show ip bgp x.x.x.x`, assess dampening, interface stability, peer logs.

37. **What are prefix-lists and route-maps?**
    Used to filter and modify route advertisements.

38. **How to prevent BGP hijacks?**
    Implement RPKI, prefix filtering, prefix-lists based on IRR/ROA.

39. **What is prefix filtering?**
    Using access-lists or prefix-lists to restrict which prefixes are advertised or accepted.

40. **How to detect route leaks?**
    Watch for unexpected AS\_PATHs, abnormal routing, prefix stats.

---

## 🧩 Advanced BGP Topics

41. **What is BGP multipath (ECMP)?**
    Allows parallel usage of multiple equal-cost BGP routes. ([PyNet Labs][3], [Wikipedia][2], [Hack The Forum][4], [WIRED][9], [arXiv][7])

42. **How does BGP support IPv6?**
    Using MP-BGP extensions to carry IPv6 NLRIs.

43. **Explain BGP communities’ function.**
    Facilitate policy control across ASes — for tagging or controlling propagation. ([Hack The Forum][4], [Wikipedia][2], [arXiv][10])

44. **What is BGP hijacking?**
    Unauthorized prefix announcement causing traffic redirection. ([Wikipedia][11])

45. **What are route reflectors’ benefits?**
    Reduce iBGP full-mesh complexity and sessions.

46. **What are BGP confederation pros and cons?**
    Improve scale in large ASes, but add policy complexity.

47. **How does BGP handle load balancing?**
    With multipath support — simultaneously install multiple routes in RIB.

48. **How does BGP provide security?**
    Through TTL-security, MD5/authentication, prefix filters, and RPKI-based origin validation.

49. **What is BGP path poisoning?**
    Advertise a prefix with your own ASN in AS\_PATH to prevent a neighbor from using it (Blackhole specific traffic).

50. **Can BGP be used internally?**
    Yes — internal routing in large enterprise ASes using iBGP with route reflectors.

---

Feel free to copy and save these Q\&As locally. Want a refined PDF version or deeper examples on any of these?

[1]: https://mindmajix.com/bgp-interview-questions?utm_source=chatgpt.com "Top 30 BGP Interview Questions and Answers in 2025 - MindMajix"
[2]: https://en.wikipedia.org/wiki/Border_Gateway_Protocol?utm_source=chatgpt.com "Border Gateway Protocol"
[3]: https://www.pynetlabs.com/bgp-interview-questions-and-answers/?utm_source=chatgpt.com "Top 25 BGP Interview Questions and Answers (2025) - PyNet Labs"
[4]: https://www.hacktheforum.com/computer-networking-computer-networking/bgp-interview-questions/?utm_source=chatgpt.com "BGP Interview Questions – Networking & Security - Hack The Forum"
[5]: https://www.vervecopilot.com/blog/bgp-interview-questions?utm_source=chatgpt.com "11 Most Common BGP Interview Questions You Should Prepare For"
[6]: https://www.interviewbit.com/bgp-interview-questions/?utm_source=chatgpt.com "Top BGP Interview Questions and Answers (2025) - InterviewBit"
[7]: https://arxiv.org/abs/2107.10938?utm_source=chatgpt.com "BGP-Multipath Routing in the Internet"
[8]: https://arxiv.org/abs/1203.1681?utm_source=chatgpt.com "Network-Destabilizing Attacks"
[9]: https://www.wired.com/story/bgp-route-leak-internet-outage?utm_source=chatgpt.com "The Infrastructure Mess Causing Countless Internet Outages"
[10]: https://arxiv.org/abs/2103.07683?utm_source=chatgpt.com "Performance Analysis of Multipath BGP"
[11]: https://en.wikipedia.org/wiki/BGP_hijacking?utm_source=chatgpt.com "BGP hijacking"
