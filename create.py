import os


def create_directory(directory):
    if not os.path.exists(directory):#To check if directory exist or not
        print("Creating Directory!!"+directory)
        os.makedirs(directory)
    else:
        print("Directory already exist")


def create_data_files(project_name, base_url):#project_name is thesite
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data+'\n')


def delete_file_content(path):
    open(path, 'w').close()


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt', encoding="utf-8") as f:
        for line in f:
            results.add(line.replace('\n', ''))

    return results


def set_to_file(links, file_name):
    with open(file_name, 'w', encoding="utf-8") as f:
        for l in sorted(links):
            f.write(l+"\n")


