Author: Mark Thekkethala & Andrew Lucia
Project 2

This project revolves around being able to receive and forward on packets
of data. The BGP router receives different types of messages in the data 
packets received. 

First the message is sent when the router run function is called and 
sockets are opened. This passes the packet and source IP to the handle
packet function. The handle_packet function then checks the type of the message
an passes the packet to the correct function to handle the type of message.

The update messages are sent to the update function. This saves the packet
in the updates data structure. The APATH is then manipulated to include
the current ASN. The routes table is then updated to include the packet
at the source IP as an index. Once the source and destination of the packet
are updated the packet is sent.

If the message is a dump message, the forwarding table is built into a message
and it is sent back to the source IP which asked for the dump message.

For the forward data message type, the program uses the get_route function 
to return the best route for a given data packet and destination. This get_route
function uses the lookup_routes function to get the route for the destination
address for the data and sends the data with the forward function.



