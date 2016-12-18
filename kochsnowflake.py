import turtle
bob = turtle.Turtle()
print(bob)

dic1 = {'a': 1, 'b': 2, 'c': 1, 'd': 1}
dic2 = {'a': 1, 'b': 2, 'c': 1, 'd': 2}
dic0 = {'a': 2}

def passando(dic):
    new_mod = {}
    for i in sorted(dic.keys()):
        if dic[i] == 1:
            new_mod[i] = dic1
        elif dic[i] == 2:
            new_mod[i] = dic2
        else:
            new_mod[i] = passando(dic[i])
    return new_mod



def instru(t,x,dic):
    for i in ['a', 'b', 'c', 'd']:
        if dic[i] == 1:
            t.fd(x)
            t.lt(60)
        elif dic[i] == 2:
            t.fd(x)
            t.rt(120)
        else:
            instru(t,x,dic[i])


def snowflake(n,t=bob,x=5,dic=dic2):
    nova = dic
    for i in range(n):
        nova = passando(nova)
    for i in range(3):
        instru(t,x,nova)


bob.pu()
bob.goto(-400,100)
bob.pd()

snowflake(int(input('How many iterations? '))-1)


turtle.mainloop()
