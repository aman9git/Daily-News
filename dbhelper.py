# from idlelib import query

import mysql.connector


class DB:
    def __init__(self):
        # connect with mysql database
        try:
            self.connect = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='news')
        except:
            print('Some Error Occured')
        else:
            self.mycursor = self.connect.cursor()
            print("Connected to DB..")

    def search(self, Email, Password):

        query = '''
        SELECT * FROM `newsuser` WHERE `Email` LIKE '{}' AND `Password` LIKE '{}' '''.format(Email, Password)

        self.mycursor.execute(query)

        data = self.mycursor.fetchall()

        return data

    def insert(self, Name, Email, Password, City, Gender):
        # query
        query = '''INSERT INTO `newsuser` (`user_id`, `Name`, `Email`, `Password`, `City`, `Gender`) VALUES (NULL, '{}', '{}', '{}', '{}', '{}')'''.format( Name, Email, Password, City, Gender)

        # execute the query
        try:
            self.mycursor.execute(query)
        except:
            return 0
        else:
            self.connect.commit()
            return 1
        # return the result
