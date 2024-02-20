import json
import os
from models.short_url_details import ShortUrlDetails

class JsonService():
    def __init__(self, file_name: str) -> None:
        self.__file_name = file_name

    def write(self, url: ShortUrlDetails):
        '''
        Adds a new URL to the JSON file

        Params:
            url (ShortUrlDetails): The url to add to the file (ShortUrlDetails object)
        '''
        
        current_urls = self.__get_old_data()
        current_urls.append(url)

        print(url)

        # Convert the urls list to a json object
        current_urls = [item.__dict__ for item in current_urls]
        
        with open(self.__file_name, 'w') as f:
            json.dump(current_urls, f, indent=4)

    def delele(self, key: str):
        '''
        Removes a URL from the JSON file

        Params: 
            key (str): The key for the URL to be removed
        '''
        current_urls = self.__get_old_data()

        for url in current_urls:
            if url.key == key:
                current_urls.remove(url)

        current_urls = [item.__dict__ for item in current_urls]

        with open(self.__file_name, 'w') as f:
            json.dump(current_urls, f, indent=4)

    def __get_old_data(self) -> list[ShortUrlDetails]:
        '''
        Gets all of the data that is curretly in the JSON file

        Returns:
            List[ShortUrlDetails]
        '''
        
        # Create new file if one does not exist
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, 'w') as f:
                json.dump([], f, indent=4)
                return []
        
        # Get the old data in the file
        with open(self.__file_name, 'r') as f:
            data = json.load(f)

        # Convert the urls json object to a list of Urls
        return [ShortUrlDetails(**url) for url in data]
    
    def read(self):
        return self.__get_old_data()    

