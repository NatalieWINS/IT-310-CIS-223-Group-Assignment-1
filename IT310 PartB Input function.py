import math

def testPoly(sides, angles, SideNum):
    Perimeter = 0
    for x in range(0,SideNum):  # Positive side length check
        if sides[x] < 0:
            return False
    for x in range(0,SideNum):  # Perimeter calculation
        Perimeter = Perimeter + sides[x]
    for x in range(0,SideNum):  # Check if valid nondegenerate polygon
        if sides[x] >= (1/2) * Perimeter:
            return False
    if SideNum == 3: # Triangle Inequality Thm check (Triangles only)
        if sides[0] >= sides[1] + sides[2]:
            return False
        if sides[1] >= sides[0] + sides[2]:
            return False
        if sides[2] >= sides[0] + sides[1]:
            return False
    angleTotal = 0
    for x in range(0,SideNum):  # Angle total check
        angleTotal = angleTotal + angles[x]
    if angleTotal != 180 * (SideNum - 2):
        return False
    i = 0
    currentSide = sides[i]
    missingSide = 0
    currentAngle = angles[i]
    nextAngle = 0
    Area = 0
    while i < SideNum - 2:  # Test if angles paired with given sides produce a polygon, also calculate Area
        if i == SideNum - 3:
            missingSide = ((currentSide * currentSide) + (sides[0] * sides[0])) - (2 * currentSide * sides[0] * math.cos(math.radians(currentAngle)))  # Law of Cosines to find a diagonal
            missingSide = math.sqrt(missingSide)
            
            Semiperimeter = (currentSide + sides[i + 1] + sides[SideNum - 1])/2
            areaSquared = (Semiperimeter) * (Semiperimeter - currentSide) * (Semiperimeter - sides[i + 1]) * (Semiperimeter - sides[SideNum - 1])  # Heron's Formula to find Area of triangle formed by diagonal
            Area = Area + math.sqrt(areaSquared)
            
        else:
            missingSide = ((currentSide * currentSide) + (sides[i + 1] * sides[i + 1])) - (2 * currentSide * sides[i + 1] * math.cos(math.radians(currentAngle)))  # Law of Cosines to find a diagonal
            missingSide = math.sqrt(missingSide)
            
            Semiperimeter = (currentSide + sides[i + 1] + missingSide)/2
            areaSquared = (Semiperimeter) * (Semiperimeter - currentSide) * (Semiperimeter - sides[i + 1]) * (Semiperimeter - missingSide)  # Heron's Formula to find Area of triangle formed by diagonal
            Area = Area + math.sqrt(areaSquared)
            
            nextAngle = (sides[i + 1] * sides[i + 1]) + (missingSide * missingSide) - (currentSide * currentSide)  # Law of Cosines to find an angle
            nextAngle = nextAngle/(2 * sides[i + 1] * missingSide)
            nextAngle = math.acos(math.radians(nextAngle))
            nextAngle = math.degrees(nextAngle)
            
        currentAngle = angles[i + 1] - nextAngle
        currentSide = missingSide
        i = i + 1
    if (currentSide >= sides[SideNum - 1] + SideNum) or (currentSide <= sides[SideNum - 1] - SideNum):  # Check for if polygon is closed after previous test, with a threshold for error
        return False
    print('Perimeter:',Perimeter)
    print('Approximate Area:',Area)
    return True

# Main Program
sides=[]
angles=[]
while 1:
    side = input('Enter a side length in order (enter [Enter] to stop adding sides): ')
    if side == '':
        break
    sides.append(int(side))
SideNum = len(sides)
while 1:
    if SideNum == len(angles):
        break
    angle = input('Enter an angle in order (angle 1 formed by sides 1 and 2) in degrees: ')
    if angle == '':
        break
    angles.append(int(angle))

print(sides,angles,SideNum)
isValidPolygon = testPoly(sides,angles,SideNum)
if isValidPolygon != True:
    print('Please enter a valid Polygon.')
