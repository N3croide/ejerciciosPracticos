for f in range(100, 1000):
    c = (f - (f % 100)) // 100
    r = f % 100
    c1 = (r - (r % 10)) // 10
    r1 = r % 10

    if f == ((r1 * 100) + (c1 * 10) + c):
        print(f, end=" ")
        
print()
