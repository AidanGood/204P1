"""A test program for the Inventory class without a web interface.
It is expected that the Inventory class developed by the students
will be able to use this test program directly, which means the student
program must have the following.

1. The Inventory class must be in a file called 'inventory.py' that resides
   in the same directory as this test program.
2. The file 'inventory.py' contains a function named 'create_inventory'.
3. The Inventory class must have the following methods.
   a. 'print_inventory(self, begin = 0, end = -1)' that prints items 
      from 'begin' to 'end' with default values of 0 and -1, respectively.
   b. 'check_type(self, item)' that returns a text form of the item type.
   c. 'compute_inventory(self)' that computes the total dollar value
      of the inventory.
   d. 'print_category(self, cat_name)' that prints the list of items in the
      category of 'cat_name', e.g., Book or fashion.
   e. 'search_item(self, item_name)' that returns all items that contain
     the given text 'item_name' as its partial name.
4. The Inventory class has a data member named 'items' which should be 
   a Python list.
"""
from inventory import *

def test_inventory():
    """Test various features of Inventory class"""

    invent = Inventory()    # Create inventory

    invent.print_inventory(3, 6)   # Print items from 3 to 5, inclusive

    # Print the name and the type of first and last item
    print('first:')
    print(invent.items[0].name)
##    print('type:', invent.check_type(invent.items[0]))
##
##    print('last:')
##    print(invent.items[invent.count-1].name)
##    print('type:', invent.check_type(invent.items[invent.count-1]))

    # Print the total value of the inventory
    #print('Total value of the inventory: $' + str(invent.compute_inventory()))

##    # Print a particular category of items
##    invent.print_category('fashion')
##    invent.print_category('Book')
##
##    # Search and print items that contain the term as a substring in its name
##    invent.search_item('Time')
##    invent.search_item('Gar')

test_inventory()
