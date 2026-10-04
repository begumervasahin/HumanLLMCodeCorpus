print("\n\t\t\t\t
print("Importing Packages...
from dataprep import data,np
print("IMPORT DONE.\n")
print("Setting Inputs and Targets ...
b1 = data.iloc[:,:-1]
b2 = data['MEDV']
print("
def fonk1(data,b14):
    print("\nRunning Train_Test_Split...\n")
    global row;
    b3 = int((b14/100)*row)
    b4 = row-b3
    print("   The size of Training Data is : ",b4)
    print("   The size of Test Data is     : ",b3,)
    print("                          Total : ",(b4+b3))
    a1 = 0
    b5 = []
    b6 = []
    print("\n\tRandomly Choosing Training Data...\n")
    b7 = pd.DataFrame(b5,columns=names)
    while(a1<b4):
        b8 = np.random.choice(data['Sn'])
        if (((b8 = =b7.Sn).any())==False):
            b9 = (data.iloc[b8-1:b8,:]).to_dict(orient='dict')
            b5.append(b9)
            a1 = a1+1
            b7 = pd.DataFrame(b5,columns=names)
        else:
            print("",b10 = "")
    a1 = 0
    b11 = pd.DataFrame(b6,columns=names)
    print("\tRandomly Choosing Test Data...\n")
    while(a1<b3):
        b8 = np.random.choice(data['Sn'])
        if (((b8 = =b7.Sn).any())==False) and (((b8==b11.Sn).any())==False):
             b12 = (data.iloc[b8-1:b8,:]).to_dict(orient='dict')
             b6.append(b12)
             a1 = a1+1
             b11 = pd.DataFrame(b6,columns=names)
    print("\t\tThe Training and Test Data ARE Split")
    return b7,b11
def fonk2():
    global b1;global b2;
    b13 = str(input("\n\t\tUse Built-IN Splitter(NOT READY!!) ?\nEnter [y/n]:   "))
    if b13 = ='y':
        print("\n
        print("
        fonk2()
        b14 = int(input("\n\t\tEnter the TEST size(IN PERCENTAGE) : "))
        b14 = (b14/100)
        b7,b11 = fonk1(data,b14)
        print("\nThe Training Data has shape :",np.shape(b7))
        print("The Test Data has shape     :",np.shape(b11))
        b7[names]=b7[names].replace({'{':''},b15 = True)
        b7[names]=b7[names].replace({'}':''},b15 = True)
        b7.to_excel('hello.xlsx')
        b16 = pd.DataFrame([b7.InvoiceNo,b7.StockCode,b7.Quantity]).transpose()
        b17 = pd.DataFrame([b11.InvoiceNo,b11.StockCode,b11.Quantity]).transpose()
        b18 = pd.DataFrame([b7.Country]).transpose()
        b19 = pd.DataFrame([b11.Country]).transpose()
    elif b13 = ='n':
        b14 = int(input("\n\t\tEnter the TEST size(IN PERCENTAGE) : "))
        print("\nRandomly Choosing Training and Test Data...
        from sklearn.model_selection import train_test_split
        b16,b17,b18,b19 = train_test_split(b1,b2,b3=b14,random_state=0)
        print("The Training & Test Data ARE Split")
    else:
        print("Wrong Choice...TRY AGAIN\n")
        fonk2()
    return b16,b17,b18,b19
Xtrain,Xtest,Ytrain,b20 = fonk2()
print("\n\t
print("\t\tExiting pre.py\n")