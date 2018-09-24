import os
import sys
import shutil

def my_ls(): 
    
    print(os.listdir(os.getcwd()))

def my_mkdir_name():
    my_mkdir(input('Enter Folder name:'))

def my_rmdir_name():
    my_rmdir(input('Enter Folder name:'))

def my_mkdir(dirname):
    try:
        os.mkdir(os.path.join(os.getcwd(), dirname))
        print('Folder "{}" created.'.format(dirname))
    except FileExistsError:
        print('Directory with name "{}" allready present in that folder.'.format (dirname))
    except NameError:
        print('You entered incorrect name.')
    except:
        print('Some other error')

def my_rmdir(dirname):
    try:
        os.rmdir(os.path.join(os.getcwd(), dirname))
        print('Folder "{}" deleted.'.format(dirname))
    except FileNotFoundError:
        print('Directory "{}" not present in that folder.'.format (dirname))
    except NameError:
        print('You entered incorrect name.')
    except:
        print('Some other error')

def my_fcopy():

    try:
        shutil.copy(os.path.join(os.getcwd(), sys.argv[0]), os.path.join(os.getcwd(), sys.argv[0].split('.py').pop(0) + '_copy.py'))
    except:
        print('Error')

def my_cd():

    try:
        os.chdir(os.path.join(os.getcwd(), input('Enter folder name')))
        print('OK')
    except FileNotFoundError:
        print('Folder not exist')