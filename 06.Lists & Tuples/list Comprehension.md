

Python Lists
Lists are one of the four built-in data structures in Python. Other data structures that you might know are tuples, dictionaries, and sets. A list in Python is different from, for example, int or bool, in the sense that it's a compound data type: you can group values in lists. These values don't need to be of the same type: they can be a combination of boolean, String, integer, float values.

List literals are a collection of data surrounded by brackets, and the elements are separated by a comma. The list is capable of holding various data types inside it, unlike arrays.

For example, let's say you want to build a list of courses then you could have:

courses = ['statistics', 'python', 'linear algebra']

Note that lists are ordered collections of items or objects. This makes lists in Python "sequence types", as they behave like a sequence. This means that they can be iterated using for loops. Other examples of sequences are Strings, tuples, or sets.

Lists are similar in spirit to strings you can use the len() function and square brackets [ ] to access the data, with the first element indexed at 0.

Tip: if you'd like to know more, test, or practice your knowledge of Python lists, you can do so by going through the most common questions on Python lists here.

Now, on a practical note: you build up a list with two square brackets (start bracket and end bracket). Inside these brackets, you'll use commas to separate your values. You can then assign your list to a variable. The values that you put in a Python list can be of any data type, even lists!

Take a look at the following example of a list:

# Assign integer values to `a` and `b`
a = 4
b = 9

# Create a list with the variables `a` and `b`
count_list = [1,2,3,a,5,6,7,8,b,10]
count_list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Note that the values of a and b have been updated in the list count_list.

Creation of List
A list is created by placing all the items inside a square bracket [] separated by commas. It can have an infinite number of elements having various data types like string, integer, float, etc.

list1 = [1,2,3,4,5,6] #with same data type
list1
[1, 2, 3, 4, 5, 6]
list2 = [1, 'Aditya', 2.5] #with mixed data type
list2
[1, 'Aditya', 2.5]
Accessing Elements from a List
Elements from the list can be accessed in various ways:

Index based: You can use the index operator to access the element from a list. In python, the indexing starts from 0 and ends at n-1, where n is the number of elements in the list.

Indexing can be further categorized into positive and negative indexing.

index = [1,2,3,4,5]
index[0], index[4] #positive indexing
(1, 5)
index[5] #this will give an error since there is no element at index 5 in the list
---------------------------------------------------------------------------

IndexError                                Traceback (most recent call last)

<ipython-input-39-fd6e7e3edbf2> in <module>
----> 1 index[5] #this will give an error since there is no element at index 5 in the list


IndexError: list index out of range
index[-1], index[-2] #negative indexing, here -1 means select first element from the last
(5, 4)
Slice based: This is helpful when you want to access a sequence/range of elements from the list. The semicolon (:) is used as a slice operator to access the elements.
index[:3], index[2:]
([1, 2, 3], [3, 4, 5])
List Methods
Some of the most commonly used list methods are :



Python List Comprehension
With the recap of the Python lists fresh in mind, you can easily see that defining and creating lists in Python can be a tiresome job. Typing in all of the values separately can take quite some time, and you can easily make mistakes.

List comprehension in Python is also surrounded by brackets, but instead of the list of data inside it, you enter an expression followed by for loop and if-else clauses.

A most basic form of List comprehensions in Python are constructed as follows: list_variable = [expression for item in collection] The first expression generates elements in the list followed by a for loop over some collection of data which would evaluate the expression for every item in the collection.

But how do you get to this formula-like way of building and using these constructs in Python? Let's dig a little bit deeper.

The Mathematics
Luckily, Python has the solution for you: it offers you a way to implement a mathematical notation to do this: list comprehension.

Remember in maths, the common ways to describe lists (or sets, or tuples, or vectors) are: S = {x² : x in {0 ... 9}} V = (1, 2, 4, 8, ..., 2¹²) M = {x | x in S and x even} In other words, you'll find that the above definitions tell you the following:

S is a sequence that contains values between 0 and 9 included, and each value is raised to the power of two.
The sequence V, on the other hand, contains the value 2 that is raised to a certain power x. The power x starts from 0 and goes till 12.

Lastly, the sequence M contains only the even elements from the sequence S.

If the above definitions look a little cryptic to you, then take a look at the actual lists that these definitions would produce: S = {0, 1, 4, 9, 16, 25, 36, 49, 64, 81} V = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096} M = {0, 4, 16, 36, 64} You see the result of each list and the operations that were described in them!

Now that you've understood some of the maths behind lists, you can translate or implement the mathematical notation of constructing lists in Python using list comprehensions! Take a look at the following lines of code:

'''
S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
S
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
V
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
'''
If you only want to extract expression for a specific set of data from the entire collection, you can add on an if clause after the for loop. The expression will be added to the list only if the if clause is True. You can even have more than one if clause, and the expression will be in the list only if all the if clauses return True.

Similarly, to select only an even number from the collection S, you will have an if clause which will check whether the given element is even or not. If it is even then that element will be added to the list.

M = [x for x in S if x % 2 == 0]