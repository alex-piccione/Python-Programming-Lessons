
# this is the method to find the "best ravel"
def find_the_best_travel(distances, max_cities, max_distance):

    travel_distance = 0  # initialize the variable we want to use

    # return the first 2 distances found in the array (wrong solution)
    travel_distance = travel_distance + distances[0]  # add the distances in the position "0" (arrays is zero-based: the first item is in position "0")
    travel_distance += travel_distance[1]  # this is te same command as the previous but it takes the second item (= position "1")

    # ###############################################
    # ###    TRY YOURSELF TO SOLVE THE PROBLEM    ###
    # ###############################################

    # 1. create an empty list  ( = [])
    # ... and a "cities counter" variable
    # ... and a "current distance"
    # 2. use a "for" to loop trough the distances
    # 3. if both the "cities counter" and "current distances" does not exceed the limits (max_cities and max_distance)
    # ... add it to the "travel_distance"

    # suggestion: to use the bigger values first sort the array and reverse it (use .sort() and .reverse() functions)

    return travel_distance


# this is a function named "main" and it has no parameters
def main():

    # these are the values we want to use to test our function
    distances = [1, 3, 5]  # this is the list of distances
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
