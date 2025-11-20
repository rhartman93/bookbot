def sort_on(items):
    return items["num"]

def word_count(text: str):
    return len(text.split())

def char_counts(text: str):
    char_map = {}
    for character in text.lower():
        try:
            char_map[character] += 1
        except KeyError:
            char_map[character] = 1

    return char_map

def char_count_list(counts: dict):
    count_list = []
    for item in counts.keys():
        if not item.isalpha():
            continue
        count_list.append({"char": item, "num": counts[item]})

    count_list.sort(reverse=True, key=sort_on)
    return count_list