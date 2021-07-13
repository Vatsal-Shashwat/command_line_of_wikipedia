
import os
from colorama import Fore, Back, Style
import webbrowser
import wikipedia
import datetime
from sys import exit

print(Back.GREEN + 'this is simple software')
print(Fore.RED + '[*] All results available ')
print(Fore.RED + '[*] Search Engine - Wikipedia')

def wiki_summary():
    ask = input('what do you want to search: ')
    if ask == 'exit':
        sys.exit()
    result = wikipedia.summary(ask)
    print(f'[*] Result found!! \n {result}')

def wiki_summary_hi():
    ask = input('what do you want to search: ')
    if ask == 'exit':
        sys.exit()
    wikipedia.set_lang('hi')
    result = wikipedia.summary(ask)
    print(result)

def wiki_page():
    ask = input('what do you want to search: ')
    if ask == 'exit':
        sys.exit()
    page_obj = wikipedia.page(ask)
    print(page_obj.html)
    print(page_object.original_title)
    print(page_object.links[0:10])

def browser():
    ask = input('what do you want to search: ')
    webbrowser.open(ask)

while(True):
    print('enter exit for exit')
    try:

        print('[1] wikipedia')
        print('[2] browser')
        choice = str(input('what do you want to do: '))
        if choice == '1':
            os.system('clear')
            print('[1] Wikipedia summary')
            print('[2] Wikipedia Summary in hindi')
            print('[3] Wikipedia page')
            usr_ans = input('what do you want to do: ')
            if usr_ans == '1':
                wiki_summary()
            elif usr_ans == '2':
                wiki_summary_hi()
            elif usr_ans == '3':
                wiki_page()
            else:
                break
        elif choice == '2':
            browser()
        else:
            break
    except Exception as err:
        print(err)
