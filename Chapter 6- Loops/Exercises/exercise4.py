sandwhich_order=["chicken","beef","pepproni","tuna"]
finished_sandwhich=[]
while sandwhich_order:
    current_sandwhich=sandwhich_order.pop()
    print("i am making your "+  current_sandwhich  +" sandwhich")
    finished_sandwhich.append(current_sandwhich)
    print("\n")
for sandwhich in finished_sandwhich:
    print("i made a " + sandwhich + " sandwhich")
