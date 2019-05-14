import xlrd
import matplotlib.pyplot as plt


file_location = "C:\\Users\\wenjli\\Desktop\\Beta_Feedback\\Apps2Beta1.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

max_cols = sheet.ncols
max_rows = sheet.nrows

'''find the index of the app'''
app_index=[]
comment_index=[]
app_str = ['Hub', 'Calendar', 'Contacts', 'Tasks', 'Notes']
for i in range(sheet.ncols):
    temp = sheet.cell_value(0, i)
    for app in app_str:
        if app in temp :
            app_index.append(i)
comment_index = app_index[1::2]
app_index = app_index[0::2]

for app_i in app_index:
    app_current = sheet.cell_value(0, app_i)
    print("######## START OF %s " % app_current.upper(),' ########')

    '''Hub Score List'''
    Hub_score = []
    score = 0
    int_score = 0
    bad_review = []
    for hub_row in range(1, max_rows):
        if sheet.cell_value(hub_row, app_i) == 'NA':
            continue
        else:
            score = sheet.cell_value(hub_row, app_i)
            int_score = int(score)
            # review = sheet.cell_value(hub_row, 4)
            Hub_score.append(int_score)

        if int_score <= 7:
            bad_review.append(sheet.cell_value(hub_row, app_i+1))

    '''Score Distribution Calculation'''
    print("=========Score Distribution============")
    for score in range(0, 11):
        percentage = Hub_score.count(score) / len(Hub_score) * 100
        print("%.2f" % round(percentage, 2), '%', ' users give Hub score of %i' % score)

    '''User Satisfaction Calculation'''
    total_respondents = max_rows-1
    satisfaction = (Hub_score.count(8)+Hub_score.count(9)+Hub_score.count(10))/total_respondents*100
    print("\n========%s " % app_current, " ==============")
    print("Total respondents =", total_respondents)
    print("%.2f" % round(satisfaction, 2), '% of people satisfied with the software ')

    '''Bad Reviews'''
    index = 1
    print('\n=============Bad Review================')
    for review in bad_review:
        if review != '':
            # print("%i: " % index, review)
            index += 1
    print("######## END OF %s" % app_current.upper(),'########\n\n')
#
# # Data to plot
# labels = 'Hub', 'Calendar', 'Contacts', 'Tasks','Notes'
# sizes = [215, 130, 245, 210]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# explode = (0.1, 0, 0, 0)  # explode 1st slice
#
# # Plot
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=140)
#
# plt.axis('equal')
# plt.show()