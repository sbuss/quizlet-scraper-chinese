from dump import get_writer
from fetch import yield_contents

urls = [
    ('https://quizlet.com/51702933/a-new-practical-primer-of-literary-chinese-lesson-1-flash-cards/', '\n', 'lesson_1'),  # nopep8
    ('https://quizlet.com/52033238/a-new-practical-primer-of-literary-chinese-lesson-2-flash-cards/', '\n', 'lesson_2'),  # nopep8
    ('https://quizlet.com/52759393/a-new-practical-primer-of-literary-chinese-lesson-3-flash-cards/', '\n', 'lesson_3'),  # nopep8
    ('https://quizlet.com/53505911/a-new-practical-primer-of-literary-chinese-lesson-4-flash-cards/', '\n', 'lesson_4'),  # nopep8
    ('https://quizlet.com/53898659/a-new-practical-primer-of-literary-chinese-lesson-5-flash-cards/', '\n', 'lesson_5'),  # nopep8
    ('https://quizlet.com/54718691/a-new-practical-primer-of-literary-chinese-lesson-6-flash-cards/', '\n', 'lesson_6'),  # nopep8
    ('https://quizlet.com/55009305/a-new-practical-primer-of-literary-chinese-lesson-7-flash-cards/', '\n', 'lesson_7'),  # nopep8
    ('https://quizlet.com/55711096/a-new-practical-primer-of-literary-chinese-lesson-8-flash-cards/', '\n', 'lesson_8'),  # nopep8
    ('https://quizlet.com/56124246/a-new-practical-primer-of-literary-chinese-lesson-9-flash-cards/', '\n', 'lesson_9'),  # nopep8
    ('https://quizlet.com/57385498/a-new-practical-primer-of-literary-chinese-lesson-10-flash-cards/', '\n', 'lesson_10'),  # nopep8
    ('https://quizlet.com/58435797/a-new-practical-primer-of-literary-chinese-lesson-11-flash-cards/', '\n', 'lesson_11'),  # nopep8
    ('https://quizlet.com/58955655/a-new-practical-primer-of-literary-chinese-lesson-12-flash-cards/', '\n', 'lesson_12'),  # nopep8
    ('https://quizlet.com/59421638/a-new-practical-primer-of-literary-chinese-lesson-13-flash-cards/', '\n', 'lesson_13'),  # nopep8
    ('https://quizlet.com/60026581/a-new-practical-primer-of-literary-chinese-lesson-14-flash-cards/', '\n', 'lesson_14'),  # nopep8
    ('https://quizlet.com/60824784/a-new-practical-primer-of-literary-chinese-lesson-15-flash-cards/', '\n', 'lesson_15'),  # nopep8
]


if __name__ == "__main__":
    writer = get_writer('output/ancient_chinese.csv')
    for url, sep, tags in urls:
        for content_dict in yield_contents(url, sep):
            content_dict['tags'] = tags
            writer.writerow(content_dict)
