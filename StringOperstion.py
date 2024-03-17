# Define the original string
original_string = "Hello guys from einfochips"

# Perform string slicing to extract parts of the string
sliced_part_1 = original_string[0:5]  # Slicing from index 0 to 4 (5 is exclusive)
sliced_part_2 = original_string[6:10]  # Slicing from index 6 to 9 (10 is exclusive)
print("Sliced Part 1:", sliced_part_1)
print("Sliced Part 2:", sliced_part_2)

# Perform string concatenation
concatenated_string = sliced_part_1 + " " + sliced_part_2 
print("Concatenated String:", concatenated_string)

# Access individual characters using indexing
first_character = original_string[0]
last_character = original_string[-1]
print("First Character:", first_character)
print("Last Character:", last_character)

# Reverse the string using slicing
reversed_string = original_string[::-1]
print("Reversed String:", reversed_string)
