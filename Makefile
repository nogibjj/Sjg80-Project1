install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py
	python -m pytest --nbval-lax *.ipynb

format:	
	black src/*.py
	nbqa black src/*.ipynb

lint:
	nbqa ruff *.ipynb
	ruff check *.py 
		
all: install lint test format deploy
