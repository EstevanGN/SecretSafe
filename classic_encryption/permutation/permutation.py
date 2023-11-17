import random

def generate_key(message, message_size):
    # Generate a random permutation key based on the length of the message
    key = list(range(message_size))
    random.shuffle(key)
    return key

def encrypt(message, key):
    # Ensure the key length matches the message length
    if len(key) != len(message):
        raise ValueError("Key length must match message length")
    encrypted_message = ['']*len(message)
    # Permute the characters in the message according to the key
    for i in range(len(message)):
        encrypted_message[key[i]] = message[i]
    return ''.join(encrypted_message)

def decrypt(encrypted_message, key):
    # Create a reverse key to decrypt the message
    reverse_key = revert_key(key)
    # Ensure the key length matches the encrypted message length
    if len(reverse_key) != len(encrypted_message):
        raise ValueError("Key length must match encrypted message length")
    return encrypt(encrypted_message, reverse_key)

# (1, 4, 5, 2, 3) -> (1, 4, 5, 2, 3)

def revert_key(key):
    reverted_key = [0]*len(key)
    for i, num in enumerate(key):
        reverted_key[num] = i
    return reverted_key


# Example usage:
message = "CRYPTOGRAPHY"
message_size = len(message)
key = generate_key(message, message_size)
reversed_key = revert_key(key)

print("The key is : ", str(key))
print("The reverse key is : ", str(reversed_key))

encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)