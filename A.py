#Q.1 Write a Python program that demonstrates the hill 
#climbing algorithm to find the maximum of a mathematical function 


def hill_climbing(f, x_start, step_size=0.1, precision=0.0001):
    x = x_start
    while True:
        x_next = x + step_size
        if f(x_next) > f(x):
            x = x_next
        else:
            break
    return x, f(x)

def f(x):
    return -x**2 + 4*x
x_start = 0
x_max, f_max = hill_climbing(f, x_start)

print("Maximum at x:", x_max)
print("Maximum value f(x):", f_max)





#Output:
#Maximum at x: 2.0
#Maximum value f(x): 4.0
