# createCandidate: sukurti ir prideti i sarasa
# updateCandidate: updated duomenims
# deleteCandidate: istrinti
# vinCandidate: laimejo


candidates = []


def createCandidate(firstName, lastName, balsaiApylinkese, balsaiPastu):
    candidate = {
        'firstName': firstName,
        'lastName': lastName,
        'balsaiApylinkese': balsaiApylinkese,
        'balsaiPastu': balsaiPastu
    }
    candidates.append(candidate)
    print(f'Kandidatas {firstName} {lastName} ')


def readCandidates():
    if not candidates:
        print('Nera kandidatu sarase.')
    else:
        for index, candidate in enumerate(candidates, start=1):
            print(f'{index}. Kandidatas: {candidate['firstName']} {candidate['lastName']}, '
                  f'Surinkti balsai apylinkese: {candidate['balsaiApylinkese']}, '
                  f'Surinkti balsai pastu: {candidate['balsaiPastu']}')


def updateCandidate(index, firstName=None, lastName=None, balsaiApylinkese=None, balsaiPastu=None):
    if 0 <= index < len(candidates):
        if firstName:
            candidates[index]['firstName'] = firstName
        if lastName:
            candidates[index]['lastName'] = lastName
        if balsaiApylinkese is not None:
            candidates[index]['balsaiApylinkese'] = balsaiApylinkese
        if balsaiPastu is not None:
            candidates[index]['balsaiPastu'] = balsaiPastu
        print(f'Kandidato {index+1} duomenys atnaujinti.')
    else:
        print('informacija klaidinga.')


def deleteCandidate(index):
    if 0 <= index < len(candidates):
        removedCandidate = candidates.pop(index)
        print(f'Kandidatas {removedCandidate['firstName']} {removedCandidate['lastName']} pasalintas.')

def vinCandidate(index):
    if 0 <= index < len(candidates):
        vinCandidate = candidates(index)
        print(f'Kandidatas {vinCandidate['firstName']} {vinCandidate['lastName']} laimejo 2024 rinkimus.')

createCandidate( 'Valentinas', 'Bukauskas', 2016, 808)
createCandidate('Agnė', 'JAKAVIČIUTĖ-MILIAUSKIENĖ', 1965, 507)


print('Esami kandidatai:')
readCandidates()

print('Atnaujiname Valentino Bukausko balsus:')
updateCandidate(0, balsaiApylinkese=500000, balsaiPastu=100000)
readCandidates()



print('Pasaliname kandidatą:')
deleteCandidate(1)
readCandidates()

print('2024 m. Rinkimus laimejo:')
vinCandidate(1)
readCandidates()

