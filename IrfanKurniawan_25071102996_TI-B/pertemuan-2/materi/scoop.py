#lingkup lokal
def myfunc():
  x = 300
  print(x)

myfunc()

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)
    
print(factorial(5))