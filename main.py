# # createCandidate: sukurti ir prideti i sarasa
# # updateCandidate: updated duomenims
# # deleteCandidate: istrinti
# # vinCandidate: laimejo
#
#
# candidates = []
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
# from operator import index
#




candidates = [
    ['Valentinas', 'Bukauskas', 20166, 808],
    ['Agnė', 'JAKAVIČIUTĖ-MILIAUSKIENĖ', 1965, 507],

  ]
def printInfo():
    print('_______________________________________________')
    print('1. kandidatai')
    print("2. add")
    print("3. Atnaujinti balsų skaičių")
    print("4. delete")
    print("5. filter out left ones")
    # print('2. surintki balsai spalio 13')
    # print('3. surinkti balsai po antro turo')
    # print('4. maziau surinkes balsu')
    # print('5. isrinktas kandidatas sekanciai kadencijai')
    print('_______________________________________________')

def printCandidate(vienasKandidatas, index = 1):
    print(f'{index}. {vienasKandidatas[0]} {vienasKandidatas[1]}, {vienasKandidatas[2]} {vienasKandidatas[3]}')

def printCandidates():
    index = 1
    for vienasKandidatas in candidates:
        printCandidate(vienasKandidatas, index)
        index +=1

def addCandidate():
    print('Kandidato Vardas:')
    firstName = input()
    print('Kandidato Pavarde:')
    lastName = input()
    print('kiek kandidatas surinko balsu spalio 13 d.?')
    surinktiBalsai = input()
    candidates.append([firstName,lastName,surinktiBalsai,0])
    # print(f'Kandidatas {firstName} {lastName}, {surinktiBalsai} ')

def updateCandidate( firstName=None, lastName=None, surinktiBalsai=None):
    # print('Kandidato Vardas:')
    # firstName = input()
    # print('Kandidato Pavarde:')
    # lastName = input()
    print('Paduokite numeriuką politiko kurio balsai buvo suskaiciuoti')
    politikas = int(input())
    print(f'kiek kandidatas {candidates[politikas -1][0]} {candidates[politikas -1][1]} surinko balsu antrame ture?')
    surinktiBalsai = input()
    candidates[politikas -1][3] = surinktiBalsai
    print(f'Kandidatas {candidates[politikas -1][0]} {candidates[politikas -1][1]}3, antrame ture surinko {surinktiBalsai} balsu ir laimejo rinkimus.')

def deleteCandidate(firstName=None, lastName=None, surinktiBalsai=None):
    print('kuris kandidatas surinko maziau balsu?')
    delete = int(input())
    candidates.pop(delete - 1)

print('2024 LR Seimo rinkimai. Telšių (Nr.40) apygarda')


# def removeTheLoosers():
#     lst = sorted(candidates, key=lambda x: x[2], reverse=True)
#     return lst[:2]

def removeTheLoosers():
    lst = sorted(candidates, key=lambda x: x[2], reverse=True)
    return lst[:2]
topCandidates = removeTheLoosers()

print('Kandidatai su didžiausiu balsų skaičiumi:')
for candidate in topCandidates:
    print(f"{candidate[0]} {candidate[1]}: {candidate[2]} balsai")



while True:
    printInfo()
    opt = int(input())
    match opt:
        case 1:
            printCandidates()
        case 2:
            addCandidate()
            printCandidates()
        case 3:
            updateCandidate()
            printCandidates()
        case 4:
            deleteCandidate()
            printCandidates()
        case 5:
            candidates = removeTheLoosers()
        case 6:
            exit(1)


