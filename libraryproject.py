catalog = {
    "b1" : {"price":20},
    "b2" : {"price":25},
    "b3" : {"price":20},
    "b4" : {"price":25},
    "b5" : {"price":20},
    "b6" : {"price":25},
    "b7" : {"price":20},
    "b8" : {"price":25},
    "b9" : {"price":20},
    "b10" : {"price":25},
}

print(" Welcome to the library you may rent 10 of our books\n")
for book_name in catalog.keys():
    print(f"{book_name}:{catalog[book_name]} \n")

person_book_choice = input(" please list the names of the books you want in order!")
person_book_choice = person_book_choice.split()
catalog_book_list = []
for book_name in person_book_choice:
    if book_name in catalog:
        catalog_book = catalog[book_name]
        catalog_book_price = catalog_book["price"]
        catalog_book_list.append(book_name)

total_price = 0
for book_name in catalog_book_list:
    if book_name in catalog:
        book = catalog[book_name]
        total_price = total_price + book["price"]
        # total_price += book["price"]
print(f" Your total price is ${total_price}")