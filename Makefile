dist:
	docker build -t quizlet .

.PHONY: new_china
new_china:
	docker run -v `pwd`/output:/srv/output -it quizlet python new_china.py

.PHONY: ancient
ancient:
	docker run -v `pwd`/output:/srv/output -it quizlet python ancient_chinese.py
