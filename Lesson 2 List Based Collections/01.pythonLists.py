"""
LIST:
List can contain any type of value.


ARRAY:
Array should keep the same type of value.
- advantage:
if you need to access a location in the middle, it is easy.
- disadvantage:
insertion and deletion

Inserting into a list is easy (happens in constant time). 
However, inserting into an array is O(n), since you may need to shift elements to make space for the one you're inserting, or even copy everything to a new array if you run out of space. 
Thus, inserting into a Python list is actually O(n), while operations that search for an element at a particular spot are O(1). 
You can see the runtime of other list operations https://wiki.python.org/moin/TimeComplexity



"""