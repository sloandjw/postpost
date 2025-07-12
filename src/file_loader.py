def load_nc_file(path):
    with open(path, 'r') as f:
        return f.readlines()
