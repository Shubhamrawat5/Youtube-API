f = open("subs.txt", 'r', encoding='utf-8')
w = open("subs_list.txt", 'w', encoding='utf-8')
print(f)

content = f.read()
print(content)

list = content.split(">")
print(list)

for i in list:
    print(i)
    if "xmlUrl" in i:
        pass
    else:
        # index = list.index(i)
        print("--Removing--")
        list.remove(i)

list.remove('\n<body')
list.remove('</body')
print(list)
print(len(list))

perfect_list = [] # containing 1st place for name, 2nd place for id

for i in range(851-1):
    print(i)
    str = list[i]
    # print(str)
    str = str.replace("="," ")
    # print(str)
    l2 = str.split(" ")
    #print(l2)

    perfect_list.append(l2[2][1:-1])
    perfect_list.append(l2[-2][:-1])
    print(perfect_list)

print(len(perfect_list))
list_string = " ".join(perfect_list)
w.write(list_string)
f.close()
w.close()