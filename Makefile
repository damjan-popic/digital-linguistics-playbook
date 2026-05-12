.PHONY: install serve build check clean

install:
	python -m pip install -r requirements.txt

serve:
	mkdocs serve

build:
	mkdocs build --strict

check:
	python scripts/check_answers.py

clean:
	rm -rf site .cache
