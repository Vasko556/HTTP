# Uncomment this to pass the first stage

import socket

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, _ = server_socket.accept()
    with conn:
        msg = conn.recv(1024)
        print(msg[0:6])
        if msg[0:6] == b"GET / ":
            data = "HTTP/1.1 200 OK\r\n\r\n"
        else:
            data = "HTTP/1.1 404 Not found\r\n\r\n"
        conn.send(data.encode("utf-8"))
if __name__ == "__main__":

    main()