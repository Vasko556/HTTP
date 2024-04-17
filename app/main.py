import socket
import threading 


server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
conn, _= server_socket.accept()

def main(conn):

    while True:
            
            with conn:
                msg = conn.recv(1024)
                msg1 = msg[10:-90]
                msg2 = len(msg1)
                msg3 = msg1.decode("utf-8")
                user_agent = ""
                user_agent_split = ""
                if msg[0:6] == b'GET / ':
                    data = "HTTP/1.1 200 OK\r\n\r\n"
                elif msg[0:10] == b'GET /echo/':
                    data = "HTTP/1.1 200 OK\r\n" + "Content-Type: text/plain\r\n" + "Content-Length: " + str(msg2) + "\r\n\r\n" + str(msg3)
                elif msg[0:15].decode("utf-8") == 'GET /user-agent':
                    user_agent = msg.decode("utf-8").split("Agent: ", 1)[-1]
                    user_agent_split = user_agent.split("\r\nAccept-", 1)[0]
                    data = "HTTP/1.1 200 OK\r\n" + "Content-Type: text/plain\r\n" + "Content-Length: " + str(len(user_agent_split)) + "\r\n\r\n" + str(user_agent_split)

                else:
                    data = "HTTP/1.1 404 Not found\r\n\r\n"
                #print(msg1)
                #print(user_agent_split)
                #print(data)
                conn.send(data.encode("utf-8"))



#if __name__ == "__main__":

t = threading.Thread(target=main, args=(conn,))
t.start()
conn2, _= server_socket.accept()
t2 = threading.Thread(target=main, args=(conn2,))
t2.start()
conn3, _= server_socket.accept()
t3 = threading.Thread(target=main, args=(conn3,))
t3.start()
#main(conn,)
