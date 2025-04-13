def read_and_modify_file():
    input_filename = input("Enter the name of the file to read: ")

    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("File read successfully.")

            # Modify content: for example, convert to uppercase
            modified_content = content.upper()

            # Create a new filename for output
            output_filename = "modified_" + input_filename

            with open(output_filename, 'w') as outfile:
                outfile.write(modified_content)
                print(f"Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write the file '{input_filename}'.")

if __name__ == "__main__":
    read_and_modify_file()
