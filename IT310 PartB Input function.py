def makePoly():
    sides=[]
    angles=[]
    while 1:
        side = input('Enter a side length (enter [Enter] to stop adding sides): ')
        if side == '':
            break
        sides.append(side)
    SideNum = len(sides)
    while 1:
        if SideNum == len(angles):
            break
        angle = input('Enter an angle: ')
        if angle == '':
            break
        angles.append(angle)

    print(sides,angles,SideNum)
makePoly()