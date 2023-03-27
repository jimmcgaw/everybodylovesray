freeze: 
	pip freeze > requirements.txt

install:
	pip install requirements.txt

run:
	python hello.py