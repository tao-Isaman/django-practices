
x = int(input("Enter number : "))
if x % 3 == 0 and x % 5 == 0 :
    print("FizzBuzz")
elif x % 3 == 0 :
    print("fizz")
elif x % 5 == 0 :
    print("buzz")
else : 
    print(x)

# if a is not None:
#     print("do something")
# if a :
#     print("do something")



def say():
    print("hello world")
say()

def say(number:int):
    print(f'hi {number}')
say(5)


