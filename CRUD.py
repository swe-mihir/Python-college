import mysql.connector
try:

   connect=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="demo1")
   print("Connection Status:",connect.is_connected())
   cursor=connect.cursor()
   #create table command
   # query="CREATE TABLE test(Name varchar(30),ID int, Phy int, Chem int, Math int, Status varchar(10))"
   # cursor.execute(query)
   # display()

   def display():
       print("table:\n")
       query = "SELECT*FROM demo1.test"
       cursor.execute(query)
       for item in cursor.fetchall():
           print(item)
       connect.commit()

   def insert(name,id,phy,chem,math,stat):
       query="INSERT INTO test(Name,Id,Phy,Chem,Math,Status) values(%s,%s,%s,%s,%s,%s)"
       values=(name,id,phy,chem,math,stat)
       cursor.execute(query,values)
       connect.commit()
       display()
       connect.commit()

   def update(newstat,gid):
       query=("UPDATE test SET Status=%s WHERE Id=%s")
       values=(newstat,gid)
       cursor.execute(query,values)
       display()
       connect.commit()

   def delete (id):
       query=("DELETE FROM test WHERE Id=%s")
       values=(id,)
       cursor.execute(query,values)
       display()
       connect.commit()
   choice=0
   while choice!=5:
       print("1.Insert\n2.Update\n3.Delete\n4.Display\n5.Exit")
       choice=int(input("Enter the choice:"))
       if choice==1:
           name=input("enter name")
           id=int(input("Enter the id:"))
           phy=int(input("Enter physics marks:"))
           chem=int(input("Enter chemistry marks:"))
           math=int(input("Enter math marks:"))
           stat=input("Enter status:")
           insert(name,id,phy,chem,math,stat)
       elif choice==2:
           gid=int(input("Enter the rollnumber whose status needs to be updated\n"))
           newstat=input("Enter the new status")
           update(newstat,gid)
       elif choice==3:
           id=int(input("Enter the id number of the student to be deleted:"))
           delete(id)
       elif choice==4:
           display()
       else:
           print("Invalid choice")

except mysql.connector.Error as er:
   print("Error:",er)
