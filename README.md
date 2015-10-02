Scrape chinese cards from quizlet.

This isn't exactly a generalized scraper, but could be made to work with
whatever you want to scrape.

# Usage with docker

```sh
$ make dist
# Get cards from "Reading into a new China"
$ make new_china
# Get cards from "A new practical primer of literary chinese"
$ make ancient
```

This creates files in the `output` directory:

```sh
output/
├── ancient_chinese.csv
└── new_china.csv
```

You can then import these files into Anki.


# Usage without docker

You can run this without docker, too:

```sh
$ pip install -r requirements.txt
$ python new_china.py
$ python ancient.py
```
