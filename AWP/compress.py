import lz4.frame
def compress(data):
    return lz4.frame.compress(data.encode())

def decompress(data):
    return lz4.frame.decompress(data).decode()