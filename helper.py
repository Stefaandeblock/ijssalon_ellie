def decoreer(tekst=""):
    lengte = len(tekst) +4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag,personen):
    try:
        bedrag_pp = bedrag/personen
    except:
        bedrag_pp = "??"
    return(f"Het bedrag per persoon is {bedrag_pp} euro")

tekst = ""

def onderstreept(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit
print(onderstreept("doorgeef"))


mijn_dict =  {'key1':1,'key2':2,'key3':3}
def som(mijn_dict):
    values = mijn_dict.values()
    totaal = sum(values) 
    return totaal   
print(som(mijn_dict))
