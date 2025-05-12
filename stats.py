def prnt_lst(entrys):
    for entry in entrys:
        print(entry)

def get_num_words(filec):
    l_str_wrd = len(filec.split())
    return l_str_wrd

def get_num_chars(filec):
    char_counts = {}
    charfls = filec.lower()
    for char in charfls:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    # return char_counts
    # char_sorts = sorted(char_counts, key = char_counts.get, reverse = False)
    # sort() ascending items
    # char_sorts = {k: v for k, v in sorted(char_counts.items(), key=lambda item: item[1])}
    # sort() reversed items
    char_sorts = {k: v for k, v in sorted(char_counts.items(), key=lambda item: item[1], reverse=True)}
    return char_sorts
    # srtd_cnt = []
    # tmps = list(char_count)
    # # tmps = sorted(dic_chars, key = dic_chars.get, reverse = False)
    # l = len(tmps)
    # for i in range(0, l, 2):
    #     # n = tmps.get(tmp)
    #     dic_each = {"char":tmps[i], "nums":tmps[i + 1]}
    #     # dic_each["char"] = tmp # assignment not supported
    #     # dic_each["nums"] = tmps[tmp]
    #     srtd_cnt.append(dic_each)
    #     del dic_each["char"]
    #     del dic_each["nums"]
    # return srtd_cnt


# def sort_char_count(dic_chars):
#     # print(dic_chars)
#     srtd_cnt = []
#     # tmps = sorted(dic_chars, key = dic_chars.get, reverse = False)
#     tmps = list(dic_chars)
#     # print(type(tmps))
#     # print(tmps)
#     l = len(tmps)
#     for i in range(0, l, 2):
#         # n = tmps.get(tmp)
#         dic_each = {"char":tmps[i], "nums":tmps[i + 1]}
#         print(dic_each)
#         # dic_each["char"] = tmp # assignment not supported
#         # dic_each["nums"] = tmps[tmp]
#         srtd_cnt.append(dic_each)
#         del dic_each["char"]
#         del dic_each["nums"]
#     return srtd_cnt

# def get_num_chars(filec):
#     char_count = {}
#     for char in filec.lower():
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     # return char_count
#     return sort_char_count(char_count)
