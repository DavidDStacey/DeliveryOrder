"""
Name: David Stacey
Student ID: 001260498
Class: C950
"""
import operator
from util.table import Table
from util.package import package
import csv


# method is called at begining of the program to fill tables
def init_tables(distance_file, package_file):
    distance_table = fill_distance_table(distance_file)
    package_table = fill_package_table(package_file)
    return distance_table, package_table


# reads file then creates weighted graph stored in dictionary
def fill_distance_table(distance_file):
    with open(distance_file, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        distance_dictionary = dict()
        # O(n) -- for loop
        for row in reader:
            distance_dictionary.update({row['START']: sort_row(row)})
        return distance_dictionary


# sorts values of dictionary after deleting unneeded row
def sort_row(row):
    distance_dictionary = dict()
    del row['START']
    # O(n) -- for loop
    for key, value in row.items():
        row[key] = float(value)
    # O(n) -- for loop
    for item in sorted(row.items(), key=operator.itemgetter(1)):
        distance_dictionary.update({item[0]: item[1]})
    return distance_dictionary


# reads package file and create package object to add to hashtable
def fill_package_table(packages_file):
    lines = packages_file.readlines()
    how_many_lines = 0
    # this loop is used so the table is the exact right
    # size for the number of packages
    # O(n) -- for loop
    for _ in lines:
        how_many_lines = how_many_lines + 1
    new_table = Table(how_many_lines)
    # O(n) -- for loop
    for line in lines:
        packages = package(line.split(','))
        new_table.insert(packages.get_id(), packages)
    return new_table
