import pymysql
import secrets
# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='fal')
import random
class mysql_connect():

    def __init__(self,host,port,db,user,passwd):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
        self.cur = conn.cursor()

    # def connect(self):
    #     conn = pymysql.connect('86', 3306, 'uktk', 'krkfkf', 'u')
    #     self.cur = conn.cursor()

    def checkDB(self):

        query = "SELECT COUNT(*) FROM `members`"
        self.cur.execute(query)
        result = self.cur.fetchone()
        return result
    def getUser(self,username):

        query = "SELECT COUNT(*) FROM `members` WHERE `members`.`username` = '{}'".format(str(username))
        # print(query)
        self.cur.execute(query)
        temp = ''
        for row in self.cur:
            temp = str(row)
            break
        if '1' in temp:
            return True
        else:
            return False

    def getProfile(self,id):
        query = "SELECT * FROM `members` WHERE `members`.`id` = '{}'".format(str(id))
        self.cur.execute(query)
        result = self.cur.fetchall()
        temp = list(result[0])
        temp.remove(temp[3])
        temp = tuple(temp)
        return temp

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
    def checkToken(self,token):
        query = "SELECT `member_id` FROM `member_sessions` WHERE member_sessions.access_token =  '{}'".format(str(token))
        self.cur.execute(query)
        result = self.cur.fetchone()
        return result[0]
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

    def getUserID(self,token):
        query = "SELECT member_sessions.member_id FROM `member_sessions` WHERE member_sessions.access_token =  '{}'".format(str(token))
        try:
            self.cur.execute(query)
            result = self.cur.fetchone()
            return result[0]
        except Exception as e:
            print(e)
            return 0

    def sendFortune(self,userid,image1,image2,image3,created_at):
        try:

            query = "INSERT INTO `waiting_fortune` (`fortune_id`, `member_id`, `image_1`, `image_2`, `image_3`, `created_at`, `is_sent`) VALUES (NULL,'{}', '{}', '{}','{}','{}','0')".format(str(userid),str(image1),str(image2),str(image3),str(created_at))
            self.cur.execute(query)
            return 1
        except Exception as e:
            print(e)
            return 0

    def getWaitings(self):
        try:
            self.waiting_users = []
            query = "SELECT `waiting_fortune`.`member_id`  FROM `waiting_fortune`"
            self.cur.execute(query)
            result = self.cur.fetchall()
            for item in result:
                self.waiting_users.append(item[0])
            query = "DELETE  FROM `waiting_fortune`"
            print(self.waiting_users)
            self.cur.execute(query)
            return result
        except Exception as e:
            print(e)
            return 0

    def sendWatingFortune(self):
        self.getWaitings()
        print("SENDİNGG...")
        if len(self.waiting_users) == 0:
            return 0
        try:
            query = "SELECT * FROM `fortunes` ORDER BY `fortunes`.`fal_id` DESC LIMIT 1"
            self.cur.execute(query)
            result = self.cur.fetchone()

            for user in self.waiting_users:
                temp = random.randint(1,result[0])
                print(user)
                query = "INSERT INTO `sent_fortune` (`sent_id`, `member_id`, `fortune_id`) VALUES (NULL, '{}', '{}')".format(str(user),str(temp))
                self.cur.execute(query)
            return result[0]
        except Exception as e:
            print(e)
            return 0
