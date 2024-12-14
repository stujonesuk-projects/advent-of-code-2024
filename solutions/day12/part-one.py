from common.board import Board
from collections import defaultdict
from common.sets import consolidate
from functools import reduce

def consolidate_regions(regions):
    def move_source_to_target(source, target):
        regions[target].extend(regions[source])
        del regions[source]
        return target
    
    def check_if_regions_are_joined(region_1_cells, region_2_cells):
        for cell in region_1_cells:
            for neighbour in cell.neighbour_cells_generator([1,3,5,7]):
                if neighbour in region_2_cells:
                    return True
        return False

    def filter_region_cells(all_region_cells):
        filtered_region_cells = set()
        for c in all_region_cells:
            if any(map(lambda x: c.metadata['region'] != x.metadata.get('region',None), c.neighbour_cells([1,3,5,7]))):
                filtered_region_cells.add(c)
        return filtered_region_cells

    finished = False
    region_cell_cache = {}
    while not finished:
        finished = True
        consolidate_regions = set()
        invalidate_cache = set()
        for k, v in regions.items():
            if k not in region_cell_cache:
                region_cell_cache[k] = filter_region_cells(set(v))
            consolidate_set = [k]
            for i, j in regions.items():
                if i == k:
                    continue
                if i not in region_cell_cache:
                    region_cell_cache[i] = filter_region_cells(set(j))
                if check_if_regions_are_joined(region_cell_cache[k], region_cell_cache[i]):
                    consolidate_set.append(i)
                    invalidate_cache.add(i)
                    invalidate_cache.add(k)
                    break
            if len(consolidate_set) > 1:
                consolidate_regions.add(frozenset(consolidate_set))
        sets_of_regions_to_combine = consolidate(consolidate_regions)
        for regions_to_combine in map(set,sets_of_regions_to_combine):
            target_region = regions_to_combine.pop()
            reduce(move_source_to_target, regions_to_combine, target_region)
            finished = False
        for i in invalidate_cache:
            del region_cell_cache[i]
        invalidate_cache.clear()

def answer(data):
    board = Board(data)
    answer = 0
    for v in board.values:
        cells = list(board.all_cells(v))
        current_region = None
        regions = defaultdict(list)
        while len(cells) > 0:
            c = cells.pop()
            if not current_region:
                current_region = 1
            elif not any(map(lambda x: x in regions[current_region], c.neighbour_cells([1,3,5,7]))):
                current_region += 1
            regions[current_region].append(c)
            c.metadata['region'] = current_region
        
        if len(regions.keys()) > 1:
            consolidate_regions(regions)
        
        for region in regions.values():
            area = len(region)
            perimeter = 0
            for c in region:
                perimeter += (4 - len(c.neighbour_cells_in_list([1,3,5,7], region)))
            answer += (perimeter * area)                            

    return answer
