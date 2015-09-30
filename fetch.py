import requests
from lxml import html


def _tree(url):
    return html.fromstring(requests.get(url).text)


def _elements(tree, index, separator):
    chinese = tree.xpath(
        '//*[@id="subpage"]/article/div[{index}]/div[2]/h3/span'.format(
            index=index))[0].text_content().strip()
    print(chinese)
    meaning = tree.xpath(
        '//*[@id="subpage"]/article/div[{index}]/div[2]/p/span'.format(
            index=index))[0].text_content().strip()
    print(meaning)
    pinyin, english = meaning.split(separator, 1)
    return {
        'chinese': chinese,
        'pinyin': pinyin,
        'english': english,
    }


def contents(url, separator):
    tree = _tree(url)
    elements = []
    index = 1
    while True:
        try:
            elements.extend(_elements(tree, index, separator))
        except IndexError:
            break
    return elements
