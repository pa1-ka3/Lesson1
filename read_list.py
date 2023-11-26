def load_url_list1(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        urls = file.readlines()
        return urls


def load_url_list2(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        urls = file.read().splitlines()
        return urls


def load_url_list3(file_path):
    urls = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            urls.append(line.strip())
    return urls


