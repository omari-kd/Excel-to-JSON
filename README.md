# Excel to JSON Converter
A simple, efficient tool to convert Excel files (.xlsx, .xls) to JSON format.

Features

- Convert Excel spreadsheets to JSON with a single function call
- Support for multiple worksheets
- Customizable JSON output format
- Simple API for easy integration into existing projects
- Handles large files efficiently

# Installation

Clone the repository

git clone https://github.com/omari-kd/Excel-to-JSON.git

cd excel-to-json

# Install dependencies

pip install -r requirements.txt

# Dependencies

- pandas
- openpyxl


# Usage
## Basic Conversion

from excel_converter import excel_to_json

Convert Excel file to JSON
json_data = excel_to_json('path/to/your/file.xlsx')

Save to file
excel_to_json('path/to/your/file.xlsx', output_json_path='output.json')
