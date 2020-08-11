"""
Name: David Stacey
Student ID: 001260498
Class: C950
"""
import datetime


# creates delivery lists
# truck 1 is sent first at the begining of the day
# truck 2 waits until the delayed packages arrive
# O(n^3) -- n(n + n^2) = n^2 + n^3 see below for details v
# for loop and another method that contains nested for loops within a for loop
def start_delivery(pack, dist):
    # initilize variables
    global package_table, distance_table, available_packages, package_count, truck_2_packages, total_weight_2, check_1, check_2, check_3
    truck_1_trip = "truck 1"
    # tables
    package_table = pack
    distance_table = dist
    available_packages = get_packages(package_table.get_all())
    truck_1_list = list()
    time = datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day, 8)
    # truck 2 only is sent 1 time so make it a boolean to make it easy to check
    truck_2_packages_delivered = False
    # checks if it has to be on truck 2
    package_eligible = False
    # certain packages have to be together
    same_truck_packages = False
    # start with earliest delivery time
    current_package = package_table.get('15')
    # total distance travelled
    total_weight = distance_table[current_package.get_address_key()]['HUB']
    # updates time
    time = add_time(time, total_weight)
    # puts the statring package on truck 1
    add_delivery(current_package, truck_1_list, time)
    print(truck_1_trip)
    print(current_package)
    # how many packages are on the truck
    package_count = 1
    # loads the truck
    while len(available_packages) > 0:
        # checks next closest address
        # O(n) -- for loop
        for address, weight in distance_table[current_package.get_address_key()].items():
            # if there's a package to the next closest address that one is next otherwise move on to next closest
            if available_packages.get(address):
                # first available package at an address
                # O(n) -- for loop
                for package_id, package in available_packages[address].items():
                    # sets package okay to be delivered next
                    if package_id not in truck_2_packages:
                        current_package = package
                        package_eligible = True
                        break
                # delivers current package
                if package_eligible:
                    # theres a handful of packages that need to be delivered on same truck load this handles that
                    if current_package.get_id() == '12' and same_truck_packages is False:
                        current_package = package_table.get('13')
                        new_weight = distance_table[truck_1_list[-1].get_address_key()][
                            current_package.get_address_key()]
                        total_weight += new_weight
                        time = add_time(time, new_weight)
                        same_truck_packages = True
                    # if no packages then at hub
                    if package_count == 0:
                        total_weight += distance_table[current_package.get_address_key()]['HUB']
                        time = add_time(time, distance_table[current_package.get_address_key()]['HUB'])
                    # add weight of package delivery
                    else:
                        total_weight += weight
                        time = add_time(time, weight)
                    # once max load is delivered head back to hub
                    if package_count == 16:
                        total_weight += distance_table[current_package.get_address_key()]['HUB']
                        package_count = 0
                        time = add_time(time, distance_table[current_package.get_address_key()]['HUB'])
                        truck_1_trip = "truck 1 trip 2"
                    # truck 2 leaves at 9:05 since that is when delayed packages arrive
                    if time.time() >= datetime.time(9, 5) and truck_2_packages_delivered is False:
                        # O(n^2) -- truck 2 delivery method
                        total_weight_2, truck_2_list = truck_2_delivery(time)  # this method send truck 2 out
                        truck_2_packages_delivered = True
                    if time.time() >= datetime.time(9, 25) and check_1 is False:
                        check_1 = True
                        print("It is now 9:25")
                        print("Would you like to see the status of all packages?")
                        print("Press 1 for yes")
                        print("Press 2 for no")
                        print()
                        response = input()
                        print()
                        if response == str(1):
                            print_packages()
                            print("Press enter to continue delivering")
                            input()
                    if time.time() >= datetime.time(10, 25) and check_2 is False:
                        check_2 = True
                        print("It is now 10:25")
                        print("Would you like to see the status of all packages?")
                        print("Press 1 for yes")
                        print("Press 2 for no")
                        print()
                        response = input()
                        print()
                        if response == str(1):
                            print_packages()
                            print("Press enter to continue delivering")
                            input()
                    if time.time() >= datetime.time(13, 12) and check_3 is False:
                        check_3 = True
                        print("It is now 1:12")
                        print("Would you like to see the status of all packages?")
                        print("Press 1 for yes")
                        print("Press 2 for no")
                        print()
                        response = input()
                        print()
                        if response == str(1):
                            print_packages()
                            print("Press enter to continue delivering")
                            input()
                    package_count = package_count + 1
                    add_delivery(current_package, truck_1_list, time)
                    print(truck_1_trip)
                    print(current_package)
                    package_eligible = False
                    break
    # package 9 had wrong address so it needs to be picked up and delivered correctly
    current_package = package_table.get('9')
    # address is manually typed in
    redelivery_weight = distance_table[truck_1_list[-1].get_address_key()][current_package.get_address_key()] + distance_table[current_package.get_address_key()]["410 S State St,84111"]
    time = add_time(time, redelivery_weight)
    # update needed info on package -- address and new delivery time
    current_package.set_address("410 S State St")
    current_package.set_zip("84111")
    current_package.set_time_delivered(time)
    # adds all weight
    final_weight = total_weight + total_weight_2 + distance_table["410 S State St,84111"]['HUB'] + redelivery_weight
    if check_1 is False or check_2 is False or check_3 is False:
        print("Deliveries are complete!")
        print("The time is now: ")
        print(time)
        print("Would you like to see the status of all packages?")
        print("Press 1 for yes")
        print("Press 2 for no")
        print()
        response = input()
        print()
        if response == str(1):
            print_packages()
        print()
        print("Press enter to find the fine miles drove!")
        input()
    return final_weight


