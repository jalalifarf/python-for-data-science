# NumPy Notes

## 1. Introduction to NumPy

NumPy stands for Numerical Python.

It is a Python library used for numerical computing and working with arrays.

NumPy is especially useful for:

- Numerical calculations
- Working with arrays
- Mathematical operations
- Statistical calculations
- Data processing

To use NumPy:

import numpy as np
## 2. Creating a NumPy Array

We can create a NumPy array using np.array().

Example:

import numpy as np


sensor_data = np.array([12.3, 11.8, 13.1, 12.7, 11.9])

A NumPy array can contain multiple numerical values.

We can check the array:

print(sensor_data)

Output:

[12.3 11.8 13.1 12.7 11.9]
## 3. NumPy Array vs Python List

A NumPy array is different from a normal Python list.

Python list:

data = [1, 2, 3, 4]

NumPy array:

data = np.array([1, 2, 3, 4])

NumPy arrays are designed for numerical operations and are generally more efficient for numerical data.

## 4. Array Attributes

NumPy arrays have several useful attributes.

Shape

shape returns the dimensions of the array.

arr = np.array([10, 20, 30, 40])


print(arr.shape)

Output:

(4,)

This means the array contains 4 elements.

Number of Dimensions

ndim returns the number of dimensions.

arr.ndim

Example:

arr = np.array([10, 20, 30])


print(arr.ndim)

Output:

1
Size

size returns the total number of elements.

arr.size

Example:

arr = np.array([10, 20, 30, 40])


print(arr.size)

Output:

4
Data Type

dtype shows the data type of the elements.

arr.dtype

Example:

arr = np.array([10, 20, 30])


print(arr.dtype)
## 5. Indexing

NumPy arrays use zero-based indexing.

For example:

sensor_data = np.array([12.3, 11.8, 13.1, 12.7])

The indexes are:

Index:       0     1     2     3
Value:     12.3  11.8  13.1  12.7

We can access an element using its index:

print(sensor_data[0])

Output:

12.3

The second element:

print(sensor_data[1])

Output:

11.8
## 6. Negative Indexing

Negative indexes start from the end of the array.

sensor_data[-1]

returns the last element.

For example:

print(sensor_data[-1])
## 7. Slicing

Slicing allows us to select part of an array.

Syntax:

array[start:stop]

Example:

sensor_data = np.array([12.3, 11.8, 13.1, 12.7, 11.9])


print(sensor_data[1:4])

Output:

[11.8 13.1 12.7]

The stop index is not included.

Slicing from the Beginning
sensor_data[:3]

This selects the first three elements.

Slicing to the End
sensor_data[2:]

This selects elements from index 2 to the end.

## 8. Mathematical Operations

NumPy allows us to perform mathematical operations directly on arrays.

Example:

data = np.array([10, 20, 30, 40])

Addition:

data + 5

Output:

[15 25 35 45]

Subtraction:

data - 5

Multiplication:

data * 2

Division:

data / 2

These operations are performed element by element.

## 9. Mathematical Operations Between Arrays

We can perform operations between arrays of the same shape.

Example:

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

Addition:

a + b

Output:

[11 22 33]

Multiplication:

a * b

Output:

[10 40 90]
## 10. Statistical Functions

NumPy provides several useful statistical functions.

Mean

The average value:

np.mean(sensor_data)

Example:

data_mean = np.mean(sensor_data)
Maximum

Find the maximum value:

np.max(sensor_data)
Minimum

Find the minimum value:

np.min(sensor_data)
Standard Deviation

Calculate standard deviation:

np.std(sensor_data)

Example:

data_std = np.std(sensor_data)
## 11. Common Statistical Functions
Function	Purpose
np.mean()	Calculate the average
np.max()	Find the maximum
np.min()	Find the minimum
np.std()	Calculate standard deviation
np.sum()	Calculate the sum
np.median()	Calculate the median

Example:

data = np.array([10, 20, 30, 40, 50])


print(np.mean(data))
print(np.max(data))
print(np.min(data))
print(np.std(data))
print(np.sum(data))
print(np.median(data))
## 12. Comparison Operations

NumPy allows us to compare array elements with a value.

Example:

sensor_data = np.array([12.3, 11.8, 13.1, 12.7, 11.9])

We can check which values are greater than 12:

sensor_data > 12

The result is a Boolean array:

[ True False  True  True False]

Each element is checked separately.

## 13. Boolean Indexing

We can use a Boolean condition to select elements.

Example:

sensor_data[sensor_data > 12]

This returns only values greater than 12.

Output:

[12.3 13.1 12.7]

This is called Boolean indexing.

## 14. np.where()

