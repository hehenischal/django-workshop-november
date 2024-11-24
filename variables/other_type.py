# Byte sequences: Immutable sequence of bytes
byte_sequence = bytes([50, 100, 150])
print(f"Bytes: {byte_sequence}")

# Bytearray: Mutable sequence of bytes
mutable_byte_sequence = bytearray([50, 100, 150])
print(f"Bytearray: {mutable_byte_sequence}")

# Memoryview: Sequence of memory buffer
memory_view = memoryview(byte_sequence)
print(f"Memoryview: {memory_view.tolist()}")