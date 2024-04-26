def write_file(file_name: str, file_content):
    file_name_with_extension = str(file_name) + ".txt"
    with open(file_name_with_extension, "w") as f:
        f.write(file_content)

def append_file(file_name, append_content):
    file_name_with_extension = str(file_name) + ".txt"
    with open(file_name_with_extension, "a") as f:
        f.write(append_content)

def read_file(file_name):
    file_name_with_extension = str(file_name) + ".txt"
    with open(file_name_with_extension, "r") as f:
        return f.read()
