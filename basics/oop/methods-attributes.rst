OOP Methods and Attributes
==========================


Rationale
---------
* Methods are functions in the class
* First argument is always instance (``self``)
* While calling function you never pass ``self``
* Prevents copy-paste code
* Improves readability
* Improves refactoring
* Decomposes bigger problem into smaller chunks

Syntax:

>>> class MyClass:
...     def __init__(self):
...         self.myfield = 'some value'
...
...     def mymethod(self):
...         print(self.myfield)
>>>
>>>
>>> my = MyClass()
>>> my.mymethod()
some value


Methods Accessing Fields
------------------------
Methods Accessing Fields:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
...
...     def say_hello(self):
...         print(f'My name... {self.name}')
>>>
>>>
>>> jose = Astronaut('José Jiménez')
>>> jose.say_hello()
My name... José Jiménez

``self.name`` must be defined before accessing:

>>> class Astronaut:
...     def say_hello(self):
...         print(f'My name... {self.name}')
>>>
>>>
>>> jose = Astronaut()
>>> jose.say_hello()
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'name'


Methods Calling Other Methods
-----------------------------
Methods Calling Other Methods:

>>> class Astronaut:
...     def get_name(self):
...         return 'José Jiménez'
...
...     def say_hello(self):
...         name = self.get_name()
...         print(f'My name... {name}')
>>>
>>>
>>> jose = Astronaut()
>>> jose.say_hello()
My name... José Jiménez

Methods calling other methods:

>>> class Iris:
...     def __init__(self):
...         self.sepal_length = 5.1
...         self.sepal_width = 3.5
...         self.petal_length = 1.4
...         self.petal_width = 0.2
...
...     def sepal_area(self):
...         return self.sepal_length * self.sepal_width
...
...     def petal_area(self):
...         return self.petal_length * self.petal_width
...
...     def total_area(self):
...         return self.sepal_area() + self.petal_area()
>>>
>>>
>>> flower = Iris()
>>> print(flower.total_area())
18.13

Since Python 3.7 there is a ``@dataclass`` decorator, which automatically generates ``__init__()`` arguments and fields.
More information in `OOP Dataclass`

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length = 5.1
...     sepal_width = 3.5
...     petal_length = 1.4
...     petal_width = 0.2
...     species: str = 'Iris'
...
...     def sepal_area(self):
...         return self.sepal_length * self.sepal_width
...
...     def petal_area(self):
...         return self.petal_length * self.petal_width
...
...     def total_area(self):
...         return self.sepal_area() + self.petal_area()
>>>
>>>
>>> flower = Iris()
>>> print(flower.total_area())
18.13


Examples
--------
* Documentation: https://atlassian-python-api.readthedocs.io
* Source Code: https://github.com/atlassian-api/atlassian-python-api
* Examples: https://github.com/atlassian-api/atlassian-python-api/tree/master/examples

.. code-block:: console

    $ pip install atlassian-python-api

>>> # doctest: +SKIP
... from atlassian import Jira
>>>
>>> # doctest: +SKIP
... jira = Jira(
...     url='http://example.com:8080',
...     username='myusername',
...     password='mypassword')
>>>
>>> JQL = 'project = DEMO AND status IN ("To Do", "In Progress") ORDER BY issuekey'
>>>
>>> # doctest: +SKIP
... result = jira.jql(JQL)
>>> # doctest: +SKIP
... print(result)

>>> # doctest: +SKIP
... from atlassian import Confluence
>>>
>>> # doctest: +SKIP
... confluence = Confluence(
...     url='http://example.com:8090',
...     username='myusername',
...     password='mypassword')
>>>
>>> # doctest: +SKIP
... result = confluence.create_page(
...     space='DEMO',
...     title='This is the title',
...     body='This is the body. You can use <strong>HTML tags</strong>!')
>>>
>>> # doctest: +SKIP
... print(result)

>>> class Point:
...     def __init__(self, x, y, z):
...         self.x = x
...         self.y = y
...         self.z = z
...
...     def get_coordinates(self):
...         return self.x, self.y, self.z
...
...     def show(self):
...         print(f'Point(x={self.x}, y={self.y}, z={self.z})')
>>>
>>>
>>> point = Point(x=1, y=2, z=3)
>>>
>>> print(point.x)
1
>>> print(point.y)
2
>>> print(point.z)
3
>>>
>>> point.get_coordinates()
(1, 2, 3)
>>>
>>> point.show()
Point(x=1, y=2, z=3)


Assignments
-----------
.. literalinclude:: assignments/oop_mthattr_a.py
    :caption: :download:`Solution <assignments/oop_mthattr_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_mthattr_b.py
    :caption: :download:`Solution <assignments/oop_mthattr_b.py>`
    :end-before: # Solution
