import sys 
class SkipThisFile(Exception):
    "Tells the generator to jump to the next file in list."
    pass


def read_lines(*files):

    for file in files:
        try:
            with open(file) as f:
                for line in f:
                    try :
                        yield line
                    except SkipThisFile:  
                        yield   
                        break

        except FileNotFoundError:
            print(f"File {file} not found. Skipping.")
            continue    


def display_files(*files):
    source = read_lines(*files)
    for line in source:
        print(line, end='')
        inp = input()
        if inp == 'n':
            print('NEXT')
            source.throw(SkipThisFile)  # return value is ignored

files=sys.argv[1:]
display_files(*files)            
