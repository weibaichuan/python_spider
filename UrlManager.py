class UrlManager:

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        return len(self.new_urls)

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


