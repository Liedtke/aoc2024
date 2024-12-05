inputs = [section.split("\n") for section in open("inputs/day05.txt").read().split("\n\n")]
rules, page_lists = ([list(map(int, line.split(sep))) for line in section] for section, sep in zip(inputs, ("|", ",")))

def valid_order(pages):
    return not any(before in pages and after in pages and pages.index(before) > pages.index(after) for before, after in rules)

print(f"part 1 = {sum(pages[len(pages) // 2] if valid_order(pages) else 0 for pages in page_lists)}")

invalid = [pages[:] for pages in page_lists if not valid_order(pages)]
for pages in invalid:
    filtered_rules = [rule for rule in rules if rule[0] in pages and rule[1] in pages]
    swapped = True
    while swapped:
        swapped = False
        for before, after in filtered_rules:
            if pages.index(before) > pages.index(after):
                del pages[pages.index(before)]
                pages.insert(pages.index(after), before)
                swapped = True

print(f"part 2 = {sum(pages[len(pages) // 2] for pages in invalid)}")
