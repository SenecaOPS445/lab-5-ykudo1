#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        result = int(number1) + int(number2)
        return result
    except ValueError:
        print_eroor = 'error: could not add numbers'
        return print_eroor
    except TypeError:
        print_eroor = 'error: could not add numbers'
        return print_eroor

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
        try:
            f = open(filename, 'r')
            lines = f.readlines()
            return lines
        except FileNotFoundError:
            print_eroor = 'error: could not read file'
            return print_eroor

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception