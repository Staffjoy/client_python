.PHONY: test
fmt: 
	yapf -r -i staffjoy/ test/ || :
test:
	pip install -r requirements-test.txt
	yapf -r -d staffjoy/ test/ || (echo "Document not formatted - run 'make fmt'" && exit 1)
	py.test test -v
 

