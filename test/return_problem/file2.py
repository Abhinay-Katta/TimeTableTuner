# file 1 has a function that calls a function in file 2,
# now the returned value in file 2 needs to be sent to
# another variable in another function in file 2. how to do this

# file2.py

def function2():

    result = "Hello from function2"
    return result


def another_function(result_from_function2):

    print(f"Result from function2: {result_from_function2}")
