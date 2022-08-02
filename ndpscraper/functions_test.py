
def clear_lists(*lists: list):
    for i in lists:
        i.clear()

l = [1,2,3,4,5]
k = ['a', 'b', 'c']
m = ['j', 342,123421,1324,1312,34,234,234,23423,4,234]
print("l and k before clearing ", l, k,m)
clear_lists(l, k,m)
print("l and k after clearing ", l, k, m)
k= {}
k["ok"] = 1
print(k)