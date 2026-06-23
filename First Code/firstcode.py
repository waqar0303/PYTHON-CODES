arrname=[]
arrmarks=[]


def names():
    name= str(input("Enter the Name: "))
    arrname.append(name)
    
   
def mark():
    marks=float(input("Enter the Marks"))
    arrmarks.append(marks)
    
 

def display():
    for x in range(len(arrname)):
        if arrmarks[x]>90:
          print("NAME : ",arrname[x]," GRADE : A " , "MARKS : ",arrmarks[x])
        elif arrmarks[x]>80:
           print("NAME : ",arrname[x]," GRADE : B " , "MARKS : ",arrmarks[x])
        elif arrmarks[x]>70:
            print("NAME : ",arrname[x]," GRADE : C " , "MARKS : ",arrmarks[x])
        elif arrmarks[x]>60:
          print("NAME : ",arrname[x]," GRADE : D " , "MARKS : ",arrmarks[x])
        elif arrmarks[x]>50:
            print("NAME : ",arrname[x]," GRADE : E " , "MARKS : ",arrmarks[x])
        elif arrmarks[x]>40:
             print("NAME : ",arrname[x]," GRADE : F " , "MARKS : ",arrmarks[x])


 


while True:
   
    print("1.Enter Name :")
    print("2.Enter Marks :")
    print("3.Display :")
    print("0.EXIT")
    
    choice=int(input())

    if choice ==1:
         names()
    elif choice ==2:
         mark()
    elif choice == 3:
        display()

    elif choice ==0:
        break
    else:
        print("Invalid Option")

               




