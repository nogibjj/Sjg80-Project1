install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py
	python -m pytest --nbval-lax *.ipynb

format:	
	black *.py 
	nbqa black *.ipynb

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	nbqa ruff *.ipynb
	ruff check *.py 

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy
