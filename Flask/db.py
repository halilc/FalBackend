import pymysql

# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='fal')





class mysql_connect():

    def __init__(self,host,port,user,passwd,db):
        # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='fal')
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
        self.cur = conn.cursor()

    def getUsers(self,username):
        query = "SELECT COUNT(*) FROM `members` WHERE `members`.`username` = "   + str(username)
        print(query)
        self.cur.execute(query)
        return self.cur
