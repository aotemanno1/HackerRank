import pyodbc
'''
    'Driver={SQL Server};'
    'Server=SQLQA04YKF.rim.net\QA4;'
    'Database=uetools;'
    'Trusted_Connection=yes
'''


def sql_connect():
    global cursor
    conn = pyodbc.connect(Driver='{SQL Server}',
                          Server='SQLQA04YKF.rim.net\QA4',
                          Database='uetools',
                          Trusted_Connection='yes'
                          )
    cursor = conn.cursor()
    # cursor.execute('SELECT * FROM uetools.go_beta.app_feedback')


def create_lists():
    global username
    global appid
    global appversion
    global rating
    global satisfaction
    global comment
    global submitdate

    username = []
    appid = []
    appversion = []
    rating = []
    satisfaction = []
    comment = []
    submitdate = []

    for row in cursor:
        # for each_ele in row:
        username.append(row.username)
        appid.append(row.appid)
        appversion.append(row.appversion)
        rating.append(row.rating)
        # satisfication.append(row.satisfaction)
        comment.append(row.comment)
        submitdate.append(row.submitdate)
        if row.username == 'ThisIsAnTest2!':
            print('i got it!!!!!!!!!!!!! your code starts here!')
            print(row.bsn)


sql_connect()
create_lists()





