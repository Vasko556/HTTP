import socket
import threading 


server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
conn, _= server_socket.accept()

def main(conn):

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
        
t = threading.Thread(target=main, args=(conn,))
t.start()
conn2, _= server_socket.accept()
t2 = threading.Thread(target=main, args=(conn2,))
t2.start()
conn3, _= server_socket.accept()
t3 = threading.Thread(target=main, args=(conn3,))
t3.start()