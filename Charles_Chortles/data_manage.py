"""
author: Alex Sutay
file: data_manage.py
"""

FILENAME = "/home/AlexS/discordbots/Charles_Chortles/im_instances"


def add_entry():
    """
    set the focus on the next image, committing the current instance
    :return: None
    """
    f = open(FILENAME,"a")
    f.write("\nfill:0")
    f.close()


def total_current():
    """
    find the total score so far of the current image
    :return: score as a float
    """
    f = open(FILENAME)
    lines = f.readlines()
    current = lines[-1].split(',')
    total = 0
    for item in current:
        item = item.strip()
        item = item.split(':')
        total += float(item[1])
    return total


def find_average():
    """
    Find the average score so far
    :return: a float of the current average
    """
    total_num = 0
    score = 0
    f = open(FILENAME)
    for line in f:
        total_num += 1
        line = line.split(',')
        for item in line:
            item = item.split(':')
            score += float(item[1])
    f.close()
    total_num -= 1
    return score/total_num


def add_to_current(userid, score):
    """
    add to the score of the current image
    :param userid: The id of the user submitting the score
    :param score: the score that user wants to give it
    """
    scores = dict()
    f = open(FILENAME)
    lines = f.readlines()
    f.close()
    this = lines[-1].split(',')
    for entry in this:
        entry = entry.strip()
        entry = entry.split(':')
        scores[entry[0]] = entry[1]
    scores[userid] = score
    remove_last_line()
    new_str = ''
    for ids in scores:
        new_str += str(ids) + ':' + str(scores[ids]) + ','
    new_str = new_str[:-1]
    f = open(FILENAME, "a")
    f.write(new_str)
    f.close()


def remove_last_line():
    """
    removes the last line of the working file
    """
    f = open(FILENAME)
    lines = f.readlines()
    f.close()
    lines = lines[:-1]
    f = open(FILENAME,"w")
    for item in range(0, len(lines)):
        f.write(lines[item])


def scores_str():
    """
    Return a string containing all of the scores in a string
    :return: string containing scores
    """
    f = open(FILENAME)
    lines = f.readlines()
    f.close()
    ret_str = ""
    score_total = 0
    amount = 0
    for line in lines:
        amount += 1
        items = line.split(',')
        item_total = 0
        for item in items:
            item = item.split(':')
            if not item[0] == "fill":
                ret_str += item[0] + " gave it a score of " + str(item[1]).strip() + ", "
                item_total += float(item[1])
        if len(items) != 1:
            ret_str += "for a total of " + str(item_total) + ";\n"
            score_total += item_total
    amount -= 1
    ret_str += "For a total score of " + str(score_total) + " across " + str(amount) + " images.\n"
    ret_str += "The average is: " + str(find_average())
    return ret_str


def remove_last_input():
    remove_last_line()
    remove_last_line()
    f = open(FILENAME, "a")
    f.write("fill:0")
    f.close()
