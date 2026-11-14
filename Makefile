.PHONY: install test unit integration coverage html clean

install:
	poetry install

test:
	poetry run pytest -v

unit:
	poetry run pytest -m unit -v

integration:
	poetry run pytest -m integration -v

coverage:
	poetry run pytest --cov --cov-report=term-missing

html:
	poetry run pytest --cov --cov-report=html

clean:
	rm -rf .pytest_cache htmlcov .coverage
