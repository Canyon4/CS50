camel = input('give string: ')
lis = []
a = 0
for i in camel:
    if camel[a] == camel[a].upper():
        lis.append(a)
    a = a + 1
b = lis[0]
camel = camel.lower()
if len(lis) > 1:
    c = lis[1]
    print(camel[:b] + '_' + camel[b:c] + '_' + camel[c:])
print(camel[:b] + '_' + camel[b:])
