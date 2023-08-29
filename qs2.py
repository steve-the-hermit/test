def remove_duplicates(sequence):
    unique_elements = []
    for item in sequence:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

# sequences