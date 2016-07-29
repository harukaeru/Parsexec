#!/usr/bin/env python
try:
    from colorama import Fore, Style
    GREEN = Fore.GREEN
    RED = Fore.RED
    RESET = Style.RESET_ALL
except ImportError:
    GREEN = RED = RESET = ''

import sys
import re

with open('import_classes.py') as f:
    lines = [l.replace('\n', '') for l in f.readlines()]
    s, e = 0, 2
    import_classes = {}

    while True:
        line = lines[s:e]
        if not line:
            break
        if len(line) == 1:
            raise ValueError("line {}:{} is crazy".format(s, e))
        import_classes[line[1]] = line[0]
        s, e = e, e + 2

filename = sys.argv[1]
with open(filename) as f:
    source = f.read()
    matched = re.search(r'( *)```(\n|)((?:.|\n)*?)```', source)
    if not matched:
        raise ValueError("Not Found ```.*``` source")
    groups = matched.groups()

    no_data_in_firstline = groups[1]
    source = groups[2]
    if not no_data_in_firstline:
        first_indent = groups[0]
        source = first_indent + source


def remove_indent(s):
    lines = s.split('\n')
    firstline = lines[0]
    matched = re.match(r'^( +).*', firstline)
    if matched:
        space = matched.groups()[0]
        new_lines = [re.sub('^' + space, '', line) for line in lines]
        return '\n'.join(new_lines)
    else:
        return s


source = remove_indent(source)
_print = print
print_list = []


def print(*args, **kwargs):
    if len(args) > 1:
        def p():
            _print(*args, **kwargs)
        print_list.append(p)
    else:
        data = args[0]

        def q():
            _print(GREEN + "data:" + RESET, data)
            _print(GREEN + "class:" + RESET, type(data))
        print_list.append(q)
source_for_test = '\n{}'.format(source)
error = True
import_statements = ''
while error:
    try:
        print_list = []
        exec(import_statements + source_for_test)

        _print(GREEN + "----- Out -----" + RESET)
        for p in print_list:
            p()
        _print(RED + '----- source -----' + RESET)
        _print(import_statements + source)
        error = False
    except NameError as e:
        # TODO: printed(twice or more)
        message = e.args[0]
        matched = re.search(r"'(.*?)'", message)
        match = matched.groups()[0]
        if import_classes.get(match):
            import_statement = import_classes[match]
            import_statements += import_statement + '\n'
        else:
            raise NameError(e)
