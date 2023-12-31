def xor(x, s):
  print(bin(x), " xor ", bin(s), " = ", bin(x^s))

xor(4, 8)

xor(4, 4)

xor(255, 1)

# Implementing one time pad

import random

def generate_key_stream(n): #psedudo random numbers
  return bytes([random.randrange(0, 256) for i in range(n)])

def xor_bytes(key_stream, message):
  length = min(len(key_stream), len(message))
  return bytes([key_stream[i]^message[i] for i in range(length)])

message = "YOU ARE AWESOME"
message = message.encode()

key_stream = generate_key_stream(len(message))

cipher = xor_bytes(key_stream, message)

print(cipher)

print(xor_bytes(key_stream, cipher))

# This is done by the enemy
message = "DO ATTACK"
message = message.encode()
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, message)

# This is us trying to break it

print(cipher)

message = "NO ATTACK"

message = message.encode()
guess_key_stream = xor_bytes(message, cipher)
print(xor_bytes(guess_key_stream, cipher))

# Therefore it illustrates that the one-time pad is unbreakable.

