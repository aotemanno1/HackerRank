import xlrd
import matplotlib.pyplot as plt
from fpdf import FPDF
import math

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
score_0_4 = 0
score_5_7 = 0
score_8_10 = 0

'''find the index of the app and comment in excel'''
app_index = []
comment_index = []
# app = input("enter the app:")
app = 'hub'
for col in range(sheet.ncols):
    temp = sheet.cell_value(0, col)
    if (app in temp) or (app in temp.lower()):
        app_index.append(col)
comment_index = app_index[1]
app_index = app_index[0]

'''Score and Comment List'''
Hub_score = []
score = 0
int_score = 0
bad_review = []
review_0_4 = []
review_5_7 = []
review_8_10 = []

for hub_row in range(1, max_rows):
    check_string = sheet.cell_value(hub_row, comment_index)
    if sheet.cell_value(hub_row, app_index) == 'NA':
        continue
    else:
        score = sheet.cell_value(hub_row, app_index)
        int_score = int(score)
        # review = sheet.cell_value(hub_row, 4)
        Hub_score.append(int_score)

    if check_string != '':
        if int_score <= 7:
            bad_review.append(check_string)
        if 0 <= int_score <= 4:
            review_0_4.append(check_string)
        if 5 <= int_score <= 7:
            review_5_7.append(check_string)
        if 8 <= int_score <= 10:
            review_8_10.append(check_string)

'''Score Distribution Calculation'''
# print("\n=========Score Distribution============")
percentage = 0

for score in range(0, 11):
    percentage = Hub_score.count(score) / len(Hub_score) * 100
    '''Percentage by Score'''
    # if score < 7:
    #     others = others + percentage
    # if score == 7:
    #     score_7 = percentage
    # if score == 8:
    #     score_8 = percentage
    # if score == 9:
    #     score_9 = percentage
    # if score == 10:
    #     score_10 = percentage
    # print("%.2f" % round(percentage, 2), '%', ' users give Hub score of %i' % score)
    '''Percentage by Range'''
    if 0 <= score <= 4:
        score_0_4 = score_0_4+percentage
    if 5 <= score <= 7:
        score_5_7 = score_5_7+percentage
    if 8 <= score <= 10:
        score_8_10 = score_8_10+percentage

'''User Satisfaction Calculation'''
total_respondents = max_rows-1
satisfaction = (Hub_score.count(8)+Hub_score.count(9)+Hub_score.count(10))/len(Hub_score)*100
# print("\n==========%s" % app, "Satisfaction============")
# print("Total respondents =", total_respondents)
# print("%.2f" % round(satisfaction, 2), '% of people satisfied with the software ')


'''Bad Reviews'''
index = 1
# print('\n==============Bad Review===============')
for review in bad_review:
    if review != '':
        # print("%i: " % index, review)
        index += 1

'''Data to Plot'''
explode_0 = 0
explode_1 = 0
explode_2 = 0
explode_3 = 0
explode_4 = 0

explode_0_4 = 0
explode_5_7 = 0
explode_8_10 = 0
'''By Score'''
# labels = 'others', '7', '8', '9', '10'
# sizes = [others, score_7, score_8, score_9, score_10]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'pink']
# explode = (0, 0, 0, 0, 0.1)  # explode 1st slice

'''By Range of Score'''
labels = '0~4', '5~7', '8~10'
sizes = [score_0_4, score_5_7, score_8_10]
colors = ['yellowgreen', 'lightskyblue', 'lightcoral']
explode_list = [explode_0_4, explode_5_7, explode_8_10]
explode_list[sizes.index(max(sizes))] = 0.1
explode = tuple(explode_list)

'''Plot'''
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Score Distribution of %s' % app.upper())
# plt.show()


'''Plot save to .png'''
plt.savefig('%s' % app.upper() + '.png')
plt.close()


'''Create PDF'''
pdf = FPDF(orientation='L', unit='mm', format='A4') #landscape
pdf.add_page()
pdf.set_font("Arial", size=12, style='')
pdf.cell(280, 10, txt="%s " % app.upper() + "Satisfication", ln=1, align="L") # ln = add a line break

'''Title and Image'''
total_respondents_str = "Total respondents = " + str(total_respondents)
pdf.cell(280, 12, txt="{}".format(total_respondents_str), ln=1, align="L")
pdf.cell(280, 12, txt="%.2f" % round(satisfaction, 2) + '% of people satisfied with the app ', ln=1, align="L")
pdf.image('%s' % app.upper() + '.PNG', x=120, y=0, w=100)

'''Generate table'''
Table_Data_0_4 = []
Table_Data_5_7 = []
Table_Data_8_10 = []
for index in range(len(review_0_4)):
    Table_Data_0_4.append(['', str(index+1)+' - '+review_0_4[index]])
for index in range(len(review_5_7)):
    Table_Data_5_7.append(['', str(index+1)+' - '+review_5_7[index]])

'''Display the table'''
count = 1
char_per_line = 22
table_width = 260
table_height = pdf.font_size+1
pdf.set_xy(10, 63)
pdf.cell(table_width, table_height, 'Score 0~4:', 1, 1)
for row in Table_Data_0_4:
    for item in row:
        split_item = item.split()
        divide = math.ceil(len(split_item) / char_per_line)
        mod = len(split_item) % char_per_line
        for i in range(divide):
            split_portion = split_item[i*char_per_line:(i+1)*char_per_line:]
            each_portion = ' '.join(split_portion)
            pdf.cell(table_width, table_height, each_portion, 1, 1)
            # if i == (divide - 1):
            #     split_portion = split_item[i*char_per_line:i*char_per_line+mod:]
            #     each_portion = ' '.join(split_portion)
            #     pdf.cell(table_width, table_height, each_portion, 1, 1)

pdf.set_xy(int(pdf.get_x()), int(pdf.get_y())+20)
pdf.cell(table_width, table_height, 'Score 5~7:', 1, 1)
for row in Table_Data_5_7:
    for item in row:
        split_item = item.split()
        divide = math.ceil(len(split_item) / char_per_line)
        mod = len(split_item) % char_per_line
        for i in range(divide):
            split_portion = split_item[i*char_per_line:(i+1)*char_per_line:]
            each_portion = ' '.join(split_portion)
            pdf.cell(table_width, table_height, each_portion, 1, 1)

pdf.output("App_Satisfication.pdf")
