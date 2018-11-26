

# example using nested functions
print('\n--- Using nested functions ---')
def add_dollar(n):
    def sign():
        resp = '$' + str(n)
        return resp
    return sign


def cost(x, y):
    return x + y


p = add_dollar(cost(10, 50))()
print(p)


# Same example using decorator
print('\n--- Using simple decorator ---')
def add_sign(func):
    def sign2(*args):
        resp2 = func(*args)
        add_signed = '$' + str(resp2)
        return add_signed
    return sign2


@add_sign
def cost2(x, y):
    return x * y


print(cost2(4, 20))
print()


# Example like flask...
print('--- FLASK LIKE EXAMPLE ---')
def tags(tag_name):
    print("1) via 'def tags': This will be from - @tags('/app'): {0:.>23}".format(tag_name))
    def tags_deco(func):
        print("2) via 'def tags_deco(func)': This will be the function - get_text(name):.......{}".format(func))
        def func_wrapper(n_name):
            print("3) via 'func_wrapper(n_name)': This will be the name variable 'chet.com': {0:.>10}".format(n_name))
            print("   'www' will be prefixed to 'chet.com' from the get_text(name) function")
            print("   note: you could use *args in place of n_name")
            return "http://{0}{1}/".format(func(n_name), tag_name)
        return func_wrapper
    return tags_deco


@tags('/app')
def get_text(name):
    return 'www.' + name


output = get_text('chet.com')
print('\n4) Output: {}'.format(output))
