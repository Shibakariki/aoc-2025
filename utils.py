def open_file(file_name: str) -> list[str]:
    with open(file_name, 'r') as file:
        lines = file.read().strip().splitlines()
    return lines