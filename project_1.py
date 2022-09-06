import mysql.connector as connector

class project:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                  port='3306',
                  user='root',
                  password='Mysql@1234',
                  database='New_Set')
        
        query='create table if not exists Restaurant_1( Id int primary key , Name varchar(200) , Members int , Date varchar(20) , slot varchar(20) )'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
        
    def insert_data(self,id,name,members,date,slot):
        query= "insert into Restaurant_1 values({},'{}',{},'{}','{}')".format(id,name,members,date,slot)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()               # Make changes to original databse also.
        print("User data added")
        
    def fetch(self):
        query="select * from Restaurant_1"
        cur=self.con.cursor()
        cur.execute(query)
        for i in cur:
            # print("Id -" ,i[0])
            # print("Name -" ,i[1])
            # print("Age -" ,i[2])
            print(f"Client_ID-{i[0]}, Name-{i[1]} , No. Of Members-{i[2]}, Date-{i[3]}, Slot_no-{i[4]}")
            
    def delete_user(self,userid):
        query="delete from Restaurant_1 where Id={}".format(userid)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()                # Make Changes to original Databse also. 
        print("Delete user= {}")
        
    def update_user(self, name , Date ,slot , id):
        query="update Restaurant_1 set Name='{}',Date='{}', slot='{}' where Id={} ".format(name,Date,slot ,id)
        print("Record Updated")
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()  

        

        

