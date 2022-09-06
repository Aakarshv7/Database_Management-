from project_1 import *

call=project()

while(True):
    print(" \n ******* Welcome to Restaurant Mangament System , Choose any - ****** \n")
    print("1 - Make a New Booking")
    print("2 - Show all bookings")
    print("3 - Delete a booking")
    print("4 - Update booking details")
    print("5 - Exit Program \n")
    
    a= int(input("Enter your Choice --  "))
    try:
        if(a==1):
            #  Inserting  New Data
            
            id=int(input(" \n Enter  Client Id - "))
            name = input("Enter Name - ")
            members=int(input("No of Members -"))
            date= input("Enter Booking Date - ")
            slot= input("Enter Slot no.- ")
            
            call.insert_data(id , name , members,date, slot)
            
        elif(a==2):
            # Showing all Users
            call.fetch()
        
        elif(a==3):
            # Deleting a User
            print("Delete a Booking")
            id_1=int(input("Enter Client_Id - "))
            call.delete_user(id_1) 
            pass
       
        elif(a==4):
            # Updatind Details
            id_2=int(input("Enter Client_Id - "))
            name_2 = input("Enter Name -  ")
            date_2=input("Enter updated Date - ")
            slot_2=input("Enter updated Slot - ")
            call.update_user(name_2 , date_2, slot_2, id_2)
        
        elif(a==5):
            break
        
    except Exception as e:
        print(e)
  
    