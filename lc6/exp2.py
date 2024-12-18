class Publisher:
	def __init__(self, publisher_id, publisher_name):
        	self.publisher_id = publisher_id
        	self.publisher_name = publisher_name

class Book(Publisher):
    	def __init__(self, publisher_id, publisher_name, title, author):
        	super().__init__(publisher_id, publisher_name)
        	self.title = title
        	self.author = author

class Python(Book):
	def __init__(self, publisher_id, publisher_name, title, author, price, no_of_pages):
        	super().__init__(publisher_id, publisher_name, title, author)
        	self.price = price
        	self.no_of_pages = no_of_pages

	def display_info(self):
		print("\nPython book\n")
		print(f"Publisher ID: {self.publisher_id}")
		print(f"Publisher Name: {self.publisher_name}")
		print(f"Title: {self.title}")
		print(f"Author: {self.author}")
		print(f"Price: {self.price}")
		print(f"Number of Pages: {self.no_of_pages}")

# User Input
publisher_id = int(input("Enter Publisher ID: "))
publisher_name = input("Enter Publisher Name: ")
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
price = float(input("Enter Price: "))
no_of_pages = int(input("Enter Number of Pages: "))

python_book = Python(publisher_id, publisher_name, title, author, price, no_of_pages)
python_book.display_info()
