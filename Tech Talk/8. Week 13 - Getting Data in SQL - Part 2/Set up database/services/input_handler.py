"""
WARNING: DO NOT MAKE ANY CHANGES TO THE CODE, 
         PLEASE FOLLOW THE INSTRUCTIONS IN THE README FILE TO SET EVERYTHING UP
"""

import argparse
from services.database_connection import read_json, is_valid_config

def get_args():
    parser = argparse.ArgumentParser()

    # Create arguments that take postgresql connection details
    parser.add_argument("-u", "--user", help="The username of the database you want to connect to")
    parser.add_argument("-pw", "--password", help="The password of the database you want to connect to")
    parser.add_argument("-sr", "--server", help="The host of the database you want to connect to")
    parser.add_argument("-p", "--port", help="The port of the database you want to connect to")
    parser.add_argument("-dr", "--driver", help="The driver for MS SQL Server")
    parser.add_argument("-db", "--database", help="The name of the database you want to connect to")    
    parser.add_argument("-cf", "--config", help="The path to the config file")
    parser.add_argument("-s", "--service", help="The connection type")
    
    args = parser.parse_args()

    return args

def is_args_valid(args):
    if not args.config and not (args.database and args.service):
        return False
    
    return True

def get_database_details(args: dict):
    if args.get('config'):
       data = read_json(args['config'])
       
       if not is_valid_config(data):
           return None
       
       print(type(data))
       return data['service'], data['connection_string']
    

    if args.get('database') == None:
        return None

    service = args.get('service') 
    return service, args



if __name__ == "__main__":
    args = get_args()

    if not is_args_valid(args):
        print("Please provide a config file or connection details")
        exit()

    # Remove None values from args and convert to dictionary 
    args = {k: v for k, v in args.__dict__.items() if v is not None}
    
    print(args)