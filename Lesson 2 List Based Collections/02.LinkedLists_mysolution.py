"""
Linkedlist is an extension of a list but it is definetly not an array.
There are no indices.
In linkedlist, we store a reference to the next element in the list.

Advantage;
adding and removing O(1)

Disadvantage:

To add an element, remember to not to lose your next element(reference) in the list. So, first 
"""

"""
The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular spot in the list.
"delete" will delete the first element with that particular value.
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist(object):
    def __init__(self, head=None):
        self.head = head

    # a method to add a new element to the end of our LinkedList
    def append(self, new_element):
        current = self.head

        if self.head:
            while current.next:
                current = current.next
                
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if the position is not in the list."""

        current = self.head

        for i in range(1, position):
            if current.next:
                current = current.next
            else:
                return None

        return current.value

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        current = self.head

        for i in range(1, position-1):
            if current.next:
                current = current.next
            else:
                return None

        new_element.next = current.next
        current.next = new_element

    def delete(self, value):
        """Delete the first node with a given value"""

        current = self.head 

        if current and current.value != value:

            while current.next:
                if current.next.value == value:

                    current.next = current.next.next
                else:
                    current = current.next
        else:
            self.head = current.next
"""
#### Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3))

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3))

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1))
# Should print 4 now
print(ll.get_position(2))
# Should print 3 now
print(ll.get_position(3))
"""