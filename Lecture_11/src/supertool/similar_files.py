"""
Similar files finder entrypoint

"""

import os
import hashlib
from collections import Counter


def get_all_path_file(directory):
    """
    Returns all paths contains in this directory

    :param directory: directory
    :type directory: str
    :return: list -- name file and path
    """
    paths_file=[]
    for folder, subfilder, files in os.walk(directory):
        paths_file += (list(map(lambda x: os.path.join(folder, x), files)))
    return paths_file


def get_hash_files(fnamelst):
    """
    Returs list with hashes of file

    :param fnamelst: list of file
    :type fnamelst: list(str)
    :return: list(hex) -- List with hashes of file
    """

    hash_list=[]
    for fname in fnamelst:
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        hash_list.append(hash_md5.hexdigest())
    return hash_list



def work(directory):
    """
    Function finds similar files in directory and subdirectories.
    :param directory: directory with files
    :return: list(list(str)) -- list of list of similar_files
    """

    if not os.path.exists(str(directory)):
        print(f"Directory {directory} does not exists")
        return []


    path_files = get_all_path_file(directory)


    hash_files = get_hash_files(path_files)


    counter_hash = Counter(hash_files)

    dict_name_files = dict()


    for name_file, hash_file in zip(path_files, hash_files):
        if counter_hash[hash_file] > 1:
            if (hash_file not in dict_name_files):
                dict_name_files[hash_file] = [name_file]
            else:
                dict_name_files[hash_file].append(name_file)


    return list(dict_name_files.values())
