Authors: Mark Thekkethala and Andrew Lucia
Project: BGP Router

Overview Design:
- Incoming message handled by handle_packet
- handle_packet send the message to corresponding method according to message type
- updates and revokes update the forwarding table, pass along the message to specific routers, and save a copy of the message
- forward looks for best route, if no route found then send_error method sends a no route message back
- dump messages send a copy of the routing table back to the requestor
- forwarding tables determine best route if available
- path aggregation and disaggregation implemented by comparing ip addresses in bits and combining or rebuilding split ips from the updates data saved


Post-Milestone Additions:
- Using Dictionaries to store an expanded forwarding table called self.routes.
- Implemeted Revoke to use same logic as update for forwarding revoke to neighboring routes
-- Revoke also uses path disaggregation to split the IP path
- Implements no route messages through the send_error method which rebuilds the packet to sned no route
- implements ip to bit methods and get longest prefix method to calculate path aggregation
- Implements path disaggregation by create a rebuild method which uses updates we saved from each incoming message.
