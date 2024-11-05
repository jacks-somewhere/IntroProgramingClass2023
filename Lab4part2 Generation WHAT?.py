
# Lab 4
# Generation WHAT?

#Variables
#Based on the year people where born
GEN_ALPHA = 2012 #After 2012
GEN_Z = 1997
MILLENNIALS = 1981
GEN_X = 1965
BOOMERS = 1946
WAR_POSTWAR = 1922
SILENT_GEN = 1922 #Before 1922

# Gets user to input the year that they were born
birth_year = int(input('In what year were you born? '))

# Locates the generation that they are from 
if birth_year >= GEN_ALPHA:
    name = 'Gen Alpha'
else:
    if birth_year >= 1997:
        name = 'Gen Z'
    else:
        if birth_year >= 1981:
            name = 'Millennial'
        else:
            if birth_year >= 1965:
                name = 'Gen X'
            else:
                if birth_year >= 1946:
                    name = 'Boomers'
                else:
                    if birth_year >= 1922:
                        name = 'War / Post-War'
                    else:
                        if birth_year < 1922:
                            name = 'Silent'

# Shows user the generation that they where born in
print(f'You are part of the {name} Generation')
