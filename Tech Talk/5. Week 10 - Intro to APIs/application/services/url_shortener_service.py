from models.short_url_details import ShortUrlDetails
import requests

class UrlShortenerService():
    __BASE_URL = "https://url.api.stdlib.com/temporary@0.3.0/"
    __CREATE_URL = "create"
    __DESTROY_URL = "destroy"

    def create(self, link: str, ttl: int) -> ShortUrlDetails:
        url = self.__BASE_URL + self.__CREATE_URL
        
        r = requests.get(url, params={"url": link, "ttl": ttl})
                
        if r.status_code != 200:
            return None    

        results = r.json()

        return ShortUrlDetails(**results)


    def destroy(self, key: str):
        url = self.__BASE_URL + self.__DESTROY_URL

        r = requests.post(url, json={"key": key})

        if r.status_code != 200:
            return False
        
        return True
        