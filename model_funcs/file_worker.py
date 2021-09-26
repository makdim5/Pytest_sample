def read_from_file(filepath):
    with open(filepath, mode="r", encoding="utf-8") as file_open:
        return file_open.readlines()