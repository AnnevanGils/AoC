import re

max_size = 100000
            
def go_to_dir(filesystem, path):
    current_dir = filesystem
    for d in path:
        current_dir = current_dir[d]
    return current_dir

filesystem = {'/': {'cummulative': 0, 'total': 0, 'files': []}}
paths_to_qualifying_dirs = []

with open("day7/input.txt", 'r') as f:
    breadcrumbs = []
    for line in f.readlines():
        line = line.strip('\n')

        if(line[0] == '$'):
            cmd = re.search("\$ ([a-z]+)", line).groups()[0]
            
            if(cmd == "cd"):
                var = re.search("\$ [a-z]+ (\S+)", line).groups()[0]
                if(var == '..'):
                    breadcrumbs.pop()
                else:                    
                    breadcrumbs.append(var)
                # navigate to dir
                current_dir = go_to_dir(filesystem, breadcrumbs)                

        elif(re.match("dir \S+", line)):
            var = re.search("dir (\S+)", line).groups()[0]
            # add dir to filesystem
            current_dir[var] = {'cummulative': 0, 'total': 0, 'files': []}
        
        elif(re.match("\d+ \S+", line)):
            # add file to current dir
            # also keep a total amount of file sizes
            # cummulative amount includes subdirs
            filesize, fname = re.search("(\d+) (\S+)", line).groups()
            filesize = int(filesize)
            current_dir['total'] += filesize
            current_dir['files'].append((fname, filesize))

# calculate cummulative values
def walk(directory):
    non_dir_keys = ['cummulative', 'total', 'files']
    if(len(directory.keys()) == len(non_dir_keys)):
        directory['cummulative'] = directory['total']
    else:
        directory['cummulative'] += directory['total']
        for d in [k for k in directory.keys() if k not in non_dir_keys]:
            walk(directory[d])
            directory['cummulative'] += directory[d]['cummulative']

walk(filesystem['/'])

count = []
def find_max_filesize_dirs(directory):
    if(directory['cummulative'] <= max_size):
        count.append(directory['cummulative'])

    non_dir_keys = ['cummulative', 'total', 'files']
    if(len(directory.keys()) == len(non_dir_keys)):
        pass
    else:
        for d in [k for k in directory.keys() if k not in non_dir_keys]:
            find_max_filesize_dirs(directory[d])

find_max_filesize_dirs(filesystem['/'])
print(sum(count))

# part 2
print()
total_space = 70000000
needed_space = 30000000
current_used = filesystem['/']['cummulative']
print("currently used space: ", current_used)
needed_freed = needed_space - (total_space - current_used)
print("space needing to be freed: ", needed_freed)

options = []
def find_delete_options(directory):
    if(directory['cummulative'] >= needed_freed):
        options.append(directory['cummulative'])

    non_dir_keys = ['cummulative', 'total', 'files']
    if(len(directory.keys()) == len(non_dir_keys)):
        pass
    else:
        for d in [k for k in directory.keys() if k not in non_dir_keys]:
            find_delete_options(directory[d])

find_delete_options(filesystem['/'])
print()
print("options to delete")
print(options)
print()
print("smallest option")
print(min(options))
