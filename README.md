# Convert_JSONdataofexcell_to_XLSX

**Automation for performing the following action:**
Input: 
    Cell 1:
     [{"FactoryId":13, "FactoryName":"qwe", "Packaging":"No", "companyId":7, "companyname":"qweqe", "Weighing":"Yes", "mixture":"Yes", "filling":"Yes", "display":"Yes", "finalinspection":"Yes", "storage":"Yes", "others1":"No", "others2":"No"}, {"FactoryId":14, "FactoryName":"gjg", "Packaging":"Yes", "companyId":7, "companyname":"qwerqe", "Weighing":"Yes", "mixture":"Yes", "filling":"Yes", "display":"Yes", "finalinspection":"Yes", "storage":"Yes", "others1":"No", "others2":"No"}, {"FactoryId":11, "FactoryName":"qweqwe", "Packaging":"No", "companyId":7, "companyname":"weqwe　トキワ", "Weighing":"No", "mixture":"No", "filling":"No", "display":"Yes", "finalinspection":"Yes", "storage":"Yes", "others1":"No", "others2":"No"}, {"FactoryId":12, "FactoryName":"dtdrrr", "Packaging":"No", "companyId":7, "companyname":"fdgdf", "Weighing":"No", "mixture":"No", "filling":"No", "display":"Yes", "finalinspection":"Yes", "storage":"Yes", "others1":"No", "others2":"No"}]
    Cell 2:
[{"FactoryId":16, "FactoryName":"eare", "Packaging":"Yes", "companyId":8, "companyname":"werewr", "Weighing":"Yes", "mixture":"Yes", "filling":"Yes", "display":"Yes", "finalinspection":"Yes", "storage":"Yes", "others1":"No", "others2":"Yes"}, {"FactoryId":15, "FactoryName":"were", "Packaging":"Yes", "companyId":8, "companyname":"werew", "Weighing":"Yes", "mixture":"Yes", "filling":"Yes", "display":"Yes", "finalinspection":"Yes", "storage":"Yes", "others1":"No", "others2":"Yes"}, {"FactoryId":17, "FactoryName":"werew", "Packaging":"No", "companyId":8, "companyname":"werewr", "Weighing":"No", "mixture":"No", "filling":"No", "display":"Yes", "finalinspection":"Yes", "storage":"Yes", "others1":"No", "others2":"Yes"}, {"FactoryId":18, "FactoryName":"中央倉庫", "Packaging":"No", "companyId":8, "companyname":"werewr", "Weighing":"No", "mixture":"No", "filling":"No", "display":"Yes", "finalinspection":"Yes", "storage":"Yes", "others1":"No", "others2":"Yes"}, {"FactoryId":19, "FactoryName":"werew", "Packaging":"Yes", "companyId":8, "companyname":"werew", "Weighing":"Yes", "mixture":"Yes", "filling":"Yes", "display":"Yes", "finalinspection":"Yes", "storage":"Yes", "others1":"No", "others2":"Yes"}, {"FactoryId":20, "FactoryName":"werew", "Packaging":"No", "companyId":8, "companyname":"werewr", "Weighing":"No", "mixture":"No", "filling":"No", "display":"Yes", "finalinspection":"Yes", "storage":"Yes", "others1":"No", "others2":"Yes"}, {"FactoryId":21, "FactoryName":"werew", "Packaging":"Yes", "companyId":8, "companyname":"werewr", "Weighing":"No", "mixture":"No", "filling":"No", "display":"Yes", "finalinspection":"Yes", "storage":"Yes", "others1":"No", "others2":"Yes"}]

and N number of cells.


Output:
FactoryId	FactoryName	Packaging	Weighing	companyId	companyname	display	filling	finalinspection	mixture	others1	others2	storage
13	qwe	No	Yes	7	qwewe	Yes	Yes	Yes	Yes	No	No	Yes
14	gjg	Yes	Yes	7	qweqe	Yes	Yes	Yes	Yes	No	No	Yes
....... and so on for all the cells



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
