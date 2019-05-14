def fib_func(n):
    if n<2:
        return n
    return fib_func(n-2) + fib_func(n-1)

func_list = [ fib_func(n) for n in range(10)]
print('func_list = ', func_list)
func_gen = (fib_func(n) for n in range(10))
print(('func_gen value = ', next(func_gen)))

for n in range(10):
    print('func_gen = ')