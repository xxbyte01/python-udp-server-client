/****************************************************************
 * Author: Suchin T.
 * Date: 10 Sep 2024
 * Version 0.1
 * Description: Draft for Client UDP Application by C++
 * 
 * Remark : This code is complied by MinGW and run on windows OS
 *     While compling and linking, ws2_32.lib file is needed.
 *     Thus command line option must be neccessary as shown bleow
 * 
 *     c:\>g++ -o cli.exe client.cpp -lws2_32
 *  
 ****************************************************************/


#include <iostream>
#include <winsock2.h>
#include <string>

#define SERVER_IP_ADDR "127.0.0.1"
#define SERVER_PORT 5000
#define BUFFER_LEN 1024
#define VERSION "0.1"
#define MAX_MESSAGE_LENGTH 100

int main() {
    WSADATA wsaData;
    int iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (iResult != 0) {
        std::cerr << "WSAStartup failed with error: " << iResult << std::endl;
        return 1;
    }

    // Create a socket
    SOCKET sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock == INVALID_SOCKET) {
        std::cerr << "socket failed with error: " << WSAGetLastError() << std::endl;
        WSACleanup();
        return 1;

    }

    //Assigned Sever IP address and Port
    sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = inet_addr(SERVER_IP_ADDR);
    server_addr.sin_port = htons(SERVER_PORT);

    std::cout << "UDP Client C++ version: " << VERSION << std::endl; 
    std::cout << "Set Server IP: " << SERVER_IP_ADDR << " & Server Port: " << SERVER_PORT <<std::endl;
    std::cout << "Type sending message, within 10 charactors below ..." << std::endl;
    
    do{
         int end_index = 0;
         std::string message;
         std::getline(std::cin, message);
         const char* sendBuf = message.c_str();

         for(int i = 0; i < MAX_MESSAGE_LENGTH; i++)
         {
           if(sendBuf[i] != '\0')
           {
              //std::cout << "textBuf[" << i << "]= " << textBuf[i] << " ; "; 
           }
           else
           {
              end_index = i;
              break;
           }
        }
    
        iResult = sendto(sock, sendBuf, end_index, 0, (sockaddr*)&server_addr, sizeof(server_addr));
        if (iResult == SOCKET_ERROR)
        {
           std::cerr << "sendto failed with error: " << WSAGetLastError() << std::endl;
           closesocket(sock);
           WSACleanup();
           return 1;
        }
        else
        {
           std::cout<<"Sendto iResult = "<< iResult <<std::endl;
        }

        // Receive a message (optional)
        char recvBuf[BUFFER_LEN];
        int recvLen = sizeof(recvBuf);
        sockaddr_in senderAddr;
        int senderAddrLen = sizeof(senderAddr);

        iResult = recvfrom(sock, recvBuf, recvLen, 0, (sockaddr*)&senderAddr, &senderAddrLen);
        if (iResult == SOCKET_ERROR)
        {
           std::cerr << "recvfrom failed with error: " << WSAGetLastError() << std::endl;
        } 
        else 
        {
           char* server_IP = inet_ntoa(senderAddr.sin_addr);
           short server_port  = ntohs(senderAddr.sin_port);
           recvBuf[iResult] = '\0';
           std::cout << "server_IP : " << server_IP << std::endl;
           std::cout << "server_port : " << server_port << std::endl;
           std::cout << "Received: " << recvBuf << std::endl;
           std::cout << "*********************************************" << std::endl;
        }
        // Just decision to quite out of loop
        auto exit_loop = message.compare("exit");

        if( exit_loop == 0)
        {
           std::cout << "exit_loop Done..." << std::endl;
           break;
        }

    }while(true);
    // Close the socket
    closesocket(sock);
    WSACleanup();
    return 0;
}