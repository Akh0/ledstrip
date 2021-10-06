run_server:
	python3 server.py

install:
	pip3 install -r requirements.txt

freeze:
	pip3 freeze | grep -v "pkg_resources==0.0.0" > requirements.txt