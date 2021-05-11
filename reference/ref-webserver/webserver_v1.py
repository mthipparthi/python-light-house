import socket

HOST, PORT = "", 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print(f"Server is listening on PORT {PORT}")

while True:
    connection, address = server.accept()
    requested_data = connection.recv(1024)
    print(requested_data.decode("utf-8"))

    response = b"""\
    HTTP/1.1 200 OK

    Hello, World!
    """
    connection.sendall(response)
    connection.close()

