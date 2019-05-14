import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\wenjli\\Desktop\\Beta_Feedback\\Apps2Beta1.csv")
app = 'notes'
satisfaction_var = app.upper().capitalize()+' Satisfaction'
comments_var = app.upper().capitalize()+' Comments'

'''Get Satisfaction col and comment col, sort and drop NAN '''
table = df[[satisfaction_var, comments_var]]
table = table.sort_values(by=[satisfaction_var], ascending=False)
table = table.dropna(subset=[satisfaction_var])

count_list = table[satisfaction_var].value_counts()
total_respond = df[satisfaction_var].count()

percentage_list = []
score_not_exit = []
for score in range(11):
    if score not in list(table[satisfaction_var]):
        score_not_exit.append(score)

for score in range(11):
    if score in score_not_exit:
        percentage_list.append("%.2f" % round(0, 2))
    else:
        percentage_list.append("%.2f" % round(count_list[score]/total_respond*100, 2))

labels = '0~4', '5~7', '8~10'
sizes = [sum(list(map(float, percentage_list[0:4]))), sum(list(map(float, percentage_list[5:7]))),
         sum(list(map(float, percentage_list[8:10])))]
colors = ['yellowgreen', 'lightskyblue', 'lightcoral']
explode_list = [0, 0, 0.1]
# explode_list[sizes.index(max(sizes))] = 0.1
explode = tuple(explode_list)

'''Plot'''
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Score Distribution of %s' % app.upper())
