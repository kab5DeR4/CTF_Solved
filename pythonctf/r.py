import base64

# Replace with the two base64 strings from 'strings Gandalf.jpg'
str1_b64 = "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"
str2_b64 = "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"

bytes1 = base64.b64decode(str1_b64)
bytes2 = base64.b64decode(str2_b64)

xor_result = bytes(a ^ b for a, b in zip(bytes1, bytes2))
flag = xor_result.decode('ascii')
print(flag)
