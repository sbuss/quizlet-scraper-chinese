from csv import DictWriter

keys = ['chinese', 'pinyin', 'english', 'lesson']


def get_writer(fname):
    f = open(fname, 'w')
    writer = DictWriter(f, fieldnames=keys)
    return writer
