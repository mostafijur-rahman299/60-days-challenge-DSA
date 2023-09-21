tokens = ["4","13","5","/","+"]

stack = []

for item in tokens:
    if item in ["+", "-", "*", "/"]:
        st2 = stack.pop()
        st1 = stack.pop()
        
        if item == "+":
            st3 = int(st1) + int(st2)
        if item == "*":
            st3 = int(st1) * int(st2)
        if item == "-":
            st3 = int(st1) - int(st2)
        if item == "/":
            st3 = int(st1) / int(st2))
            
        stack.append(st3)
        
    else:
        stack.append(item)

print(stack)
