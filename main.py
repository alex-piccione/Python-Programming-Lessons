def main():

    # to run the code read the README file

    print("Welcome to lesson 1 !!!")
    print("\n\n")
    print("Press any key to close...")
    input()

'''
This function is the solution to the problem.
To run it it must be called, as it is done in test.py.
Example:
result = get_max_distances(distances, cities, distance_limit)
'''
def get_max_distances(distances, cities, distance_limit):
    current_distance = 0
    city_counter = 0

    distances.sort()
    distances.reverse()

    for distance in distances:

        if current_distance < distance_limit and city_counter < cities:
            if current_distance + distance <= distance_limit:
                current_distance += distance
                city_counter += 1
        else:
            break

    return current_distance or None


if __name__ == "__main__":
    main()