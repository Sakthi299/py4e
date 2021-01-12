x = b'sakthi'
print(type(x))

# encode and decode methods
# bytes.decode(encoding="utf-8", errors="strict")
# str.encode(encoding="utf-8", errors="strict")

original = 'sakthi'
print("Original Type : " + str(type(original)))
sentdata = original.encode(encoding="utf-8")
print("SentData Type : " + str(type(sentdata)))
receivedata = sentdata.decode(encoding="utf-8")
print("ReceivedData Type : " + str(type(receivedata)))

x = u'sakthi'
print(type(x))