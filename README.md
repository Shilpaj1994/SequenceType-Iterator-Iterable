

# Iterators and Iterables



### Pre-requisites

Before we go into details of Iterators and Iterables, we will need to cover some pre-requisites concepts

- If the `__getitem__` method is implemented in a class, use the `next()` to access the next element in the sequence

- Internal for-loop

  - The Python's `for-loop` works internally as coded below
  - When the `StopIteration` is raised, the `for-loop` handles it internally

  ```python
  while True:
      try:
          next(some_obj)
      except StopIteration:
          break
  ```

  



[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nL9Fva2DdagWse5qa4DQb2InRuf84jN2?usp=sharing)

### DataSet Class

- To explain the sequence types, iterators and iterables, we will use a normal class and convert it to adding dunder methods

- Below is the bare-minimum class for this purpose:

  ```python
  class DataSet:
      """
      Class with functionalities of sequence types and iterables
      """
      def __init__(self):
          """
          Constructor
          """
          self._raw_data = ["Apple", "Mango", "Banana", "Pineapple", "Papaya"]
  ```

   

### Sequence Type

- A sequence type is a datatype which has a concept of **positional ordering** that is, we can access the element of the datatype by indexing

- This is like accessing the elements of the Python `list` by indexing and slicing

- In order to make our class a sequence type, we need to add the following two dunder methods:

  - `__len__`
  - `__getitem__`

  ```python
  class DataSet:
      """
      Class with functionalities of sequence types and iterables
      """
      def __init__(self):
          """
          Constructor
          """
          self._raw_data = ["Apple", "Mango", "Banana", "Pineapple", "Papaya"]
          
      def __len__(self):
          """
          Method to return the length of the object
          """
          return len(self._raw_data)
      
      def __getitem__(self, index):
          """
          Method to implement the indexing and slicing
          """
          length_of_sequence = len(self._raw_data)
          
          if isinstance(index, int):
              if index < 0:
                  index = length_of_sequence + index
              if index < 0 or index > length_of_sequence:
                  raise IndexError
              else:
                  return self._raw_data[index]
          else:
              start, stop, step = index.indices(length_of_sequence)
              rng = range(start, stop, step)
              return [self._raw_data[index] for index in rng]
          
  ```

- By adding the above two methods, we can create an object of our class and access the data using indexing as well as slicing

  ```python
  if __name__ == '__main__':
      # Create an object of the class
      _object = DataSet()
      
      # Access elements by indexing
      favourite_fruit = _object[1]
      
      # Access elements by slicing
      fruits_reverse = _object[::-1]
  ```

- This is one way of accessing the elements from `DataSet`

- The restrictions that we have with sequence types are: 

  - `DataSet` should have ordered elements and 
  - The elements should be numerically index-able

- Sometimes, we might need to access data elements in the different sections of the code. This can be done by adding another variable to keep track of the index but a better way of achieving this is by using Iterators



### Iterators

- In order to access our `DataSet` which is unordered and might not have indexable data, we can use the `__next__` method

- Implementing `__next__` method will provide us 2 features:

  - we will know when to stop
  - we can access the unordered data

  ```python
  class DataSet:
      """
      Class with functionalities of sequence types and iterables
      """
      def __init__(self, length):
          """
          Constructor
          """
          self._raw_data = ["Apple", "Mango", "Banana", "Pineapple", "Papaya"]
          self._index = 0
          self.length = length
          
      def __len__(self):
          """
          Method to return the length of the object
          """
          return len(self._raw_data)
      
      def __next__(self):
          """
          Method to access next element of the iterator
          """
          if self._index >= self.length:
              raise StopIteration
          else:
              result = self._raw_data[self._index]
              self._index += 1
              return result
  ```

  ```python
  _obj = DataSet(3)
  
  while True:
    try:
      print(next(_obj))
    except StopIteration:
      break
  ```

- But the issue is -  we cannot use the class objects with `for-loop`

- If we add the `__getitem__` then it will work with `for-loop` but the restriction of using ordered data and numerically indexable data will be back in place

- In order to make our class as iterator, we need to add another dunder functions - `__iter__`

- `__iter__` method will return itself and that will give the class ability to iterate over in the `for-loop`

  ```python
  class DataSet:
      """
      Class with functionalities of sequence types and iterables
      """
      def __init__(self, length):
          """
          Constructor
          """
          self._raw_data = ["Apple", "Mango", "Banana", "Pineapple", "Papaya"]
          self._index = 0
          self.length = length
          
      def __len__(self):
          """
          Method to return the length of the object
          """
          return len(self._raw_data)
      
      def __getitem__(self, index):
          """
          Method to implement the indexing and slicing
          """
          length_of_sequence = len(self._raw_data)
          
          if isinstance(index, int):
              if index < 0:
                  index = length_of_sequence + index
              if index < 0 or index > length_of_sequence:
                  raise IndexError
              else:
                  return self._raw_data[index]
          else:
              start, stop, step = index.indices(length_of_sequence)
              rng = range(start, stop, step)
              return [self._raw_data[index] for index in rng]
          
      def __iter__(self):
          """
          Method to make the class iterator
          """
          return self
      
      def __next__(self):
          """
          Method to access next element of the iterator
          """
          if self._index >= self.length:
              raise StopIteration
          else:
              result = self._raw_data[self._index]
              self._index += 1
              return result
  ```

