def reduce_file_path(path):
    final_path = []
    split_the_path = path.split('/')

    for path in split_the_path:
        if path == '..' and final_path != []:
            final_path.pop()
        elif path in ['.', '..'] or not path:
            pass
        else:
            final_path.append(path)

    if not final_path:
        return '/'

    return '/' + "/".join(final_path)
