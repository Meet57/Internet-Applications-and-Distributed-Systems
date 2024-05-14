def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found.")

def write_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
    print("Content has been written to", file_name)

def append_to_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content)
    print("Content has been appended to", file_name)

# Example usage
file_name = "example.txt"

write_to_file(file_name, "This is some content.\n")

read_file(file_name)

append_to_file(file_name, "This is additional content.\n")

read_file(file_name)