def sorter(key: str):
    key_len = len(key)
    key_count = 0
    sort_order = [*map(sorted(key).index, key)]

    def fn(__unused__: str):
        nonlocal key_count, key_len, sort_order
        sort_value = sort_order[key_count % key_len] + (key_count // key_len * key_len)
        key_count += 1
        return sort_value
    return fn


def solution(message: str, key: str):
    len_message, len_key = len(message), len(key)
    return ''.join(sorted(message.ljust(-len_message // len_key * -len_key, ' '), key=sorter(key)))


print(solution("Tech with Tim", "help") == "eTchw it hTi m  ")
print(solution("Pancakes", "poly"),"naPcekas    ")
print(solution("Pancakes", "poly") == "naPcekas    ")
print(solution("Random Chat", "jokes"),"dRnaohmC a t   ")
print(solution("Random Chat", "jokes") == "dRnaohmC a t   ")
print(solution("HelpHere", "m7nd") == "epHleeHr")
