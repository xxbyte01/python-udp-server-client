# Author: Suchin Th.
# Date 04 Sep 2024
# version 0.3
# Description: Set default value for textbox IP and textbox Port
#              , Implemented server message as echo client message  

from tkinter import *
from tkinter import messagebox
import socket
import threading
VERSION = "0.3"

Server_Port = 1000
Server_IP = "0.0.0.0"
# // Server_Address = (Server_IP,Server_Port)

win = Tk()
win.title(f"Win UDP Server ... ver. {VERSION} ")
win.geometry("450x500")
m_Edit = Text(master=win,)
m_Edit.config(height=10,width=50)
m_Edit.pack()

m_Fram_First = Frame(master=win)
m_Fram_First.pack()

m_Label_IP = Label(master=m_Fram_First,text="IP :")
m_Label_IP.grid(column=0,row=0)

m_Edit_IP = Text(master=m_Fram_First)
m_Edit_IP.config(height=1,width=50)
m_Edit_IP.grid(column=1,row=0)
m_Edit_IP.insert(END,"127.0.0.1")

m_label_Port = Label(master=m_Fram_First, text="Port :")
m_label_Port.grid(column=0,row=1)

m_Edit_Port = Text(master=m_Fram_First)
m_Edit_Port.config(height=1,width=50)
m_Edit_Port.grid(column=1,row=1)
m_Edit_Port.insert(END,"5000")

m_Fram_Second = Frame(master=win)
m_Fram_Second.pack()

m_Button_Start = Button(master=m_Fram_Second,text="Start", bg="green")
m_Button_Start.grid(column=0,row=0)
Server_Run_Flag = False

m_Button_Clear = Button(master=m_Fram_Second,text="Clear",bg="gray")
m_Button_Clear.grid(column=1,row=0)

# function button event handler

def Server_Recv(textbox):
      global Server_IP
      global Server_Port
      global Server_Run_Flag
      buffer_size = 1024
      server = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
      Server_Address = (Server_IP,Server_Port)
      print(Server_Address)
      server.bind(Server_Address)
      win.title(f"Win Server is running ... {Server_Address} ver. {VERSION}")
      Server_Run_Flag = True
      while(True):
        client_message_byte, client_address = server.recvfrom(buffer_size)
        
        server_acknowledge_message = "server echo : " + client_message_byte.decode()
        server_acknowledge_byte = server_acknowledge_message.encode()
        server.sendto(server_acknowledge_byte,client_address)

        client_message = client_message_byte.decode()
        
        textbox.insert(END,str(client_address) + '\n')
        textbox.insert(END,client_message + '\n')
        textbox.insert(END,"**************" + '\n')
        if client_message == "exit":
           break
      server.close()
      print("server close ()")
      win.title(f"Server Close () ... ver. {VERSION}")
      Server_Run_Flag = False

def Click_Button_Start(event):
      global Server_Run_Flag
      global Server_IP
      global Server_Port
      if Server_Run_Flag == False:
         # // if m_Edit_IP.get('1.0',END)[:-1] != "":
         Server_IP = m_Edit_IP.get('1.0',END)[:-1]
         # // if m_Edit_Port.get('1.0',END)[:-1] != "":
         Server_Port = int(m_Edit_Port.get('1.0',END)[:-1])
         x = threading.Thread(target=Server_Recv,args=(m_Edit,))
         x.start()
      else:
         messagebox.showinfo("warning","Server Thread is Running")
def Click_Button_Clear(event):
    m_Edit.delete("1.0",END)

# Map function and event handler
m_Button_Clear.bind('<Button-1>',Click_Button_Clear)
m_Button_Start.bind('<Button-1>',Click_Button_Start)
win.mainloop()
