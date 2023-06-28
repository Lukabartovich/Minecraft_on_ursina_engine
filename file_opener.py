def open_file(file_path: str):
    with open(str(file_path), 'r+') as file:
        file_text = file.read()
    return file_text

def write_file(file_path: str, text: str):
    with open(str(file_path), 'w+') as file:
        file.truncate(0)
        file.write(text)
        