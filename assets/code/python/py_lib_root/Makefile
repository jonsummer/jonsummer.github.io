.PHONY: all build clean test run

all:build

build: clean
	@python2 ./setup.py build sdist bdist_wheel
	@python3 ./setup.py build sdist bdist_wheel

clean: uninstall
	rm -rf ./build ./dist *.egg-info
run: 
	@python3 ./addhelper/api.py
	@python2 ./addhelper/api.py
	
test: install
	@python3 tests/addhelper_test.py
	@python2 tests/addhelper_test.py

install: build
	@pip3 install --user ./dist/*.whl
	@pip2 install --user ./dist/*.whl

uninstall:
	@pip3 uninstall -y addhelper
	@pip2 uninstall -y addhelper

dep:
	@easy_install --user install  pip==19.2.3
