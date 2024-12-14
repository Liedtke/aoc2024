free_list = []
used_list = []

block = 0
for i, c in enumerate(open("inputs/day09.txt").read()):
    num = int(c)
    if i % 2 == 0:
        used_list.append((block, num, i//2))
    elif num != 0:
        free_list.append((block, num))
    block += num

def compress(free_list, used_list):
    free_idx = 0
    used_list_new = []
    for start, file_len, file_id in reversed(used_list):
        if free_idx == len(free_list):
            used_list_new.append((start, file_len, file_id))
        while file_len > 0:
            free_start, free_len = free_list[free_idx]
            if free_start > start:
                used_list_new.append((start, file_len, file_id))
                break
            move_size = min(file_len, free_len)
            used_list_new.append((free_start, move_size, file_id))
            remaining_free = free_len - move_size
            file_len = file_len - move_size
            # print(f"moved file {file_id} to {free_start} length {move_size}")
            if remaining_free == 0:
                free_idx += 1
            else:
                free_list[free_idx] = (free_start + move_size, remaining_free)
    return used_list_new

def compress2(free_list: list, used_list):
    used_list_new = []
    for start, file_len, file_id in reversed(used_list):
        for j, (free_start, free_len) in enumerate(free_list):
            if free_start > start:
                break
            if file_len <= free_len:
                start = free_start
                # print(f"moved file {file_id} to {free_start}")
                if file_len < free_len:
                    free_list[j] = (free_start + file_len, free_len - file_len)
                else:
                    free_list.remove((free_start, free_len))
                break
        used_list_new.append((start, file_len, file_id))
    return used_list_new

def check_sum(used_list):
    return sum(sum(i * file_id for i in range(file_start, file_start+file_len)) for file_start, file_len, file_id in used_list)

print(f"part 1 = {check_sum(compress(free_list[:], used_list))}")
print(f"part 2 = {check_sum(compress2(free_list[:], used_list))}")
