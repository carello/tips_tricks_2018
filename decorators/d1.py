
def display_arguments(func):
    def display_and_call(*args, **kwargs):
        args = list(args)
        print('must-have arguments are:')
        for i in args:
            print(i)
        print('optional arguments are:')
        for kw in kwargs.keys():
            print( kw+'='+str( kwargs[kw] ) )
        return func(*args, **kwargs)
    return display_and_call


@display_arguments
def my_add(m1, p1=0):
    output_dict = {}
    output_dict['r1'] = m1+p1
    return output_dict


@display_arguments
def my_deduct(m1, p1=0):
    output_dict = {}
    output_dict['r1'] = m1-p1
    return output_dict


res = my_add(100, p1=1)
print(res)

print("$$$$$$$$$$$$$$$$\n")
# ========================
# Without doing decorators but manually creating wrappers

new_input_dict={
    'm1':100,
    'p1':1,
}


def reform_argument(input_dict):
    m1 = input_dict.get('m1')
    p1 = input_dict.get('p1')
    return m1, p1


def wrapped_my_add(r_new_input_dict):
    m1,p1= reform_argument(r_new_input_dict)
    return my_add2(m1, p1=p1)


def my_add2(m1, p1=0):
    output_dict2 = dict()
    output_dict2['r1'] = m1+p1
    return output_dict2


result = wrapped_my_add(new_input_dict)
print(result)
