import socket
import numpy
import time
from hamming import hamming_encode, flip_random_bit

class TelemetryPacket:
    def __init__(self):
            self.altitude = numpy.random.uniform(300, 400)
            self.velocity = numpy.random.uniform(5,10)
            self.battery_voltage = numpy.random.uniform(2, 4)
            self.temperature = numpy.random.normal(20, 5)

    def serialize(self):
        alt_bits = format(int(self.altitude * 10), '012b')
        vel_bits = format(int(self.velocity * 10), '07b')
        volt_bits = format(int(self.battery_voltage * 10), '07b')
        temp_bits = format(int((self.temperature + 273) * 10), '12b')

        binary_data = alt_bits + vel_bits + volt_bits + temp_bits
        return binary_data
    

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 9999)

print("Ground Station Live on ", server_address)

try:
    while True:

        packet = TelemetryPacket()
        data = packet.serialize()
        data = hamming_encode(data)
        _, data = flip_random_bit(data)
        print("Sending Packet:", data)
        print("--------------------")
        client_socket.sendto(str(data).encode(), server_address)

        # data, _ = client_socket.recvfrom(1024)
        # print(f"Server: {data.decode()}")
        time.sleep(1)


except:
    print("Error")

client_socket.close()