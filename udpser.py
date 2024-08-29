import socket

IP = "127.0.0.1"
PORT = 5000
buffer_size = 1024

UDP_Server = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
Server_Address = (IP,PORT)
UDP_Server.bind(Server_Address)
print("UDP Server running...")
print(f"listening ... address {Server_Address}")

while True:
    client_message_bytes, client_address = UDP_Server.recvfrom(buffer_size)
    client_message = client_message_bytes.decode()
    


    server_msg = "echo " + client_message
    server_bytes = server_msg.encode()
    number_byte_send = UDP_Server.sendto(server_bytes,client_address)
    print(f'number_byte_send = {number_byte_send}')
    print(f"UDP_Server Address : {UDP_Server.getsockname()}")
    print(f"client_message : {client_message}")
    print(f"client_address : {client_address}")
    print("********************************************")
    if client_message == "exit":
        break
UDP_Server.close()
print('UDP_Server close()')