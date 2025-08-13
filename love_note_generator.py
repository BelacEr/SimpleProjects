from random import choice


name = input("What's your name? ")

love_notes = [  
    f"You compile my heart perfectly, {name}~",  
    "Roses are red, Vim is blue… I’m obsessed with you.",  
    "Did you just smile? Because my code detected a 100% increase in cuteness.",
]
print(choice(love_notes))
