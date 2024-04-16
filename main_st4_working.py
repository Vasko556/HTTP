import socket

def main():

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, _= server_socket.accept()
    with conn:
        msg = conn.recv(1024)
        msg1 = msg[10:-90]
        msg2 = len(msg1)
        msg3 = msg1.decode("utf-8")
        if msg[0:6] == b'GET / ':
            data = "HTTP/1.1 200 OK\r\n\r\n"
        elif msg[0:10] == b'GET /echo/':
            data = "HTTP/1.1 200 OK\r\n" + "Content-Type: text/plain\r\n" + "Content-Length: " + str(msg2) + "\r\n\r\n" + str(msg3)

        else:
            data = "HTTP/1.1 404 Not found\r\n\r\n"
        print(data)
        conn.send(data.encode("utf-8"))
        

if __name__ == "__main__":
    main()
