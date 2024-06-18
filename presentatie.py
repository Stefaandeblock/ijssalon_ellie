mijn_dict1 = {
        "vis" : 10,
        "vlees" : 25,
        "overig" : 15}
totaal = 50    

def presenteer(mijn_dict1,totaal):
    
    for k,v in mijn_dict1.items():
        print(f"{k} : {v} euro")
    print(f"==========================")
    return (f"Totaal: {totaal} euro") 
    
print(presenteer(mijn_dict1,totaal)) 
