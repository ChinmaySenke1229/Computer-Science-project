import csv

f=open("record.csv","w",newline="")#Creates csv file
x=['id','car name','price']#Name of records 
details=[[1,'Yaris',2000000],[2,'Corrola',5000000],[3,'Tocoma',4000000],[4,'GR86',3800000]]#Values of records
r=csv.writer(f)#writer object
r.writerow(x)
r.writerows(details)
f.close()


def add():#To add new records

    f=open("record.csv","a")
    r=csv.writer(f)#Creates writer object

    while True:#Asking user for input
        n=input("enter your vehicle id=")
        m=input("enter vehicle name=")
        s=int(input("enter vehicle cost="))
        v=[n,m.upper(),s]  
        r.writerow(v)
        c=input("more records(y/n)")
        if(c=='n'):
            break

    f.close()
    
def displayone():#To display a particular record

    f=open("record.csv","r")
    r=csv.reader(f)
    n=input("enter name of the car you want to search=")#Takes input from user

    for i in r:
        if(i[1]==n):
            print(i)
        
    f.close()

def displayall():#To display all records

    f=open("record.csv","r")
    r=csv.reader(f)
    for i in r:
        print(i)
        
    f.close()

def delete():#To delete a record

    l=[]#values excluding header
    t=[]#will store header
    f=open("record.csv")
    r=csv.reader(f)
    c=1#to track row number

    for i in r:
        if(c==1):#first row will be added to t
            t.append(list(i))
        else:
            l.append(list(i))#subsequent rows will be added to l
        c+=1

    '''print(t)
    for i in l:
        print(i)'''

    q=0#to indicate whether vehicle was found
    n=[]#to store rows that dont match the vehicle to be deleted
    m=input("enter vehicle name you want to delete=").title()

    for i in l:
        if(i[1]!=m):
            n.append(i)#added to n if doesnt match
            q=1
    if(q==0):# if q remains zero after loop ie vehicle hasnt been fond 
        print("vehicle not found")
    print(t)#to check if the code is working fine(prints header and filtered rows)
    
    for i in n:
        print(i)
   
    d=[]#to store the final data
    d.extend(t)

    for i in n:
        d.append(i)
    f=open("record.csv","w",newline="")
    g=csv.writer(f)#writes back into the file
    g.writerows(d)

def update():#To update the values  of a record

    l=[]#the first row(header)
    t=[]#subsequent rows
    f=open("record.csv")
    r=csv.reader(f)
    c=1

    for i in r:
        if(c==1):
            t.append(list(i))
        else:
            l.append(list(i))
        c+=1

    '''print(t)
    for i in l:
        print(i)'''

    q=0
    n=[]
    m=input("enter vehicle name you want to update=").title()#gets vehicles name for updation

    for i in l:
        data=[]#To store updated values
        if(i[1]==m):#if vehicles name matches then proccedes
            m.isupper()
            o=input("enter vehicle id=")#prompts the user to entr new values
            name=input("enter vehicle name=")
            cost=input("enter price=")
            data.append(o)
            data.append(name)
            data.append(cost)
            n.append(data)#list of list
        else:
            n.append(i)#if vehicle name doesnt match
            q=1

    if(q==0):#to check if the variable has been found
        print("vehicle not found")
    print(t)

    for i in n:
        print(i)
    
    d=[]
    d.extend(t)

    for i in n:#writes the modified data back to the csv file
        d.append(i)
    f=open("record.csv","w",newline="")
    g=csv.writer(f)
    g.writerows(d)

def purchase():#To purchase a car

    f=open("record.csv","r")
    r=csv.reader(f)
    next(r)#To retieve the next item from the iterator(to avoid a loop)
    displayall()

    m=input("enter vehicle name you want to purchase=")#Takes input from user 

    for i in r:
        if(i[1]==m):
            print(i)
            n=i[2]

    e=int(n)
    print("Vehicle cost",e)
    print("purchase successful")
    return e
    f.close()


def menu():

    while True:#To make to program menu driven

        print("1. add new vehicle")
        print("2. display one vehicle")
        print("3. display all vehicles")
        print("4. delete a vehicle")
        print("5. update a vehcle")
        print("6. purchase a vehicle")
        print("7. exit")

        n=int(input("enter ur choice="))

        if(n==1):
            add()
        elif(n==2):
            displayone()
        elif(n==3):
            displayall()
        elif(n==4):
            delete()
        elif(n==5):
            update()
        elif(n==6):
            purchase()
        elif(n==7):
            print("Thanks for coming!")
            break
        else:
            print("enter choice between 1 to 7")

menu()
        
