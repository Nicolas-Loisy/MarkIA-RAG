#
# gmake
#
SHELL := /bin/bash
CHDIR_SHELL := $(SHELL)
PYTHON := python


#
# Common
#
load-env:
	@echo "***** $@"
	$(call load_dotenv)

#
# Setup
#
init-venv:
	@echo "***** $@"
	${PYTHON} -m venv .venv

update-venv: init-venv
	@echo "***** $@"
	@source .venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt

update-datasets-with-delete:
	@echo "***** $@"
	@echo "** Updating docs"
	python -m eurelis_llmatoolkit.llamaindex.console --config="llmatk.json" dataset --id="doc" ingest --delete
