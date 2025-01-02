
#BLL
class Customer:
    cus_list=[]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mob=0

    def addCustomer(self):
        Customer.cus_list.append(self)

    def SearchCustomer(self):
        id1=self.id
        for e in Customer.cus_list:
            if(e.id==self.id):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                return
    def DeleteCustomer(self):
       
        for e in Customer.cus_list:
            if(e.id==self.id):
                Customer.cus_list.remove(e)
                
    def UpdateCustomer(self):
        for e in Customer.cus_list:
            if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                



#PL
print('welcome to CMS')
def ShowCustomer(cus):
    print(cus.id, cus.name, cus.age, cus.mob)
while(1):
    cus=Customer()
    choice=input("Enter Choice 1 Add, 2 Search, 3 Delete, 4 Update, 5 Display all data, 6 exit: ")
    if (choice=="1"):
        cus=Customer()
        cus.id=input("Enter Cust Id: ")
        cus.name=input("Enter Cust name: ")
        cus.age=int(input("Enter Cust age: "))
        cus.mob=int(input("Enter Cust mob: "))
        cus.addCustomer()
        print("Customer added Successfully ")

    elif(choice=="2"):
        cus=Customer()
        cus.id=input("Enter Cust ID to search: ")
        cus.SearchCustomer()
        ShowCustomer(cus)

    elif(choice=="3"):
        cus=Customer()
        cus.id=input("Enter Cust ID to Delete: ")
        cus.DeleteCustomer()
        print("Customer with id:",cus.id,"and name:",cus.name,"deleted successfully")

    elif(choice=="4"):
        cus=Customer()
        cus.id=input("Enter Cus ID to update: ")
        cus.name=input("Enter Updated name: ")
        cus.age=input("Enter updated age: ")
        cus.mob=input("Enter update mob: ")
        cus.UpdateCustomer()
        print("Customer Updated Successfully!")

    elif(choice=="5"):
        cus=Customer()
        for e in Customer.cus_list:
            ShowCustomer(e)
    elif(choice=="6"):
        print("Thanks for using .__.")
        break
    else:
        print("Incorrect Choice")