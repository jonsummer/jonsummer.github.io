all: build

build:
	@bundle exec jekyll build 

doctor:
	@bundle exec jekyll doctor 

run: build
	@bundle exec jekyll serve --livereload --drafts

config: 
	@bundle config set --local path 'vendor/bundle'              
 
update:
	@bundle update
	@bundle install

clean:
	@bundle exec jekyll clean

release:
	JEKYLL_ENV=production bundle exec jekyll build