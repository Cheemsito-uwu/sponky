#!/usr/bin/env python3

help = """The script helps to convert C/C++ sources to C/C++ -like Python sources.

It does some simple edit operations like removing semicolons and type declarations.
After it you must edit code manually, but you'll probably spend less time doing it.
Example:

    if (a && b)               -->    if a and b:
    {                         -->        object.method()
        object->method();     -->
    }                         -->

The utility **will** make mistakes and **will not** generate ready for use code,
therefore it won't be useful for you unless you know both C/C++ and Python.

For better result, it is recomented to format your code to ANSI style
before doing conversion.

    astyle --style=ansi your.cpp source.cpp files.cpp

Usage:

    cpp2python.py DIR                     Find C/C++ files in the directory
                                          by suffix and process.
    cpp2python.py FILE                    Process the file.
    cpp2python.py -v|--version|-h|--help  Display the help message.

After the processing new file is created.
File name is {old file name with suffix}.py. i.e. main.cpp.py

Author: Andrei Kopats <hlamer@tut.by>
License: GPL
"""

import sys
import os.path
import re

def is_source(filename):
    suffixes = ('.cpp', '.c', '.cxx', '.c++', '.cc', '.h', '.hpp', '.hxx', '.h++')
    for s in suffixes:
        if filename.endswith(s):
            return True
    return False

def process_line(line):

    """ remove semicolons

        codecode(param, param);
                V
        codecode(param, param)
    """
    line = re.sub(';([\r\n]?)$', '\\1', line) # remove semicolon from the end of line


    """ remove strings containing opening bracket

        if (blabla)
        {
            codecode
              V
        if (blabla)
            codecode
    """
    line = re.sub('\s*{\n$', '', line)

    """ remove closing brackets. Empty line preserved

        if (blabla)
        {
            codecode
              V
        if (blabla)
            codecode
    """
    line = re.sub('\s*}$', '', line)

    """ replace inline comment sign

        // here is comment
              V
        # here is comment
    """
    line = re.sub('//', '#', line)

    """ replace /* comment sign

        /* here is comment
              V
        ''' here is comment
    """
    line = re.sub('/\*', "'''", line)
    line = re.sub('\*/', "'''", line)
    line = re.sub('\|\|', 'or', line)
    line = re.sub('&&', 'and', line)
    line = re.sub('!([^=\n])', 'not \\1', line)
    line = re.sub('->', '.', line)
    line = re.sub('false', 'False', line)
    line = re.sub('true', 'True', line)
    line = re.sub('const ', ' ', line)
    line = re.sub(' const$', '', line)
    line = re.sub('if\s*\((.*)\)$', 'if \\1:', line)
    line = re.sub('if\s*\((.*)\)$', 'if \\1:', line)
    #return line
    line = re.sub('\(\s*self,\s*\)', '(self)', line)
    line = re.sub(',\s*[\w\d:&\*<>]+\s+([\w\d:&\*]+)', ', \\1', line)
    line = re.sub('[\w\d:&\*]+\s+([\w\d]+)\s*= ', '\\1 = ', line)
    line = re.sub('^def [\w\d]+::([\w\d]+\([^\)]*\):)$', 'def \\1', line)
    line = re.sub('::', '.', line)
    line = re.sub('else\s+if', 'elif', line)
    line = re.sub('else\s*$', 'else:\n', line)
    line = re.sub(' new ', ' ', line)
    line = re.sub('([^\w])this([^\w])', '\\1self\\2', line)
    line = re.sub('foreach\s*\(\s*[\w\d:&\*]+\s+([\w\d]+)\s*,\s*([\w\d\.\(\)]+)\s*\)', 'for \\1 in \\2:', line)
    line = re.sub('emit ([\w\d]+)', '\\1.emit', line)
    line = re.sub('connect\s*\(\s*([^,]+)\s*,\s*' + \
                'SIGNAL\s*\(\s*([\w\d]+)[^\)]+\)\s*\)\s*,'+ \
                '\s*([^,]+)\s*,\s*' + \
                'S[A-Z]+\s*\(\s*([\w\d]+)[^\)]+\)\s*\)\s*\)',
              '\\1.\\2.connect(\\3.\\4)', line)

    return line

def process_file(in_filename, out_filename):
    """
    generator - outputs processed file
    """
    with open(in_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # probably would die on sources more than 100 000 lines :D
    with open(out_filename, 'w+', encoding='utf-8') as file:
        for line in lines:
            file.write(process_line(line))


def main():
    if '--help' in sys.argv or \
       '-h' in sys.argv or \
       '--version' in sys.argv or \
       '-v' in sys.argv:
        print(help)
        sys.exit(0)
    if len (sys.argv) != 2:
        print('Invalid parameters count. Must be 1', file=sys.stderr)
        print(help)
        sys.exit(-1)
    if os.path.isdir(sys.argv[1]):
        for root, dirs, files in os.walk(sys.argv[1]):
            for file in files:
                in_filename = root + '/' + file
                if is_source(in_filename):
                    out_filename = in_filename + '.py' # not ideal
                    process_file(in_filename, out_filename)
    elif os.path.isfile(sys.argv[1]):
        process_file(sys.argv[1], sys.argv[1] + '.py')
    else:
        print('Not a file or directory', sys.argv[1], file=sys.stderr)
        sys.exit(-1)

if __name__ == '__main__':
    main()