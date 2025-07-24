Here are **50 frequently asked AWS Cloud & Networking** questions and answers, perfect to save locally as a reference document.

---

## 1–10: AWS Core & VPC Basics

1. **What is AWS?**
   A cloud services platform providing on-demand compute, storage, networking, analytics, and more — with global data centers in Regions and Availability Zones ([Whizlabs][1], [Simplilearn.com][2], [DEV Community][3]).

2. **Define a VPC.**
   A **Virtual Private Cloud** is an isolated virtual network in AWS where you define your IP CIDR, subnets, routing, and security ([Wikipedia][4], [DEV Community][3]).

3. **What is a subnet in AWS?**
   A subdivision of VPC IP range, existing within a specific Availability Zone, used to segment resources ([DEV Community][3]).

4. **Public vs Private Subnet?**

   * *Public Subnet*: has route to an Internet Gateway (IGW).
   * *Private Subnet*: no IGW route — used for internal resources ([DEV Community][3]).

5. **What is an Internet Gateway (IGW)?**
   Provides internet access to resources in a VPC. Only one per VPC. ([DEV Community][3])

6. **What is a NAT Gateway?**
   Enables outbound internet from private subnets while blocking inbound traffic. ([Whizlabs][1])

7. **What is a Route Table?**
   Defines traffic routing rules within VPC: local routes, IGW, NAT, VPC peering, VPN, etc. ([DEV Community][3])

8. **What’s a Security Group?**
   Stateful firewall at instance level that allows inbound/outbound rules. ([DEV Community][3])

9. **What’s a Network ACL?**
   Subnet-level stateless firewall, requires both inbound and outbound rules ([Medium][5], [DEV Community][3])

10. **What are AZs and Regions?**
    Regions are geographic areas; AZs are isolated data centers within a region ([Wikipedia][6], [Simplilearn.com][2])

---

## 11–20: Networking & Connectivity

11. **What is VPC peering?**
    Enables direct, private routing between VPCs without using the internet ([Whizlabs][1], [DEV Community][3]).

12. **Limitations of VPC peering?**
    No transitive routing; requires non-overlapping CIDRs ([Whizlabs][1], [Medium][5]).

13. **What is a Transit Gateway?**
    Central hub connecting multiple VPCs and on-prem sites ([Medium][5]).

14. **Role of Direct Connect?**
    Private, dedicated network link between on-premise and AWS with low latency ([Test Prep Training][7]).

15. **Role of Site-to-Site VPN?**
    Encrypted IPsec tunnel from on-prem to AWS VPC for hybrid cloud setups ([Test Prep Training][7]).

16. **What is AWS PrivateLink?**
    Securely connects VPCs/services without routing traffic over public internet ([Whizlabs][1], [Medium][5])

17. **What is ClassicLink?**
    Connects EC2 classic instances to a VPC using private IPs (legacy) ([Whizlabs][1])

18. **What is an ENI?**
    Elastic Network Interface—attachable virtual NIC for EC2 with multiple IPs ([Medium][5])

19. **What is VPC Flow Logs?**
    Captures metadata (source/dest IPs, ports, action) for traffic in VPC for monitoring/troubleshooting ([Medium][5]).

20. **What is VPC endpoint?**
    Private connection to AWS service resources (S3, DynamoDB) within VPC ([DEV Community][3], [Medium][5])

---

## 21–30: DNS, ELB & Hybrid Scenarios

21. **What is Route 53?**
    AWS’s scalable DNS service, supports routing policies & Health Checks ([Test Prep Training][7])

22. **About ELB types?**
    ALB (HTTP), NLB (TCP/UDP), and CLB (deprecated/classic) ([Whizlabs][1])

23. **What is Auto Scaling?**
    Dynamically adds/removes EC2 instances based on configured policies ([Simplilearn.com][2], [Test Prep Training][7])

24. **What is CloudFront?**
    Global CDN that accelerates content delivery via edge locations ([Test Prep Training][7])

25. **What is S3?**
    Scalable object storage with global data durability ([YouTube][8])

26. **How to secure communication on AWS?**
    Use Security Groups, NACLs, VPC Flow Logs, IAM, TLS in transit, encryption at rest ([DEV Community][3])

27. **What is AWS VPN?**
    Managed Site-to-Site IPsec VPN for secure connectivity ([Test Prep Training][7])

28. **What is Transit VPC?**
    Centralized E2E routing hub in AWS for hybrid multi-VPC networks ([Test Prep Training][7], [DEV Community][3])

29. **Explain CIDR in VPCs.**
    IP block mask /16 to /28 that defines address space in VPC/subnets ([Whizlabs][1])

