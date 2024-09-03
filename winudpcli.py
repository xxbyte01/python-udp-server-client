# Author: Suchin Th.
# Date : 03 Sep 2024
# Version : 0.1
# Description: Draft for Windows UDP Client

from tkinter import *
import socket

VERSION = 0.1


m_Win_Client = Tk()
m_Win_Client.geometry("450x450")
m_Win_Client.title(f"Win Client ver. {VERSION}")

m_Frame_First = Frame(m_Win_Client)
m_Frame_First.pack()

m_Label_Server_IP = Label(m_Frame_First,text="Server IP :")
m_Label_Server_IP.grid(column=0,row=0,sticky=W)

m_Text_Server_IP = Text(m_Frame_First)
m_Text_Server_IP.insert(END,"127.0.0.1")
m_Text_Server_IP.grid(column=1,row=0,sticky=W)
m_Text_Server_IP.configure(height=1,width=20)

m_Label_Server_Port = Label(m_Frame_First,text="Server Port :")
m_Label_Server_Port.grid(column=0,row=1,sticky=W)

m_Text_Server_Port = Text(m_Frame_First)
m_Text_Server_Port.insert(END,"5000")
m_Text_Server_Port.grid(column=1,row=1,sticky=W)
m_Text_Server_Port.configure(height=1,width=20)

m_Frame_Second = Frame(m_Win_Client)
m_Frame_Second.pack()

m_Label_Display = Label(m_Frame_Second,text="Display :")
m_Label_Display.grid(row=0,column=0)

m_Text_Display = Text(m_Frame_Second)
m_Text_Display.configure(height=5,width=40)
m_Text_Display.grid(row=0,column=1)

m_Label_Edit = Label(m_Frame_Second,text="Edit :")
m_Label_Edit.grid(row=1,column=0)

m_Text_Edit = Text(m_Frame_Second)
m_Text_Edit.configure(height=5,width=40)
m_Text_Edit.grid(row=1,column=1)

m_Button_Send = Button(m_Frame_Second,text="Send")
m_Button_Send.grid(row=2,column=0)

# function

def Click_Button_Send(event):
    Server_IP = m_Text_Server_IP.get('1.0',END)[:-1]
    Server_Port = int(m_Text_Server_Port.get('1.0',END)[:-1])
    Server_Address = (Server_IP,Server_Port)
    print(f'Server_Address : {Server_Address}')
    
    buffer_send = (m_Text_Edit.get('1.0',END)[:-1]).encode()
    print(f"buffer_send = {buffer_send.decode()}")
    client = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    client.sendto(buffer_send,Server_Address)
    buffer_read, return_address = client.recvfrom(1024)
    m_Text_Display.delete('1.0',END)
    m_Text_Display.insert(END,str(return_address) + '\n')
    m_Text_Display.insert(END,buffer_read.decode() + '\n')
    m_Text_Display.insert(END,"*****************" + '\n')
    client.close()

    # // m_Text_Display.insert(END,Server_IP)
    # // m_Text_Display.insert(END,Server_Port)
# Map function with events

m_Button_Send.bind('<Button-1>',Click_Button_Send)

m_Win_Client.mainloop()
