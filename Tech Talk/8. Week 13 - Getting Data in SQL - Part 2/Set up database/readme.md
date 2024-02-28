# Database Setup 
Run this script to create the tables and insert the data into the tables.

If you already have data in the tables, all of the existing data will be removed and replaced with the new data.

Follow the guide below to help you use the tool, you do not need to touch any of the code, the service should work for postgres, ms sql server and my sql, just make sure that you have all of your credentails.

### Prerequisites
- Your database service must be running 
- The database that you want to store the values in should be created 

# Environment set up

## Packages
- Pandas
- sqlalchemy
- pydantic

### Setting up virtual Environment 
If you don't want the packages to be installed to your local environment, you can set up a virtual environment using the following steps.

*Windows* 
```shell
python -m venv venv
```

```shell
python -m venv venv
```

```shell
source venv/Scripts/activate
```

Close the environment when you are done
```shell
deactivate
```

*Linux/Mac*
```shell
python -m venv venv
```

```shell
source venv/bin/activate
```

Close the environment when you are done
```shell
deactivate
```

### Install Packages 
```shell 
pip install -r requirements.txt
```

# Running the script 

## Config file
The easiest way to run the applicaiton would be to use a config file. The data that you write in the file will depend on the database type that you are using, you can copy the template for the different databases from the code below.

When using the config file, you must make sure that you include the `service` and `connection_string`, these are used for connecting to the right database service and passing the credentials to the database.

Within the `connection_string` object, `database` is a mandetory field, this is required to make sure that the service is connecting to the right database. Additionally, the database needs to exist before connecting to the service.

Besides the mandetory fields, any missing values will be given default values based on the service being used.

You can create your `config.json` file using the templates below (copy and paste the json), you can then fill in the data that is relevant to your setup. If there are any fields that don't need to be filled out, you can delete the field, do not leave it blank, but remember that `database` is mandetory.


### Process 
To populate the database, you will need to run the following command in your terminal, make sure that the terminal is opened to the same directory as the `setup.py` file for the command to work.

**Step 1**

Update the `config.json` file with the values for your database of choice. You can copy the templates below and replace the values where needed. Remember that the `service`, `connection_string` and `database` fields are mandetory, the process will not run if any of those fields are empty.

**Step 2**

Run the following command to start the process using the `config.json` file.
```shell
python setup.py -cf config.json
```

**Step 3**

Go through the steps and wait for the process to finish, it might take a bit of time depending on the machine that you are using.


#### Postgres

Template
```json
{
    "service": "postgres",
    "connection_string": {
        "username": "[your-username]",
        "password": "[your-password]",        
        "database": "[database-name]",
        "port": 5432,
        "server": "[server-name]"
    }
}
```

Example
```json
{
    "service": "postgres",
    "connection_string": {
        "username": "postgres",
        "password": "mysecretpassword",        
        "database": "film_rental",
        "server": "localhost",
        "port": 5432        
    }
}
```

##### MySQL

Template
```json
{
    "service": "mysql",
    "connection_string": {
        "username": "[your-username]",
        "password": "[your-password]",        
        "database": "[database-name]",
        "port": 3306,
        "server": "[server-name]"
    }
}
```

Example
```json
{
    "service": "mysql",
    "connection_string": {
        "username": "mysql",
        "password": "mysecretpassword",        
        "database": "film_rental",
        "server": "localhost",
        "port": 3306        
    }
}
```

##### MS SQL Server

Template
```json
{
    "service": "ms_sql_server",
    "connection_string": {
        "username": "[your-username]",
        "password": "[your-password]",        
        "database": "[database-name]",
        "server": "[server-name]",
        "driver": "[Driver Version]"
    }
}
```

Example
```json
{
    "service": "ms_sql_server",
    "connection_string": {
        "username": "user1",
        "password": "mysecretpassword",        
        "database": "film_rental",
        "server": "localhost",     
        "driver": "SQL Server Native Client 11.0"
    }
}
```

*NOTES*
- If the database has a URL, you can put the URL as the `server`

## Command Line 

If you don't want to use the config file, you can make use of flags to pass the different paramters, you can get a full list of the paramters that you can pass by running the following command in your terminal, firstly make sure that the terminal is open to the same directory as the `setup.py` file.

```shell 
python setup.py -h
```

The `-db` and `-s` flags are mandetory, the setup will not be performed without these two flags, if any other flags are left out, the defaults for that database system will be used.

Example using Postgres
```shell 
python script.py -s postgres -sr localhost -p 5432 -db film_rental -u postgres -pw postgres
```

# Additional 

Once the script has run, you can go into Azure Data Studio (Or the tool of your choice) and create a new query, you can run a select statment in one of the table to make sure that the values exist.

```sql 
SELECT * 
FROM rental 
```

If that command works, then you can run the following command to set the NULL values for the films that were not returned.

```sql 
UPDATE rental 
SET return_date = NULL
WHERE return_date = '1800-01-01 00:00:00+00'
```