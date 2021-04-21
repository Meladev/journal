import sys


def info():
    f = open('what_to_do.txt', 'a')
    f.write('\nthis is a E-diary in which you can write whatever you want.
\n\nNobody can read what you are writing, so feel free to write whatever you please:)'
            '\n\nTo skip a question, press ENTER'
            '\n\nI hope you are ok, enjoy!\n')


info()


def show_info():
    aiuto = input('type "help" if you are confused, press ENTER if you know what to do')
    if aiuto in 'help':
        with open('what_to_do.txt', 'r') as f:
            f.seek(1)
            halp = f.read(225 - 1)
            print(halp)


def idk():
    show_info()
    date = input("what's the date today?... ")
    with open('diary.txt', 'a') as f:
        f.write(date + ' - ')
        feelings = input('how are you?(honestly)... ')
        f.write(feelings + '\n')


idk()


def altro():
    more = input("I'm all ears :)... ")
    with open('diario.txt', 'a') as f:
        f.write('same day' + ' - ')
        f.write(more + '\n')
    diario = input("take a look at how you've been?(Y/N)... ")
    while diario not in ('y', 'n', 'Y', 'N'):
        diario = input('can you repeat that?... ')
    if diario in ('n', 'N'):
        print('ok, still love you :)')
        sys.exit()
    elif diario in ('y', 'Y'):
        with open('diary.txt', 'r') as f:
            f_contents = f.read()
            print('\n' + f_contents)
    succo = input('anything else i can do for you?(Y/N)...')
    while succo not in ('Y', 'N', 'y', 'n'):
        succo = input('can you repeat that?... ')
    if succo in ('y', 'Y'):
        altro()
    elif succo in 'no':
        print('ok, still love you :)')
        sys.exit()


def test():
    diario = input('vuoi vedere come sei stata in passato?(si/no) ')
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