30. **What is prefix list?**
    AWS-managed or custom lists to simplify security group/NACL rules (optional Q).

---

## 31–40: Performance & Security

31. **How to monitor VPC traffic?**
    Combine VPC Flow Logs + CloudWatch Insights ([Medium][5])

32. **Difference between stateful/stateless?**

    * Security groups are stateful.
    * NACLs are stateless. ([DEV Community][3])

33. **What are ENI attachments?**
    Add/remove network interfaces dynamically for redundancy and multiple IPs ([Whizlabs][1])

34. **What is AWS Global Accelerator?**
    Improves network performance using Amazon global backplane (optional Q).

35. **What is AWS Shield/WAF?**
    DDoS protection (Shield) + web app firewall to protect apps ([Test Prep Training][7])

36. **What is AWS GuardDuty?**
    Threat identification service analyzing event logs (VPC, API, CloudTrail) ([DEV Community][3])

37. **Explain hybrid failover design?**
    Combine Direct Connect + VPN for redundancy — automatic failover to VPN.

38. **How do you optimize network costs?**
    Use PrivateLink, VPC endpoints, Transit Gateway aggregation, flow log analysis (optional Q).

39. **What is AWS Traffic Mirroring?**
    Clone VPC network traffic for monitoring or intrusion detection (optional Q from Turn0search1).

40. **What is ENA?**
    EC2 Elastic Network Adapter – used in high performance compute instances (optional Q).

---

## 41–50: Scenario & Troubleshooting

41. **Troubleshoot no internet from EC2?**
    Check subnet route table (IGW/NAT route), Security Group and NACL, ENI and DHCP options.

42. **Compute VPC CIDR for requirement?**
    Choose /16 to /28 based on size; avoid overlap; same region for AZ expansion ([Test Prep Training][7], [Medium][5])

43. **Explain Transit Gateway use case?**
    Simplifies and scales hub-and-spoke or multi-region on-prem-VPC connectivity ([Medium][5], [Whizlabs][1])

44. **Explain VPC peering vs Transit Gateway.**
    Peering is one-to-one; Transit Gateway supports many-to-many with transitive routing ([Medium][5])

45. **Why use PrivateLink?**
    For secure internal access to services like S3/DynamoDB via AWS backbone ([Medium][5])

46. **How to rotate IGW?**
    Not supported. Replace by creating new VPC and migrational design (edge-case question).

47. **Troubleshoot VPC Flow Log gaps?**
    Ensure logging enabled and proper IAM roles, turn internal buffer/config issues.

48. **How to enforce restrictions with NACL?**
    Use stateless rules—must allow both inbound and outbound ports & IPs.

49. **Explain cross-account VPC peering?**
    Peer VPCs from different AWS accounts, route tables and security groups updated accordingly.

50. **Example: multi-region hybrid failover?**
    Use Direct Connect + VPN + Transit Gateway + dynamic routing protocol (BGP) for high availability.

---

Let me know if you'd like **Diagrams, CLI commands, or lab exercises** for any of these scenarios!

[1]: https://www.whizlabs.com/blog/aws-vpc-interview-questions/?utm_source=chatgpt.com "Top 20 AWS VPC Interview Questions and Answers - Whizlabs Blog"
[2]: https://www.simplilearn.com/tutorials/aws-tutorial/aws-interview-questions?utm_source=chatgpt.com "100+ AWS Interview Questions and Answers (2025) - Simplilearn.com"
[3]: https://dev.to/imsushant12/interview-questions-on-aws-networking-vpc-subnets-and-security-groups-40g7?utm_source=chatgpt.com "Interview Questions on AWS Networking: VPC, Subnets, and ..."
[4]: https://en.wikipedia.org/wiki/Amazon_Virtual_Private_Cloud?utm_source=chatgpt.com "Amazon Virtual Private Cloud"
[5]: https://medium.com/%40nbkumar2103/-3ccb42bf2e7c?utm_source=chatgpt.com "AWS VPC Service Interview Questions & Answers - Medium"
[6]: https://en.wikipedia.org/wiki/Amazon_Web_Services?utm_source=chatgpt.com "Amazon Web Services"
[7]: https://www.testpreptraining.com/tutorial/aws-advanced-networking-specialty-interview-questions/?utm_source=chatgpt.com "AWS Advanced Networking Specialty Interview Questions"
[8]: https://www.youtube.com/watch?v=OsK9IA0-ciE&utm_source=chatgpt.com "Top 15 AWS Networking Interview Questions You Must ... - YouTube"
