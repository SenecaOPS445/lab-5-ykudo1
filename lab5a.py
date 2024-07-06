#!/usr/bin/env python3
# Author ID: ykudo


def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    read_data = f.read()
    f.close
    return read_data

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    
    #l = open(file_name, 'r')
    #read_data = l.read()
    #read_data.split('\n')
    #list_of_lines = read_data.split('\n')
    #l.close
    #return list_of_lines

    f = open(file_name, 'r')
    lines = f.read().splitlines()
    f.close
    return lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))