import pandas as pd
import json


# Load the Excel file
def excel_to_json(excel_file_path, output_json_path=None):
    # Read the Excel file
    df = pd.read_excel(excel_file_path)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    # Parse the JSON string to get a Python object
    parsed_json = json.loads(json_data)

    # Pretty print the JSON for readability
    formatted_json = json.dumps(parsed_json, indent=4)

    # Save to file if output path is provided
    if output_json_path:
        with open(output_json_path, 'w') as json_file:
            json_file.write(formatted_json)
        print(f"JSON saved to {output_json_path}")

    return formatted_json

# Example usage
# excel_to_json('your_file.xlsx', 'output.json')