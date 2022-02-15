
def merge_sorted(a,b):
    c = []
    i = 0
    j = 0


    while i < len(a) or j < len(b):
        if i >= len(a):
            for num in b:
                c.append(num)
            break
        if j >= len(b):
            for num in a:
                c.append(num)
            break
        else:
            if a[i] < b[j]:
                c.append(a[i])
                a.remove(a[j])
            elif a[i] > b[j]:
                c.append(b[j])
                b.remove(b[j])
            elif a[i] == b[j]:
                c.append(a[i])
                c.append(b[j])
                a.remove(a[i])
                b.remove(b[i])





    return c



print(merge_sorted([1,3,5,6,10], [1,4,6,8]))




