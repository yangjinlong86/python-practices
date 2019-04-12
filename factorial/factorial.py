
def factorial(n):
    if n == 1: # base case
        return n;
    else: # recursive call
        return n * factorial(n -1)

if __name__ == '__main__':
    print(factorial(5))