from csvObject.csvObject import CsvObject

if __name__ == '__main__':
    # Simple case, with no data typing
    csv_object = CsvObject("Example Data.csv")
    print(csv_object.row_data)
