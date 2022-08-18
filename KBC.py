question=["Q.1-:what is capitial of india","Q.2-:what is national animal of india","Q.3-:what is national bird of india","Q.4-:what is capital of maharashtra"]
options=[["A - new delhi","B - kolkata","C - chandigarh","D - pune"],
        ["A-lion","B-elephant","C-tiger","D-dog"],
        ["A-parrot","B-peacock","c-duck","D-crow"],
        ["A-mumbai","B-pune","C-ahemadnagar","D-beed"]]
line=[["A-new delhi","B-kolkata"],
       ["C-tiger","A-lion"],
       ["B-peacock","A-parrot"],
       ["A-mumbai","B-pune"]]
answer=["A","C","B","A"]
i=0
c=0
s=0
while i<len(question):
    print(question[i])
    j=0
    while j<len(options):
        print(j+1,options[i][j])
        j=j+1
    life_line=input("do you want to take life line yes/no")
    if life_line=="yes":
        if c==0:
            k=0
            while k<len(line[i]):
                print(line[i][k])
                s=s+1000
                k=k+1
            ans=input("enter your answer")
            if answer[i]==ans:
                print("correct option")
                s=s+1000
            else:
                print("incorrect answer")
                break
            c=c+1
        else:
            print("!you can use lifeline once!#")
            ans=input("enter your answer")
            if answer[i]==ans:
                print("correct answer")
                s=s+1000
            else:
                print("incorrect answer")
                break
    else:
        ans=input("enter your answer")
        if answer[i]==ans:
            print("correct answer")
            s+=1000
        else:
            print("incorrect answer")
            break
    i+=1