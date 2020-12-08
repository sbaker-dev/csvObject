![logo](logoDocs.png)

# csvObject

Simple Objected based approach to using data from a csv
All the source code can be found at the [csvObject git repository](https://github.com/sbaker-dev/csvObject)

<!--Table OF CONTENTS -->

## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
* [Examples](#examples)
  * [Simple Case](#simple-case)
  * [Dealing with Headers](#non-header-files)
  * [Uniformed typing](#uniformed-element-typing)
  * [List column typing](#list-element-typing)
  * [Handing type errors](#handling-type-errors)
* [If unclear](#) 
 

<!--ABOUT THE PROJECT -->

## About The Project

csvObject is just a simple object base approach to loading in a csv file and using the data. In more complex cases when
doing actual data analysis or changing the structure of the file, using [pandas](https://github.com/pandas-dev/pandas)
makes much more sense. But if all you want is to have a light weight way of extracting the data from the csv file parsed
into an object with a few basic options without Numpy then this may be of interest.

<!-- GETTING STARTED --> 
   
## Getting Started 

csvObject is available as a package via Pypi so you can pip install by the following command

```
python -m pip install csvObject
```

<!-- EXAMPLES -->

## Examples

All the code and some simple example data can be found in the [Examples Folder](
https://github.com/sbaker-dev/csvObject/tree/master/Examples) on the github repository. In this case lets say you have a
list of information on Cat's, shown in the table below.

| Cat's Name | Age   | Breed            | Owner Number  | Subscriber    |
|:-----------|:----- |:-----------------|---------------|---------------|
| Mitten     | 17.5  | Tabby            | 5550112       | FALSE         |
| Squitten   | 10.2  | Tortoiseshell    | 5550432       | TRUE          |

#### Simple case

The simplest use case is when the only argument to passed to the object is the path to the file. In this case the only
thing this package is doing is creating an object that holds the filename, the headers, and the data in a row and column
format from the csv module within python.

```python
from csvObject.csvObject import CsvObject

# Simple case, with no data typing
print("Simple Case")
csv_object = CsvObject("Example Data.csv")
print(csv_object.row_data)
```

In this case we will get the row data as strings, as no type information was provided and csv module by default sets all
information from all the rows to be a str. If all you want is to have a 'one liner' of sorts that creates an object that
holds row and column data, then this might be all you need. 

```
[['Mitten', '17.5', 'Taby', '5550112', 'FALSE'], ['Squitten', '10.2', 'Tortoiseshell', '', 'TRUE']]
```

#### Non Header files

By default csv object expects you to have a header, but you don't have to have one! If you don't have a header, then 
csvObject will evaluate the first row to contain data rather than header information.

```python
from csvObject.csvObject import CsvObject

# Dealing with files without headers
print("File Headers")
csv_object = CsvObject("Example Data.csv")
print(csv_object.headers)
print(csv_object.row_data)

print("")

csv_object = CsvObject("Example Data.csv", file_headers=False)
print(csv_object.headers)
print(csv_object.row_data)
```
When you don't have a header, headers will be generated for you of type Untitled(N), where n is the column index + 1 
for this column. In this example the 5th column's subscriber to service header was missing, so it is also set to be a
Untitled_5. In this case since we did have a header so if we call the class objected to load the data without headers we
end up with an extra row of data.

```
['Cat Name', 'Age', 'Breed', 'Owner Number', 'Untitled_5']
[['Mitten', '17.5', 'Taby', '5550112', 'FALSE'], ['Squitten', '10.2', 'Tortoiseshell', '', 'TRUE']]

['Untitled_1', 'Untitled_2', 'Untitled_3', 'Untitled_4', 'Untitled_5']
[['Cat Name', 'Age', 'Breed', 'Owner Number', ''], ['Mitten', '17.5', 'Taby', '5550112', 'FALSE'], ['Squitten', '10.2', 'Tortoiseshell', '', 'TRUE']]
```

#### Uniformed Element Typing

If your data contains a uniform type, then its possible to set this during the construction and it will convert all
valid elements into this type

```python
from csvObject.csvObject import CsvObject
print("# Uniform Typing #")
csv_object = CsvObject("Example Data.csv", column_types=int)
print("")
print(csv_object.row_data)
print(csv_object.invalid_typed)
```

If your data is generally uniform in terms of type, then there is no problem. If there is a none uniform type, then all
the errors will be print along side a warning in the format of a column - row - value - type list. The principle here
is if the types you have specified are the expected types, then your data may contain unexpected characters you might 
want to fix. 

You can use the Column and row indexing to change these errors within python if you so wish. They are held in a list 
within .invalid_typed. Alternatively it may be faster/better to just correct the original file and then reload it in 
depending on your situation.

```
Warning: The following column-row-value-type where not correct so loaded as strings:
[[1, 2, 'Mitten', <class 'int'>] ... [5, 3, 'TRUE', <class 'int'>]]

[['Mitten', '17.5', 'Taby', 5550112, 'FALSE'], ['Squitten', '10.2', 'Tortoiseshell', '', 'TRUE']]
```

#### List element typing

It is also possible to do element typing on a per column level by setting a type list equal to the length of the number
of columns. Be warned, if you get the length incorrect it will throw a ValueError at you.

```python
from csvObject.csvObject import CsvObject

print("# List element Typing #")
csv_object = CsvObject("Example Data.csv", column_types=[str, float, str, int, bool])
print(csv_object.row_data)
print("")

```
As with before when a uniform type is applied, anything that is not correct in terms of type will be assigned as a 
string type of that element as it is assumed that this error in type miss-match is an error in the data.

```
# List element Typing #
Warning: The following column-row-value-type where not correct so loaded as strings:
[[4, 3, '', <class 'int'>]]
[['Mitten', 17.5, 'Taby', 5550112, False], ['Squitten', 10.2, 'Tortoiseshell', '', True]]
```

#### Handling type errors

Whilst errors may exist in the data, it may also be the case that the data just has missing, None or other delimiters 
to express no data present. For example in numeric cases, if a cell is empty, then the csv module will load that cell 
as and empty string. This will not convert into a int/float and will through a warning. There are Two options here, you
can set missing numeric values to zero, or disable the warnings

```python
from csvObject.csvObject import CsvObject
csv_object = CsvObject("Example Data.csv", column_types=[str, float, str, float, bool], missing_to_zero=True)
print(csv_object.row_data)

csv_object = CsvObject("Example Data.csv", column_types=[str, float, str, int, bool], print_warnings=False)
print(csv_object.row_data)
```

In the first case, if the type was supposed to be an int/float and a value error is raise it will be set to zero. Keep
in mind this is uniform, so **ANY** type-errors in these columns will be set to zero. So make sure this is the desired
functionality before setting it. An alternative is to silence the errors and accept the strings. You may want the values
to stay as strings. For example if missing data is generally an empty cell then if element: will evaluate to False and
that might be the desired functionality. If Print warning's is set to False, the system will not store errors, so even
if they occur if you print csv_object.invalid you will get an empty list.

```
[['Mitten', 17.5, 'Taby', 5550112.0, False], ['Squitten', 10.2, 'Tortoiseshell', 0.0, True]]
[['Mitten', 17.5, 'Taby', 5550112, False], ['Squitten', 10.2, 'Tortoiseshell', '', True]]
```

### Column data

You may also load data in with column data as well as row data by setting set_columns to be True. This is not on by 
default **and may be slow for very large data sets**. If you ever just print the object, then it will tell you the file
name of the file that was loaded, as well as the column dimensions (if set), and row dimensions. 

If column data has been set, you can also use indexing of the loaded object to return that column of data. The getitem 
will allow you to pass either the index of the column, or the name of the header of that column. If you ever need the 
index of a given header, you can also call if from index_from_headers

```python
from csvObject.csvObject import CsvObject
csv_object = CsvObject("Example Data.csv", set_columns=True)
print(csv_object.column_data)
print(csv_object)

header_indexing = csv_object['Owner Number']
print(header_indexing)

cat_name_index = csv_object.index_from_headers("Cat Name")
int_indexing = csv_object[cat_name_index]
print(int_indexing)
```


<!-- IF UNCLEAR -->
## If unclear

Hopefully this has provided enough information to give you an idea of the options you have when using this object but 
if not, the source code is available for you to tinker with and your always welcome to submit a pull request for an 
example that you don't think was appropriately covered. 


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[logo]: ../images/logo.png