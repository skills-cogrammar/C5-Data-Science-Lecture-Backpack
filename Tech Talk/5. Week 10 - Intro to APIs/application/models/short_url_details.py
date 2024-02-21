class ShortUrlDetails():
    def __init__(self, url: str, key: str, ttl: int, link_url: str):
        self.url = url
        self.key = key
        self.ttl = ttl
        self.link_url = link_url

    def __str__(self) -> str:
        output = f"URL: {self.url}\n"
        output += f"Key: {self.key}\n"
        output += f"TTL: {self.ttl}\n"
        output += f"Link URL: {self.link_url}\n"
        return output
    