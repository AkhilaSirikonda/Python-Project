# for loops iteration
# prints the names in the given list


names = ['Akhi', 'Jyo', 'Mana']
for i in names:
    print(i)

# prints the subject id in the given list
subjs_id = [6160, 5122, 6166, 8122]
for id in subjs_id:
    if id == 6160:
        print(f'subject id is {id}')
    elif id == 5122:
        print(f'subject id is {id}')
    elif id == 6166:
        print(f'subject id is {id}')
    else:
        print(f'subject id is {id}')

# prints the subject id in the given list in the same line separated by ,
subjs_id = [6160, 5122, 6166, 8122]
for i in subjs_id:
    if i == 8122:
        print(8122)
    else:
        print(i, end=',')

# same question but diff logic
# subj_len = len(subjs_id)
# print(len(subjs_id))
# counter = 0
# strOut = ''
# for id in subjs_id:
#     counter = counter + 1
#     strOut = strOut + str(id)
#     if subj_len != counter:
#         strOut = strOut + ','
# print(strOut)


# prints the univ UNCC index in the given list using break
univs = ['SDSU', 'UNCC', 'ASU', 'SJSU']
count = 0
for univ in univs:
    if univ == 'UNCC':
        count += 1
        print(f'{univ} is at index {count}')
        break
