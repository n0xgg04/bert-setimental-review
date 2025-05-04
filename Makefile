install:
	conda env create -f environment.yml
	conda activate imdb-sentiment
	conda env list | grep imdb-sentiment

install-mcp:
	pip install cursor-notebook-mcp

run-mcp:
	cursor-notebook-mcp --allow-root /Users/n0x/PycharmProjects/BertSentimental/


