from string import ascii_uppercase

ceasar = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. """
task_url = """http://www.pythonchallenge.com/pc/def/map.html"""


def shift_char(input_char):
    start_index = ord('A')
    index = ord(input_char)
    if input_char.upper() in ascii_uppercase: 
        result_index = (index - start_index + 2) % 26 + start_index
    else:
        result_index = index 
    result = chr(result_index)
    return result


def shift_string(task_string : str):
    task_string = task_string.upper()
    return_string = ''
    for char in task_string:
        return_string += shift_char(char)
    return return_string.lower()


def shift_sentence(task_sentence):
    return shift_string(task_sentence)

    
        

