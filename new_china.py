from dump import get_writer
from fetch import yield_contents

urls = [
    ('https://quizlet.com/12455900/1-l1-all-flash-cards/', ':', 'lesson_1'),  # nopep8
    ('https://quizlet.com/12455865/1-l2-all-flash-cards/', ':', 'lesson_2'),  # nopep8
    ('https://quizlet.com/12588906/1-l3-all-flash-cards/', '\n', 'lesson_3'),  # nopep8
    ('https://quizlet.com/12589825/1-l4-all-flash-cards/', '\n', 'lesson_4'),  # nopep8
    ('https://quizlet.com/12589998/1-l5-all-flash-cards/', '\n', 'lesson_5'),  # nopep8
    ('https://quizlet.com/12590420/1-l6-all-flash-cards/', '\n', 'lesson_6'),  # nopep8
    ('https://quizlet.com/12591711/1-l7-all-flash-cards/', '\n', 'lesson_7'),  # nopep8
]


if __name__ == "__main__":
    writer = get_writer('output/new_china.csv')
    for url, sep, tags in urls:
        for content_dict in yield_contents(url, sep):
            content_dict['tags'] = tags
            writer.writerow(content_dict)
