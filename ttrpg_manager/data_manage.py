"""
author: Alex Sutay
file: data_manage.py
"""


"""
Something to think about, it would probably be more efficient if all of the loading was done at the beginning, instead
of each time a resource was needed. However, if it ends up running multiple times in parallel like Bread Bot does,
that could lead to corrupted data. 
"""


class Item:
    """This class is used to represent an item someone can have in their inventory"""
    def __init__(self, title, description, creator, secrets=None):
        """
        Constructor for an item object
        :param title: the name of the object
        :param description: the description of the object
        :param creator: creator of the object
        :param secrets: list of strings representing secret text that needs to be revealed
        """
        self.title = title
        self.desc = description
        self.creator = creator
        self.secrets = secrets

    def __hash__(self):
        return hash(self.title) * hash(self.creator)

    def __str__(self):
        rtn_str = '<title>' + self.title + '<description>' + self.desc + '<creator>' + self.creator + '<secrets>'
        if self.secrets is not None:
            for secret in self.secrets:
                rtn_str += '<si>' + secret
        return rtn_str


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
    key_dict = read_dict_file(KEY_DICT)
    if str(guild.id) in key_dict:
        return key_dict[str(guild.id)]
    else:
        return '!'


def set_key_char(guild, char):
    key_dict = read_dict_file(KEY_DICT)
    key_dict[str(guild.id)] = char
    write_dict_file(key_dict, KEY_DICT)


def read_dict_file(filename):
    """
    Read one of the dict file and return it as a dictionary
    :return: dict of items in the file
    """
    key_dict = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            ind = line.find(':')
            key_dict[line[:ind]] = line[ind+1:]
    return key_dict


def write_dict_file(write_dict, filename):
    """
    Write out and save a dictionary
    :param write_dict: dict of strings to other strings
    :param filename: the name of the file to write to
    :return: None
    """
    write_str = ''
    for key in write_dict:
        write_str += key + ':' + write_dict[key] + '\n'

    with open(filename, 'w') as f:
        f.write(write_str)


def add_new_item(item, creator):
    """
    Add a new item to the save file
    :param item: the item object being added
    :param creator: the userid of the person creating the item
    :return: None
    """
    item_key = str(hash(item))
    item_dict = read_dict_file(ITEMS)
    item_dict[item_key] = str(item)
    write_dict_file(item_dict, ITEMS)
    add_to_inventory(item_key, creator)


def remove_item(item):
    """
    destroy an item, removing it from the ITEMS dictionary and the owner's inventory
    :param item:
    :return: TODO Finish this, but also, decide if you're going to add an owner attribute to items,
    or require something here
    """
    pass


def add_to_inventory(item_hash, owner):
    """
    Add a reference to an item object to their inventory
    :param item_hash: str of the item's hash
    :param owner: the userid of the owner receiving the item
    :return:
    """
    inventories = read_dict_file(INVENTORIES)
    if owner in inventories:
        inv = inventories[owner]
        inv += '<item>' + item_hash
        inventories[owner] = inv
    else:
        inventories[owner] = '<item>' + item_hash
    write_dict_file(inventories, INVENTORIES)


def remove_from_inventory(item_hash, owner):
    """
    Remove an item from an inventory
    :param item_hash: str of the item's hash
    :param owner: the userid of the current owner
    :return: TODO
    """


def get_inventory(owner):
    """
    Get the contents of a user's inventory
    :param owner: the user whose inventory is going to be returned
    :return: dict of hash strings to Item objects
    """
    inv_dict = read_dict_file(INVENTORIES)

    if owner not in inv_dict:
        return []

    inv = inv_dict[owner]
    inv = inv.split('<item>')
    items = read_dict_file(ITEMS)
    rtn_inv = {}

    for idx in range(1, len(inv)):
        this_hash = inv[idx]
        item_str = items[this_hash]
        rtn_inv[this_hash] = create_item(item_str)

    return rtn_inv


def create_item(item_str):
    """
    Recreate an Item object from it's given string
    :param item_str: string created from an object
    :return: Item object represented by the given string
    """
    # extract the basic attributes
    attributes = []
    for attr in ['<title>', '<description>', '<creator>']:
        idx1 = item_str.find(attr) + len(attr)
        idx2 = item_str[idx1:].find('<') + idx1
        attributes.append(item_str[idx1:idx2])
    title = attributes[0]
    print(title)
    desc = attributes[1]
    print(desc)
    creator = attributes[2]
    print(creator)
    return Item(title, desc, creator)
