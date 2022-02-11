def is_triangle_exists(a, b, c):


    is_exists = (a + b > c) and (a+c>b) and (b+c>a)
    return is_exists

print(is_triangle_exists(10, 12, 21))    
