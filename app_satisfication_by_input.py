import xlrd
import matplotlib.pyplot as plt


file_location = "C:\\Users\\wenjli\\Desktop\\Beta_Feedback\\Apps2Beta1.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

max_cols = sheet.ncols
max_rows = sheet.nrows


others = 0
score_7 = 0
score_8 = 0
score_9 = 0
score_10 = 0

'''find the index of the app'''
app_index=[]
comment_index=[]

app = input("enter the app:")
for col in range(sheet.ncols):
    temp = sheet.cell_value(0,col)
    if (app in temp) or (app in temp.lower()):
        app_index.append(col)
comment_index = app_index[1]
app_index = app_index[0]


'''Hub Score List'''
Hub_score = []
score = 0
int_score = 0
bad_review = []

for hub_row in range(1, max_rows):
    if sheet.cell_value(hub_row, app_index) == 'NA':
        continue
    else:
        score = sheet.cell_value(hub_row, app_index)
        int_score = int(score)
        # review = sheet.cell_value(hub_row, 4)
        Hub_score.append(int_score)

    if int_score <= 7:
        bad_review.append(sheet.cell_value(hub_row, comment_index))


'''Score Distribution Calculation'''
print("\n=========Score Distribution============")
percentage = 0

for score in range(0, 11):
    percentage = Hub_score.count(score) / len(Hub_score) * 100

    if score < 7:
        others = others + percentage
    if score == 7:
        score_7 = percentage
    if score == 8:
        score_8 = percentage
    if score == 9:
        score_9 = percentage
    if score == 10:
        score_10 = percentage


    print("%.2f" % round(percentage, 2), '%', ' users give Hub score of %i' % score)

'''User Satisfaction Calculation'''
total_respondents = max_rows-1
satisfaction = (Hub_score.count(8)+Hub_score.count(9)+Hub_score.count(10))/total_respondents*100
print("\n==========%s" % app, "Satisfaction============")
print("Total respondents =", total_respondents)
print("%.2f" % round(satisfaction, 2), '% of people satisfied with the software ')

'''Bad Reviews'''
index = 1
print('\n==============Bad Review===============')
for review in bad_review:
    if review != '':
        print("%i: " % index, review)
        index += 1

# Data to plot
labels = 'others', '7', '8', '9', '10'
sizes = [others, score_7, score_8, score_9, score_10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'pink']
explode = (0, 0, 0, 0, 0.1)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Score Distribution of %s' % app.upper())
plt.show()
