# Convert_JSONdataofexcell_to_XLSX

**Steps**:
1. Copy the column that you wanna convert to a new sheet.
2. Select all the cells in this column and go to data tab on top and 
    -> select text to columns, 
    -> select delimited, 
    -> click next,
    -> select other and add “{“ , 
    -> click next, 
    -> select general and in destination add “=$B$3”
3. The step 2 segregates the data and delimits the data by " { "
4. Copy the delimited data to a new sheet and name it as Input2. This acts as the primary input to the python code of this repo.
5. Run the python code. Pre reqs being pandas.
6. The output will be in a file named output.xlsx
