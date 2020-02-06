import csv

# Parent Item class
class Item:
    def __init__(self, ID, name, price, quantity, date):
        self.ID = ID
        self.name = name
        self.price = price
        self.quantity = quantity
        self.date = date
    def __str__(self):
        return'''ID: {}
Name: {}
Price: ${}
Date: {}
Quantity: {}'''.format(self.ID, self.name, self.price, self.date, self.quantity)
        
# Book subclass 
class Book(Item):
    def __init__(self, ID, name, date, publisher, author, price, ISBN, quantity):
        super().__init__( ID, name, price, quantity, date )
        self.publisher = publisher
        self.author = author
        self.ISBN = ISBN
    def __str__(self):
        return super().__str__() + '''
Author: {1}
Publisher: {0}
ISBN: {2}'''.format(self.publisher, self.author, self.ISBN)

# CD_Vinyl subclass
class CD(Item):
    def __init__( self, ID, name, artist, label, ASIN, date, price, quantity ):
        super().__init__( ID, name, price, quantity, date )
        self.artist = artist
        self.label = label
        self.ASIN = ASIN

    def __str__(self):
        return super().__str__() + '''
Artist: {}
Label: {}
ASIN: {}'''.format(self.artist, self.label, self.ASIN)

# Collectible subclass
class Collectible(Item):
    def __init__( self, ID, name, price, date, owner, quantity ):
        super().__init__( ID, name, price, quantity, date )
        self.owner = owner

    def __str__(self):
        return super().__str__() + '''
Owner: {}'''.format(self.owner)

# Ebay parent class Item subclass
class Ebay(Item):
    def __init__( self, ID, name, price, date, manufacturer, quantity ):
        super().__init__( ID, name, price, quantity, date )
        self.manufacturer = manufacturer
        
    def __str__(self):
        return super().__str__() + '''
Manufacturer: {}'''.format(self.manufacturer)

# Electronics subclass
class Electronics(Ebay):
    def __init__( self, ID, name, price, date, manufacturer, quantity ):
        super().__init__( ID, name, price, date, manufacturer, quantity )

    def __str__(self):
        return super.__str__()

# Fashion subclass
class Fashion(Ebay):
    def __init__( self, ID, name, price, date, manufacturer, quantity ):
        super().__init__( ID, name, price, date, manufacturer, quantity )
        
    def __str__(self):
        return super.__str__()
    
# Home Garden subclass
class Home(Ebay):
    def __init__( self, ID, name, price, date, manufacturer, quantity ):
        super().__init__( ID, name, price, date, manufacturer, quantity )
        
    def __str__(self):
        return super.__str__()
                 

# Implement Inventory Class
class Inventory:
    def __init__( self ):
        self.items = []
        # Variables to keep track of # of items per category
        # and the category's index range within the list
        self.book = -1
        self.cd_vinyl = -1
        self.index_cd = -1
        self.collectible = -1
        self.index_col = -1
        self.electronics = -1
        self.index_ele = -1
        self.fashion = -1
        self.index_fas = -1
        self.home_garden = -1
        self.index_home = -1
        # Methods to run at initialization to get a list of items
        self.parse_file()
        self.organize_item_list()

            
    # Method to read through each csv, create class object,
    # and add the object to list
    # also keeps track of how many items were in each csv file
    # and the index range of the item categories
    def parse_file( self ):
        ID = -2
        reader = csv.reader(open('book.csv'))
        for line in reader:
            ID += 1
            b = Book(ID, *line) #Puts items and attributes into relevent class
            self.items.append(b) 
            self.book += 1
        ID -= 1
        reader = csv.reader(open('cd_vinyl.csv'))
        for line in reader:
            ID += 1
            c = CD(ID, *line) #Puts items and attributes into relevent class
            self.items.append(c)
            self.cd_vinyl += 1
            self.index_cd += 1
        self.index_col += self.index_cd
        ID -= 1
        reader = csv.reader(open('collectible.csv'))
        for line in reader:
            ID += 1
            d = Collectible(ID, *line) #Puts items and attributes into relevent class
            self.items.append(d)
            self.collectible += 1
            self.index_col += 1
        self.index_ele += self.index_col
        ID -= 1
        reader = csv.reader(open('electronics.csv'))
        for line in reader:
            ID += 1
            e = Electronics(ID, *line) #Puts items and attributes into relevent class
            self.items.append(e)
            self.electronics += 1
            self.index_ele += 1
        self.index_fas += self.index_ele
        ID -= 1
        reader = csv.reader(open('fashion.csv'))
        for line in reader:
            ID += 1
            f = Fashion(ID, *line)
            self.items.append(f)
            self.fashion += 1
            self.index_fas += 1
        self.index_home += self.index_fas
        ID -= 1
        reader = csv.reader(open('home_garden.csv'))
        for line in reader:
            ID += 1
            g = Home(ID, *line)
            self.items.append(g)
            self.home_garden += 1
            self.index_home += 1

    # Method to remove the categories from the item list & saving them for future use
    def organize_item_list( self ):
        #get book categories and remove from item_list
        self.book_category = self.items[0]
        self.items.pop(0)
        #get cd_vinyl categories and remove from item_list
        self.cd_vinyl_category = self.items[self.book]
        self.items.pop(self.book)
        #get collectible category and remove from item_list
        self.collectible_category = self.items[self.book + self.cd_vinyl]
        self.items.pop(self.book + self.cd_vinyl)
        #get ebay item categories and remove from item_list
        self.ebay_category = self.items[self.book + self.cd_vinyl + self.collectible]
        self.items.pop(self.book + self.cd_vinyl + self.collectible)
        self.items.pop(self.book + self.cd_vinyl + self.collectible + self.electronics)
        self.items.pop(self.book + self.cd_vinyl + self.collectible + self.electronics + self.fashion)
        
    # Method to return requested items in the list
    def print_inventory( self, first_item, last_item ):
        for x in range( first_item, last_item ):
            print( '----------' )
            print( self.items[x] )
            print("")
        
    # Method to print the total value of the inventory
    def compute_inventory( self ):
        self.value = 0.0
        # scan through books and add up Prices
        for x in range( self.book ):
            self.value += float(self.items[x][self.book_category.index('Price')])
        return self.value
        # scan through cd_vinyl and add up Prices
        
    #testing method
    def print_list(self):
        return self.items


c = Inventory()


