import pandas as pd

# Reading the input data from an Excel file which is called as input2.xlsx, which acts as the primary of this code.
input_file = "input2.xlsx"
df = pd.read_excel(input_file)

# Converting the DataFrame (df) to a string
data = df.to_string(index=False)

# Removing unnecessary characters and spliting into separate cells
data = data.replace('},', '|').replace('{', '').replace('}', '').replace('"', '')
cells = data.split('|')

# Creating a list of dictionaries for each cell
cell_dicts = []
for cell in cells:
    cell_dict = {}
    pairs = cell.split(',')
    for pair in pairs:
        pair = pair.strip()
        if ':' in pair:
            # Split at the first occurrence of colon
            key, value = pair.split(':', 1)  
            key = key.strip()
            value = value.strip()
            cell_dict[key] = value
    cell_dicts.append(cell_dict)

# Creating a DataFrame from the list of dictionaries
df = pd.DataFrame(cell_dicts)

# Rearranging columns alphabetically
df = df.reindex(sorted(df.columns), axis=1)

# Fill missing values with NaN. This gets neglected as there is no NONE data in the entire sheet of JSON values
df = df.fillna('')

output_file = "output.xlsx"
df.to_excel(output_file, index=False)

#This acts as the statement stating the program has run successfully.
print("Output file created successfully.")
