# Shopping API 
This is a basic API that simulates an online store where a user can create an account and add items to their wishlist and shopping cart.

Admin users are able to update and add products.

Anyone with an API key is able to view the products.

# Quick Start 

### Set up virtual environment 

```shell 
python -m venv .venv
```

*windows*
```shell 
source .venv/Script/activate
```

*mac/linux*
```shell 
source .venv/bin/activate
```

### Installation 

To install all of the dependencies run:

*windows*
```shell 
pip install -r requirements.txt
```

*mac/linux*
```shell 
pip3 install -r requirements.txt
```

### Set up .env

1. Create the `.env` file in the main directory 
2. Add the following values to the `.env` file 

```yaml
HOST=localhost
PORT=8080
RELOAD=True
SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
```

### Create SQLite database and add data 
In your terminal run the following command 

```shell
python data/load_data.sql
```