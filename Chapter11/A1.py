def format_name(city, state, population=''):
    if population:
        formatted_name = city + ", " + state + " - " + str(population)
    else:
        formatted_name = city + ", " + state
    return formatted_name.title()
