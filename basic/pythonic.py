# Idiomatic Python code

# 1. Avoid comparing directly to `True`, `False`, or `None`
a = True
if a is True:
    print('a is True')

# Do is instance
if a:
    print('a is True')

# 2. Avoid repeating variable name in compound if statement
a = 1
if a == 1 or a == 2 or a == 3 or a == 4:
    print('a: ', a)

# Do is instance
if a in [1, 2, 3, 4]:
    print('a: ', a)

# 3. 3. Use `in` to iterate over iterable

l = [1, 2, 3, 4]
for item in l:
    print(item)

# 4. Use default parameter of `dict.get`

a = {
    'name': 'tao'
}
if 'name' in a:
    print(a['name'])

# Do is instance
print(a.get('name', None))

# 5. Use `enumerate` function in loops

count = 1
names = ['kan', 'tao', 'atb', 'teema', 'top', 'BB']
for name in names:
    print(f'{count}. {name}')
    count += 1

# Do is instance
names = ['kan', 'tao', 'atb', 'teema', 'top', 'BB']
for index, name in enumerate(names):
    print(f'{index + 1}. {name}')


# 6. Use `_` for data that should be ignored
names = ['kan', 'tao', 'atb', 'teema', 'top', 'BB']
for _, name in enumerate(names):
    print(f'{name}')

# 7. Use (for) `else` after iterator is exhausted!
check = False
for name in names:
    if name != 'Air':
        check = True
        break
if not check:
    print('Yes')

# Do is instance
for name in names:
    pass
    # do something
else:
    print('Air is not hear')

# 8. List comprehension to create a transformed list

names = []
for i in range(10):
    names.append(i)

# Do is instance
name = [i for i in range(10)]

# 9. Use context manager to ensure resources are managed

# f = open('test.txt')
# f.close()

# # Do is instance
# with open('test.txt') as f:
#     pass

# 10. Use generator to lazily load infinite sequences


def fibo(number):
    current_value, next_value = 0, 1
    for _ in range(number):
        print(current_value)
        current_value, next_value = next_value, current_value + next_value

# fibo(10)


def fibo(number):
    current_value, next_value = 0, 1
    for _ in range(number):
        yield current_value
        current_value, next_value = next_value, current_value + next_value


gen = fibo(10)
print(list(gen))
