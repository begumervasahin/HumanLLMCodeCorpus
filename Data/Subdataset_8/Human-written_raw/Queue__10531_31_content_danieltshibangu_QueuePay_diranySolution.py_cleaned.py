class Queue:
    def __init__( self ):
        self.items = []
    def is_empty( self ):
        return self.items == []
    def enqueue( self, item ):
        self.items.insert( 0, item )
    def dequeue( self ):
        return self.items.pop()
    def size( self ):
        return len( self.items )
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        self.bonus = 0
    def getPay(self):
        return self.pay
    def setPay(self,pay):
        self.pay=pay
    def setBonus( self, amount ):
        self.bonus = amount
    def getBonus( self ):
        return self.bonus
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    def __str__(self):
       return '\nEmployee name: '+ self.fullName() +\
              '\nEmployee pay: ' + str(self.pay) +\
              '\nEmployee bonus: ' + str( format(self.bonus, '.2f') )
def main():
    payRate = 0.2
    totalBonus = 0
    employeeQ = Queue()
    dirany_file = open( '/Users/danieltshibangu/Desktop/dirany.txt', 'r' )
    lineData = dirany_file.readline()
    while lineData != "":
        data_attr = lineData.split()
        employee = Employee( data_attr[0], data_attr[1], data_attr[2] )
        employee.setBonus( float( data_attr[2] ) * payRate )
        totalBonus += employee.getBonus()
        employeeQ.enqueue( employee )
        payRate -= 0.01
        lineData = dirany_file.readline()
    dirany_file.close()
    print( "The total number of employees:", employeeQ.size() )
    print( "The total bonus amount:", format( totalBonus, '.2f' ) )
    print( "\nDisplays all the objects in the queue:" )
    for item in range( employeeQ.size() ):
        print( employeeQ.dequeue() )
if __name__ == "__main__":
    main()