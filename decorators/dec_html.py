class CGImethod(object):
    def __init__(self, title):
        self.title = title

    def __call__(self, fn):
        def wrapped_fn(*args):
            print("Content-Type: text/html\n\n")
            print("<HTML>")
            print("<HEAD><TITLE>{}</TITLE></HEAD>".format(self.title))
            print("<BODY>")
            try:
                fn(*args)
            except Exception as e:
                print(e)
            print("</BODY></HTML>")

        return wrapped_fn

@CGImethod("Hello with Decorator")
def say_hello():
    print('<h1>Hello from CGI-Land</h1>')


say_hello()
