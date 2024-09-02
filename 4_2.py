
def test_function():
    print('Я в области видимости test_function')
    def inner_function():
        print(9956)
    inner_function()

test_function()

