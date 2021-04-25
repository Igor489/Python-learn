import os


def get_offset(line):
    cnt = 0
    try:
        while line[cnt] == ' ':
            cnt += 1
    except IndexError:
        pass
    return cnt


def read_config(config_filename):
    with open(config_filename, 'r', encoding='utf-8') as f:
        config = f.readlines()
    return config


def get_file_structure(config):
    folders = {}
    if len(config) > 0:
        first_line = config[0]
        for line in config[1:]:
            if get_offset(line) < get_offset(first_line):
                raise ValueError('Неравильные отступы')

        start_line_num = 0
        line_num = 1
        while line_num < len(config):
            line = config[line_num]
            if get_offset(line) == get_offset(first_line):
                dirname = config[start_line_num].strip()
                folders[dirname] = get_file_structure(config[start_line_num+1:line_num])
                start_line_num = line_num
            line_num += 1
        dirname = config[start_line_num].strip()
        folders[dirname] = get_file_structure(config[start_line_num + 1:line_num])

    return folders


def build_folders_tree(path, folders):
    for folder, children in folders.items():
        full_name = os.path.join(path, folder)
        if os.path.exists(full_name):
            pass
        else:
            if children or '.' not in full_name:
                os.mkdir(full_name)
                build_folders_tree(full_name, children)
            else:
                with open(full_name, 'w') as f:
                    pass


config = read_config('config2.txt')
folders = get_file_structure(config)
try:
    os.mkdir('structure2')
except:
    pass
build_folders_tree('structure2', folders)
