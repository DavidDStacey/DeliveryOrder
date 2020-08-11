"""
Name: David Stacey
Student ID: 001260498
Class: C950
"""
import datetime
from util.csvReader import *
from util.delivery import start_delivery


# this is the main method where the program starts
def main():
    global eod
    global package_table
    # basic input for options
    print("Select an option using the number keys:")
    print("Press 1 to manage packages")
    print("Press 2 to start delivering packages")
    print("Press 3 to exit")
    print()
    response = input()
    print()
    if response == str(1):
        # calls another method
        manage_packages()
    elif response == str(2) and eod is False:
        # starts the deliveries
        print(start_delivery(package_table, distance_table))
        print()
        # sets eod to true so we cant try to send deliveries oput more than once
        eod = True
        # back to beginning of main
        main()
    elif response == str(3):
        exit()
    else:
        print("Response not valid\n")
        main()


# different ways of looking up packages
def manage_packages():
    global package_table
    # easy way to keep going back to this menu after looking at packages
    # rather than ending program or going back to main
    # O(n)
    while True:
        print("Select an option using the number keys:")
        print("Press 1 to look up a package by ID")
        print("Press 2 to show deliveries between specific times")
        print("Press 3 to view all packages")
        print("Press 4 to go to previous prompt")
        print()
        response = input()
        print()
        if response == str(1):
            # calls another method and prints what is returned
            print(package_table.get(find_package_prompt()))
        elif response == str(2):
            # checks to see if delivers have been made yet
            # could also have used the eod boolean to check
            temp_package = package_table.get("15")
            is_packages_delivered = temp_package.status
            if is_packages_delivered == "Delivered":
                pick_time()
            else:
                print("Deliveries have not started yet.\n")
        elif response == str(3):
            # prints all details of all packages
            # O(n) -- for loop
            for packages in package_table.get_all():
                print(packages)
        elif response == str(4):
            # back to main method
            main()
        else:
            print("Response not valid\n")


def find_package_prompt():
    print("\nEnter a package id: ")
    return input()


# shows deliveries within specified time gaps from prompt
# or you can check between custom times
def pick_time():
    print("Press 1 to see deliveries from 8:35 am to 9:25 am")
    print("Press 2 to see deliveries from 9:35 am to 10:25 am")
    print("Press 3 to see deliveries from 12:03 pm to 1:12 pm")
    print("Press 4 to see deliveries between custom times")
    print()
    response = input()
    print()
    # each if statement calls a different method
    if response == str(1):
        before_925()
    elif response == str(2):
        before_1025()
    elif response == str(3):
        before_112()
    elif response == str(4):
        before_custom()
    else:
        print("Response not valid\n")


# shows packages delivered between 2 times
def before_925():
    packages_found = False
    time_frame = [datetime.time(int("08"), int("35")), datetime.time(int("09"), int("25"))]
    print("\nShowing deliveries between 8:35 and 9:25 am")
    # O(n^2) -- package_table.get_all() is another for loop within this for loop
    for PACKAGE in package_table.get_all():
        package_time = PACKAGE.get_time_delivered().time()
        if time_frame[0] <= package_time <= time_frame[1]:
            packages_found = True
            print(PACKAGE)
    if packages_found is False:
        print("No packages delivered within this time frame.")
    print()


# shows packages delivered between 2 times
def before_1025():
    packages_found = False
    time_frame = [datetime.time(int("09"), int("35")), datetime.time(int("10"), int("25"))]
    print("\nShowing deliveries between 9:35 and 10:25 am")
    # O(n^2) -- package_table.get_all() is another for loop within this for loop
    for PACKAGE in package_table.get_all():
        package_time = PACKAGE.get_time_delivered().time()
        if time_frame[0] <= package_time <= time_frame[1]:
            packages_found = True
            print(PACKAGE)
    if packages_found is False:
        print("No packages delivered within this time frame.")
    print()


# shows packages delivered between 2 times
def before_112():
    packages_found = False
    time_frame = [datetime.time(int("12"), int("03")), datetime.time(int("13"), int("12"))]
    print("\nShowing deliveries between 12:03 and 1:12 pm")
    # O(n^2) -- package_table.get_all() is another for loop within this for loop
    for PACKAGE in package_table.get_all():
        package_time = PACKAGE.get_time_delivered().time()
        if time_frame[0] <= package_time <= time_frame[1]:
            packages_found = True
            print(PACKAGE)
    if packages_found is False:
        print("No packages delivered within this time frame.")
    print()


# shows packages delivered between 2 custom times
def before_custom():
    packages_found = False
    time_frame = []
    print("\nEnter numbers in 24 hour format -- 3pm = 15:00")
    # O(1) -- goes through loop a constant number of times not n number
    for _ in range(0, 2):
        print("Enter hour: ")
        hour = input()
        print("Enter minute: ")
        minute = input()
        print()
        time_frame.append(datetime.time(int(hour), int(minute)))
    # O(n^2) -- package_table.get_all() is another for loop within this for loop
    for PACKAGE in package_table.get_all():
        package_time = PACKAGE.get_time_delivered().time()
        if time_frame[0] <= package_time <= time_frame[1]:
            packages_found = True
            print(PACKAGE)
    if packages_found is False:
        print("No packages delivered within this time frame.")
    print()


# python will auto go through these as they are not within a method
# initialize the tables
distance_table, package_table = init_tables('data/distance.csv', open('data/packages.csv', 'r'))
eod = False  # used so you cant try to do deliveries more than once
main()  # starts the main mathod of program
