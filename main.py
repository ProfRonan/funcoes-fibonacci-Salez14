# action
def fibonacci(num):
    if num < 0 :
        raise ValueError("n tem que ser maior do que zero")
    if num == 0 :
        return 0
    n1 = 1
    n2 = 0
    count = 0 
    while count < num :
        nx = n1 + n2
        n1 = n2
        n2 = nx
        count +=1
    return nx
