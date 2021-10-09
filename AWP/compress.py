import lz4.frame
def compress(data):
    print(data)
    print(lz4.frame.compress(data.encode()))
    return lz4.frame.compress(data.encode())

def decompress(data):
    print(data)
    print(lz4.frame.decompress(data))
    return lz4.frame.decompress(data).decode()

print('Hello World I like spaghetti fries and tomato fries and tomato fries')
print(lz4.frame.compress('Hello World I like spaghetti fries and tomato fries and tomato fries'.encode()))