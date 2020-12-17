all:  
	jupyter-book build page

clean: page_clean

page:
	jupyter-book build page

page_clean:
	jupyter-book clean page

deploy: page
	mkdir -p /home/darlon/public_html/darlonv/work
	cp -v -r page/_build/html/* /home/darlon/public_html/darlonv/work
