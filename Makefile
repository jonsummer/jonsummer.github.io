all: build

build:
	@bundle exec jekyll build

run: build
	@bundle exec jekyll serve