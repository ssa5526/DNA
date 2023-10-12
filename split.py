# Open the input file
with open('long_read_8.txt', 'r') as input_file:
    # Read the content of the file
    content = input_file.read()

# Split the content into 8-letter strings
strings_8 = content.split()

# Initialize an empty list for 4-letter strings
strings_4 = []

# Iterate through the 8-letter strings and split them into 4-letter strings
for string in strings_8:
    for i in range(0, len(string), 4):
        strings_4.append(string[i:i+4])

# Open an output file for writing
with open('long-read_4.txt', 'w') as output_file:
    # Write the 4-letter strings to the output file
    for string in strings_4:
        output_file.write(string + '\n')