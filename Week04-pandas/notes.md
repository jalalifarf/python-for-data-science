# Pandas Notes


## 1. Introduction to Pandas


Pandas is a Python library used for data analysis and data manipulation.


It is especially useful for working with tabular data such as CSV files, Excel files, and databases.


To use Pandas:


```python
import pandas as pd

The pd is a common alias for Pandas.

2. Reading a CSV File

We can use read_csv() to read a CSV file and create a DataFrame.

df = pd.read_csv('bridges.csv')

If the file is located in another folder, we can use a relative path:

df = pd.read_csv('Week02-Functions/bridge_information_system/bridges.csv')
3. DataFrame

A DataFrame is a two-dimensional data structure consisting of rows and columns.

It is similar to a table.

For example:

Bridge Name	Material	Bridge Length
Bridge A	Concrete	120
Bridge B	Steel	200

The variable df usually represents a DataFrame.

4. DataFrame Shape

The shape attribute returns the number of rows and columns.

df.shape

Example output:

(10, 6)

This means:

10 rows
6 columns

We can access the number of rows and columns separately:

df.shape[0]   # number of rows
df.shape[1]   # number of columns
5. DataFrame Columns

The columns attribute returns the names of the columns.

df.columns

We can convert the column names to a list:

list(df.columns)
6. DataFrame Information

The info() method displays general information about the DataFrame.

df.info()

It provides information such as:

Number of rows
Column names
Number of non-null values
Data types
Memory usage

Important:

df.info()

is a method, so we need parentheses.

7. Statistical Information

The describe() method provides statistical information about numerical columns.

df.describe()

It can provide:

count
mean
standard deviation
minimum
25% percentile
50% percentile
75% percentile
maximum

For example:

df.describe()
8. Selecting One Column

We can select one column using its name:

df['Material']

For example:

df['Bridge Length']

This returns a Pandas Series.

9. Selecting Multiple Columns

We can select multiple columns by passing a list of column names:

df[['Bridge Name', 'Material']]

For example:

df[['Bridge Name', 'Bridge Length', 'Material']]
10. Filtering Data

We can filter rows based on a condition.

For example, to find concrete bridges:

df[df['Material'] == 'Concrete']

To find steel bridges:

df[df['Material'] == 'Steel']

To find bridges constructed after 2000:

df[df['Construction Year'] > 2000]

The expression inside the brackets creates a Boolean condition.

11. Multiple Filtering Conditions

We can combine conditions using:

& for AND
| for OR
~ for NOT

Example:

df[
    (df['Material'] == 'Concrete') &
    (df['Construction Year'] > 2000)
]

This finds concrete bridges constructed after 2000.

Important:

Each condition should be placed inside parentheses.

12. Checking if a DataFrame is Empty

The .empty attribute tells us whether a DataFrame contains any rows.

df.empty

It returns:

True

if the DataFrame is empty.

It returns:

False

if the DataFrame contains data.

Example:

df_concrete = df[df['Material'] == 'Concrete']


if df_concrete.empty:
    print('There is no Concrete bridge')
else:
    print(df_concrete)
13. Working with Text

Pandas provides string methods through .str.

For example:

df['Bridge Name'].str.lower()

converts the text to lowercase.

We can remove extra spaces using:

df['Bridge Name'].str.strip()

We can combine them:

df['Bridge Name'].str.strip().str.lower()

This is useful when comparing user input with data in a DataFrame.

Example:

name = input('Please enter the bridge name: ').strip().lower()


result = df[
    df['Bridge Name'].str.strip().str.lower() == name
]
14. Searching for Data

We can use filtering to search for a specific bridge.

Example:

name = input('Please enter the bridge name: ').strip().lower()


result = df[
    df['Bridge Name'].str.strip().str.lower() == name
]


if result.empty:
    print('The bridge was not found')
else:
    print(result)

The .empty check is useful because it tells us whether the search returned any results.

15. Sorting Data

We can sort a DataFrame using sort_values().

Ascending order:

df.sort_values('Bridge Length')

Descending order:

df.sort_values('Bridge Length', ascending=False)

We can also sort by another column:

df.sort_values('Construction Year')

Important:

sort_values() returns a new DataFrame.

For example:

sorted_df = df.sort_values('Bridge Length')
print(sorted_df)

The original df is not changed.

16. Grouping Data

The groupby() method is used to group data based on a column.

For example:

df.groupby('Material')

We can calculate the average bridge length for each material:

df.groupby('Material')['Bridge Length'].mean()

This gives the average bridge length for each material.

For example:

Material
Concrete    150.5
Steel       220.3
17. Common Statistical Functions

Pandas provides several useful statistical functions.

Mean:

df['Bridge Length'].mean()

Maximum:

df['Bridge Length'].max()

Minimum:

df['Bridge Length'].min()

Standard deviation:

df['Bridge Length'].std()

Sum:

df['Bridge Length'].sum()

Count:

df['Bridge Length'].count()
18. Using .loc

.loc can be used to select rows and columns by labels.

For example:

df1 = df.describe()


df1.loc[['mean', 'min', 'max'], ['Bridge Length']]

This selects:

mean
minimum
maximum

for the Bridge Length column.

19. Important Difference: Attribute vs Method

Some Pandas features are attributes and do not require parentheses.

Examples:

df.shape
df.columns
df.empty

Some are methods and require parentheses.

Examples:

df.info()
df.describe()
df.sort_values()
df.groupby()

Remember:

Attribute → no ()
Method → ()
20. Important Pandas Methods and Attributes
Method / Attribute	Purpose
pd.read_csv()	Read a CSV file
df.shape	Get number of rows and columns
df.columns	Get column names
df.info()	Display DataFrame information
df.describe()	Display statistical information
df.empty	Check whether DataFrame is empty
df.sort_values()	Sort data
df.groupby()	Group data
.str.lower()	Convert text to lowercase
.str.strip()	Remove extra spaces
.mean()	Calculate average
.max()	Find maximum
.min()	Find minimum
.std()	Calculate standard deviation
.count()	Count values
.sum()	Calculate total
Key Lessons

Pandas provides powerful tools for working with tabular data.

The main things I learned this week are:

How to read CSV files using Pandas.
How to work with DataFrames.
How to inspect a DataFrame.
How to select columns.
How to filter rows.
How to search for specific data.
How to sort data.
How to group data.
How to perform basic statistical operations.
How to work with text data using .str.
Project Application

I applied these concepts in my Bridge Dataset Analysis project.

The project uses Pandas to:

Read bridge data from a CSV file.
Display general information about the dataset.
Calculate bridge statistics.
Filter bridges based on different conditions.
Search for a bridge by name.
Sort bridges by different properties.
Group bridges by material.
Calculate the average bridge length for each material.
