from dump import get_writer
from fetch import yield_contents

urls = [
    ('https://quizlet.com/47828476/reading-into-a-new-china-chapter-1-flash-cards/', ';'),  # nopep8
    ('https://quizlet.com/53308491/reading-into-a-new-china-1-l2-flash-cards/', '\n'),  # nopep8
    ('https://quizlet.com/53308523/reading-into-a-new-china-1-l3-flash-cards/', '\n'),  # nopep8
]


if __name__ == "__main__":
    writer = get_writer('output/new_china.csv')
    for url, sep in urls:
        for content_dict in yield_contents(url, sep):
            writer.writerow(content_dict)
