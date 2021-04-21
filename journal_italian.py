import sys


def info():
    f = open('che_faccio.txt', 'a')
    f.write('\nQuesto è un diario dove puoi scrivere ciò che vuoi.\n\nNessuno legge ciò che scrivi quindi sentiti '
            'libero/a di rispondere sinceramente :).\n\nPremi INVIO '
            'per saltare domanda/passare alla prossima.\n\nSpero tu stia bene, divertiti :)\n')


info()


def show_info():
    aiuto = input('scrivi "aiuto" se serve aiuto o premi INVIO se sai cosa fare... ')
    if aiuto in 'aiuto':
        with open('che_faccio.txt', 'r') as f:
            f.seek(1)
            halp = f.read(225 - 1)
            print(halp)


def idk():
    show_info()
    date = input('che giorno è oggi?... ')
    with open('diario.txt', 'a') as f:
        f.write(date + ' - ')
        feelings = input('come stai?(sinceramente)... ')
        f.write(feelings + '\n')


idk()


def altro():
    more = input('dimmi tutto :)... ')
    with open('diario.txt', 'a') as f:
        f.write('stesso giorno' + ' - ')
        f.write(more + '\n')
    diario = input('vuoi vedere come sei stato/a in passato?(si/no)... ')
    while diario not in ('si', 'no'):
        diario = input('come prego?... ')
    if diario in 'no':
        print('ok, still love you :)')
        sys.exit()
    elif diario in 'si':
        with open('diario.txt', 'r') as f:
            f_contents = f.read()
            print('\n' + f_contents)
    succo = input('posso fare altro per te?(si/no)...')
    while succo not in ('si', 'no'):
        succo = input('come prego?... ')
    if succo in 'si':
        altro()
    elif succo in 'no':
        print('ok, still love you :)')
        sys.exit()


def test():
    diario = input('vuoi vedere come sei stato/a in passato?(si/no) ')
    while diario not in ('si', 'no'):
        diario = input('come prego? ')
    if diario in 'no':
        print('ok, still love you:)')
        sys.exit()
    elif diario in 'si':
        with open('diario.txt', 'r') as f:
            f_contents = f.read()
            print('\n' + f_contents)
    succo = input('posso fare altro per te?(si/no)')
    while succo not in ('si', 'no'):
        succo = input('come prego? ')
    if succo in 'si':
        altro()
    elif succo in 'no':
        print('ok, still love you:)')
        sys.exit()


test()
