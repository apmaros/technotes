# must use TABS instead of spaces
# otherwise fails with makefile:X: *** missing separator.  Stop.
generate-table-of-content:
	python -m metadata-generator/main.py -v
