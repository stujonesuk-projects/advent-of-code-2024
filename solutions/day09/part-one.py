from itertools import batched, chain, repeat

def checksum(diskMap):
    checksum = 0
    for i in range(len(diskMap)):
        if((file_id := diskMap[i]) >= 0):
            checksum += (i * file_id)
    return checksum 

def answer(data):
    disk_map = []
    for file_id, (file, free) in enumerate(batched(chain(map(int, data[0]),repeat(0)),2)):
        if file == free == 0:
            break
        disk_map.extend(chain(repeat(file_id, file), repeat(-1, free)))
    
    scan_pointer = len(disk_map) - 1
    free_space = 0
    while(free_space < scan_pointer):
        if disk_map[free_space] != -1:
            free_space += 1
        elif disk_map[scan_pointer] == -1:
            scan_pointer -= 1
        else:
            disk_map[free_space] = disk_map[scan_pointer]
            disk_map[scan_pointer] = -1
            free_space += 1
            scan_pointer -= 1

    return checksum(disk_map)
