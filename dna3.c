#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Define the filename and the number of lines (x) in the file
    const char* filename = "short_read.txt";
    int x = 56642; // Replace with the actual number of lines in your file

    // Attempt to open the file
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Allocate memory for an array of strings to store the lines
    char** lines = (char**)malloc(x * sizeof(char*));
    if (lines == NULL) {
        perror("Memory allocation error");
        return 1;
    }

    // Read lines from the file and store them in the array
    for (int i = 0; i < x; i++) {
        char buffer[256]; // Adjust buffer size as needed
        if (fgets(buffer, sizeof(buffer), file) == NULL) {
            // End of file reached
            break;
        }

        // Allocate memory for the line and copy it
        lines[i] = strdup(buffer); // Requires <string.h>
    }

    // Close the file
    fclose(file);

    // Now, 'lines' contains the first 'x' lines from the file
    // You can access them like this:
    for (int i = 0; i < x; i++) {
        if (lines[i] != NULL) {
            printf("Line %d: %s", i + 1, lines[i]);
            free(lines[i]); // Free allocated memory for each line
        }
    }

    // Free the array of strings and exit
    free(lines);
    return 0;
}
