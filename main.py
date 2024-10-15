# # createCandidate: sukurti ir prideti i sarasa
# # updateCandidate: updated duomenims
# # deleteCandidate: istrinti
# # vinCandidate: laimejo
#
#
# candidates = []
#
#
# def createCandidate(firstName, lastName, balsaiApylinkese, balsaiPastu):
#     candidate = {
#         'firstName': firstName,
#         'lastName': lastName,
#         'balsaiApylinkese': balsaiApylinkese,
#         'balsaiPastu': balsaiPastu
#     }
#     candidates.append(candidate)
#     print(f'Kandidatas {firstName} {lastName} ')
#
#
# def readCandidates():
#     if not candidates:
#         print('Nera kandidatu sarase.')
#     else:
#         for index, candidate in enumerate(candidates, start=1):
#             print(f'{index}. Kandidatas: {candidate['firstName']} {candidate['lastName']}, '
#                   f'Surinkti balsai apylinkese: {candidate['balsaiApylinkese']}, '
#                   f'Surinkti balsai pastu: {candidate['balsaiPastu']}')
#
#
# def updateCandidate(index, firstName=None, lastName=None, balsaiApylinkese=None, balsaiPastu=None):
#     if 0 <= index < len(candidates):
#         if firstName:
#             candidates[index]['firstName'] = firstName
#         if lastName:
#             candidates[index]['lastName'] = lastName
#         if balsaiApylinkese is not None:
#             candidates[index]['balsaiApylinkese'] = balsaiApylinkese
#         if balsaiPastu is not None:
#             candidates[index]['balsaiPastu'] = balsaiPastu
#         print(f'Kandidato {index+1} duomenys atnaujinti.')
#     else:
#         print('informacija klaidinga.')
#
#
# def deleteCandidate(index):
#     if 0 <= index < len(candidates):
#         removedCandidate = candidates.pop(index)
#         print(f'Kandidatas {removedCandidate['firstName']} {removedCandidate['lastName']} pasalintas.')
#
# def vinCandidate(index):
#     if 0 <= index < len(candidates):
#         vinCandidate = candidates(index)
#         print(f'Kandidatas {vinCandidate['firstName']} {vinCandidate['lastName']} laimejo 2024 rinkimus.')
#
# createCandidate( 'Valentinas', 'Bukauskas', 2016, 808)
# createCandidate('Agnė', 'JAKAVIČIUTĖ-MILIAUSKIENĖ', 1965, 507)
#
# print('Esami kandidatai:')
# readCandidates()
#
# print('Atnaujiname Valentino Bukausko balsus:')
# updateCandidate(0, balsaiApylinkese=500000, balsaiPastu=100000)
# readCandidates()
#
# print('Pasaliname kandidatą:')
# deleteCandidate(1)
# readCandidates()
#
# print('2024 m. Rinkimus laimejo:')
# vinCandidate(1)
# readCandidates()
from operator import index

# def createCandidate(firstName, lastName, surinktiBalsai):
#     candidate = {
#         'firstName': firstName,
#         'lastName': lastName,
#         'surinktiBalsai': surinktiBalsai,
#     }
#     candidates.append(candidate)
#     print(f'Kandidatas {firstName} {lastName} ')



candidates = [{'Valentinas', 'Bukauskas', 2016, 808},
              {'Agnė', 'JAKAVIČIUTĖ-MILIAUSKIENĖ', 1965, 507}
              ]
def printInfo():
    print('_______________________________________________')
    print('1. sarasas 2. ideti 3. update 4. delete 5. end')
    print('1. kandidatai')
    print('2. surintki balsai spalio 13')
    print('3. surinkti balsai po antro turo')
    print('4. maziau surinkes balsu')
    print('5. isrinktas kandidatas sekanciai kadencijai')
    print('_______________________________________________')

def printCandidate(firstName, lastName, surinktiBalsai, index = 1):
    print(f'{index}. {firstName} {lastName}, {surinktiBalsai}')

def printCandidates():
    index = 1
    for index in candidates:
        printCandidate(index)
        index +=1

def addCandidates():
    print('Kandidato Vardas:')
    firstName = input()
    print('Kandidato Pavarde:')
    lastName = input()
    print('kiek kandidatas surinko balsu spalio 13 d.?')
    surinktiBalsai = input()

    print(f'Kandidatas {firstName} {lastName}, {surinktiBalsai} ')

def updateCandidate( firstName=None, lastName=None, surinktiBalsai=None):
    print('Kandidato Vardas:')
    firstName = input()
    print('Kandidato Pavarde:')
    lastName = input()
    print('kiek kandidatas surinko balsu antrame ture?')
    surinktiBalsai = input()
    print(f'Kandidatas {firstName} {lastName}, antrame ture surinko {surinktiBalsai} balsu ir laimejo rinkimus.')

def deleteCandidate(firstName=None, lastName=None, surinktiBalsai=None):
    print('kuris kandidatas surinko maziau balsu?')
    delete = int(input())
    candidates.pop(delete - 1)

print('2024 LR Seimo rinkimai. Telšių (Nr.40) apygarda')

while True:
    printInfo()
    opt = input()
    match opt:
        case 1:
            printCandidate()
        case 2:
            addCandidates()
            printCandidates()
        case 3:
            updateCandidate()
            printCandidates()
        case 4:
            deleteCandidate()
            printCandidates()
        case 5:
            exit(1)


