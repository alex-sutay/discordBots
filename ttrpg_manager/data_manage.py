"""
author: Alex Sutay
file: data_manage.py
"""

"""
Something to think about, it would probably be more efficient if all of the loading was done at the beginning, instead
of each time a resource was needed. However, if it ends up running multiple times in parallel like Bread Bot does,
that could lead to corrupted data. 
"""

# filename constants
KEY_DICT = "keys"  # dictionary of guild ids to key characters
INVENTORIES = "inv"  # lists of items in each person's inventory
ITEMS = "items"  # dictionary of item hashes to information necessary


def get_key_char(guild):
    """
    This function will retrieve a guild's chosen key character. Defaults to '!'
    :param guild: The guild object to look up
    :return: a string of a chosen key character
    """
    key_dict = read_key_dict()
    if str(guild.id) in key_dict:
        return key_dict[str(guild.id)]
    else:
        return '!'


def set_key_char(guild, char):
    key_dict = read_key_dict()
    key_dict[str(guild.id)] = char
    write_key_dict(key_dict)


def read_key_dict():
    """
    Read the key dict file and return it as a dictionary
    :return: dict of guild ids to key characters
    """
    key_dict = {}
    with open(KEY_DICT) as f:
        for line in f:
            line = line.strip().split(':')
            key_dict[line[0]] = line[1]
    return key_dict


def write_key_dict(key_dict):
    """
    Write out and save the dictionary of key characters
    :param key_dict: dict of guild ids to key characters
    :return: None
    """
    write_str = ''
    for guild_id in key_dict:
        write_str += guild_id + ':' + key_dict[guild_id] + '\n'

    with open(KEY_DICT, 'w') as f:
        f.write(write_str)
