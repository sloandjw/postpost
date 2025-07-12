def write_output(lines, path):
    with open(path, 'w') as f:
        f.writelines(lines)
