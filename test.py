
from csv import DictReader
for row in DictReader(open("C:/Users/wenjli/AppData/Local/Programs/Python/"
                 "Python37-32/myScripts/Ex_Files_Learning_Django/GitFile/app_satisfaction/Apps2Beta1.csv")):
    print(1)


# import pandas as pd
# df = pd.read_csv("C:/Users/wenjli/AppData/Local/Programs/Python/"
#                  "Python37-32/myScripts/Ex_Files_Learning_Django/GitFile/app_satisfaction/Apps2Beta1.csv")
# # df = pd.read_csv("C:\\Users\\wenjli\\Desktop\\Beta_Feedback\\Apps2Beta1.csv")
#
# # table = df[['Hub Satisfaction', 'Calendar Satisfaction']]
# table = df.fillna(-1)
# # table = table['Hub Satisfaction']
# # table = table.sort_values()
#
# # apps = ['Hub', 'Calendar']
# # for app in apps:
# for i in range(0, table['Hub' + ' Satisfaction'].size):
#     print(table.loc[i, 'Hub' + ' Satisfaction'])
# # table = table['Hub Satisfaction']
