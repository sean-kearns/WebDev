#object oriented programming 

#class to make points with x and y values
class Point():
    #magic function 
    #automatically will run when a new instance of the object is created 
    #self references the object that we are currently dealing with 
    def __init__(self, x_input, y_input):
        self.x = x_input #value being stored in the instance of the object 
        self.y = y_input

p = Point(2, 8) #creating a new object of type Point

#print two attributes of this object 
# print(p.x)
# print(p.y)


class Flight():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passengers = []
    
    #new method (function) to add passengers
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name) #adding someone new to the end of the list of passengers 
        return True #returns true if there are open seats and the if statement is bypassed 

    #create a function to return how many open seats there are 
    #only input arg needed is self because the attributes are all that are needed 
    def open_seats(self):
        return self.capacity - len(self.passengers)


#making a new flight object with capacity of three 
flight = Flight(3)

people = ['Harry', 'Sean', 'Tom', 'Addy']

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight.")
    else:
        print(f'No available flights for {person}.')



