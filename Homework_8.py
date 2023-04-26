a=[5,6,4,7,3,8,2,1,9,22,56,89,78]
b=[]
while True:
    abc = min (a)
    b.append(abc)
    a.remove(abc)
    if a == []:
        break
print(b)
Value=3
right = b.index(max(b))
left = b.index(min(b))
OK="on"
while OK=="on":
    if left<=right:
        center = (left+right) // 2
        if Value == b[center]:
            print(f"число {b[center]}")
            OK="OFF"
        else:
            if Value>b[center]:
                left = center+1
            else:
                right = center-1
    else:
        OK="OFF"
        print("Нет искаемого числа")

        
        



