class multipleFunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in lists:
            print(temp)
            
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle:",(Height*Breadth/2))
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula:Height1+Height2+Breadth")
        print("Perimeter of Triangle:",Height1+Height2+Breadth)
       
    
    def percentage():
        s1=int(input("Subject1="))
        s2=int(input("Subject2="))
        s3=int(input("Subject3="))
        s4=int(input("Subject4="))
        s5=int(input("Subject5="))
        Total=s1+s2+s3+s4+s5;
        print("Total:",s1+s2+s3+s4+s5)
        Percentage=(Total/500)*100
        print("Percentage:",Percentage)
       
    
    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="Male"):
            if(age>21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(gender=="Female"):
            if(age>18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            print("INVALID INPUT DATA")
           
        
    def OddEven():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print("{0} is Even number".format(num))
        else:
            print("{0} is Odd number".format(num))