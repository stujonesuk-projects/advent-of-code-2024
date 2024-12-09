from itertools import batched, chain, repeat

def checksum(diskMap):
    checksum = 0
    for i in range(len(diskMap)):
        if((file_id := diskMap[i]) >= 0):
            checksum += (i * file_id)
    return checksum 

def get_space(spaces, length):
    for space_position in sorted(spaces.keys()):
        if spaces[space_position] >= length:
            yield space_position, spaces[space_position]

def get_space_below(spaces, position):
    last_position = None
    for space_position in sorted(spaces.keys()):
        if space_position > position:
            yield last_position
        last_position = space_position

def answer(data):
    position = 0
    files = {}
    space = {}
    for file_id, (file, free) in enumerate(batched(chain(map(int, data[0]),repeat(0)),2)):
        if file == free == 0:
            break
        if file > 0:
            files[file_id] = {position: file}
            position += file
        if free > 0:
            space[position] = free
            position += free

    for file_id in reversed(sorted(files.keys())):
        for position in reversed(sorted(files[file_id].keys())):                
            length = files[file_id][position]           
            space_position, space_length = next(get_space(space, length), (None,None))
            if space_position and space_position < position:
                files[file_id][space_position] = length
                space[position] = length
                del files[file_id][position]
                if (position + length) in space:
                    space[position] += space[position + length]
                    del space[position + length]
                if below := next(get_space_below(space, position), None):
                    if space[below] + below == position:
                        space[below] += space[position]
                        del space[position]
                if space_length > length:
                    del space[space_position]
                    space[space_position + length] = space_length - length
                else:
                    del space[space_position]
    
    answer = 0
    for file_id, positions in files.items():
        for position, length in positions.items():
            for i in range(position, position + length):
                answer += i * file_id

    return answer
