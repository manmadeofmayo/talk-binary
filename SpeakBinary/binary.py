def to_bin(st):
    toReturn = ""
    for char in st:
        char = ord(char)
        size = 128
        byte = ""
        for i in range(8):
            if char >= size:
                byte +="1"
                char -= size
            else: byte += "0"
            size /= 2
        toReturn += byte + " " 

    return toReturn

def from_bin(st):
    vals = st.split(" ")
    toReturn = ""
    for val in vals:
        if val: toReturn += str(unichr(int(val, 2)))
    return toReturn
        
