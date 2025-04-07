def modify_file(filename, new_filename):
    """Reads a file, modifies its content, and writes to a new file, then prints the new file's contents."""
    try:
        with open(filename, 'r') as infile, open(new_filename, 'w') as outfile:
            for line in infile:
                modified_line = line.upper() # Example modification
                outfile.write(modified_line)

        # Print the contents of the new file
        print(f"\nContents of '{new_filename}':")
        with open(new_filename, 'r') as outfile: # Open the new file again for reading
            print(outfile.read())

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    filename = input("Enter the input filename: ")
    new_filename = input("Enter the output filename: ")
    modify_file(filename, new_filename)