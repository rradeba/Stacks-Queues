class BrowsingHistory:
    def __init__(self):
        self.history = []  

    # Add a page
    def add_page(self, page):
        self.history.append(page)
        print(f"Added: {page}")

    # Remove last visited
    def remove_page(self):
        if not self.is_empty():
            removed_page = self.history.pop()
            print(f"Removed: {removed_page}")
        else:
            print("No more pages to remove.")

    # Number of pages viewed 
    def num_pages(self):
        return len(self.history)

    # Check if empty
    def is_empty(self):
        return len(self.history) == 0

    # Current Page
    def current_page(self):
        if not self.is_empty():
            return self.history[-1]
        else:
            return "None viewed yet."

# Testing 

if __name__ == "__main__":
    browsing_history = BrowsingHistory()

    # Adding pages
    browsing_history.add_page("amazon.com")
    browsing_history.add_page("facebook.com")
    browsing_history.add_page("apple.com")

    # current page
    print(f"Current page: {browsing_history.current_page()}")

    # number of pages
    print(f"Pages viewed: {browsing_history.num_pages()}")

    # Remove pages
    browsing_history.remove_page()


    # Check after removing
    print(f"Current page: {browsing_history.current_page()}")

    # Remove the last page
    browsing_history.remove_page()

    # Try remove from empy stack 
    browsing_history.remove_page()

    # Check if browsing history is empty
    print(f"Browsing history is empty: {browsing_history.is_empty()}")
