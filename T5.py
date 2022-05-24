notes = [{"id": 1, "note": 9, "appreciation": "Tu es nul Toto"},
         {"id": 2, "note": 14, "appreciation": "Peux faire mieux"},
         {"id": 3, "note": 22, "appreciation": "Splendide! Magnifique"}
         ]

eleves = [{"nom": "Toto", "jour de naissance": 31, "ville": "Turtoin"},
         {"nom": "Momo", "jour de naissance": 7, "ville": "Bidule"},
         {"nom": "Mumu", "jour de naissance": 1, "ville": "Loucoum"}
         ]

for i in range(len(eleves)):
    eleves[i]["id"] = i+1
    

def fusion(e, n):
    assert e["id"] == n["id"], "lignes incompatibles"
    return {
        "id": e["id"],
        "nom": e["nom"],
        "jour de naissance": e["jour de naissance"],
        "ville": e["ville"],
        "note": n["note"],
        "appreciation": n["appreciation"]
        }
    
    
eleves_notes = [
    fusion(e, n)
    for e in eleves
    for n in notes
    if e["id"] == n["id"]
    ]

print (eleves_notes)