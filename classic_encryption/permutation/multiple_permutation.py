import permutation
import random

def generate_keys(list_permutations):
    keys_list = []
    for i in range(len(list_permutations)):
        key = list(range(list_permutations[i]))
        random.shuffle(key)
        keys_list.append(key)
    return keys_list

# JAKSHJAKHDJKA|SHDJKA|SHDKJA|SHDJ
# 15 -> 7 5 3
# 15 -> (1, 5, 4, 6, 7, 2, 3) (1, 4, 5, 2, 3) (3, 2, 1)

def random_partition_with_length(n, length):
    if n <= 0:
        raise ValueError("Input number must be greater than 0")
    if length <= 0:
        raise ValueError("Length must be greater than 0")
    partition = []
    remaining = n
    for _ in range(length - 1):
        # Generate a random integer between 1 and the remaining value
        value = random.randint(1, remaining - (length - len(partition) - 1))

        # Append the generated value to the partition
        partition.append(value)

        # Subtract the generated value from the remaining amount
        remaining -= value

    # The last element in the partition is the remaining amount
    partition.append(remaining)

    return partition

def multiple_encrypt(message, keys_list, list_permutations):
    starting_index = 0
    encrypted_message = ''
    for i in range(len(list_permutations)):
        temp_message = message[starting_index : starting_index + list_permutations[i]]
        encrypted_message += permutation.encrypt(temp_message, keys_list[i])
        starting_index += list_permutations[i]
    return encrypted_message

def multiple_decrypt(message, key_list, list_permutations):
    starting_index = 0
    decrypted_message = ''
    for i in range(len(list_permutations)):
        temp_message = message[starting_index : starting_index + list_permutations[i]]
        decrypted_message += permutation.decrypt(temp_message, key_list[i])
        starting_index += list_permutations[i]
    return decrypted_message

message = "CRYPTOGRAPHY"
random_partitions = random_partition_with_length(len(message), 3)
print("List of partitions: ", str(random_partitions))

list_keys = generate_keys(random_partitions)
print("List of keys: ", str(list_keys))

encrypted_message = multiple_encrypt(message, list_keys, random_partitions)
print("Encrypted message:", encrypted_message)

decrypted_message = multiple_decrypt(encrypted_message, list_keys, random_partitions)
print("Decrypted message:", decrypted_message)