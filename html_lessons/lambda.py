people = [
    {'name':'Sean', 'house':"Marquette"},
    {'name':'Addy', 'house':"Indiana"},
    {'name':'Tom', 'house':"Illinois"}
]

#these two together
def f(person):
    return person['name']
people.sort(key=f) #uses the function that was created to sort the objeects 
print(people)


people2 = [
    {'name':'Zach', 'house':"Marquette"},
    {'name':'Beast', 'house':"Indiana"},
    {'name':'X', 'house':"Illinois"}
]
#this does the same thing 
people2.sort(key=lambda person: person['name'])

print(people2)
