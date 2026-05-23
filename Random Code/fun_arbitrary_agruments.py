
def Show(**colors):   #when we use arbitrary arguments **, actually we are passing dictionary

    print(colors["c1"])
    print(colors["c2"])
    print(colors["c3"])


Show(c1='Red', c2='Green', c3='yellow')
