#   Run file from command line with Python3 or use IDE. It will ask for list file name first; if this tool is not in the 
# same dir as the list file, include path with name.
#   Will ask for file name to store checked domain/status code list. If does not exist will create. Again include path
# or will create in dir with SubDoChck.py tool.
# -- Enjoy and feedback is welcome. --
import requests

# Read from
ask_read = input('Domain list file: ')
sub_list = open(ask_read,'r')
split_list = sub_list.read().splitlines()

# Write to
ask_write = input('Status list name (will create if does not exist): ')
stat_list = open(ask_write,'a')

def get_code(url):
    try:
        get = requests.get(url)
        stat_code = str(get.status_code)
        return stat_code
    
    except requests.ConnectionError:
        return 'Connection Error'

def write_list(url, code):
    stat_list.write(url + ' ---- ' + code + '\n')

def main(list):
    
    for line in list:
        write_list(line, get_code(line))

    sub_list.close()
    stat_list.close()
    
    print('-- List checked. Written to: %s' % ask_write)


main(split_list)
