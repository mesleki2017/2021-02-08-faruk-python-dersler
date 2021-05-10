#A lambda function can take any number of arguments, but can only have one expression.
#https://www.w3schools.com/python/python_lambda.asp
#https://stackoverflow.com/questions/21035437/passing-a-function-as-an-argument-in-python

#aaa fn1 fonksiyonun argument i
fn1 = lambda aaa : aaa + 10
print(fn1(5))

#bbb ve cc fn2 fonksiyonun argument i
fn2 = lambda bbb, ccc : bbb * ccc
print(fn2(5,9))


#https://stackabuse.com/lambda-functions-in-python/
# commonly used when you want to pass a function as an argument to 
# higher-order functions, that is, functions that take other functions as their arguments.
def testfunc(num):
    return lambda x : x * num
result1 = testfunc(10)
result2 = testfunc(1000)
print(result1(9))
print(result2(9))