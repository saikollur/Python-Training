import multiprocessing

def server(connection):
    connection.send("Server connection established.")
    connection.close()
def client(connection):
    print("Message from server: ",connection.recv())

if __name__ == "__main__":
    ser,cli = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=server, args=(ser,))
    p2 = multiprocessing.Process(target=client, args=(cli,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
