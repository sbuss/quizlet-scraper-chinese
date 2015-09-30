import requests
from lxml import html


def _tree(url):
    return html.fromstring(requests.get(url).text)


def _elements(tree, index, separator):
    chinese = tree.xpath(
        '//*[@id="subpage"]/article/div[{index}]/div[2]/h3/span'.format(
            index=index))[0].text_content().strip()
    meaning = tree.xpath(
        '//*[@id="subpage"]/article/div[{index}]/div[2]/p/span'.format(
            index=index))[0].text_content().strip()
    try:
        pinyin, english = meaning.split(separator, 1)
    except:
        pinyin, english = '', meaning
    return {
        'chinese': chinese,
        'pinyin': pinyin,
        'english': english,
    }


def yield_contents(url, separator):
    tree = _tree(url)
    index = 1
    while True:
        try:
            yield _elements(tree, index, separator)
            index += 1
        except IndexError:
            break
