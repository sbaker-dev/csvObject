from distutils.util import strtobool
import csv
import re


class CsvObject:
    """
    Simple Objected based approach to using data from a csv
    """

    def __init__(self, csv_path, column_types=None, set_columns=False, file_headers=True, encoding="utf-8-sig",
                 missing_to_zero=False, print_warnings=True):
        """
        This class reads in the data from the path provided with the specified encoding standard. It then sets the
        headers from the first row if headers exist, else it generates incremental column names as header names. It also
        loads the data and formats it into a column data structure and a row data structure. If a type or type list is
        provided, then the data can be typed as well; with the option of setting missing numeric data to zero
        missing_to_zero.

        :param csv_path: path to the load file
        :type csv_path: str

        :key column_types: A type, list of types to type the row's data, or None if a string representation of the data
            is sufficient
        :type column_types: type | list[type] | None

        :key file_headers: Equals True if the first row should be interpreted as a file header, False if not.
        :type file_headers: bool

        :key encoding: The encoding style of the file
        :type encoding: str

        :key missing_to_zero: Equals True if you want missing data in numeric columns of type int or float to be set to
            zero, False if not.
        :type missing_to_zero: bool

        :key print_warnings: Equals True if you want to log and print the column-row-value-type entries that were not
            successfully typed vus defaulting to string, False otherwise.
        :type print_warnings: bool
        """

        self.headers, self._raw_data = self._extract_data(csv_path, file_headers, encoding)
        self.file_name = self._extract_filename(csv_path)
        self.column_length = len(self._raw_data[0])
        self.column_types = self._determine_column_types(column_types)

        self.missing_to_zero = missing_to_zero
        self.print_warnings = print_warnings
        self.invalid_typed = []

        self.row_data, self.column_data = self._set_data(set_columns)

        if len(self.invalid_typed) > 0 and self.print_warnings:
            print(f"Warning: The following column-row-value-type where not correct so loaded as strings:\n"
                  f"{sorted(self.invalid_typed)}")

    @staticmethod
    def _extract_data(csv_path, file_headers, encoding):
        """
        Returns a tuple of the the raw untyped row data minus the header, as well as the headers.

        :param csv_path: path to the load file
        :type csv_path: str

        :param file_headers: If the first row should be interpreted as a file header or not
        :type file_headers: bool

        :param encoding: The encoding style of the file
        :type encoding: str

        :return: A tuple of raw untyped row data minus the header, as well as the headers
        """
        with open(csv_path, "rt", encoding=encoding) as csv_file:
            raw_data = [row for row in csv.reader(csv_file)]

        # If we have read in a .txt or prn file then we
        if ".txt" in csv_path:
            raw_data = [row[0].split() for row in raw_data if len(row) == 1]
        elif ".tsv" in csv_path:
            raw_data = [re.split(r"\t+", row[0]) for row in raw_data]

        if file_headers:
            headers = [header if header != "" else f"Untitled_{index + 1}" for index, header in enumerate(raw_data[0])]
            return headers, raw_data[1:]
        else:
            return [f"Untitled_{i + 1}" for i in range(len(raw_data[0]))], raw_data

    def _determine_column_types(self, column_types):
        """
        Returns a list, where each element in the list represents the type of data in the column data

        :param column_types: A python type or list a list of types
        :type column_types: type | list[type]

        :return: A list types, where said types equal to the length of columns
        :rtype: list[type]
        """
        if isinstance(column_types, list):
            # List based typing
            if len(column_types) != len(self.headers):
                raise ValueError(f"You must provide as many column types as columns of data\nFound {len(column_types)}"
                                 f" but expected {len(self.headers)}")
            else:
                return [col_type if col_type != bool else self._string_to_bool(col_type) for col_type in column_types]

        elif isinstance(column_types, type):
            # Uniform Typing of type column_types
            if column_types == bool:
                return [self._string_to_bool for _ in range(self.column_length)]
            else:
                return [column_types for _ in range(self.column_length)]

        elif not column_types:
            # None Typed operation
            return column_types

        else:
            raise TypeError(f"Column_types takes a list[types], type or None. Yet {type(column_types)} was found")

    def _format_column(self, row_data):
        """
        Reformat a list of rows to a list of columns

        Example
        --------
        row_data = [[1, 2, 3, 4], [5, 6, 7, 8]]
        column_data = [[1, 5], [2, 6], [3, 7], [4, 8]]

        :param row_data: A list of lists, where each list within the list is a list of entry's
        :type row_data: list[list]

        :return: A list of lists, where each list within the list is a list of entries found in a given column.
        :rtype: list[list]
        """
        return [[row[i] for row in row_data] for i in range(self.column_length)]

    def _type_data(self, row, index):
        """
        Set entry's to their provide type

        Further information
        ---------------------
        Where it is possible the system will type the data to the given type. A common point of failure is numeric data
        with missing values. If self.missing_to_zero is set to true, then in the case of this ValueError a zero will be
        added to the row data rather than an empty string.

        The principle here is to avoid crashing, so if a invalid type is found it simply adds the entry as a string and
        raises a warning at the end that some data wasn't typed correctly.

        :param row: A list of entries
        :type row: list

        :return: A typed list of entries
        :rtype: list
        """
        typed_row = []
        for i, (entry, entry_type) in enumerate(zip(row, self.column_types)):
            try:
                typed_row.append(entry_type(entry))
            except ValueError:
                if (entry_type == int or entry_type == float) and self.missing_to_zero:
                    typed_row.append(entry_type(0))
                else:
                    if [i + 1, index + 2, entry, entry_type] not in self.invalid_typed and self.print_warnings:
                        self.invalid_typed.append([i + 1, index + 2, entry, entry_type])
                    typed_row.append(entry)
        return typed_row

    def _check_row_length(self):
        """
        csv does not read in empty rows at the end of csv, so if we have 40 headers but only 26 columns for a given row
        then we will end up not being able to index call. This sets all rows with length less than the column length to
        be equal to it via blanks.

        :return: A list of rows, where each row is equal to the length of the number of columns
        :rtype: list[list]
        """

        row_data = []
        for row in self._raw_data:
            if len(row) < self.column_length:
                row_data.append(row + ["" for _ in range(self.column_length - len(row))])
            else:
                row_data.append(row)

        return row_data

    def _set_data(self, set_columns):
        """
        Set the row and column data of the csv, with the entries typed if types where provided

        :return: Two lists, where the first list is a list of entries in row format and the second a list a list of
            entries in column formant
        :rtype: tuple[list, list]
        """
        if self.column_types:
            row_data = [self._type_data(row, index) for index, row in enumerate(self._check_row_length())]
        else:
            row_data = self._check_row_length()

        if set_columns:
            return row_data, self._format_column(row_data)
        else:
            return row_data, None

    @staticmethod
    def _string_to_bool(string_representation_of_bool):
        """
        Convert a string of False or True to a bool representation
        """
        return bool(strtobool(string_representation_of_bool))

    @staticmethod
    def _extract_filename(csv_path):
        """
        This just uses slicing to extract the file name, maybe useful for users writing new data

        :return: File name
        :rtype: str
        """
        name = csv_path.replace("\\", "/")
        return name.split("/")[len(name.split("/")) - 1].split(".")[0]
