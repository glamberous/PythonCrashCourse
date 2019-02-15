
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
    return [(magician + " The Great") for magician in magicians]
    
magicians = ["Mickey", "Todd", "Carl", "Sigfried"]
magicians_copy = make_great(magicians[:])
show_magicians(magicians_copy)
show_magicians(magicians)
