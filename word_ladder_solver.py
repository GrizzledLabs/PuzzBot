#!/usr/bin/python3
# bot.py

import wordladderlist

def get_pairs():
    word_map = {}
    for word in wordladderlist.words:
        keys = get_subwords(word)
        for i in range(3):
            for j in range(i + 1, 4):
                if keys[i] in word_map:
                    word_map[keys[i]].add(keys[j])
                else:
                    word_map[keys[i]] = set([keys[j]])
                if keys[j] in word_map:
                    word_map[keys[j]].add(keys[i])
                else:
                    word_map[keys[j]] = set([keys[i]])
    return word_map

def get_shortest_route(start, end):
    start_keys = get_subwords(start)
    end_keys = get_subwords(end)
    word_map = get_pairs()
    searched = {x: "start" for x in start_keys}
    current_level = start_keys
    while len(current_level) > 0:
        next_level = []
        for key in current_level:
            if key in end_keys:
                return backtrace(start, end, searched)
            if key in word_map:
                for neighbor in word_map[key]:
                    if neighbor in word_map:
                        if neighbor not in searched:
                            searched[neighbor] = key
                            next_level.append(neighbor)
        current_level = next_level

def backtrace(start, end, searched):
    start_keys = get_subwords(start)
    end_keys = get_subwords(end)
    word_list = [end]
    key = [x for x in end_keys if x in searched][0]
    while key not in start_keys:
        next_key = searched[key]
        word_list.append(assemble_word(key, next_key))
        key = next_key
    word_list.append(start)
    return list(reversed(word_list))

def assemble_word(key_1, key_2):
    word = ""
    for i in range(4):
        if key_1[i] != "_":
            word += key_1[i]
        else:
            word += key_2[i]
    return word

def subword(word, position):
    temp = list(word)
    temp[position] = '_'
    return "".join(temp)

def get_subwords(word):
    return [subword(word, x) for x in range(4)]
