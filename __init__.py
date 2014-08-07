#! /usr/bin/python3

import os
import pickle
import random

data_dict = {}

def init_data():
    global data_dict
    if not os.path.exists('/tmp/humvimdata'):
        os.makedirs('/tmp/humvimdata')
    if not os.path.isfile('/tmp/humvimdata/data.pickle'):
        # 'a' for undone commands, 'd' for perfected commands
        data_dict = {'a': {},
                     'b': {},
                     'c': {},
                     'd': {},
        }
    else:
        data_dict = pickle.load(open('/tmp/humvimdata/data.pickle', 'rb'))

def commit_data():
    global data_dict
    pickle.dump(data_dict, open('/tmp/humvimdata/data.pickle', 'wb'))

def add_new(command, description):
    global data_dict
    data_dict['a'][command] = description

def review():
    global data_dict
    commands = []
    for outer_key in ['a', 'b', 'c', 'd']:
        for inner_key in data_dict[outer_key].keys():
            commands.append((data_dict[outer_key][inner_key],
                             outer_key, inner_key))
    print commands
    random_key = random.randint(0, len(commands)-1)
    cmd = commands[random_key][2]
    cmd_group = commands[random_key][1]
    desc = commands[random_key][0]
    print('command: %s' % cmd)
    print('description: %s' % desc)
    print('d: perfected')
    print('c: remember')
    print('b: faint memory')
    print('a: too new to remember')
    ans = raw_input()
    if ans != cmd_group:
        del data_dict[cmd_group][cmd]
        data_dict[ans][cmd] = desc
    print data_dict


if __name__ == '__main__':
   pass 
