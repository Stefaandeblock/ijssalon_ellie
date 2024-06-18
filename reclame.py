from Algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    vprijs = prijs
    vsmaak = smaak
    vkorting = (prijs - (prijs*korting)) 
    return(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {vsmaak}, van {vprijs} euro voor {vkorting} euro.")
print(aanbieding_1("aardbei", 4, 0.1 ))

inkomsten = [220,430,125,160,205,90,345]
def inkomsten_totaal(inkomsten, btw):
    totaal =  sum(inkomsten)
    vbtw = (totaal * btw)
    return(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover een {vbtw} euro btw betaald dient te worden.")
print(inkomsten_totaal(inkomsten, 0.09))


mijn_lijst = [220,430,125,160,205,90,345]
def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return(hoogste,laagste)
print(laag_en_hoog(mijn_lijst))

inkomsten =  [220,430,125,160,205,90,345]
def gemiddelde(inkomsten):
    vgemiddelde = sum(inkomsten)/len(inkomsten)
    return(f"De gemiddelde inkomsten deze week zijn {vgemiddelde} euro")
print(gemiddelde(inkomsten))

invoerlijst = [10,5,3,1,2,9]
def meervoudig(mijn_lijst):
    return laag_en_hoog(mijn_lijst)
print(meervoudig(invoerlijst))

def combinatie(invoer_lijst_2):
    korte_lijst =  laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return korte_lijst




