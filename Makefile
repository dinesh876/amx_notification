HOST="0.0.0.0"
PORT="5000"

define USAGE
Super awesome hand-crafted build system ⚙️ 

Commands:
	init      Install Poetry
	build     Install Python dependecy with Poetry.
	stop      stop gunicorn server
	serve     Run gunicorn WSGI 
endef

export USAGE

help:
	@echo "$$USAGE"

init:
	pip3 install poetry

build:
	poetry install

stop:
	pkill gunicorn

serve:
	poetry run gunicorn --bind $(HOST):$(PORT) --workers 5 wsgi:app --daemon
	@echo "[*] Application running on http://$(HOST):$(PORT)/notification"