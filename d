# set classes
class Publication(title, author):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_title():
        
    def get_author():
        
    def set_title(title):
        
    def set_author(author):
        
    def display_info():
        

class Book:


class Magazine:

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_paes(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
