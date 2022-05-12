def solution(phone_book):
    answer = {}
    phone_book.sort(key = lambda x : len(x))
    for phone in phone_book:
        num = ""
        for i in phone:
            num += i
            if num in answer :
                return False
            elif num == phone :
                answer[num] = True
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["1","123","1235","567","88"]))