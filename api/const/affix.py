ALL_AFFIX = {}

def load_affix():
    f = open('affixes.txt')
    for x in f.readlines():
        affix_id, affix_format = x.split(',')
        ALL_AFFIX[affix_id] = affix_format