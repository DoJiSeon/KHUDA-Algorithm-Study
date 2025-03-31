def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == p1[i%len(p1)]:
            scores[0] += 1
        if answers[i] == p2[i%len(p2)]:
            scores[1] += 1
        if answers[i] == p3[i%len(p3)]:
            scores[2] += 1
    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i + 1)
    return answer
