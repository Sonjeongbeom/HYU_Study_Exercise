import re

# 1단계
def first(id) : 
    id = id.lower()
    # print("1단계 : " + id)
    return id

# 2단계
def second(id) : 
    id = re.sub(r"[^a-z0-9-_.]", "", id)
    # print("2단계 : " + id)
    return id

# 3단계
def third(id) : 
    for i in range(len(id)) :
        if ".." in id :
            id = id.replace("..", ".")
    # print("3단계 : " + id)
    return id

# 4단계
def fourth(id) : 
    if len(id) > 0 and id[0] == "." :
        id = id[1:]
    if len(id) > 0 and id[-1] == "." :
        id = id[:-1]   
    # print("4단계 : " + id)
    return id

# 5단계
def fifth(id) : 
    if len(id) == 0 :
        id = id.replace("", "a")
    # print("5단계 : " + id)
    return id

# 6단계
def sixth(id) : 
    if len(id) >= 16 :
        id = id[0:15]
        if id[-1] == "." :
            id = id[:-1]
    # print("6단계 : " + id)
    return id

# 7단계 : 
def seventh(id) : 
    if len(id) <= 2:
        while (len(id) < 3) :
            id += id[-1]
    # print("7단계 : " + id)
    return id


def solution(new_id):
    id = new_id
    id = first(id)
    id = second(id)
    id = third(id)
    id = fourth(id)
    id = fifth(id)
    id = sixth(id)
    id = seventh(id)

    answer = id

    return answer

# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))
