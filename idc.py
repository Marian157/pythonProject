text = '''Presa din Spania, surprinsă că Leo Messi l-a numit pe Lautaro Martinez câștigătorul de drept la Balonul de Aur 2024
Cel mai titrat jucător la acest capitol, Lionel Messi, care a pus mâna de opt ori pe trofeul individual, a fost întrebat recent cine ar trebui să câștige.
Căpitanul de 37 de ani al Argentinei l-a numit pe Lautaro Martinez (27 de ani) de la Inter, care sezonul trecut a ieșit golgheter în Serie A și Copa America și a câștigat ambele competiții. "'''
z = len(text)//2
if len(text)%2 == 1:
    z +=1
print(text[:z].upper().strip() + text[:z:-1].replace(".","").replace(",","").replace("?","").replace("!","").capitalize())
