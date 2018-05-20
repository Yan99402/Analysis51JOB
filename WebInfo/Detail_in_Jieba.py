import jieba
import openpyxl as ox
import pandas as pd

workbook = ox.load_workbook('F:/python数据/51Job/51JobPositionDetail.xlsx')
sheet = workbook['51JobPositionDetail']
df_detail = pd.DataFrame(sheet.values)
df_detail.columns = list(df_detail.iloc[0])
df_detail = df_detail.drop(0)
df_detail = df_detail.reset_index(drop=True)

position_keyword_list = df_detail['detail'].values
detail_text = open("detail_txt.txt", "a")
i=0
for position_keyword in position_keyword_list:
    try:
        cell_jieba_list = jieba.lcut(position_keyword,cut_all = True)
        for cell_jieba in cell_jieba_list:
            detail_text.write(cell_jieba+',')
        i += 1
    except Exception:
        print(i)
        print(Exception)
detail_text.close()