def solution(word) :

    result = ""
    length = []
    
    if len(word) == 1 :
        return 1

    for i in range(1, len(word)//2+1) :
        cnt = 1
        cut = word[0:i]
        for j in range(i, len(word), i) :
            if word[j:j+i] == cut :
                cnt += 1
            else :
                if cnt == 1 :
                    cnt = ""
                result += str(cnt) + cut
                cut = word[j:j+i]
                cnt = 1
        if cnt == 1 :
            cnt = ""
        result += str(cnt) + cut
        length.append(len(result))
        result = ""

    return min(length)
