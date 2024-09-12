/****************************************************************
 * Author: Suchin T.
 * Date: 12 Sep 2024
 * Version 0.1
 * Description: Draft for Server UDP Application by C++
 * 
 * Remark : This code is complied by MinGW and run on windows OS
 *     While compling and linking, ws2_32.lib file is needed.
 *     Thus command line option must be neccessary as shown bleow
 * 
 *     c:\>g++ -o serv.exe server.cpp -lws2_32
 *  
 ****************************************************************/

#include <iostream>
#include <winsock2.h>
#include <string>

#define SERVER_IP "127.0.0.1"
#define SERVER_PORT 5000
#define BUFFER_LENGTH 1024
#define MAX_SEND_BUFFER_LENGTH 100

#define VERSION "0.1"
//#pragma comment(lib, "ws2_32.lib")

int main() {
    WSADATA wsaData;
    int iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (iResult != 0) {
        std::cerr << "WSAStartup failed with error: " << iResult << std::endl;
        return 1;
    }

    // Create a socket
    SOCKET sock = socket(AF_INET, SOCK_DGRAM, 0); //IPPROTO_UDP);
    if (sock == INVALID_SOCKET) {
        std::cerr << "socket failed with error: " << WSAGetLastError() << std::endl;
        WSACleanup();
        return 1;

    }

    // Bind the socket to a local address and port
    sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = inet_addr(SERVER_IP);
    server_addr.sin_port = htons(SERVER_PORT); // Replace with desired port

    iResult = bind(sock, (sockaddr*)&server_addr, sizeof(server_addr));
    if (iResult == SOCKET_ERROR) {
        std::cerr << "bind failed with error: " << WSAGetLastError() << std::endl;
        closesocket(sock);
        WSACleanup();
        return 1;
    }

    // Receive a message (optional)
    char recv_buf[BUFFER_LENGTH];
    int recv_len = sizeof(recv_buf);
    sockaddr_in client_addr;
    int client_addr_len = sizeof(client_addr);

    std::cout << "UDP Server C++ version: " << VERSION << std::endl; 
    std::cout << "Set Server IP: " << SERVER_IP << " & Server Port: " << SERVER_PORT <<std::endl;
    std::cout << "Server is listening ..." << std::endl;

    while(true)
    {

    
      iResult = recvfrom(sock, recv_buf, recv_len, 0, (sockaddr*)&client_addr, &client_addr_len);
      if (iResult == SOCKET_ERROR) {
          std::cerr << "recvfrom failed with error: " << WSAGetLastError() << std::endl;
      } else {
          char* address = inet_ntoa(client_addr.sin_addr);
          u_short port = ntohs(client_addr.sin_port);
          recv_buf[iResult] = '\0';
          std::cout << "client address : " << address << std::endl;
          std::cout << "client port : " << port << std::endl; 
          std::cout << "Received: " << recv_buf << std::endl;
          std::cout << "*********************************************" << std::endl;
      }

      // Send a message
      std::string send_msg = "server echo: ";
      send_msg.append(recv_buf);

      const char* send_buf = send_msg.c_str();
      int send_buf_len = 0;
      for(int i = 0; i < MAX_SEND_BUFFER_LENGTH; i++ )
      {
        if(send_buf[i] == '\0')
        {
           send_buf_len = i;
           break;
        }
      }
      iResult = sendto(sock, send_buf, send_buf_len, 0, (sockaddr*)&client_addr, sizeof(client_addr));
      if (iResult == SOCKET_ERROR) 
      {
          std::cerr << "sendto failed with error: " << WSAGetLastError() << std::endl;
          closesocket(sock);
          WSACleanup();
          return 1;
      }

      // check to exit loop
      if(strcmp(recv_buf,"exit") == 0 )
      {
        std::cout << "exit_loop Done..." << std::endl;
        break;
      }
    }
    // Close the socket
    closesocket(sock);
    WSACleanup();
    return 0;
}