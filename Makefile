install:
	pip install -r requirements.txt

lint:
	invoke lint

format:
	invoke format

test:
	invoke test

cli:
	invoke run_cli

web:
	invoke run_web