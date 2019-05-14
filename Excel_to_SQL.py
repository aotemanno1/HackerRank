import pyodbc
import datetime, xlrd

'''
    'Driver={SQL Server};'
    'Server=SQLQA04YKF.rim.net\QA4;'
    'Database=uetools;'
    'Trusted_Connection=yes
'''


def load_excel():
    global sheet
    global workbook
    file_location = "C:\\Users\\wenjli\\Desktop\\Beta_Feedback\\Apps2Beta1.xlsx"
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_index(0)


def get_col():
    global username_col
    global submitdate_col
    global comment_col
    global satisfaction_col
    global appid
    # app = input("enter the app:")
    app = 'hub'
    appid = 'com.blackberry.' + app
    for col in range(sheet.ncols):
        temp = sheet.cell_value(0, col)
        if app in temp.lower():
            satisfaction_col = col - 1
            comment_col = col
        elif 'email' in temp.lower():
            username_col = col
        elif 'date' in temp.lower():
            submitdate_col = col


def get_username_list():
    global username_list
    username_list = []
    for row in range(sheet.nrows-1):
        '''remove @gmail.com'''
        temp_username = sheet.cell_value(row+1, username_col)
        temp = temp_username.split('@')
        username_list.append(temp[0])


def get_submitdate_list():
    global submitdate_list
    submitdate_list = []
    for row in range(sheet.nrows-1):
        float_submitdate = sheet.cell_value(row+1, submitdate_col)
        date_submitdate = datetime.datetime(*xlrd.xldate_as_tuple(float_submitdate, workbook.datemode))
        submitdate_list.append(date_submitdate)


def get_satisfaction_list():
    global satisfaction_list
    satisfaction_list = []
    for row in range(sheet.nrows-1):
        satisfaction_list.append(sheet.cell_value(row+1, satisfaction_col))


def get_comment_list():
    global comment_list
    comment_list = []
    for row in range(sheet.nrows-1):
        comment_list.append(sheet.cell_value(row+1, comment_col))


def sql_connect():
    global cursor
    global conn
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=SQLQA04YKF.rim.net\QA4;'
                          'Database=uetools;'
                          'Trusted_Connection=yes;'
                          )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM uetools.go_beta.app_feedback')


def clear_lists():
    for score in satisfaction_list:
        if score.upper() == 'NA':
            del_index = satisfaction_list.index(score)
            del satisfaction_list[del_index]
            del comment_list[del_index]
            del submitdate_list[del_index]
            del username_list[del_index]


def sql_insert(i):
    # cursor.execute(
    #     # "INSERT INTO go_beta.app_feedback(username,bsn,appid,appversion,rating,satisfaction,comment,submitdate) VALUES (%s,external,%s,%s,%s,%s,%s,%s)", (username_list[i], appid, 11111111, '',, satisfaction_list[i], comment_list[i], submitdate_list[i])
    #     "INSERT INTO go_beta.app_feedback VALUES (%s,external,%s,%s,%s,%s,%s,%s)",
    #     (username_list[i], appid, 11111111, '', satisfaction_list[i], comment_list[i], submitdate_list[i])
    #
    # )
    cursor.execute(
        "INSERT INTO go_beta.app_feedback (username, bsn, appid,appversion,rating, satisfaction, comment, submitdate) "
        "\nVALUES (\'" + username_list[i] + "\'," + "\'external\'," + "\'" + appid + "\',"
        + "\'2.1810.0.16754\'," + "\'\'," + "\'" + satisfaction_list[i] + "\'," + "\'" + comment_list[i] + "\',"
        + "\'" + str(submitdate_list[i]) + "\')"
    )

    conn.commit()


load_excel()
get_col()
get_username_list()
get_submitdate_list()
get_comment_list()
get_satisfaction_list()
clear_lists()
sql_connect()
# for i in range(len(comment_list)):
#     sql_insert(i)

cursor.execute(
               "INSERT INTO go_beta.app_feedback (username, bsn, appid,appversion,rating, satisfaction, comment, submitdate) "
               "\nVALUES (\'" + username_list[0] + "\'," + "\'testexternal\'," + "\'" + appid + "\',"
               +"\'2.1810.0.16754\',"+ "\'\'," + "\'"+satisfaction_list[0]+"\',"+"\'"+comment_list[0]+"\',"
               +"\'"+str(submitdate_list[0])+"\')"
                )

conn.commit()



