def my_decorator(func):
    def decorator():
        print('----------------------');
    func();
    print('_____________________');
    return decorator;

def text():
    print('welcome to the python class for ever.');

call_function = my_decorator(text);

call_function()
