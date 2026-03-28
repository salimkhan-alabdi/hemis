

import pandas as pd
import json

df = pd.read_excel("MBII_Ruscha_2025-26.xlsx")
print(df.head(10).to_json(orient="records", force_ascii=False))