np.where() can be used to find the indexes where a condition is true.

Example:

sensor_data = np.array([12.3, 11.8, 13.1, 12.7, 11.9])


indices = np.where(sensor_data > 12)

The result is a tuple containing an array of indexes.

For a one-dimensional array:

indices = np.where(sensor_data > 12)[0]

The [0] extracts the first element of the tuple.

Example:

print(indices)

Output:

[0 2 3]

This means the values at indexes 0, 2, and 3 are greater than 12.

## 15. Finding Values Above the Average

We can combine NumPy functions.

Example:

data_mean = np.mean(sensor_data)


indices = np.where(sensor_data > data_mean)[0]

Now indices contains the indexes of sensors whose values are above the average.

We can access the corresponding values:

sensor_data[indices]
## 16. Looping Through NumPy Arrays

We can use a for loop to access array elements.

Example:

for value in sensor_data:
    print(value)

We can also use indexes:

for i in range(len(sensor_data)):
    print(i, sensor_data[i])
## 17. Creating Arrays with Special Values

NumPy provides functions for creating arrays with predefined values.

Zeros
np.zeros(5)

Output:

[0. 0. 0. 0. 0.]
Ones
np.ones(5)

Output:

[1. 1. 1. 1. 1.]
Range
np.arange(1, 6)

Output:

[1 2 3 4 5]
## 18. Reshaping Arrays

reshape() changes the shape of an array without changing its data.

Example:

arr = np.array([1, 2, 3, 4, 5, 6])


new_arr = arr.reshape(2, 3)

The result is:

[[1 2 3]
 [4 5 6]]

The total number of elements must remain the same.

For example:

6 elements → 2 × 3
## 19. Two-Dimensional Arrays

A NumPy array can have multiple dimensions.

Example:

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

This is a 2-dimensional array.

Its shape is:

arr.shape

Output:

(2, 3)

This means:

2 rows
3 columns

Number of dimensions:

arr.ndim

Output:

2
## 20. Indexing Two-Dimensional Arrays

For a two-dimensional array:

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

We can access an element using:

arr[row, column]

Example:

arr[0, 1]

Output:

2

The first index represents the row and the second represents the column.

## 21. Copying Arrays

When working with NumPy arrays, it is important to understand the difference between copying and referencing.

A copy can be created using:

new_arr = arr.copy()

This creates a separate array.

Changing new_arr will not change arr.

## 22. Important NumPy Attributes
Attribute	Purpose
arr.shape	Returns the shape of the array
arr.ndim	Returns the number of dimensions
arr.size	Returns the number of elements
arr.dtype	Returns the data type
23. Important NumPy Functions
Function	Purpose
np.array()	Create an array
np.mean()	Calculate the mean
np.max()	Find the maximum
np.min()	Find the minimum
np.std()	Calculate standard deviation
np.sum()	Calculate the sum
np.median()	Calculate the median
np.where()	Find indexes based on a condition
np.zeros()	Create an array of zeros
np.ones()	Create an array of ones
np.arange()	Create a sequence of values
Key Lessons

The main concepts I learned this week are:

NumPy is used for numerical computing.
NumPy arrays are useful for working with numerical data.
Arrays use zero-based indexing.
Slicing can be used to select part of an array.
NumPy supports element-wise mathematical operations.
NumPy provides useful statistical functions.
Boolean indexing can be used to filter array values.
np.where() can be used to find indexes based on a condition.
NumPy arrays can have multiple dimensions.
Array attributes such as shape, ndim, size, and dtype provide useful information about arrays.
Project Application

I applied these concepts in my Bridge Sensor Analysis project.

The project uses NumPy to:

Store sensor data in a NumPy array.
Calculate the mean sensor value.
Find the maximum sensor value.
Find the minimum sensor value.
Calculate the standard deviation.
Find sensors with values above the average.
Display sensor values when requested.

Example:

import numpy as np


sensor_data = np.array([
    12.3, 11.8, 13.1, 12.7, 11.9,
    12.5, 13.0, 12.4, 11.7, 12.8
])


data_mean = np.mean(sensor_data)
data_max = np.max(sensor_data)
data_min = np.min(sensor_data)
data_std = np.std(sensor_data)


indices = np.where(sensor_data > data_mean)[0]


print("Mean:", data_mean)
print("Maximum:", data_max)
print("Minimum:", data_min)
print("Standard deviation:", data_std)
print("Indexes above average:", indices)
print("Values above average:", sensor_data[indices])
Important Reminder

NumPy is an important foundation for Data Science.

The concepts I learned in NumPy will be useful when working with:

Pandas
Data Visualization
Machine Learning
Scientific Computing