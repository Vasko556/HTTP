import socket


def main():

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, _= server_socket.accept()

    with conn:
        msg = conn.recv(1024).decode()
        substring = "GET / "
        substring2 = "/echo/"
        substring3 = "/user-agent"
       
        if msg.__contains__ (substring):
            data = "HTTP/1.1 200 OK\r\n\r\n"
        
        elif msg.__contains__(substring2):
            content2 = msg.split("/echo/", 1)[-1]       #from where to cut
            info = content2.split(" HTTP/1.1", 1)[0]    #until where to cut 
            data = "HTTP/1.1 200 OK\r\n" + "Content-Type: text/plain\r\n" + "Content-Length: "+ str(len(info)) + "\r\n\r\n" + str(info)
        
        elif msg.__contains__(substring3):
            content2 = msg.split("Agent: ", 1)[-1]
            info = content2.split("\r\nAccept-Encoding:", 1)[0]
            data = "HTTP/1.1 200 OK\r\n" + "Content-Type: text/plain\r\n" + "Content-Length: "+ str(len(info)) + "\r\n\r\n" + str(info)
        
        else: 
            data = "HTTP/1.1 404 Not found\r\n\r\n"
       
        conn.send(data.encode("utf-8"))
if __name__ == "__main__":
    main()