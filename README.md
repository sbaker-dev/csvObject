![logo]

# csvObject
Simple Objected based approach to using data from a csv
All the source code can be found at the [csvObject git repository](https://github.com/sbaker-dev/csvObject)


<!--Table OF CONTENTS -->
## Table of Contents
* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Contributions](#contributions)
* [License](#license)

<!--ABOUT THE PROJECT -->
## About The Project
csvObject is just a simple object base approach to loading in a csv file and using the data. In more complex cases when
doing actual data analysis or changing the structure of the file, using [pandas](https://github.com/pandas-dev/pandas)
makes much more sense. But if all you want is to have a light weight way of extracting the data from the csv file parsed
into an object with a few basic options without Numpy then this may be of interest.

<!-- GETTING STARTED -->    
## Getting Started 
csvObject is available as a package via Pypi so you can pip install by the following command

```shell script
python -m pip install csvObject
```


<!-- USAGE -->
## Usage
The simplest use case is when the only argument to passed to the object is the path to the file. In this case the only
thing this package is doing is creating an object that holds the filename, the headers, and the data in a row and column
format from the csv module within python. CsvObject does have other options, detailed on the [docs page](
https://sbaker-dev.github.io/csvObject/) although you may find it more useful to look at it in a interactive session 
via the jupyter file within the Examples folder.


```python
from csvObject.csvObject import CsvObject

csv_object = CsvObject("Example Data.csv")
print(csv_object.row_data)
```

<!-- CONTRIBUTIONS -->
## Contributions
Contributions are always welcome, if you want to make a contribution simply make a pull request based on your fork of
the project

<!-- License -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

 
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[logo]: images/logo_50.png