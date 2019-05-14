import xlrd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


file_location = "C:\\Users\\wenjli\\Desktop\\Beta_Feedback\\Apps2Beta1.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

max_cols = sheet.ncols
max_rows = sheet.nrows

score_7 = 0
score_8 = 0
score_9 = 0
score_10 = 0

the_grid = GridSpec(1, 5)
sub_index = 0

'''find the index of the app'''
app_index = []
comment_index = []
app_str = ['Hub', 'Calendar', 'Contacts', 'Tasks', 'Notes']
for i in range(sheet.ncols):
    apps = sheet.cell_value(0, i)
    for app in app_str:
        if app in apps :
            app_index.append(i)
comment_index = app_index[1::2]
app_index = app_index[0::2]

for app_i in app_index:

    bad_percentage = 0
    app_current = sheet.cell_value(0, app_i)
    app_current = app_current.split()
    app_current = app_current[0]
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
    percentage = 0
    for score in range(0, 11):
        percentage = Hub_score.count(score) / len(Hub_score) * 100

        if score < 7:
            bad_percentage = bad_percentage + percentage
        if score == 7:
            score_7 = percentage
        if score == 8:
            score_8 = percentage
        if score == 9:
            score_9 = percentage
        if score == 10:
            score_10 = percentage

        print("%.2f" % round(percentage, 2), '%', ' users give Hub score of %i' % score)

    ''' Data Plot'''
    labels = 'bad ', '7', '8', '9', '10'
    sizes = [bad_percentage, score_7, score_8, score_9, score_10]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'pink']

    explode_0 = 0
    explode_1 = 0
    explode_2 = 0
    explode_3 = 0
    explode_4 = 0
    explode_list = [explode_0, explode_1, explode_2, explode_3, explode_4]
    explode_list[sizes.index(max(sizes))] = 0.1
    explode = tuple(explode_list)
    # explode = (explode_0, explode_1, explode_2, explode_3, explode_4)  # explode 1st slice

    plt.subplot(the_grid[0, sub_index], aspect=1)
    sub_index += 1
    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title('%s' % app_current.upper())
    plt.show()

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
    print("######## END OF %s" % app_current.upper(), '########\n\n')

f = plt
# plt.show()
f.savefig("foo.pdf")
