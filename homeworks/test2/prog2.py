def read_prices(filename):
    mylist = []
    with open(filename, "r") as f:
        for l in f:
            mylist.append([l.strip()])   
    return mylist


def find_change(dlist):
    mylist = []
    for item in dlist:
        splitted = item[0].split(";")
        name = splitted[0]
        low = float(splitted[1])
        high = float(splitted[len(splitted)-1])
        diff = round(high - low, 2)
        j = (name, low, high, diff)
        mylist.append(j)
    return mylist
    
    
def main():
    name = input("Enter file name: ") or "prices.txt"
    dlist = read_prices(name)
    items = find_change(dlist)
    highest = ("","","",0)
    for item in items:
        if abs(highest[3]) < abs(item[3]):
            highest = item
        if float(item[3]) < 0:
            print("The price of "+item[0]+" decreased by "+str(item[3])+" euros.")
        else:          
            print("The price of "+item[0]+" increased by "+str(item[3])+" euros.")
    print("The price of "+highest[0]+" increased the most: "+str(highest[1])+" --> "+str(highest[2])+" (change "+str(highest[3])+" euros)")        
        
        
    
main()    