inputs = [section.split("\n") for section in open("inputs/day05.txt").read().split("\n\n")]
rules, page_lists = ([list(map(int, line.split(sep))) for line in section] for section, sep in zip(inputs, ("|", ",")))

def valid_order(pages):
    pos = {page: i for i, page in enumerate(pages)}
    return not any(before in pos and after in pos and pos[before] > pos[after] for before, after in rules)

print(f"part 1 = {sum(pages[len(pages) // 2] if valid_order(pages) else 0 for pages in page_lists)}")

invalid = [pages[:] for pages in page_lists if not valid_order(pages)]
for pages in invalid:
    pos = {page: i for i, page in enumerate(pages)}
    filtered_rules = [rule for rule in rules if rule[0] in pos and rule[1] in pos]
    swapped = True
    while swapped:
        swapped = False
        for before, after in filtered_rules:
            if pos[before] > pos[after]:
                del pages[pos[before]]
                pages.insert(pos[after], before)
                pos = {page: i for i, page in enumerate(pages)}
                swapped = True

print(f"part 2 = {sum(pages[len(pages) // 2] for pages in invalid)}")

# Nicer solution for part 2 using builtin sorting.
import functools
invalid = [pages[:] for pages in page_lists if not valid_order(pages)]
rules_set = set((before, after) for before, after in rules)
key = functools.cmp_to_key(lambda a, b: 1 if (a, b) in rules_set else -1 if (b, a) in rules_set else 0)
print(f"part 2 (alt) = {sum(sorted(pages, key=key)[len(pages) // 2] for pages in invalid)}")
