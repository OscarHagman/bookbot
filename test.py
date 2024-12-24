dic = {}
foo = "foo"
try:
    dic[foo] = dic[foo] + 1
except KeyError:
    dic[foo] = 0

print(dic)