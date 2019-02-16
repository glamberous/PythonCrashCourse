
from collections import OrderedDict

dictionary = OrderedDict()

dictionary['float'] = "A number with a decimal point that isn't super accurate."
dictionary['double'] = "A number with a decimal point that is decently accurate."
dictionary['decimal'] = "A number with a decimal point that is extremely accurate."
dictionary['integer'] = "A number that can't have a decimal point"
dictionary['string'] = "An array of characters"
dictionary['character'] = "A single letter"


for word, definition in dictionary.items():
    print(word + ": " + definition)