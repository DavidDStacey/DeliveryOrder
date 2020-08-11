"""
Name: David Stacey
Student ID: 001260498
Class: C950
"""


class package(object):
    # O(1) -- constant
    def __init__(self, new_package):
        self.id = new_package[0]
        self.address = new_package[1]
        self.city = new_package[2]
        self.zip = new_package[4]
        self.deadline = new_package[5]
        self.weight = new_package[6]
        if new_package[7] == "\n":
            self.notes = "No special notes. \n"
        else:
            self.notes = new_package[7]
        self.status = "Preparing"
        self.time_delivered = None

    # O(1) -- constant
    def get_address_key(self):
        return self.address + "," + self.zip

    # O(1) -- constant
    def set_address(self, address):
        self.address = address

    # O(1) -- constant
    def get_id(self):
        return self.id

    # O(1) -- constant
    def set_zip(self, zip):
        self.zip = zip

    # O(1) -- constant
    def set_status(self, new_status):
        self.status = new_status

    # O(1) -- constant
    def set_time_delivered(self, time):
        self.time_delivered = time

    # O(1) -- constant
    def get_time_delivered(self):
        return self.time_delivered

    # O(1) -- constant
    def __str__(self):
        package_info = "Package ID: " + self.id + " \nCurrent Status: " + self.status + \
                       " \nAddress: " + self.address + ", " + self.city + ", " + self.zip + " \nWeight: " + self.weight + \
                       " \nDeliver By: " + self.deadline + " \nSpecial Notes: " + self.notes
        if self.status == "Delivered":
            package_info += "Delivered at: " + str(self.time_delivered) + "\n"
        return package_info
