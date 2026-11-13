print("--------SCHOOL MANAGEMENT SYSTEM--------")
class tms:
    def __init__(self):
        self.database=[]
        self.grade=[]
    def info(self):
        while True:
            self.stdname = input("ENTER STUDENT NAME (QUIT) \n").lower()
            if(self.stdname=="quit"):
                print("RECORD SAVE SUCCESSFULLY\n")
                break
            self.stdgrade = int(input("ENTER STUDENT GRADE:\n"))
            self.database.append(self.stdname)
            self.grade.append(self.stdgrade)
class ms(tms):
    def pri(self):
        for i in range(len(self.database)):
            print(f"STUDENT:{self.database[i]} AND GRADE:{self.grade[i]}")
a=ms()
a.info()
a.pri()


