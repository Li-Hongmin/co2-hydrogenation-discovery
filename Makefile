PYTHON ?= python

.PHONY: test

test:
	PYTHONPATH=src $(PYTHON) -m unittest discover -s tests -v
