# Using rasie keyword..
a = 10;
b = 9;

try: 
    if a < 0 or b  < 0:
        raise ZeroDivisionError
    print(a/b);
except ZeroDivisionError:
    print('please enter the value:');