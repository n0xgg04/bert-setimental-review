### Requirements:

- Cursor (with MCP)
- Conda
- Python 3.11
- Makefile
- Install `Jupeter` extension in Cursor

### Installlations:

##### I. Configure env & get python path

###### USE MAKEFILE

```
make install
```

###### OR INSTALL MANUALLY

1. Create env

```bash
 conda env create -f environment.yml
```

2. Active env

```bash
 conda activate imdb-sentiment
```

3. Get python path

```bash
 conda env list | grep imdb-sentiment
```

##### II. Set up kernel in `Jupeter`

- Open `run.ipynb`
- Select `Change Kernel` and find conda kernel

##### III. Set up MCP

- Install `mcp-server`

```bash
make install-mcp
```

- Run MCP server

```bash
make run-mcp
```

- Reference to [this document](https://github.com/jbeno/cursor-notebook-mcp)
