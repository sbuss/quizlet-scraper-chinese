from csv import DictWriter

keys = ['chinese', 'pinyin', 'english', 'tags']


def get_writer(fname):
    f = open(fname, 'w')
    writer = DictWriter(f, fieldnames=keys)
    return writer
