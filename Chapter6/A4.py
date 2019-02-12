
dictionary = {
    'float': "A number with a decimal point that isn't super accurate.",
    'double': "A number with a decimal point that is decently accurate.",
    'decimal': "A number with a decimal point that is extremely accurate.",
    'integer': "A number that can't have a decimal point",
    'string': "An array of characters",
    'character': "A single letter"
}

for word, definition in dictionary.items():
    print(word + ": " + definition)