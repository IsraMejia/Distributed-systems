from client import Client
from server import Server

def calculate_time_difference(client_time, server_time):
    client_minutes = client_time[0] * 60 + client_time[1]
    server_minutes = server_time[0] * 60 + server_time[1]
    return client_minutes - server_minutes

def main():
    client1 = Client("Client 1", 20)
    client2 = Client("Client 2", -10)
    server = Server()

    server_time = server.get_current_time()
    print("Server time:", server_time)

    client1_time = client1.get_current_time()
    print("Client 1 time:", client1_time)

    client2_time = client2.get_current_time()
    print("Client 2 time:", client2_time)

    difference_client1 = calculate_time_difference(client1_time, server_time)
    print("Difference Client 1:", difference_client1)

    difference_client2 = calculate_time_difference(client2_time, server_time)
    print("Difference Client 2:", difference_client2)

if __name__ == "__main__":
    main()
