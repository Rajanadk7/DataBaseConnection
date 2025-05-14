import mysql.connector as connector #as connector is an alias  a shorter or custom name you give to the module when you import it.'''

class DBhelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='R1a2j3a4n5@',
                                     database='pythontest')
        
        query = "create table if not exists user (userid int primary key, username varchar(200), phone varchar(12))"

        cur =self.con.cursor()  #A cursor object is created from self.con to allow sending SQL commands through the database connection.
        cur.execute(query)     #This line executes the SQL command (in your case, probably a CREATE TABLE or INSERT).
        print('created')




    #insert
    def insert_user(self,userid,username,phone):
        query="iNSERT INTO user (userid,username,phone) values({},'{}','{}')".format(userid, username,phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")




    #fetch all

    def fetch_all(self):
        query="select * from user"
        cur =self.con.cursor()
        cur.execute(query)
        for row in cur:
           # print(row)
           print("user id : ", row[0])
           print("user Name  : ", row[1])
           print("user phone: ", row[2])
           print()
           print()

    def fetch_1(self):
        query ="select * from user"
        cur =self.con.cursor()
        cur.execute(query)
        for column in cur:
            print("user id:", column[0])



    #delete data

    def delete_user(self,userid):
        query = "delete from user where userid = {}".format(userid)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    

    #update 

    def update_user(self,userid,newname,newphone):
        query = "update user set username='{}',phone= '{}' where userid={}".format(newname, newphone, userid)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")



#main code

'''helper = DBhelper() # object 'helper' of the class 'dbhelper' is created
helper.insert_user(1453,"durgesh thapa","980000000")
helper.insert_user(1400,"durga nath","980000001")
helper.insert_user(1430,"ram bahadur","980000002")
helper.insert_user(1413,"python","980000003")
helper.insert_user(1460,"program","980000004")
helper.fetch_all()
helper.fetch_1()
helper.delete_user(1400)
helper.fetch_all()
helper.update_user(1452, 'anukul rai', '1234567890')'''




''' A cursor is:
A control structure that allows you to:
1.Execute SQL commands (like SELECT, INSERT, UPDATE, DELETE)
2.Fetch results from the database
3.Iterate over rows from a query result
It acts like a middleman between your Python code and the database.'''