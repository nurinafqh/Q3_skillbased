import random
import threading
import socket

#array of quotes
quotes = ["When you reach the end of your rope, tie a knot in it and hang on. -Franklin D. Roosevelt",
"“The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
"“Life is either a daring adventure or nothing at all. -Helen Keller",
"“Life is what happens when you're busy making other plans. -John Lennon",
"“Never let the fear of striking out keep you from playing the game. -Babe Ruth"]

#random quotes from array and send to client
def handle_client(sockfd):
    quote = random.choice(quotes)
    sockfd.sendall(quote.encode())
    sockfd.close()

def main():
    #server ip and port
    bind_ip = "192.168.68.102" 
    bind_port = 8888

    #create and bind socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((bind_ip, bind_port))

    #listen for client
    server.listen(5)
    print("Listen on %s:%d for request" % (bind_ip, bind_port))

    #start connections and execute handle_client function
    while True:
        client, addr = server.accept()
        print("Accepting connection from %s" % str(addr))
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
        
#call main function
main()