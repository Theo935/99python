#!/usr/local/bin/python3.5
i=0
while i <= 9:
    j = 1
    while j <= i:
        print(str(i) + "*" + str(j) +  "=" +  str(i*j),end=" ")
        j+=1
    print()
    i+=1
print() #我在干这活，这回干完了
