def open_file(file_name: str) -> list[str]:
    with open(file_name, 'r') as file:
        lines = file.read().strip().splitlines()
    return lines

def open_file_one_line(file_name: str) -> str:
    with open(file_name, 'r') as file:
        line = file.read().strip()
    return line

def open_file_two_lists(file_name: str) -> tuple[list[str], list[str]]:
    list1 = []
    list2 = []
    list1_finished = False
    with open(file_name, 'r') as file:
        for line in file:
            if line.strip() == "":
                list1_finished = True
                continue
            if list1_finished:
                list2.append(line.strip())
            else:
                list1.append(line.strip())
    return list1, list2