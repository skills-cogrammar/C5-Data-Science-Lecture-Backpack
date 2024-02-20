from services.url_shortener_service import UrlShortenerService
from services.json_service import JsonService


def get_all_urls():
    '''
    List all of the URLs from the file
    '''    
    print("\033c", end="")

    print("-"*50)
    print('URLs')
    print("-"*50)

    urls = json.read()

    for url in urls:
        print(f"Original: {url.url}")
        print(f"Shortened: {url.link_url}")
        print("-"*50)

    input("Press enter to continue...")
    
def create_url():    
    '''
    Creates a new URL
    '''
    print("\033c", end="")

    print("-"*50)
    print('Create URL')
    print("-"*50)

    url = input("Enter URL: ")
    ttl = __get_valid_ttl()

    output = url_shortner.create(url, ttl)
    json.write(output)

    input("Press enter to continue...")

def __get_valid_ttl():
    '''
    Gets a valid Time to Live input
    '''
    while True:
        try:
            ttl = int(input("Enter URL life (in seconds): "))
            if ttl >= 60 and ttl <= 604800:
                return ttl
            else:
                print("Invalid TTL, time needs to be between 60 - 604800 seconds")

        except:
            print("Invalid TTL, time needs to be between 60 - 604800 seconds")            


def destory_url():
    '''
    Deletes a URL
    '''
    print("\033c", end="")

    print("-"*50)
    print('DESTORY URL')
    print("-"*50)

    __list_urls_and_keys()
    
    key = input("Enter key: ")

    urls = json.read()

    if key not in [url.key for url in urls]:
        print("Invalid key")
        return
    
    url_shortner.destroy(key)
    json.delele(key)

    input("Press enter to continue...")

def __list_urls_and_keys():
    urls = json.read()

    for url in urls:
        print(f"{url.key} - {url.link_url}")


def view_active_urls():
    '''
    Option 1:
        - Create a 'created_at' attribute in the ShortUrlDetail model,
        - Add the ttl seconds to the created_at attribute                 
        - if the ttl + created_date is greater than current time, the URL is not active

    OPTION 2:
        - create an 'expires_at' attribute by getting the current time + ttl in the ShortUrlDetail model
        - If the expires_at time is greater than the current time, the URL is active       

    '''
    
    
    # INSERT CODE HERE
    pass

def show_main_menu_options():
    print("\033c", end="")

    print("-"*50)
    print("Welcome to URL Shortener")
    print("-"*50)

    print("\n1. All URLs")
    print("2. Create URL")
    print("3. Destory URL")
    print("4. View Active URLs")
    print("5. Exit")

def main():
    global json, url_shortner

    json = JsonService('short_links.json')
    url_shortner = UrlShortenerService()    

    while True:
        show_main_menu_options()

        choice = input("-> ")

        if choice == "1":
            get_all_urls()
        elif choice == "2":
            create_url()
        elif choice == "3":
            destory_url()
        elif choice == "4":
            # INSERT CODE
            print("PLEASE IMPLEMENT ME")
            input("Press enter to continue...")
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()


