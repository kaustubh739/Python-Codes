class Employee:   
    CompanyName = "Marvellous" # class variable
    def __init__(self,A,B,C,D):   # constructor
        print("Inside Constructor : 3")
        self.Name = A      # Instance variable
        self.Salary = B    # Instance variable
        self.City = C      # Instance variable
        self.Companyname = D
    
    def __del__(self):    # Destructor
        print("Inside Destructor")

    def DisplayInfo(self):   # Instance method
        print("Inside Instance method DisplayInfo")
        print("Employee Name : "+self.Name)
        print("Employee salary : ",self.Salary)
        print("Employee City : "+self.City)
        print("company name : "+self.Companyname)
        print("JY : "+ Employee.CompanyName)

    @classmethod # special function (decorator)
    def DisplayCompanyDetails(cls):   # class method
        print("Inside Instance method DisplayCompanyDetails")
        print("Company Name : "+cls.CompanyName)
        print("JY : "+ Employee.CompanyName)
    @staticmethod
    def DisplayCompanyPolicy():
        print("Inside static method DisplayCompanypolicy")
        print("All employee are 18+")
        print("Working hours are 9 to 6")
        print("Holidays : saturday & sunday")
        print("JY : "+ Employee.CompanyName)

def main():

    print("class variable : "+Employee.CompanyName)
    Employee.DisplayCompanyDetails()

    emp1 = Employee('Rahul',15000,'Pune','ensono')    # Object creation
    emp2 = Employee('Pooja',25000,'Mumbai','madhavbagh')  # object creation
    emp3 = Employee('kaustubh',30000,'jalgaon','yes')  # object creation
    

    print("Employee Name : "+emp1.Name)
    print("Employee salary : ",emp1.Salary)
    print("Employee city : "+emp1.City)
    print("company name : "+emp1.Companyname)
    
    emp2,emp3.DisplayInfo()
    # emp1.DisplayCompanyPolicy()
    Employee.DisplayCompanyPolicy()

    del emp1 
    del emp2
    del emp3

if __name__ == "__main__":
    main()