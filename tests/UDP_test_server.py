# Server code used on the ubuntu VM to host test server

import socket 

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("0.0.0.0", 9999))

while True:
    data, address = server.recvfrom(1024)

    print(f"Address : {address} Data : {data}")

    server.sendto(b"MININNAP RESPONSE", address)