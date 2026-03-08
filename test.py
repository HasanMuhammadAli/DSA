import sys

def get_total_list_memory(list_data):
    """Calculates the total memory size (in bytes) of the list and its contents."""
    
    # 1. Start with the size of the list object itself
    total_size = sys.getsizeof(list_data)
    print(total_size)
    
    # 2. Add the size of each item (this accounts for different data types)
    for item in list_data:
        total_size += sys.getsizeof(item)
        print(sys.getsizeof(item))
    return total_size

# Example with different data types
mixed_list = [100, "hello", 3.14159, (1, 2)]

total_memory = get_total_list_memory(mixed_list)
print(f"Total memory consumed by the list and its elements: {total_memory} bytes")