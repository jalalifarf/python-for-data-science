
def is_file_empty(filename):
    with open(filename, "a+", encoding="utf-8") as file:
        file.seek(0)
        return file.read() == ""
