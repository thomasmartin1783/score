from collections import OrderedDict
import xlrd
import json
from rouge import Rouge
from rouge import FilesRouge
import pandas as pd


# model = "Generated-Bangla-1-Shot"
# model = "Generated-Bangla-10-Shot"
# model = "Generated-Bangla-25-Shot"
# model = "bnbphoneticparser"
# model = "Google Translate"
# model = "Indic Transliteration"
# model = "BN Transliterate"
# model = "G Input Tools"
model = "auvipy/PyAvroPhonetic"

xls = pd.ExcelFile(r"final_revision2.xlsx")
sheetX = xls.parse(0)
var1 = sheetX['Bangla'].astype('string')
var2 = sheetX[model].astype('string')

output = []


for i in range(len(var1)):
    ref = f"{var1[i]}"
    hyp = f"{var2[i]}"
    data = {"hyp": hyp, "ref": ref}
    output.append(data)

with open('temp_data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
