#Q8. Write python code to demonstrate binary datatypes.

# Bytes Example

print("Bytes Example:")
b = bytes([65, 66, 67, 68])
print(b)

for byte in b:
    print(byte, end=' ')

# Bytearray Example

print("\n\nBytearray Example:")
ba = bytearray([65, 66, 67, 68])
print(ba)

# Memoryview Example

print("\nMemoryview Example:")
b_mv = bytes([65, 66, 67, 68, 69])
print(b_mv)

print("\nThis program is executed by Niharika")