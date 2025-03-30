import random 

def hamming_encode(data):

    encoded_message = "".join([format(ord(i), '08b') for i in data])
    data = list(map(int, list(encoded_message)))
    binary_data = data.copy()

    n = len(data)

    r = 0
    while n > 2**r - r - 1:
        r += 1

    total_bits = n+r

    parity_bits = [i for i in range(r)]
    parity_positions = [2**i-1 for i in range(r)]
    # print(parity_positions)

    bits = [None]*total_bits
    for i in range(total_bits):
        bits[i] = data.pop(0) if i not in parity_positions else -1
    # print(bits)

    bin_positions = [i+1 for i in range(n+r)]
    f = '0{}b'.format(r)
    bin_positions = [format(i, f) for i in bin_positions]
    # print(bin_positions)


    for i, bit in enumerate(bits): # iterate over all bits n+r
        # print(i, bit)
        if i in parity_positions: # if is parity bit
            curr_parity_pos = i+1 # parity bit 0 indexed to 1 indexed
            f = '0{}b'.format(r) 
            curr_parity_pos_bin = format(curr_parity_pos, f)
            index = curr_parity_pos_bin.find("1")
            # print("index", index)
            indexes = []
            for j, bin_bit in enumerate(bin_positions):
                if bin_bit[index] == "1":
                    indexes.append(j)
            xor = bits[indexes[1]]
            for k in indexes[2:]:
                xor =  xor ^ bits[k]
            # print("xor", xor)
            bits[i] = xor

    return "".join(str(bit) for bit in bits)


def hamming_decode(bits):

    bits = list(map(int, list(bits)))

    max_n = len(bits)

    parity_positions = [2**i-1 for i in range(max_n)]
    while parity_positions[-1]>=max_n:
        parity_positions.pop()
    # print(parity_positions)

    r = len(parity_positions)
    n = max_n - r

    bin_positions = [i+1 for i in range(n+r)]
    f = '0{}b'.format(r)
    bin_positions = [format(i, f) for i in bin_positions]
    # print(bin_positions)

    syndrome = ""

    for i, bit in enumerate(bits): # iterate over all bits n+r
        # print(i, bit)
        if i in parity_positions: # if is parity bit
            curr_parity_pos = i+1 # parity bit 0 indexed to 1 indexed
            f = '0{}b'.format(r) 
            curr_parity_pos_bin = format(curr_parity_pos, f)
            index = curr_parity_pos_bin.find("1")
            indexes = []
            for j, bin_bit in enumerate(bin_positions):
                if bin_bit[index] == "1":
                    indexes.append(j)
            xor = bits[indexes[0]]
            for k in indexes[1:]:
                xor =  xor ^ bits[k]
            # print("xor", xor)
            syndrome += str(xor)

    syndrome = syndrome[::-1]
    error_position = int(syndrome, base=2)
    if error_position!=0:
        bits[error_position-1] ^= 1
    # print(bits)


    decoded_message = []
    for i in range(len(bits)):
        if i not in parity_positions:
            decoded_message.append(bits[i])

    # print(decoded_message)

    bin_string = ""
    string = ""
    for i, bit in enumerate(decoded_message):
        bin_string += str(bit)

    for i in range(0, len(bin_string), 8):
        string += chr(int(bin_string[i:i+8], 2))

    return string


def flip_random_bit(data):
    random_pos = random.randint(0, len(data)-1)

    bit = data[random_pos]
    flipped_bit = "1" if bit=="0" else "0"
    changed_bits = data[:random_pos] + flipped_bit + data[random_pos+1:]

    return random_pos, changed_bits
                    
        