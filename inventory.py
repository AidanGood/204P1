'''CSCI 204 Project 1 
Professor Meng
Aidan Good
'''
import csv

# Parent Item class
class Item:
    # Construct variables that are shared among all items
    def __init__( self, ID, name, price, quantity, date ):
        self.ID = ID
        self.name = name
        self.price = price
        self.quantity = quantity
        self.date = date
        
    # returns string common among all items    
    def __str__( self ):
        return'''
<ul style="list-style-type:none;">
    <li>----------</li>
    <li>ID: {}</li>
    <li>Name: {}</li>
    <li>Price: ${}</li>
    <li>Date: {}</li>
    <li>Quantity: {}</li>'''.format( self.ID, self.name, self.price, self.date, self.quantity )

    # Method to search the name for a specific phrase and return
    # True if found or False if not found in the name.
    # Common among all items
    def search( self, string ):
        if string in self.name:
            return True
        else:
            return False

    # Method to calculate the value of total collection of the item
    # Common among all items
    def compute_value( self ):
        return float(self.price) * float(self.quantity)
        
# Book subclass 
class Book( Item ):
    def __init__( self, ID, name, date, publisher, author, price, ISBN, quantity ):
        super().__init__( ID, name, price, quantity, date )
        self.publisher = publisher
        self.author = author
        self.ISBN = ISBN

    # Returns string common to all book items    
    def __str__( self ):
        return super().__str__() +'''
    <li>Author: {1}</li>
    <li>Publisher: {0}</li>
    <li>ISBN: {2}</li>
</ul>'''.format( self.publisher, self.author, self.ISBN )

# CD_Vinyl subclass
class CD( Item ):
    def __init__( self, ID, name, artist, label, ASIN, date, price, quantity ):
        super().__init__( ID, name, price, quantity, date )
        self.artist = artist
        self.label = label
        self.ASIN = ASIN

    # Returns string common to all CD Vinyl items
    def __str__( self ):
        return super().__str__() + '''
    <li>Artist: {0}</li>
    <li>Label: {1}</li>
    <li>ASIN: {2}</li>
</ul>'''.format( self.artist, self.label, self.ASIN )

# Collectible subclass
class Collectible( Item ):
    def __init__( self, ID, name, price, date, owner, quantity ):
        super().__init__( ID, name, price, quantity, date )
        self.owner = owner

    # returns string common to all collectible items
    def __str__( self ):
        return super().__str__() + '''
    <li>Owner: {0}</li>
</ul>'''.format( self.owner )

# Ebay parent class Item subclass
class Ebay( Item ):
    def __init__( self, ID, name, price, date, manufacturer, quantity ):
        super().__init__( ID, name, price, quantity, date )
        self.manufacturer = manufacturer

    # returns string common to all ebay class items
    def __str__( self ):
        return super().__str__() + '''
    <li>Manufacturer: {0}</li>
</ul>'''.format( self.manufacturer )

# Electronics subclass
class Electronics( Ebay ):
    def __init__( self, ID, name, price, date, manufacturer, quantity ):
        super().__init__( ID, name, price, date, manufacturer, quantity )



# Fashion subclass
class Fashion( Ebay ):
    def __init__( self, ID, name, price, date, manufacturer, quantity ):
        super().__init__( ID, name, price, date, manufacturer, quantity )


    
# Home Garden subclass
class Home( Ebay ):
    def __init__( self, ID, name, price, date, manufacturer, quantity ):
        super().__init__( ID, name, price, date, manufacturer, quantity )


                 

