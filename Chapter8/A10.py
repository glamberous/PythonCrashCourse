
"""
def show_magicians(magicians):
    for magician in magicians:
        print(magician + " is a magician!")

def make_great(magicians):
    for magician in magicians:
        magician = magician.title() + " the Great"
    print(magicians) # Changes from the previous for loop are dropped here
    return magicians

magicians = ["Mickey", "Todd", "Carl", "Sigfried"]
magicians = make_great(magicians)
show_magicians(magicians)
"""
###########################################################################
"""
def show_magicians(magicians):
    for magician in magicians:
        print(magician + " is a magician!")

def make_great(magicians):
    magicians_the_great = []
    while magicians:
        magician_popped = magicians.pop()
        magician_popped = magician_popped.title() + " the Great"
        magicians_the_great.append(magician_popped)
    return magicians_the_great

magicians = ["Mickey", "Todd", "Carl", "Sigfried"]
magicians = make_great(magicians)
show_magicians(magicians)
"""
###########################################################################

def show_magicians(magicians):
    for magician in magicians:
        print(magician + " is a magician!")

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = magicians[i].title() + " the Great"
    print(magicians)

magicians = ["Mickey", "Todd", "Carl", "Sigfried"]
make_great(magicians)
show_magicians(magicians)
