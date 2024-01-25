#decorator 

#function to create a function
#takes a function, adds some capabilites, and givs us back a new function 
#accepts a function as an argument, then prints a statement, then runs the inputted function, then prints another statement 
def announce(f):
    def wrapper():
        print('About to run the function...')
        f()
        print("Done with the function.")

    return wrapper 


#adding the announce decorator to this function 
@announce
def hello():
    print('Hello world!')


hello()