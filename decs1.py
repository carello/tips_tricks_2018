

# example using nested functions
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
def add_sign(n):
    def sign2(*args):
        resp2 = n(*args)
        add_signed = '$' + str(resp2)
        return add_signed
    return sign2


@add_sign
def cost2(x, y):
    return x * y


print(cost2(4, 20))

print()
# Example like flask...
def tags(tag_name):
    print("1) Under def tags -  This will be from @tags('/app'): {}'".format(tag_name))
    def tags_deco(func):
        print("2) Under tags_deco(func) - This will be the function get_text: {}".format(func))
        def func_wrapper(n_name):
            print("3) Under func_wrapper(n_name) - This will be the name variable' chet.com': {}".format(n_name))
            print("   www will be added to chet.com from the get_text(name) function")
            return "http://{0}{1}".format(func(n_name), tag_name)
        return func_wrapper
    return tags_deco


@tags('/app')
def get_text(name):
    return 'www.' + name


print(get_text('chet.com'))
