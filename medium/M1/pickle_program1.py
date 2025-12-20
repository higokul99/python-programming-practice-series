import pickle

data = {
    1: 'a',
    2: 'b',
    3: 'c'
    }

print("OG:",data)
bytestream = pickle.dumps(data)
print("ByteStream:",bytestream)


restoredata = pickle.loads(bytestream)
print(restoredata)
