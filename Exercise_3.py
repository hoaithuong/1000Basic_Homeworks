# Exercise 3: S(n) = 1+ 1/2 + 1/3 + ... + 1/n = ?
def exe3():
    s = 0.0
    n = int(input("Nhap n lon hon 0: "))
    if n < 0:
        return
    elif n==0:
        return s
    else:
        for i in range(1,n+1):
            s = s + 1/i
        return s

print("S(n)= " + str(exe3()))
