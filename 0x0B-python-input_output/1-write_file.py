# 1-write_file.py

def write_file(filename="", text=""):
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)