# truck 2 only loads once
# O(n^2) -- for loop nested in another for loop
def truck_2_delivery(time):
    delivery_list = list()
    package_eligible = False
    # manually start with package 25
    current_package = package_table.get('25')
    total_weight = distance_table[current_package.get_address_key()]['HUB']
    time = add_time(time, total_weight)
    add_delivery(current_package, delivery_list, time)
    print("truck 2")
    print(current_package)
    # keeps going thoruigh as long as the number of packages in the
    # lsit is less than 10 for truck 2
    # fairly identical to delivery from truck 1
    while len(delivery_list) < 12:
        # O(n) -- for loop
        for address, weight in distance_table[current_package.get_address_key()].items():
            if available_packages.get(address):
                # O(n) -- for loop
                for package_id, package in available_packages[address].items():
                    if package_id in truck_2_packages:
                        current_package = package
                        package_eligible = True
                        break
                if package_eligible:
                    total_weight += weight
                    time = add_time(time, weight)
                    add_delivery(current_package, delivery_list, time)
                    package_eligible = False
                    print("truck 2")
                    print(current_package)
                    break
    return total_weight + distance_table[delivery_list[-1].get_address_key()]['HUB'], delivery_list


# add to truck list and updates package info
# O(1) -- constant
def add_delivery(package, delivery_list, time):
    update_list(package)
    package_table.get(package.get_id()).set_time_delivered(time)
    package_table.get(package.get_id()).set_status('Delivered')
    delivery_list.append(package)


# package isnt available now
# O(1) -- constant
def update_list(package):
    if len(available_packages[package.get_address_key()]) > 1:
        package_list = available_packages[package.get_address_key()]
        del package_list[package.get_id()]
    else:
        del available_packages[package.get_address_key()]


# adjust time based on how far truck drove
# truck is 18 mph with instant unload times
# O(1) -- constant
def add_time(time, miles):
    seconds_elapsed = (3600 / 18) * miles
    time = time + datetime.timedelta(seconds=seconds_elapsed)
    return time


# creates dictionary of packages
# O(n) -- for loop
def get_packages(package_list):
    address_table = dict()
    # O(n) -- for loop
    for package in package_list:
        if address_table.get(package.get_address_key()):
            address_table[package.get_address_key()].update({package.get_id(): package})
        else:
            address_table.update({package.get_address_key(): {package.get_id(): package}})
    return address_table


def print_packages():
    for packages in package_table.get_all():
        print(packages)

# gloabal variables
# all below is constant -- O(1)
package_table = None
distance_table = None
available_packages = None
package_count = 0
total_weight_2 = 0
# packages for truck 2 that either are delayed or must be on truck 2 etc
#truck_2_packages = ['3', '6', '9', '18', '25', '28', '31', '32', '36', '38', '7', '29']
#truck_2_packages = ['3', '6', '9', '25', '32', '28', '36', '18', '38']
truck_2_packages = ['3', '6', '9', '8', '25', '26', '31', '32', '28', '36', '18', '38']
check_1 = False
check_2 = False
check_3 = False


