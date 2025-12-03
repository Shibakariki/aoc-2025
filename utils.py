def open_file(file_name: str) -> list[str]:
    with open(file_name, 'r') as file:
        lines = file.read().strip().splitlines()
    return lines

def open_file_one_line(file_name: str) -> str:
    with open(file_name, 'r') as file:
        line = file.read().strip()
    return line