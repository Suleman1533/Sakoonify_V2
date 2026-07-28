def add(*args):
    for i in args:
        print(i)
    return sum(args)

print(add(1,2,3,4))
print("==================================================================================================================")

lst = [("suleman", 23), ("Rayan", 21), ("Saifullah" , 22)]

sorted_list = sorted(lst, key = lambda lst : lst[1])

print(sorted_list)
print(lst)