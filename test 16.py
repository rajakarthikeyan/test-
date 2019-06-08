def reverse(s):
    str=" "
    for i in s:
        str=i+str
    return str
s="raja for raja"
print("the originalstring is:",end=" ")
print(s)
print("the reversed string(using recursion) is:",end=" ")
print(reverse(s))
