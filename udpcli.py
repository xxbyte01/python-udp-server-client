import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000
buffer_size = 1024

UDP_Client = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
print("UDP_Client running ...")
print(f"-- client to server address {SERVER_IP} port {SERVER_PORT}")
while(True):
  message_send = input("Enter:")
  buffer_send = message_send.encode()

  number_byte_send = UDP_Client.sendto(buffer_send,(SERVER_IP,SERVER_PORT))
  print(f'number_byte_send = {number_byte_send}')

  recv_bytes, server_address = UDP_Client.recvfrom(buffer_size)
  recv_message = recv_bytes.decode()
  print(f"Client_Address : {UDP_Client.getsockname()}")
  print(f"server_address = {server_address}")
  print(f"server message = {recv_message}")
  print("****************************************")
  if message_send == "exit":
    break
UDP_Client.close()
print("UDP_Client close()")