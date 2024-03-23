class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_term_input = page.locator("#userName")

    def navigate(self):
        self.page.goto("https://demoqa.com/text-box")

    def search(self, text):
        self.search_term_input.fill(text)
        self.search_term_input.press("Enter")