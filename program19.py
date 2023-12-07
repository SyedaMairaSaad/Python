import socket, ssl

HOST = "www.psx.com.pk"
PORT = 443

#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s_sock = context.wrap_socket(s, server_hostname=HOST)
#s_sock.connect((HOST, 443))

socketHandler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock = ssl.create_default_context().wrap_socket(socketHandler, server_hostname=HOST)
s_sock.connect((HOST, 443))
s_sock.send("GET / HTTP/1.1\r\nHost: www.psx.com.pk\r\n\r\n ".encode())

while True:
    data = s_sock.recv(2048)
    if ( len(data) < 1 ) :
        break
    print(data)

s_sock.close()