# File Read & Write Challenge 🖋️ with Error Handling Lab 🧪
# This program reads a user-specified file, modifies its contents, and writes the modified content to a new file.
# It also includes error handling for common file-related issues like missing files, permission problems, and empty files.

# Function to read the content of a file
def read_file_content(filename):
    try:
        # Try to open the file in read mode ("r")
        with open(filename, "r") as file:
            print(f"\n-- Reading from '{filename}' --\n")
            content = file.read()  # Read the full content of the file as a single string

            if not content.strip():
                # If the file is empty or contains only whitespace, warn the user
                print("⚠️ The file is empty or contains only whitespace.")
                return None  # Treat it as an unsuccessful read

            print(content)  # Optionally print the content for confirmation
            return content  # Return the content to be used later
    except FileNotFoundError:
        # If the file doesn't exist, show this message
        print(f"\n❌ Error: File '{filename}' not found. Please check the name and try again.")
        return None
    except PermissionError:
        # If the program doesn't have permission to read the file
        print(f"\n❌ Error: Permission denied. Cannot access '{filename}'.")
        return None
    finally:
        # This block always runs, whether there's an error or not
        print("\n-- Reading process completed. --")

# Function to write modified content to a new file
def write_modified_file(original_filename, content):
    try:
        # Create a new filename using the original one
        modified_filename = f"modified_{original_filename}"
        
        # Open the new file in write mode ("w")
        with open(modified_filename, "w") as file:
            print(f"\n-- Writing to '{modified_filename}' --")
            
            # Modify the content before writing (in this case, convert it to uppercase)
            modified_content = content.upper()
            
            file.write(modified_content)  # Write the modified content to the new file

        # Let the user know the new file has been created successfully
        print(f"✅ Successfully created '{modified_filename}' with modified content.")
    except PermissionError:
        # Handle any write permission errors
        print(f"\n❌ Error: Permission denied when writing '{modified_filename}'.")
    finally:
        # Always run this after attempting to write
        print("-- Writing process completed. --")

# Main program starts here
if __name__ == "__main__":
    # Ask the user for the filename to read
    user_filename = input("📄 Enter the name of the file to read (e.g., my_file.txt): ").strip()
    
    # Read the content from the specified file
    file_content = read_file_content(user_filename)

    # Only continue if the file was read successfully and is not empty
    if file_content is not None:
        write_modified_file(user_filename, file_content)  # Write the modified content to a new file
    else:
        # If there was an error or the file was empty, exit the program gracefully
        print("\n🚫 File was not read successfully or is empty. Exiting without writing.")
