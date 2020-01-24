import socket

neu_id = '001880538'
host_ip = 'fring.ccs.neu.edu'
port = 27993
tup1 = (host_ip, port)

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Connect to an IP with Port, could be a URL
s.connect(tup1)

## Send some data, this method can be called multiple times
m1 = 'cs3700spring2020 HELLO ' + neu_id + '\n'
s.sendall(m1.encode('ascii'))

from_server = ''
continue_recv = True
find_continue_recv = True

# Loop while FIND message are being sent from Server
while find_continue_recv:
  ##### GET SERVER MESSAGE ######
  while continue_recv:
    ## Receive up to 4096 bytes from a peer
    curMessage = s.recv(8192)
    from_server += curMessage.decode('ascii')
    newline_count = from_server.count("\n", 0, len(from_server))
    if newline_count > 0:
      continue_recv = False

  # If server responds with another find message reply with count
  find_count = from_server.count("FIND",0,len(from_server)) 
  if find_count > 0:
    ##### SEND COUNT MESSAGE ######
    key = from_server[22]
    key_count = from_server.count(key, 23, len(from_server))
    m2 = 'cs3700spring2020 COUNT ' + str(key_count) + '\n'
    s.sendall(m2.encode('ascii'))
    m2 = ''
    m1 = ''
    from_server = ''
    continue_recv = True
  # If server responds with BYE message print secret key
  else: 
    bye_count = from_server.count("BYE",0,len(from_server))
    if  bye_count > 0:
      if from_server.split(' ')[2] == 'Unknown_Husky_ID':
        print("Unknown_Husky_ID")
      else:
        print(from_server.split(' ')[2].replace('\n',''))
      find_continue_recv = False;

## Close the socket connection, no more data transmission
s.close()
