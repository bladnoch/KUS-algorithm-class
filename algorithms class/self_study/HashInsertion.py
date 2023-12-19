def hash_insert(T, k):
    m = len(T)  # Number of slots in the table
    i = 0
    while True:
        q = h(k, i)
        if T[q] is None:  # If the slot at index q is empty
            T[q] = k  # Insert the key k into the hash table at index q
            return q  # Return the index where the key was inserted
        else:
            i += 1  # Increment i and try the next slot
            if i == m:  # If we have tried all slots
                raise Exception("hash table overflow")  # The table is full

# Example hash function that uses linear probing
def linear_probing_hash(k, i, m):
    return (k + i) % m

def h(key, attempt):
    """
    선형 탐사를 사용하여 해시 충돌을 해결하는 함수.

    :param key: 삽입하려는 키.
    :param attempt: 현재 충돌 해결을 위한 시도 횟수..
    :return: 새로운 해시 인덱스.
    """
    return (key + attempt) % len(hash_table)

# Example usage:
# Create an empty hash table with 10 slots
hash_table = [None] * 10

# Insert a key into the hash table
index_inserted = hash_insert(hash_table, 23)
print(f"Key 23 inserted at index {index_inserted}")
print(hash_table)  # Show the current state of the hash table
