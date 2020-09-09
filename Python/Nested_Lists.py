# marksheet and scorelist declartion
marksheet=[]
scorelist=[]

if __name__ == '__main__':

        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet.append([name,score])
                scorelist.append(score)

        # extration of second most greated marks
        # we here converting set to list as set elements are not indexed
        score_max = sorted(list(set(scorelist)))[1] 
        
        # here we are sorting the marksheet by the order n(name) and s(score).
        for n,s in sorted(marksheet):
             # if the score is same as score_max 
             if s == score_max:
                    print(n)
