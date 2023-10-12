# Open the input file
with open('long_read.txt', 'r') as input_file:
    # Read the content of the file
    content = input_file.read()

# Split the content into 16-letter strings
strings_16 = content.split()

# Initialize an empty list for 8-letter strings
strings_8 = []

# Iterate through the 16-letter strings and split them into 8-letter strings
for string in strings_16:
    for i in range(0, len(string), 8):
        strings_8.append(string[i:i+8])

# Open an output file for writing
with open('long_read_8.txt', 'w') as output_file:
    # Write the 8-letter strings to the output file
    for string in strings_8:
        output_file.write(string + '\n')
