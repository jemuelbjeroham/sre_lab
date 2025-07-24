1–10: Basic Switching Concepts
What is a switch?
A Layer 2 device that forwards frames based on MAC addresses. It learns MACs and sends frames only to the relevant port. 
Wikipedia
+13
networkerinterview.net
+13
Wikipedia
+13

How does a switch differ from a hub?
A hub broadcasts frames to all ports; a switch forwards only to the destination MAC, reducing collisions and improving bandwidth. 
networkerinterview.net
+1
I-MEDITA
+1

What is a MAC address table (CAM table)?
A lookup table in the switch mapping MAC addresses to switch ports, built dynamically by observing source MACs. 
networkerinterview.net

What is ARP and how does a switch handle ARP traffic?
ARP resolves an IP to a MAC. A switch simply forwards ARP broadcasts to all ports except the origin. 
Reddit
+8
networkerinterview.net
+8
Cisco Community
+8

Explain broadcast and collision domains.
Broadcast domain: all devices that receive broadcast frames. Collision domain: the segment where frames can collide (hubs); switches break up collision domains. 
I-MEDITA
+10
networkerinterview.net
+10
nwkings.com
+10

What is VLAN?
Virtual LAN—a logical broadcast domain within a switch, allowing network segmentation even on the same physical switch.

How does VLAN tagging work?
IEEE 802.1Q tags packets with a VLAN ID in the frame header so the switch forwards based on VLAN, separating traffic.

What is trunking?
A trunk port carries multiple VLANs' traffic using tagging (e.g., 802.1Q), connecting switches while preserving VLAN separation.

What is access mode vs trunk mode on a switch port?
Access mode: untagged frames, assigned to a single VLAN. Trunk mode: tagged frames from multiple VLANs.

What is inter-VLAN routing?
Routing traffic between VLANs, typically done via a Layer 3 switch or a router-on-a-stick setup.

11–20: Spanning Tree Protocol (STP)
What problem does STP solve?
Prevents loops in Layer 2 networks by blocking redundant paths. 
Wikipedia
+15
networkerinterview.net
+15
PyNet Labs
+15

What are STP port states?
Listening, learning, forwarding, blocking, disabled.

What is the root bridge?
The central reference point in STP, elected using the lowest bridge ID; all paths are calculated from it.

What influences root bridge selection?
Lowest bridge priority (default 32768) and MAC address as tiebreaker.

What is root port and designated port?
Root port: closest path to root bridge. Designated port: forwards traffic on a network segment.

What is BPDU?
Bridge Protocol Data Units carry STP information like root ID and port cost.

What are STP convergence and convergence time?
Process of recalculating paths when topology changes; classic STP takes ~30–50 seconds.

What is RSTP?
Rapid Spanning Tree Protocol (802.1w); faster convergence (~6 seconds).

What is PVST+ and MST?
Per-VLAN STP, Multiple Spanning Tree—provide VLAN-specific or multiple spanning tree instances.

How does STP react to a link failure?
Ports are re-evaluated; blocked ports may transition to forward, converging on a new loop-free topology.

21–30: Advanced Switching Concepts
What is EtherChannel?
Aggregates multiple physical links into one logical link for higher bandwidth and redundancy.

What is LACP?
Link Aggregation Control Protocol—part of 802.3ad; negotiates and maintains EtherChannels automatically.

What is load balancing in EtherChannel?
Hash-based distribution of traffic across member links, using source/destination MAC/IP or TCP ports.

What is VLAN pruning?
Disables unused VLANs on a trunk to reduce broadcast traffic.

What is a private VLAN?
VLAN variant that isolates devices within the VLAN except for communication to a shared router (community/private).

What’s switch stacking?
Multiple switches connected to operate as a single unit, with shared config and control plane.

What is QoS in switching?
Quality of Service managing priority queues based on markings like VLAN priority or DSCP.

What are VLAN ACLs (VACLs)?
Access control lists applied within VLANs for intra-VLAN traffic control, not just at layer 3 boundaries.

What is MAC address flooding?
Attack sends many frames with fake MACs to exhaust CAM table, forcing the switch to flood all frames—security risk.

How do you protect against MAC flooding?
Use port-security, limit MAC addresses per port, enable sticky MAC.

31–40: Performance & Optimization
What is cut-through vs store-and-forward switching?
Cut-through forwards as soon as destination MAC is read—lower latency but cannot check full frame. Store-and-forward verifies CRC before forwarding. 
InterviewBit
+9
Cisco Community
+9
Wikipedia
+9
Cisco Community
+3
Reddit
+3
networkerinterview.net
+3
Wikipedia
+15
Reddit
+15
I-MEDITA
+15
Reddit
+2
Cisco Community
+2
Reddit
+2
webasha.com
Wikipedia
+1
Wikipedia
+1

What is adaptive switching?
Switch dynamically shifts between cut-through and store-forward based on error rate. 
Wikipedia
+1
Wikipedia
+1

What is jumbo frame support?
Enables Ethernet frames larger than 1500 bytes (e.g., up to 9000 bytes), improving throughput on LANs.

What is non-blocking switch fabric?
Architecture that allows full bandwidth on all ports simultaneously without congestion. 
Wikipedia

What is head-of-line blocking?
A packet at the front of a FIFO queue prevents packets behind from being forwarded, causing performance delays.

What is backpressure?
A congestion control mechanism where the switch signals ingress ports to slow down rather than drop packets.

What is buffer memory on a switch?
Temporary packet storage to handle traffic bursts and prevent frame loss during congestion.

What is latency and how does switching add latency?
The time to process frames (analyze, lookup, forward). Minimal in hardware-based switching (microseconds).

What is switch forwarding rate?
Number of frames per second a switch can handle—measured in Mpps (million packets per second).

What is VLAN hopping?
Attack where attacker sends double-tagged packets to break VLAN separation; prevented via proper VLAN trunk config.

41–50: Troubleshooting & Real-World Scenarios
How do you troubleshoot a port that’s not forwarding?
Check: VLAN membership, trunk/access config, STP state, port status, duplex/speed, and error counters.

How do you mirror a port?
Configure a SPAN session: source port (to monitor) and destination port (connected to analysis device).

What causes high CPU on a switch?
Control-plane load—STP flaps, traffic storms, excessive ARP, or management protocols.

What is loopguard?
STP feature preventing loops when BPDUs stop arriving on non-designated ports.

What is UDLD?
Unidirectional Link Detection—avoids issues from unidirectional fiber cable failures.

What is MSTP?
Multiple Spanning-Tree Protocol—allows multiple VLANs to share STP instances for scalability.

How do you handle spanning-tree root issues?
Set root bridge priority manually using spanning-tree vlan X root primary to control root design.

How do you resolve MAC flapping?
Look for loops, misconfig, or port-security causing multiple ports learning same MAC.

What is BPDU filter and guard?
BPDU Guard disables ports receiving unexpected BPDUs (useful on access ties); filter stops BPDUs from being sent.

How would you scale a network with many VLANs and switches?
Use hierarchical design: Core-Distribution-Access, implement VTP carefully, use L3 boundaries and redundant links.
