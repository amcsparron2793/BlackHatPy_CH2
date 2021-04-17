import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("[*] Listening on {bind_ip}:{bind_port}".format(bind_ip=bind_ip, bind_port=bind_port))


# client-handling thread
def handle_client(client_socket):
    # print what the client sends
    request = client_socket.recv(1024)

    print("[*] Received: {req}".format(req=request))

    # send back a packet
    client_socket.send("HELLOOO CLIENT FROM SERVER")

    client_socket.close()


while True:
    client, addr = server.accept()

    print("[*] Accepted connection from: {addr0}:{addr1}".format(addr0=addr[0], addr1=addr[1]))

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
    # FIXME: if the server is stopped using the stop button, then the program fails with
    #  File "/root/Desktop/BlackHatPython/ch2/stdMultiThreadTCPServer.py", line 30, in <module>
    #     client, addr = server.accept()
    #   File "/usr/lib/python2.7/socket.py", line 206, in accept
    #     sock, addr = self._sock.accept()
    #  KeyboardInterrupt
