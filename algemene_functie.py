def mijn_functie_1(a):
    teruggeefwaarde = 0
    teruggeefwaarde =  a ** 2
    return teruggeefwaarde
print(mijn_functie_1(4))

def mijn_functie_2(b,c):
    teruggeefwaarde1 = 0
    teruggeefwaarde2 = 0
    teruggeefwaarde3 = 0
    teruggeefwaarde4 = 0

    teruggeefwaarde1 = b + c 
    teruggeefwaarde2 = b - c 
    teruggeefwaarde3 = b * c 
    teruggeefwaarde4 = b / c 
    return [teruggeefwaarde1,teruggeefwaarde2,teruggeefwaarde3,teruggeefwaarde4]
print(mijn_functie_2(12,3))
