import re

def extract_numeric_value(input_string):
    # Define a regular expression pattern to match numeric characters
    pattern = r'(\d+(\.\d+)?)'  # Matches one or more digits optionally followed by a dot and more digits

    # Use re.findall to extract all numeric values from the input string
    numeric_values = re.findall(pattern, input_string)

    # Convert the extracted numeric values from strings to floats
    numeric_values = [float(value[0]) for value in numeric_values]

    return numeric_values