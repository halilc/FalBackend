import pymysql

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
        # INSERT
        # INTO
        # `members`(`id`, `username`, `email`, `password`, `banned`, `created_at`, `updated_at`)
        # VALUES(NULL, 'deneme3', 'deneme3@gmail.com', '123456', '0', '2019-12-06 00:00:00', '2019-12-06 00:00:00');

        # print(query)
        return self.cur.execute(query)

        # temp = ''
        # for row in self.cur:
        #     temp = str(row)
        #     break
        # if '1' in temp:
        #     return True
        # else: return False

