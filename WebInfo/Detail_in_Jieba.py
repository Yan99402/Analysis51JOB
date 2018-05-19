import jieba
import openpyxl as ox
import pandas as pd

workbook = ox.load_workbook('F:/python数据/51Job/51JobPositionDetail.xlsx')
sheet = workbook['51JobPositionDetail']
df_detail = pd.DataFrame(sheet.values)
df_detail.columns = list(df_detail.iloc[0])
df_detail = df_detail.drop(0)
df_detail = df_detail.reset_index(drop=True)

position_keyword_list = df_detail[]
cell_jieba_list = jieba.lcut(cell_value,cut_all = True)
print(cell_jieba_list)