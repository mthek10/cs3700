Name: Mark Thekkethala
Language: Python
Date: January 24, 2020

Overview:

Reads in parameters for neu_id, host_ip, port
Creates socket
Connects to socket using parameters
Sends Initial HELLO message

Loops through receiving messages from SERVER until BYE message 
Either FIND or BYE message
Applies the COUNT method and sends the message if FIND is found

Print out the secret_flag returned from the BYE message (could be flag or "Unknown_Husky_ID")
