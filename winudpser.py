# Author: Suchin Th.
# Date 01 Sep 2024
# version 0.1
# Description: Draft of win-udp-server.

from tkinter import *
import socket
import threading
VERSION = "0.1"

Server_Port = 5000
Server_IP = "127.0.0.1"
Server_Address = (Server_IP,Server_Port)

m_Edit_Color = 0

win = Tk()
win.title(f"Win UDP Server {Server_Address} ver. {VERSION} ")
win.geometry("450x700")
m_Edit = Text(master=win,)
m_Edit.config(height=40,width=50)
m_Edit.pack()
button_clear = Button(master=win,text="Clear",bg="gray")
button_clear.pack()

# function button event handler
def Click_Button_Clear(event):
    m_Edit.delete("1.0",END)

def Server_Recv(text_box):

      buffer_size = 1024
      server = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
      server.bind(Server_Address)
      while(True):
        client_message_byte, client_address = server.recvfrom(buffer_size)
        
        server_acknowledge_message = "server acknowledge"
        server_acknowledge_byte = server_acknowledge_message.encode()
        server.sendto(server_acknowledge_byte,client_address)

        client_message = client_message_byte.decode()
        
        text_box.insert(END,str(client_address) + '\n')
        text_box.insert(END,client_message + '\n')
        text_box.insert(END,"**************" + '\n')
        if client_message == "exit":
           break
      server.close()
      print("server close ()")
      win.title(f"Server Close () ... ver. {VERSION}")

x = threading.Thread(target=Server_Recv,args=(m_Edit,))
x.start()

# Map function and event handler
button_clear.bind('<Button-1>',Click_Button_Clear)

win.mainloop()
