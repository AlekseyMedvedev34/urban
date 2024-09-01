
def test_function():
    print('Я в области видимости test_function')
    def inner_function():
        print()

test_function()
inner_function()


# inner_function()

