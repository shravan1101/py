# decorate


def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thx")

    return mfx


# there are two ways use decorate fuction

# # @greet
#   def name(args):
#    pass


# greet(hello)()


@greet
def hello():
    print("hello boy or girl ")


# hello()


# when there a agr involed


def greet(fx):
    def mfx(*args , **kwargs):
        print("good morning")
        fx(*args , **kwargs)
        print("thx")

    return mfx


def add (a ,b ):
    print(a+b)
    
greet(add)(1,2)