- Now, we can iterate over the data by providing the length of the data that we need in the `for-loop`

  ```python
  some_obj = DataSet(3)
  for data in some_obj:
    print(data)
  ```

- If we use the same iterator object again, we cannot access the data from it

  ```python
  for data in some_obj:
    print(data)
  ```

  Now, this code will not print anything

- This is because the iterator is **exhausted**. This is the main difference between the Iterator and the Iterable

- Iterator gets exhausted while the Iterables cannot get exhausted

- Python `list` is an Iterable and hence they can return the data even after called over multiple time i.e. they don't get exhausted

- In this case, if we want to use that object again then we need to create an object again to iterate over it



### Iterables

- In the iterator, every time we call the object the `__iter__` method is called **once** and then `__next__` till `StopIteration` is raised

- So, we have to modify the code in such a way that when the object is exhausted, it should call the `__iter__` method

- Hence, we created a separate Iterator class which is called by the `__iter__` method of the `DataSet`

- In order to convert our code into an Iterable, we have to do the following changes:

  - We will need to create a separate class for Iterator
  - This class should have `__iter__` and `__next__` since it is an iterator
  - This Iterator class should take an instance of the `DataSet` class
  - In the `DataSet` class, the `__iter__ ` method should return the class instance to the Iterator class

  ```python
  class DataSet:
      """
      Class with functionalities of sequence types and iterables
      """
      def __init__(self):
          """
          Constructor
          """
          self._raw_data = ["Apple", "Mango", "Banana", "Pineapple", "Papaya"]
          
      def __len__(self):
          """
          Method to return the length of the object
          """
          return len(self._raw_data)
      
      def __getitem__(self, index):
          """
          Method to implement the indexing and slicing
          """
          length_of_sequence = len(self._raw_data)
          
          if isinstance(index, int):
              if index < 0:
                  index = length_of_sequence + index
              if index < 0 or index > length_of_sequence:
                  raise IndexError
              else:
                  return self._raw_data[index]
          else:
              start, stop, step = index.indices(length_of_sequence)
              rng = range(start, stop, step)
              return [self._raw_data[index] for index in rng]
          
      def __iter__(self):
          """
          Method to make the class iterator
          """
          return self.Iterator(self)
          
      class Iterator:
          """
          """
          def __init__(self, iterable_obj):
              """
              """
              self._iterable_obj = iterable_obj
              self._index = 0
              
          def __iter__(self):
              """
              """
              return self
      
          def __next__(self):
              """
              Method to access next element of the iterator
              """
              if self._index >= len(self._iterable_obj):
                  raise StopIteration
              else:
                  result = self._iterable_obj._raw_data[self._index]
                  self._index += 1
                  return result
  ```

- Now, if we create an object of this class and iterate over it multiple times, we will still get output values. Just like Python `list`

- This is how we created a `DataSet` class which is a sequence type as well as an Iterable



### Summary

| Methods       | Sequence | Iterator | Iterable |
| ------------- | -------- | -------- | -------- |
| `__getitem__` | YES      | Maybe    | Maybe    |
| `__len__`     | YES      | Maybe    | Maybe    |
| `__next__`    | NO       | YES      | Maybe    |
| `__iter__`    | NO       | YES      | YES      |





---



[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1olYVpdNqSY_2bbL82ny3cexDu3a_2BN3?usp=sharing)

## Code Details

