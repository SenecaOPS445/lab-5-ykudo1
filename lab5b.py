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

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    a = open(file_name, 'a')
    ap_lines = a.write(string_of_lines)
    a.close
    return ap_lines


def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    w = open(file_name, 'w')
    for line in list_of_lines:
        wr_lines = w.write(str(line) + '\n')
    w.close
    return wr_lines


def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    
    #count = 1
    #c = open(file_name_read, 'r')
    #for line in c:
    #    cw = open(file_name_write, 'a')
    #    cww = cw.write(str(count) + ':' + str(line))
    #    count += 1
    #    c.close
    #return cww

    count = 1
    cr = open(file_name_read, 'r')
    cr1 = cr.readlines()
    cr.close

    cp = open(file_name_write, 'w')
    for line in cr1:
        cp.write(str(count) + ':' + line)
        count += 1
    return cp


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
