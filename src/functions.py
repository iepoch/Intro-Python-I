# Write a function is_even that will return true if the passed-in number is even.
def is_even(num):
    if num > 0:
        print("Odd")
    else:
        print("Even!")


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num) % 2
is_even(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"
# if num  > 0:
#     print("Odd")
# else:
#     print("Even!")


def double(n):
    return n * 2


my_int = 10
double(my_int)

# if pass by reference  my int = 20(changed)
#if (pass by VALUE  my int - 10(we modified a copy)
print(my_int)