import socket
from hamming import hamming_decode

def decode(bits):
    alt_bits = bits[:12]
    vel_bits = bits[12:19]
    volt_bits = bits[19:26]
    temp_bits = bits[26:]
      
    alt = int(alt_bits, 2)/10
    vel = int(vel_bits, 2)/10
    volt = int(volt_bits, 2)/10
    temp = int((int(temp_bits, 2)/10 - 273)*100)/100

    return alt, vel, volt, temp


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 9999)
server_socket.bind(server_address)

print("Live on ", server_address)

while True:
    try:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Data: {data.decode()}")
        decoded_data = hamming_decode(data.decode())
        alt, vel, volt, temp = decode(decoded_data)
        print("Altitude: ", alt)
        print("Velocity: ", vel)
        print("Battery Voltage: ", volt)
        print("Temperature Voltage: ", temp)
        print("--------------------")
        # response = "Message received!".encode()
        # server_socket.sendto(response, client_address)
    except:
        print("Error")
        break

server_socket.close()