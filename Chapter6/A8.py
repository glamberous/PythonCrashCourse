

koda = {'name':'koda', 'animal':'cat', 'owner':'justine styles'}
gizmo = {'name':'gizmo', 'animal':'cat', 'owner':'grant lamb'}
gaspard = {'name':'gaspard', 'animal':'cat', 'owner':'johnny vo'}
spot = {'name':'spot', 'animal':'dog', 'owner':'john snow'}

pets = [koda, gizmo, gaspard, spot]

for pet in pets:
    print('Name: ' + pet['name'].title())
    print('Animal: ' + pet['animal'].title())
    print('Owner: ' + pet['owner'].title())
    print()