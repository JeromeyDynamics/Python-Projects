#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

print("Lists:")
us_presidents_list = ['Joe Biden', 'Donald Trump', 'Barack Obama',
                      'Barack Obama', 'George W. Bush', 'George W. Bush']
for president in us_presidents_list:
    print(president)
    
print("---------------------------------------")

print(us_presidents_list[1])

print("---------------------------------------")

us_presidents_list.append('Bill Clinton')
print(us_presidents_list)

print("---------------------------------------")

us_presidents_list.remove('Bill Clinton')
print(us_presidents_list)

print("---------------------------------------")

us_presidents_list[4] = 'George Bush'
print(us_presidents_list)

print("Tuples:")

us_president_tuple = ('Joe', 'Biden', '2021-01-20', 'Democratic')
for i in us_president_tuple:
    print(i)

print("---------------------------------------")

print(us_president_tuple[2])

print("---------------------------------------")

print(us_president_tuple[0], ' ', us_president_tuple[1])

print("Sets:")

us_presidents_set = {'Bill Clinton', 'Joe Biden',
                     'Donald Trump', 'Barack Obama', 'George W. Bush'}
for president in us_presidents_set:
    print(president)

print("---------------------------------------")

reagan = False
for president in us_presidents_set:
    if president == 'Ronald Reagan':
        reagan = True
print(reagan)

print("---------------------------------------")

us_presidents_set.add('George H. W. Bush')
print(us_presidents_set)

print("---------------------------------------")

us_presidents_set.remove('Bill Clinton')
print(us_presidents_set)