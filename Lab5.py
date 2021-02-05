import turtle


def svTree(trunkLength, depth):
    '''substring'''
    turtle.color("red")
    if(depth == 0):
        return
    turtle.forward(trunkLength)
    turtle.color("green")
    turtle.left(50)
    turtle.color("blue")
    svTree(trunkLength/2, depth-1)
    turtle.color("orange")
    turtle.right(100)
    turtle.color("pink")
    svTree(trunkLength/2, depth-1)
    turtle.color("black")
    turtle.left(50)
    turtle.color("purple")
    turtle.backward(trunkLength)
