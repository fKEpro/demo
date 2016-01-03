import bz2
MESSAGE = "hello"
compressed_message = bz2.compress(MESSAGE.encode("utf-8"))
decompressed_message = bz2.decompress(compressed_message)
print ("original:", repr(MESSAGE))
print ("compressed message:",
repr(compressed_message))
print ("decompressed message:",repr(decompressed_message.decode("utf-8")))