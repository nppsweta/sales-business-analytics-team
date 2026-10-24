Data Preparation and Quality Validation

Role

Responsible for preparing and validating the Superstore sales dataset for analysis and dashboard development.

Tasks

- Inspect dataset structure, rows, columns, and data types.
- Check missing values and duplicate records.
- Validate order dates and shipping dates.
- Clean and validate the dataset.
- Maintain the cleaned dataset and data dictionary.
- Document data-quality checks and results.

Initial Dataset Checks

- Original row count: 9,994
- Missing values: 0
- Invalid dates: 0
- Suspected duplicate rows: 2

Note: Investigate suspected duplicate records before deciding whether to remove them.

Deliverables

- Original dataset
- Cleaned dataset
- Data dictionary
- Data-quality validation report
Day 4: Data Types and Validation Checks

Objective: Document the data types and validation checks performed on the Superstore dataset.

Dataset: Superstore Sales Dataset

Total Records: 9,994 rows

Total Columns: 9

Data Types

Column| Data Type
Order Date| Datetime
Region| Text
State| Text
Category| Text
Sub-Category| Text
Segment| Text
Sales| Float
Profit| Float
Quantity| Integer

Validation Results

- Missing values: 0
- Invalid dates: 0
- Duplicate rows detected: 2
- Date conversion: Completed
- Dataset shape: 9,994 rows × 9 columns

Conclusion

The dataset was checked for missing values, duplicate rows, invalid dates, and appropriate data types. No missing values or invalid dates were found. Two duplicate rows were detected and documented for further review.

Status: Day 4 documentation completed.

## Day 5: Data Quality Validation

### Validation Summary

The Superstore dataset was checked to verify its data quality before further analysis.

- Total records: 9,994
- Total columns: 9
- Missing values: 0
- Invalid order dates: 0
- Duplicate rows detected: 2

### Validation Checks

1. Checked the dataset shape and column names.
2. Verified missing values in all columns.
3. Checked duplicate records.
4. Converted Order Date into a date format.
5. Verified the earliest and latest order dates.
6. Confirmed the cleaned dataset was saved as `Superstore_Cleaned.csv`.

### Date Range

- Earliest order date: 2014-01-03
- Latest order date: 2017-12-30

### Conclusion

The dataset contains 9,994 records and 9 columns. No missing values or invalid dates were detected. Two duplicate rows were identified and documented for further review.

The validation results were recorded as part of the Data Preparation role.
