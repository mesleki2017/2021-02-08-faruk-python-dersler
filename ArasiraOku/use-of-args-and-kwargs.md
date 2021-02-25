[stackoverflow](https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs)

[stackoverflow](https://stackoverflow.com/questions/1769403/what-is-the-purpose-and-use-of-kwargs)

# Use of \*args and \*\*kwargs

The syntax is the * and \*\*. The names *args and \*\*kwargs are only by convention but there's no hard requirement to use them.

You would use \*args when you're not sure how many arguments might be passed to your function, i.e. it allows you pass an arbitrary number of arguments to your function. For example:

> > > def print_everything(\*args):

        for count, thing in enumerate(args):

... print( '{0}. {1}'.format(count, thing))
...

> > > print_everything('apple', 'banana', 'cabbage') 0. apple

1. banana
2. cabbage
   Similarly, \*\*kwargs allows you to handle named arguments that you have not defined in advance:

> > > def table_things(**kwargs):
> > > ... for name, value in kwargs.items():
> > > ... print( '{0} = {1}'.format(name, value))
> > > ...
> > > table_things(apple = 'fruit', cabbage = 'vegetable')
> > > cabbage = vegetable
> > > apple = fruit
> > > You can use these along with named arguments too. The explicit arguments get values first and then everything else is passed to \*args and **kwargs. The named arguments come first in the list. For example:

def table_things(titlestring, **kwargs)
You can also use both in the same function definition but \*args must occur before **kwargs.

You can also use the \* and \*\* syntax when calling a function. For example:

> > > def print*three_things(a, b, c):
> > > ... print( 'a = {0}, b = {1}, c = {2}'.format(a,b,c))
> > > ...
> > > mylist = ['aardvark', 'baboon', 'cat']
> > > print_three_things(\_mylist)
> > > a = aardvark, b = baboon, c = cat
> > > As you can see in this case it takes the list (or tuple) of items and unpacks it. By this it matches them to the arguments in the function. Of course, you could have a * both in the function definition and in the function call.

---

One place where the use of \*args and \*\*kwargs is quite useful is for subclassing.

class Foo(object):
def **init**(self, value1, value2): # do something with the values
print value1, value2

class MyFoo(Foo):
def **init**(self, *args, \*\*kwargs): # do something else, don't care about the args
print 'myfoo'
super(MyFoo, self).**init**(*args, \*\*kwargs)

This way you can extend the behaviour of the Foo class, without having to know too much about Foo. This can be quite convenient if you are programming to an API which might change. MyFoo just passes all arguments to the Foo class.
