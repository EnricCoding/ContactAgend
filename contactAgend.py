

agenda = [  ]
class contacte(object):
    def __init__(self, nomContacte, edat, telefon, aficions): 
        self.nomContacte = nomContacte 
        self.edat = edat
        self.telefon = telefon
        self.aficions = aficions

def demantarEnter(edat):
    if edat.isnumeric():  
        return "number"
    else:
        return "text"

def nom_ja_existeix(nom):
    for i in agenda:
        if (i.nomContacte == nom):
            print('El nom ja existeix!')
            return "repetido"


def alta_contacte():

    nomContacte = str(input('Indica el nom del contacte: '))
    checkName = nom_ja_existeix(nomContacte)
    if checkName == "repetido":
        print('Ja existeix un usuari amb el seu nom de usuari')
        return

    edat = input('Indica la edat del contacte: ')
    checkEdat = demantarEnter(edat)
    if (checkEdat == "text"):
        while (checkEdat != "number"):
            edat = input('Indica la edat del contacte amb un valor numeric siusplau : ')
            checkEdat = demantarEnter(edat)    
        
    
    telefon = input('Indica el telefon del contacte:')
    checkTelefon = demantarEnter(telefon)
    if (checkTelefon == "text"):
        while (checkTelefon != "number"):
            telefon = input('Indica el telefon del contacte amb un valor numeric siusplau:')
            checkTelefon = demantarEnter(telefon)
    
    aficions = str(input('Indica las aficions del contacte: '))
    agenda.append(contacte(nomContacte, edat, telefon , aficions) ) 


    
def llistar_agenda():
    print('AQUEST SON ELS SEUS CONTACTES:')
    print('------------------------------')
    for i in agenda:
        print(i.nomContacte, i.edat, i.telefon, i.aficions)

def mostrar_aficions():
    print('------------------------------')
    print('Presioni 1 - Per obtenir aficions de la agenda ')
    print('Presioni 2 - Per llistar elements  ')
    print('Presioni 3 - Per sortir al menu principal ')
    opcioAficionats = int(input('Que opcio desitja escogir'))
    if opcioAficionats == 1:
        obtenir_aficions_agenda()

    elif opcioAficionats == 2:
        lista = [ ]
        tematica = input('De que tematica vols que sigue la llista? ')
        elementos = int(input('Cuantos elementos quieres añadir a la lista? '))
        for i in range(0, elementos):
            añadir = input('Que quieres añadir?')
            lista.append(añadir)
        
        llistar_elements(tematica, lista)
    elif opcioAficionats == 3:
        return
    else:
        return



def obtenir_aficions_agenda():
    print('Les aficions de la agenda')
    unicos = [ ]
    repetidos = [ ]
    for i in agenda:
        if i.aficions not in unicos:
            unicos.append(i.aficions)
        else:
            repetidos.append(i.aficions)
    print('Las aficions de la agenda', unicos)


def mostrar_aficionats():
    print('\n\nMOSTRAR AFICIONATS')
    print('Presioni 1 . Per demar una aficio en concret')
    print('Presioni 2 - Per buscar aficionats ')
    print('Presioni 3 - Per llistar elements ')
    print('Presioni 4 - Per sortir al menu principal ')

    print('---------------------------------------------')

    opcioAficionats = int(input('Que opcio desitja escogir'))
    if opcioAficionats == 1:
        
        if(len(agenda) >= 1):
            print('AFICIONS DISPONIBLES: ')
            for i in agenda:
                print(i.aficions)

            aficio = str(input('Que aficio vols buscar?'))
            demanar_aficio(aficio)
        else:
            print('No hi contactes per mostrar aficions...')
            return

    elif opcioAficionats == 2:
        nom = input('Com es diu el aficionat? ')
        buscar_aficionats(nom)

    elif opcioAficionats == 3:
        lista = [ ]
        tematica = input('De que tematica vols que sigue la llista? ')
        elementos = int(input('Cuantos elementos quieres añadir a la lista? '))
        for i in range(0, elementos):
            añadir = input('Que quieres añadir?')
            lista.append(añadir)
        
        llistar_elements(tematica, lista)
    elif opcioAficionats == 4:
        return
    else:
        return


def buscar_aficionats(nom):
    for i in agenda:
        if (i.nomContacte == nom):
            print('El usuari', i.nomContacte, 'te la aficio que has dit:',i.aficions)
        else:
            print('No existeix ningun usuari amb aquest nombre a la nostra agenda')

    

def demanar_aficio(aficio):
    for i in agenda:
        if i.aficions == aficio:
            print('------------------------------')
            print('El usuari', i.nomContacte, 'te la aficio que has dit:',i.aficions)
        else:
            print('La aficio que has seleccionat no existeix')



def llistar_elements(tematica, lista):
    print('-----------------')
    print('LLISTAR ELEMENTS')
    contador = 0
    for i in lista:
        contador = contador + 1  
        print( tematica , contador ,': '+ i)    

opcio = '0'
#agenda = [
# {'nom': 'Pepe', 'edat': 140, 'tel': 999345, 'aficions': ['música', 'esport']},
# {'nom': 'Joanjo', 'edat': 15, 'tel': 456, 'aficions': []},
# {'nom': 'Pere', 'edat': 16, 'tel': 34567, 'aficions': ['llegir']},
# {'nom': 'Emili', 'edat': 16, 'tel': 34567, 'aficions': []},
# {'nom': 'Pau', 'edat': 26, 'tel': 987674, 'aficions': ['llegir', 'reflexionar',
#'nedar']}
#]

while opcio != '':
    print('\n\nGESTIÓ DE LA AGENDA')
    print('-------------------')
    print('1: Alta de contacte')
    print('2: Llistar tota l\'agenda')
    print('3: Llistar totes les aficions que apareixen a l\'agenda')
    print('4: Llistar aficionats a una afició')
    print('ENTER: Sortir')
    opcio = input('\nEscollir opció:')
    if opcio == '1':
    # Alta contacte
        alta_contacte()
    elif opcio == '2':
    # Llistar agenda
        llistar_agenda()
    elif opcio == '3':
    # Mostrar les aficions que hi ha a l'agenda
        mostrar_aficions()
    elif opcio == '4':
    # Mostrar els noms dels aficionats a una afició
        mostrar_aficionats()
    elif opcio != '':
        input('Opció desconeguda\n... ENTER per continuar')
    else:
        print('Gràcies per utilitzar aquest programa. Adéu.')
        break