```python
# Standard Library Imports
import math
from operator import sub, mul, truediv
from functools import lru_cache
from collections import namedtuple
from typing import Union


class Polygons:
    """
    Class containing methods for a regular polygon
    """

    def __init__(self, edges, circumradius) -> None:
        """
        Constructor
        :param edges: number_of_edges of largest circumscribed polygon
        :param circumradius: common radius of a circle in which polygon is inscribed
        """
        if not isinstance(edges, int) or edges <= 2:
            raise ValueError(f"Enter valid input for number of edges. It cannot be less than 3. Current value: {edges}")
        elif not isinstance(circumradius, int) or circumradius < 1:
            raise ValueError(f"Enter valid input for number of circumradius. It cannot be less than or equal to 1. "
                             f"Current value: {circumradius}")
        else:
            self.max_edges = edges
            self.circumradius = circumradius

            self._ratio_data = dict()
            self._records = []

            self._ratio_data = {edge: self._property_calculations(edge) for edge in range(3, edges + 1)}
            self._index = 0

    def __iter__(self):
        """
        Method to
        """
        return self.Iterator(self)

    class Iterator:
        """
        Iterator Class
        """
        def __init__(self, obj):
            """
            Constructor for Iterator
            """
            self._obj = obj
            self._index = 0

        def __iter__(self):
            """
            Iter method to make class as an Iterator
            """
            return self

        def __next__(self):
            """
            Next method to access next element of the dataset
            """
            if self._index >= len(self._obj):
                raise StopIteration
            else:
                item = self._obj._records[self._index]
                self._index += 1
                return item

    def __getitem__(self, index) -> Union[float, list]:
        """
        Method to return the properties of a regular polygon
        :param index: index number of a polygon considering polygon with 3 edges has 0 index
        :return: NamedTuple or list of namedtuple containing the properties of regular polygon
        """
        # Length of sequence considering polygons starts from triangle(i.e. edges=3)
        length_of_sequence = self.max_edges - 2

        if isinstance(index, int):
            if index < 0:
                index = length_of_sequence + index
            if index < 0 or index > length_of_sequence:
                raise IndexError
            else:
                return self._records[index]
        else:
            start, stop, step = index.indices(length_of_sequence)
            rng = range(start, stop, step)
            return [self._records[index] for index in rng]

    @lru_cache(2 ** 10)
    def _property_calculations(self, edges):
        """
        Method to calculate all the property value for a regular polygon
        :param edges: Number of edges for a polygon
        :return: output of area:perimeter ratio
        """
        # NamedTuple to store the record of data
        PolygonData = namedtuple('PolygonData',
                                 "edges vertices interior_angle edge_length apothem area perimeter ratio")
        PolygonData.__doc__ = "Data associated with a regular polygon inscribed in a circle"
        PolygonData.edges.__doc__ = "Number of edges of a regular polygon"
        PolygonData.vertices.__doc__ = "Number of vertices of a regular polygon"
        PolygonData.interior_angle.__doc__ = "Interior angle of a regular polygon"
        PolygonData.edge_length.__doc__ = "Edge length of a regular polygon"
        PolygonData.apothem.__doc__ = "Apothem of a regular polygon"
        PolygonData.area.__doc__ = "Area of a regular polygon"
        PolygonData.perimeter.__doc__ = "Perimeter of a regular polygon"
        PolygonData.ratio.__doc__ = "Ratio of area to perimeter for a regular polygon"

        # Calculate all the properties of polygon
        _edges = edges
        _vertices = _edges
        _interior_angle = truediv(mul(sub(_edges, 2), 180), _edges)
        _edge_length = mul(mul(2, self.circumradius), math.sin(truediv(math.pi, _edges)))
        _apothem = mul(self.circumradius, math.cos(truediv(math.pi, _edges)))
        _area = mul(mul(0.5, _edges), mul(_edge_length, _apothem))
        _perimeter = mul(_edges, _edge_length)
        _ratio = truediv(_area, _perimeter)

        # Store all the data
        self._records.append(PolygonData(edges=_edges, vertices=_vertices, interior_angle=_interior_angle,
                                         edge_length=_edge_length, apothem=_apothem, area=_area, perimeter=_perimeter,
                                         ratio=_ratio))
        # Return the ratio of area:perimeter
        return _ratio

    def __repr__(self) -> str:
        """
        Method returning a string representation of a class object
        :return: String representation
        """
        return f"Regular Polygons with edges ranging from 3 to {self.max_edges} all inscribed in a circle of radius {self.circumradius}"

    def max_efficiency_polygon_edges(self) -> int:
        """
        Method to return the edges value of a polygon with maximum efficiency of area:perimeter ratio
        :return: number of edges of polygon with max efficiency
        """
        max_ratio = max(self._ratio_data.values())
        return list(self._ratio_data.keys())[list(self._ratio_data.values()).index(max_ratio)]

    def __len__(self) -> int:
        """
        Method to print total number of polygons in the sequence
        :return: Length of an object
        """
        return self.max_edges - 2
```





## Test Cases

| Test Cases                                    | Description                                                  |
| --------------------------------------------- | ------------------------------------------------------------ |
| `test_custom_polygon_edges()`                 | Test case to check if exceptions are raised when invalid value of edges is passed |
| `test_custom_polygon_circumradius()`          | Test case to check if exceptions are raised when invalid value of circumradius is passed |
| `test_custom_polygon_repr()`                  | Test case to check if `__repr__` method is implemented       |
| `test_custom_polygon_len()`                   | Test case to check if `__len__` method is implemented        |
| `test_custom_polygon_getitem()`               | Test case to check if `__getitem__` method is implemented    |
| `test_custom_polygon_max_efficiency()`        | Test case to check if `__getitem__` method is implemented    |
| `test_custom_polygon_max_efficiency_output()` | Test case to return the number of edges of a polygon with maximum area:perimeter ratio |
| `test_getitem_inputs()`                       | Test case to check positive, negative and zero indexing is supported by `__getitem__` function |
| `test_getitem_raises()`                       | Test case to check if proper errors are raised when wrong index are passed to `__getitem__` |
| `test_getitem_slicing()`                      | Test case to check if `__getitem__` supports slicing         |
| `test_len()`                                  | Test case to check if the length of object is correct        |
| `test_iterables()`                            | Test case to check if Polygons is an Iterables and not Iterator |

