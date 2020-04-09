v = """
Section.notes.txt
Pja 10-25-2019


T sections((Section-number))
T peerGroup((Section-number,optionID))
T option((optionID) text)

Sections --0< peerGroup >0-- option

Assembly is gathering all options in peerGroup into section by number

All options.text are final strings (completed templates)
"""
print(v)
