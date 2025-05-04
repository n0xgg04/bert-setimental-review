### Requirements:

- cursor (with MCP)
- conda
- python 3.11
- install `Jupeter` extension in Cursor

### Installlations:

##### I. Configure env & get python path

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

- Reference to [this document](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Fn0xgg04%2Fbert-setimental-review%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR6UntwL3hCQtGr5KdWKsML8BTCAotpZjNbgq3SzDO0W3T1DHmaXmc9hX5wMyA_aem_y448GyeJX1DGvxV1NHb_IA&h=AT2E1u528yFvyTqzB7sa8v1DHpj5k1wVzypADQX_1-xX1T8BAoJsi-wdykHv4B9EvgMvCSvyucjqUF3c6w6opS1W_1maW7npQzP22U4rWBe6L1fQP-D7m9QsFS266zo&s=1)
