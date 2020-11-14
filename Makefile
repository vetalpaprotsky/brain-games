install:
	poetry install

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

publish-test:
	poetry publish -r test-pypi

.PHONY: install lint selfcheck check build publish-test
