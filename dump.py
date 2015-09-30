from csv import DictWriter

keys = ['chinese', 'pinyin', 'english', 'lesson']


def write(fname, elements):
    f = open(fname, 'w')
    writer = DictWriter(f, fieldnames=keys)
    for element_dict in elements:
        writer.writerow(element_dict)
