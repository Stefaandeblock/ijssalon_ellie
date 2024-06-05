from algemene_functie import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
       
    vsmaak = smaak
    vprijs= prijs
    vkorting= (prijs - (prijs * korting))
    return(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {vsmaak}, van {vprijs} euro voor {vkorting} euro") 
print(aanbieding_1("aardbei",4,0.1))



inkomsten = [220,430,125,160,205,90,345]
def inkomsten_totaal(inkomsten,btw):
    totaal = 0
    for i in inkomsten:
        totaal = totaal + i
        btwbedrag = (totaal * btw)
    return(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btwbedrag} euro btw betaald dient te worden.")
print(inkomsten_totaal(inkomsten,0.09))


mijn_lijst = [220,430,125,160,205,90,345]
def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return hoogste , laagste
print(laag_en_hoog(mijn_lijst))

mijn_lijst = [220,430,125,160,205,90,345]
def gemiddelde(mijn_lijst):
    som = 0
    gemiddelde = 0
    for i in mijn_lijst:
        som = som + i
    gemiddelde = som / len(mijn_lijst)
    return(f"de gemiddelde inkomsten deze week zijn {gemiddelde} euro.")
print(gemiddelde(mijn_lijst))

invoer_lijst = [10,5,3,2,1,2,9]
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
print(meervoudig(invoer_lijst))


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer

