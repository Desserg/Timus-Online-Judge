log = list(input() for _ in range(int(input())))

user = {}
login = []


for i in log:
    step = list(i.split(' '))
    
    if step[0] == "register":
        if step[1] in user:
            print("fail: user already exists")
        else:
            user[step[1]] = step[2]
            print("success: new user added")
            
    elif step[0] == "login":
        if user.get(step[1]) == step[2]:
            if (step[1] in login) == False:
                login.append(step[1])
                print("success: user logged in")
            else:
                print("fail: already logged in")
        else:
            if step[1] in user:
                print("fail: incorrect password")
            else:
                print("fail: no such user")
        
    elif step[0] == "logout":
        if (step[1] in user) and (step[1] in login):
            login.remove(step[1])
            print("success: user logged out")
        elif (step[1] in user) == False:
            print("fail: no such user")
        elif (step[1] in login) == False:
            print("fail: already logged out")