from csvObject.csvObject import CsvObject

# Print the filename
print(f"File name is: {CsvObject('Example Data.csv').file_name}\n")

# Simple case, with no data typing
print("# Simple Case #")
csv_object = CsvObject("Example Data.csv")
print(csv_object.row_data)
print("")

# Dealing with files without headers
print("# File Headers #")
csv_object = CsvObject("Example Data.csv")
print(csv_object.headers)
print(csv_object.row_data)
print("")

csv_object = CsvObject("Example Data.csv", file_headers=False)
print(csv_object.headers)
print(csv_object.row_data)
print("")

# Uniform type
print("# Uniform Typing #")
csv_object = CsvObject("Example Data.csv", column_types=int)
print("")
print(csv_object.row_data)
print(csv_object.invalid_typed)
print("")

# List element typing
print("# List element Typing #")
csv_object = CsvObject("Example Data.csv", column_types=[str, float, str, int, bool])
print(csv_object.row_data)

csv_object = CsvObject("Example Data.csv", column_types=[str, float, str, float, bool], missing_to_zero=True)
print(csv_object.row_data)

csv_object = CsvObject("Example Data.csv", column_types=[str, float, str, int, bool], print_warnings=False)
print(csv_object.row_data)
print("")
