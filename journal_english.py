import sys


def info():
    f = open('what_to_do.txt', 'a')
    f.write('\nthis is a E-diary in which you can write whatever you want.
'\n\nNobody can read what you are writing, so feel free to write whatever you please:)'
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
    with open('diary.txt', 'a') as f:
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
    succo = input('anything else i can do for you?(Y/N)... ')
    while succo not in ('Y', 'N', 'y', 'n'):
        succo = input('can you repeat that?... ')
    if succo in ('y', 'Y'):
        altro()
    elif succo in ('n', 'N'):
        print('ok, still love you :)')
        sys.exit()


def test():
    diario = input("want to see how you've been in the past?(Y/N)... ")
    while diario not in ('y', 'n', 'Y', 'N'):
        diario = input('can you repeat that?... ')
    if diario in ('n', 'N'):
        print('ok, still love you:)')
        sys.exit()
    elif diario in ('y', 'Y'):
        with open('diary.txt', 'r') as f:
            f_contents = f.read()
            print('\n' + f_contents)
    succo = input('nything else i can do for you?(Y/N)... ')
    while succo not in ('y', 'n', 'Y', 'N'):
        succo = input('can you repeat that?... ')
    if succo in ('y', 'Y'):
        altro()
    elif succo in ('n', 'N'):
        print('ok, still love you:)')
        sys.exit()


test()
