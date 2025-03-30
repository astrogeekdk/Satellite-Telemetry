import numpy

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
    
packet = TelemetryPacket()
bits = packet.serialize()
print(bits)
print(decode(bits))