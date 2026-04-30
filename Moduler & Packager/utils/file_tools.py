# Create file
def create_file(filename):
    try:
        with open(filename, "x") as f:
            return "File created successfully"
    except FileExistsError:
        return "File already exists"

# Write file
def write_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)
    return "File written successfully"

# Read file
def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except:
        return "File not found"

# Append file
def append_file(filename, data):
    with open(filename, "a") as f:
        f.write("\n" + data)
    return "Data appended successfully"