import os
import click
from pathlib import Path

import inquirer

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def run():
    try:
        csv()
    except KeyboardInterrupt:
        click.echo('User exit...')
    except Exception as e:
        pass

@click.group()
def csv():
    ''' 
    This is a script to change measurement comments by values from source file
    '''
    pass

@csv.command()
def mando():
    '''
    This is the way!
    '''
    click.echo('''
    ⣿⣿⣿⣿⣿⣿⢸⣿⡇⠀⣿⣿⡇⣿⣿⡇⣼⣿⣿⣿⣿⣿⠀⠀⡇⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀
    ⠉⠉⣿⣿⠉⠉⢸⣿⡇⠀⣿⣿⡃⣿⣿⡇⣿⣿⡇⠀⣿⣿⠀⠀⡇⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀
    ⠀⠀⣿⣿⠀⠀⢸⣿⣧⣤⣿⣿⡇⣿⣿⡇⠻⣿⣷⣦⡀⠀⠀⠀⡇⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀
    ⠀⠀⣿⣿⠀⠀⢸⣿⡟⠛⣿⣿⡇⣿⣿⡇⠀⠈⠻⢿⣿⣦⠀⠀⡇⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀
    ⠀⠀⣿⣿⠀⠀⢸⣿⡇⠀⣿⣿⡇⣿⣿⡇⣿⣿⡇⠀⣿⣿⠀⠀⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀
    ⠀⠀⣿⣿⠀⠀⢸⣿⡇⠀⣿⣿⡇⣿⣿⡇⣿⣿⣷⣶⣿⣿⠀⠀⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀
    ⠀⠀⠛⠛⠀⠀⠘⠛⠃⠀⠛⠛⠃⠛⠛⠃⠈⠛⠛⠛⠛⠋⠀⠀⠿⢟⣛⣛⣛⣛⣛⣛⣛⣛⣛⣰⡄
    ⣿⡇⢴⣿⣿⣿⡆⠀⢸⣿⣿⣿⣿⣿⣿⠀⣿⡇⢸⣿⣿⣿⡇⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⣷
    ⣿⡇⢸⣿⡀⠛⠃⠀⠀⠀⣿⡇⠀⣿⣿⠀⣿⡇⢸⣿⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣶⣶⣶⣾⣿⣿
    ⣿⡇⠈⠻⢿⣶⡄⠀⠀⠀⣿⡇⠀⣿⣿⠿⣿⡇⢸⣿⠿⠿⠇⠀⠀⠀⢸⣿⣿⣿⣿⣿⡿⠛⠋⣹⡿
    ⣿⡇⢰⣶⡀⣿⡇⠀⠀⠀⣿⡇⠀⣿⣿⠀⣿⡇⢸⣿⣀⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⠋⠀⠀⢰⣿⡇
    ⠿⠇⠸⠿⠿⠿⠇⠀⠀⠀⠿⠇⠀⠿⠿⠀⠿⠇⠸⠿⠿⠿⠇⠀⠀⠀⣿⣿⣿⣿⠃⠀⠀⢠⣿⣿⡇
    ⣶⣶⡆⠀⣶⣶⠀⢰⣶⣶⠀⢰⣶⣶⡀⢲⣶⣦⠀⢰⣶⣶⠀⠀⠀⠀⣿⣿⣿⠃⠀⣠⣤⣿⣿⣿⠃
    ⢸⣿⣧⠀⣿⣿⡇⢸⣿⣿⠀⣿⣿⣿⡇⠈⣿⣿⡀⣼⣿⡏⠀⠀⠀⠀⣿⣿⡏⢀⣾⣿⣿⣿⣿⣿⠀
    ⢸⣿⣿⢸⣿⣿⡇⣼⣿⡇⢸⣿⡿⣿⣧⠀⢻⣿⣇⣿⣿⠁⠀⠀⠀⠀⣿⣿⠇⣼⣿⣿⣿⣿⣿⣿⠀
    ⠀⣿⣿⢸⣿⣿⣇⣿⣿⠇⢸⣿⡇⣿⣿⡀⠘⣿⣿⣿⡏⠀⠀⠀⠀⠀⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⠀
    ⠀⣿⣿⣿⣿⢿⣿⣿⣿⠀⣾⣿⠷⢿⣿⡇⠀⢻⣿⣿⠀⠀⠀⠀⠀⠀⣿⡿⣾⣿⣿⣿⣿⣿⠟⠁⠀
    ⠀⢸⣿⣿⡏⢸⣿⣿⡿⢰⣿⣿⠀⢸⣿⣷⠀⢸⣿⣿⠀⠀⠀⠀⠀⢀⣿⡇⣿⣿⣿⠟⠋⠀⠀⠀⠀
    ⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⡇⠀⠀⣿⣿⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠻⡇⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

@csv.command()
def change():
    ''' 
    Start the changes
    '''

    all_files = list_valid_files()
        
    
    click.echo('Select source\n - reads every line starting from 2nd line\n - takes measurement until first \';\'')
    click.echo('Selected file will be excluded from scan!')
    answer = inquirer.prompt([inquirer.List('source', message='choose', choices=all_files)])
    source = answer['source']
    click.echo(f'Choose: {source}\n')

    source_file = all_files.pop(all_files.index(source))
    all_files.sort()

    with open(source_file) as s:
        next(s) # skip 1st line
        source_lines = s.readlines()
        s.close()
    source_lines_first_column = list(map(lambda line: str(line).split(';')[0], source_lines))
    
    for index, csv in enumerate(all_files):
        f = open(csv, 'r+')
        csv_lines = f.readlines()
        if len(csv_lines) > 0:
            if not csv_lines[0].startswith(';'):
                print_warning(f'Skipped "{csv}" as no comment in first line indicated by starting with \';\'')
                continue
            print_green(f'{csv} | {csv_lines[0]} --> {source_lines_first_column[index]}'.replace('\n', ''))
            csv_lines[0] = source_lines_first_column[index] + "\n"
            f.seek(0,0)
            f.writelines(csv_lines)
        f.close()


def list_valid_files():
    click.echo(f'CSV loading...\n')
    valid_files = list(file for file in os.listdir() if os.path.isfile(file) and is_valid_file(file))
    if len(valid_files) == 0:
        print_error('No valid files found. You must have .csv or .txt files in this directory!')
        exit(1)
    return valid_files

def is_valid_file(file):
    return file.endswith('.csv') or file.endswith('.txt')

def print_warning(string):
    click.echo(f'{bcolors.WARNING}{string}{bcolors.ENDC}')

def print_green(string):
    click.echo(f'{bcolors.OKGREEN}{string}{bcolors.ENDC}')

def print_error(string):
    click.echo(f'{bcolors.FAIL}{string}{bcolors.ENDC}')
