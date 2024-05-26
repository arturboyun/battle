test:
	pytest

test_html:
	pytest --cov-report html

lint:
	pylint ./src