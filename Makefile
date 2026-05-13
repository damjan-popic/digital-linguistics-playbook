.PHONY: install serve build check clean

install:
	python -m pip install -r requirements.txt

serve:
	mkdocs serve

build:
	mkdocs build --strict

check:
	python scripts/check_answers.py
	python scripts/check_projects.py

clean:
	rm -rf site .cache
