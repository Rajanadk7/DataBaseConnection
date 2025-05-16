from dbhelper import DBhelper

def main():
    db=DBhelper()
    while True:
        print("******welcome******")
        print()
        print("press 1 to insert new user")
        print("press 2 to display all user")
        print("press 3 to delete user")
        print("press 4 to update user")
        print("press 5 to exit program")
        print()

        try:
            choice=int(input())
            if(choice==1):
                #insert user
                uid =int(input("enter user id:"))
                username =input("enter user name:")
                phoneno=input("enter user phone:")
                db.insert_user(uid,username, phoneno)


            elif choice==2:
                #display user
                db.fetch_all()


            elif choice==3:
                #delete user
                userid=int(input("enter userid which you wanna delete"))
                db.delete_user(userid)
                pass


            elif choice==4:
                #update user
                uid =int(input("enter user id:"))
                username =input("enter new user name:")
                phoneno=input("enter user new phone:")
                db.update_user(uid,username,phoneno)
                pass


            elif choice==5:
                #close program
                break

            else:
                print("invalid input! try again")

        except Exception as e:
            print(e)
            print("invalid details!")

            /xklhfdbohbda

if __name__ == "__main__":
    main()
