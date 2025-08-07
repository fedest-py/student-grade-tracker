#******************************************************************************
# student.py
#******************************************************************************
# Name: Eduardo Esteves
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

#create the class
class Student:
    def __init__ (self, name, scores):
        #attributes
        self._name = name
        self._scores = scores
        
        #methos for saverage of scores
    def average(self):
        #if the list for scores is empty counter = 1 to prevent 0/0
        if len(self._scores) != 0:
            counter = 0
        else:
            counter = 1
        suma = 0
        for element in self._scores:
            counter += 1
            suma += element
        
        return (suma/counter)
    #method to display name and average
    def display(self):
        aver = self.average()
        print(f'{self._name}, Average: {aver}')
    #method returns boolian depending depnding on player's score    
    def passes(self):
        return self.average() >+ 60
    
            
        
        
            
    








################################################################################
# PUT YOUR CLASS DEFINITION ABOVE!
################################################################################

def main():
    a = Student('Alice', [40, 80, 90, 78])
    b = Student('Bob', [80, 70, 60])
    c = Student('Carol', [])
    d = Student('Dennis', [50, 40, 30])
    e = Student('Evan', [1, 2, 3, 4, 5])
    f = Student('Frank', [90, 90, 90])

    print('This should print: Alice, Average = 72.0')
    a.display()

    print('This should print: 70.0 True') 
    print(b.average(), b.passes())

    print('This should print: 0 False') 
    print(c.average(), c.passes())
    
    all_students = [a, b, c, d, e, f]
    
    

    ####################################################
    # Write code which displays info for the students in
    # all_students who have passing averages.
    ####################################################
    
    #loop displays all the names and averages from students in all_students
    for person in all_students:
        person.display()




    
main()    
















