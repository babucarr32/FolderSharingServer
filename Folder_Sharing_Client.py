import socket  # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
# host = socket.gethostname()  # Get local machine name
host = "localhost"
port = 55555  # Reserve a port for your service.
s.bind((host, port))  # Bind to the port

# file = input("Enter file path: ")
# file_Conc = f'"{file}"'
# file_to_send = "r" + file_Conc



s.listen(5)  # Now wait for client connection.
while True:
    print("Listening...")
    c, addr = s.accept()  # Establish connection with client.
    print("-" * 20)
    print('Got connection from', addr)
    print("Receiving...")
    # print(f"Sending {file_to_send}")
    print("-" * 20)
    print("\n")

    l = c.recv(10000024)
    while (l):
        print("Receiving...")

        # for i in range(3):
        f = open(r"C:\Users\USER\Desktop" + "\\" + "file" + ".rar", 'wb')

        f.write(l)
        f.close()

        decoder = l.decode('ansi')
        if decoder == "nothing":
            print("Done Receiving The Program Will Quit Very Soon.")
            c.send(bytes('Thank you for connecting', encoding="utf-8"))
            c.close()  # Close the connection
            quit()
        l = c.recv(10000024)
