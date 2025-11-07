.PHONY: env html clean

# Create or update the conda environment
.ONESHELL:
SHELL = /bin/bash

env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate notebook
	conda install ipykernel
	python -m ipykernel install --user --name make-env --display-name "IPython - Make"
# Build HTML version of the MyST site
html:
	myst build --html

# Clean generated folders
clean:
	rm -rf figures audio _build