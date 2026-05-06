import socket
import threading

# Ports that will be opened
ports = [8080, 5000, 6000]

def handle_client(conn, addr):
    print("Client connected:", addr)

    try:
        data = conn.recv(1024)

        # Send HTTP-style banner for service detection
        response = b"HTTP/1.1 200 OK\r\nServer: UbuntuTestServer\r\n\r\nHello"
        conn.send(response)

    except:
        pass

    conn.close()

def start_server(port):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(("0.0.0.0", port))
    server.listen(5)

    print("Listening on port:", port)

    while True:
        conn, addr = server.accept()

        client_thread = threading.Thread(
            target=handle_client,
            args=(conn, addr)
        )

        client_thread.start()

# Start servers on multiple ports
for port in ports:
    threading.Thread(target=start_server, args=(port,)).start()

print("Servers running....")