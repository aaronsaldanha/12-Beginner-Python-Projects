def madlib():
    noun1 = input('Noun1: ')
    verb1 = input('Verb1: ')
    place1 = input('Place1: ')
    place2 = input('Place2: ')
    noun2 = input('Noun2: ')
    adj = input('Adjective: ')
    noun3 = input('Noun3: ')
    noun4 = input('Noun4: ')
    noun5 = input('Noun5: ')
    color = input('Color: ')

    madlib = f"The {noun1} arrives without warning.\n\
No announcements {verb1} it, no paper notices, on downtown {place1} and {place2},\
no mentions or advertisements in local {noun2}. It is simply there, when yesterday\
it was not.\n\
The {adj} {noun3} are striped in white and black, no golds and crimson to be\
seen. No color at all save for neighboring {noun4} and {noun5} of the surrounding\
fields. Black-and-white stripes on {color} sky; countless {noun3} of varying shapes\
and sizes, with elaborate wrought-iron fence encasing them in a colorless world.\
Even what little ground is visible from outside is black or white, painted, or\
powdered, or treated with some other {noun1} trick.\n\
- An excerpt from Erin Morgenstern's 'The Night {noun1}'"

    print(madlib)
