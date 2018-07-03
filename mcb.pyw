#! python3
#mcb.pyw - saves and loads pieces of text to the clipboard
#usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword
#       py.exe mcb.pyw <keyword> - loads keyword to clipboard
#       py.exe mcb.pyw list - loads all keywords to clipboard
#---------------------------------------------------------------------------------------------------
#project - extend the multiclipboard program so that it has a delete <keyword> command line argument
#that will delete a keyword from the shelf
#then add a delete command line argument that will delete all keywords

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
#delete keyword
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf:
        mcbShelf.pop(sys.argv[2])
#delete all keywords
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delall':
    for i in list(mcbShelf.keys()):
        del mcbShelf[i]
#list keywords and load content
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
