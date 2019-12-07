import pymysql
import secrets
# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='fal')

class mysql_connect():

    def __init__(self,host,port,user,passwd,db):
        # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='fal')
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
        self.cur = conn.cursor()

    def getUsers(self,username):
        query = "SELECT COUNT(*) FROM `members` WHERE `members`.`username` = '{}'".format(str(username))
        # print(query)
        self.cur.execute(query)
        temp = ''
        for row in self.cur:
            temp = str(row)
            break
        if '1' in temp:
            return True
        else: return False

    def getUsersFromMail(self,email):
        query = "SELECT COUNT(*) FROM `members` WHERE `members`.`email` = '{}'".format(str(email))
        print(query)
        self.cur.execute(query)
        temp = ''
        for row in self.cur:
            temp = str(row)
            break
        if '1' in temp:
            return True
        else: return False

    def createUser(self,username,email,password,create_time):
        query = "INSERT INTO `members`(`id`, `username`, `email`, `password`, `banned`, `created_at`, `updated_at`) VALUES(NULL, '{}', '{}', '{}', '0', '{}', NULL )".format(str(username),str(email),str(password),str(create_time))
        return self.cur.execute(query)

    def createToken(self,email,created_at):

        query = "SELECT members.id FROM `members` WHERE members.email =  '{}'".format(str(email))
        self.cur.execute(query)
        result = self.cur.fetchone()
        token = secrets.token_urlsafe(20)
        query = "INSERT INTO `member_sessions`(`id`, `member_id`, `user_agent`, `ip`, `access_token`, `created_at`, `updated_at`) VALUES(NULL, '{}', NULL, NULL,'{}','{}', NULL)".format(int(result[0]), str(token), str(created_at))
        self.cur.execute(query)
        return token

    def LoginUser(self,email,password):

        query = "SELECT COUNT(*) FROM `members` WHERE members.email =  '{}' AND members.password =  '{}'".format(str(email),str(password))
        self.cur.execute(query)
        result = self.cur.fetchone()
        return result[0]


    def LogoutUser(self,username):
        # print(username)
        query = "SELECT members.id FROM `members` WHERE members.username =  '{}'".format(str(username))
        self.cur.execute(query)
        result = self.cur.fetchone()
        print("------")
        print(result[0])
        query2 = "DELETE FROM `member_sessions` WHERE member_sessions.member_id =  '{}'".format(str(result[0]))
        self.cur.execute(query2)
        # result2 = self.cur2.fetchone()
        # print(result2[0])
        # for item in self.cur:
        #     print(item)
        return "Logout"
