from dump import write
from fetch import contents

urls = [
    'https://quizlet.com/47828476/reading-into-a-new-china-chapter-1-flash-cards/',
    'https://quizlet.com/53308491/reading-into-a-new-china-1-l2-flash-cards/',
    'https://quizlet.com/53308523/reading-into-a-new-china-1-l3-flash-cards/',
]


if __name__ == "__main__":
    all_contents = []
    for url in urls:
        all_contents.extend(contents(url, '\n'))

    write('new_china.csv', all_contents)
