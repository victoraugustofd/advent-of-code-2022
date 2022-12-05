def read_file(file_name: str) -> str:
    with open(file_name) as file:
        return file.read()
