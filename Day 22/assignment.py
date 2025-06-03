import os

def create_directory():
    dir_name = input("Enter directory name to create: ")
    try:
        os.makedirs(dir_name, exist_ok=True)
        print(f"Directory '{dir_name}' created or already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")
    return dir_name

def create_file(dir_name):
    file_name = input("Enter file name to create (e.g., example.txt): ")
    file_path = os.path.join(dir_name, file_name)
    try:
        with open(file_path, 'w') as f:
            pass  # Create an empty file
        print(f"File '{file_path}' created.")
    except Exception as e:
        print(f"Error creating file: {e}")
    return file_path

def write_to_file(file_path):
    text = input("Enter text to write to the file: ")
    try:
        with open(file_path, 'w') as f:
            f.write(text)
        print("Text written to the file.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        print("File contents:")
        print(content)
    except Exception as e:
        print(f"Error reading file: {e}")

def append_to_file(file_path):
    text = input("Enter text to append to the file: ")
    try:
        with open(file_path, 'a') as f:
            f.write(text)
        print("Text appended to the file.")
    except Exception as e:
        print(f"Error appending to file: {e}")

def get_file_info(file_path):
    try:
        cwd = os.getcwd()
        abs_path = os.path.abspath(file_path)
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        file_ext = os.path.splitext(file_path)[1]
        print(f"Current Working Directory: {cwd}")
        print(f"File Path: {abs_path}")
        print(f"File Name: {file_name}")
        print(f"File Size: {file_size} bytes")
        print(f"File Extension: {file_ext}")
    except Exception as e:
        print(f"Error retrieving file info: {e}")

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted.")
    except Exception as e:
        print(f"Error deleting file: {e}")

def main():
    dir_name = None
    file_path = None

    while True:
        print("\nMenu:")
        print("1. Create Directory")
        print("2. Create File in Directory")
        print("3. Write to File")
        print("4. Read File")
        print("5. Append to File")
        print("6. Get File Info")
        print("7. Delete File")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            dir_name = create_directory()
        elif choice == '2':
            if dir_name:
                file_path = create_file(dir_name)
            else:
                print("Please create a directory first.")
        elif choice == '3':
            if file_path:
                write_to_file(file_path)
            else:
                print("Please create a file first.")
        elif choice == '4':
            if file_path:
                read_file(file_path)
            else:
                print("Please create a file first.")
        elif choice == '5':
            if file_path:
                append_to_file(file_path)
            else:
                print("Please create a file first.")
        elif choice == '6':
            if file_path:
                get_file_info(file_path)
            else:
                print("Please create a file first.")
        elif choice == '7':
            if file_path:
                delete_file(file_path)
                file_path = None  # Reset file_path after deletion
            else:
                print("Please create a file first.")
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