# Implement Inventory Class
class Inventory:
    def __init__( self ):
        self.items = []
        self.count = 0 
        # Variables to keep track of # of items per category
        self.book = -1
        self.cd_vinyl = -1
        self.collectible = -1
        self.electronics = -1
        self.fashion = -1
        self.home_garden = -1
        
        # Methods that run at initialization to get list of objects
        # and variables
        self.parse_file()
        self.organize_item_list()
        self.invent_count()

            
    # Method to read through each csv, add object to respective class,
    # and add the object to the inventory list
    # also keeps track of how many items were in each csv file
    def parse_file( self ):
        ID = -2
        # Reads the Book csv file
        reader = csv.reader( open('book.csv') )
        for line in reader:
            ID += 1
            b = Book( ID, *line ) #Puts item and attributes into relevent class
            self.items.append(b)  #Adds object to inventory list
            self.book += 1
        ID -= 1
        #reads the CD Vinyl csv file
        reader = csv.reader( open('cd_vinyl.csv') )
        for line in reader:
            ID += 1
            c = CD( ID, *line ) #Puts item and attributes into relevent class
            self.items.append(c) #Adds object to inventory list
            self.cd_vinyl += 1
        ID -= 1
        # Reads the Collectible csv file
        reader = csv.reader( open('collectible.csv') )
        for line in reader:
            ID += 1
            d = Collectible( ID, *line ) #Puts item and attributes into relevent class
            self.items.append(d) #Adds object to inventory list
            self.collectible += 1
        ID -= 1
        # Reads the Electronics csv file
        reader = csv.reader( open('electronics.csv') )
        for line in reader:
            ID += 1
            e = Electronics( ID, *line ) #Puts item and attributes into relevent class
            self.items.append(e) #Adds object to inventory list
            self.electronics += 1
        ID -= 1
        # Reads the Fashion csv file
        reader = csv.reader( open('fashion.csv') )
        for line in reader:
            ID += 1
            f = Fashion( ID, *line ) # Puts item and attributes into relevent class
            self.items.append(f) # Adds object to inventory list
            self.fashion += 1
        ID -= 1
        # Reads the Home Garden csv file
        reader = csv.reader( open('home_garden.csv') )
        for line in reader:
            ID += 1
            g = Home( ID, *line ) # Puts item and attributes into relevent class
            self.items.append(g) # Adds object to inventory list
            self.home_garden += 1

    # Method to remove the category titles from the item list,
    # otherwise column titles from csv files will appear in list
    def organize_item_list( self ):
        # column titles are the first line for each csv file, we tracked
        # the end of each csv file in method parse_file(), so we know
        # where the titles are stored within self.items
        self.items.pop( 0 )
        self.items.pop( self.book )
        self.items.pop( self.book + self.cd_vinyl )
        self.items.pop( self.book + self.cd_vinyl + self.collectible )
        self.items.pop( self.book + self.cd_vinyl + self.collectible \
                        + self.electronics )
        self.items.pop( self.book + self.cd_vinyl + self.collectible \
                        + self.electronics + self.fashion )

    # Method to count number of items in inventory
    def invent_count( self ):
        for x in self.items:
            self.count += 1
    
    # Method to print requested items in the list 
    def print_inventory( self, first_item, last_item ):
        staging = ''
        for x in range( first_item, last_item ):
            staging += str(self.items[x] )
        return staging
        
    # Method to print the total value of the inventory
    def compute_inventory( self ):
        self.value = 0.0
        for x in self.items:
            # get value from each item in list and add it all together
            self.value += float( x.compute_value() )
        return self.value

    # Method to return type of item
    def check_type( self, item ):
        if isinstance( item, Book ):
            return ' Book'
        elif isinstance( item, CD ):
            return ' CD Vinyl'
        elif isinstance( item, Collectible ):
            return ' Collectible'
        elif isinstance( item, Electronics ):
            return ' Electronics'
        elif isinstance( item, Fashion ):
            return ' Fashion'
        elif isinstance( item, Home ):
            return ' Home Garden'
        else:
            return "Item Category not found"

    # Method to print out every item in a category
    def print_category( self, category ):
        # make input case insenstive by always converting to lowercase
        staging = ''
        staging += '<p>--- Print information of items of the type {} ---</p>'.format(category)
        category = category.lower()
        
        # check for which category was asked for, and return requested one.
        # covers some common variants of the categories, and returns message 
        # if none found 
        if category in ('book', 'books'):
            for x in self.items:
                if isinstance( x, Book ):
                    staging += str(x) 
        elif category in ('cd', 'cd vinyls', 'cd_vinyl', 'vinyl'): 
            for x in self.items:
                if isinstance( x, CD ):
                    staging += str(x)
        elif category in ('collectible', 'collectibles'):
            for x in self.items:
                if isinstance( x, Collectible ):
                    staging += str(x)
        elif category in ('electronic', 'electronics'):
            for x in self.items:
                if isinstance( x, Electronics ):
                    staging += str(x)
        elif category in ('fashion'):
            for x in self.items:
                if isinstance( x, Fashion ):
                    staging += str(x)
        elif category in ('home garden', 'home_garden', 'home', 'garden'): 
            for x in self.items:
                if isinstance( x, Home ):
                    staging += str(x)
        # In case no matching category
        else:
            staging += '<p>No category of that type found</p>' 
        return staging
        
    # Method to search for all items that contain the searched for phrase 
    def search_item( self, string ):
        staging = ''
        string = str( string ) # Convert numbers, etc. to string
        staging += '<p>Search for all items with "{}" in name:</p>'.format( string )
        # For loop to go through each item and seach the name for the string
        for x in range( self.count ):
            # search() method in Item parent class that returns True if found
            if self.items[x].search( string ): 
                staging += str( self.items[x] )
            else:
                pass
        return staging
            
        
    
    # Method for testing purposes
    def print_list( self ):
        return self.items





