
# this is the method to find the "best ravel"
def find_the_best_travel(distances, max_cities, max_distance):

    result = 0  # initialize the variable we want to use

    # return the first 2 distances found in the array
    result = result + distances[0]  # add the distances in the position "0" (arrays is zero-based: the first item is in position "0")
    result += distances[1]  # this is te same command as the previous but it takes the second item (= position "1")

    ## try yourself to use a "for" loop on distances
    ## suggestion: to use the bigger values first sort the array and reverse it (use .sort() and .reverse() functions)

    return result


# this is a function named "main" and it has no parameters
def main():

    ## these are the values we want to use to test our function
    distances = [1, 3, 5]  # this is the aray of distances
    max_cities = 2  # this is the max number of cities to visit
    max_distance = 8  # this is the

    # this is the expected result , the max distances we can obtain using 2 cities from the array
    expected_result = 8  # it should be  5 + 3 = 8

    # execute the function that solve the problem and get the result value
    result = find_the_best_travel(distances, max_cities, max_distance)

    if result == expected_result:
        print("Yeah !!!")
    else:
        print("The result is wrong. You have {0} but it should be {1}.".format(result, expected_result))

    print("\n END")
    aaa = input()  # this command just wait for an input by the user


# when I execute the main.py file it is "named" "__main__"...
if __name__ == "__main__":

    # so this code is executed because the "if" is true

    # ... and this function (main) is called
    main()