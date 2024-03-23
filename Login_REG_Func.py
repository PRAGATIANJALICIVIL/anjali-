import csv
class LandR:
    def Registration(self,username,password,phoneno,pincode,city):
        self.uname = username
        self.pwd = password
        self.phoneno = phoneno
        self.pin = pincode
        self.city = city
        #writing details to users data file
        
        with open('E-Com_proj/user_reg.csv','a',newline='') as file:
            store = csv.writer(file)
            store.writerow([self.uname,self.pwd,self.phoneno,self.pin,self.city])  
        #Resgistration done successfully
    def login(self,username,password):

        with open('E-Com_proj/user_reg.csv','r',newline='') as file:
            read = csv.DictReader(file)
            for row in read:
                if row['uname'] == username and row['password'] == password:
                    print("yes")
            else:
                print("no")
        # return False

obj = LandR()
obj.Registration("ram",123,1234,50019,"hyd")
obj.login("ram","1234")



    

        