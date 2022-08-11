from collections import OrderedDict
import xlrd
import json
from rouge import Rouge
from rouge import FilesRouge
import pandas as pd


xls = pd.ExcelFile(r"final_revision.xlsx")
sheetX = xls.parse(0)
var1 = sheetX['Bangla'].astype('string')
var2 = sheetX['auvipy/PyAvroPhonetic'].astype('string')

output = []


for i in range(len(var1)):
    ref = f"{var1[i]}"
    hyp = f"{var2[i]}"
    data = {"hyp": hyp, "ref": ref}
    output.append(data)

with open('data_py_avro_phonetic.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
