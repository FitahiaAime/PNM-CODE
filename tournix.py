from itertools import cyle 

def generer_planning(eleves, taches):
    planning = []
    groupes = cycle(eleves.keys())
    for jour in range(1, 6):  # 5 jours
        groupe = next(groupes)
        planning.append({
            "jour": f"Jour {jour}",
            "groupe": groupe,
            "eleves": eleves[groupe],
            "tache": taches[(jour-1) % len(taches)]
        })
    return planning

planning = generer_planning(eleves, taches)
for p in planning:
    print(p)