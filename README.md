# Jupyter Notes

A place to play with Notebooks and organize Python related code snippets

## Setup

Setup your `.venv`. From the root of the repository:

```bash
python3 -m venv .venv --system-site-packages
```

Activate the `.venv` if you don't have an automated script:

```bash
source .venv/bin/activate
```

Install all dependencies

```bash
pip install -r requirments.txt
```

Add your `.venv` as a Juypyter kernel

```bash
python -m ipykernel install --user --name=.venv
```

Start the Jupyter Lab
```bash
jupyter lab notebooks
```



