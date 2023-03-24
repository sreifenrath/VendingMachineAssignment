
table = [
    #d|q|D|C
    [1,3,0,0], # currentBin = 0 (state 0)
    [2,5,1,0],  # currentBin = 10 (state 1)
    [4,7,2,0], # currentBin = 20 (state 2)
    [5,8,3,0], # currentBin = 25 (state 3)
    [6,8,4,0],  # currentBin = 30 (state 4)
    [7,8,5,0],  # currentBin = 35 (state 5)
    [8,8,6,0], # currentBin = 40 (state 6)
    [8,8,7,0],  # currentBin = 45 (state 7)
    [8,8,0,0]  # currentBin >= 50 (state 8)
]

output = [
    ["Bin = 10","Bin = 25","Not enough coins for dispense","Canceled. Returned all coins in currentBin"],
    ["Bin = 20","Bin = 35","Not enough coins for dispense","Canceled. Returned all coins in currentBin"],
    ["Bin = 30","Bin = 45","Not enough coins for dispense","Canceled. Returned all coins in currentBin"],
    ["Bin = 35","Bin >= 50","Not enough coins for dispense","Canceled. Returned all coins in currentBin"],
    ["Bin = 40","Bin >= 50","Not enough coins for dispense","Canceled. Returned all coins in currentBin"],
    ["Bin = 40","Bin >= 50","Not enough coins for dispense","Canceled. Returned all coins in currentBin"],
    ["Bin >= 50","Bin >= 50","Not enough coins for dispense","Canceled. Returned all coins in currentBin"],
    ["Bin >= 50","Bin >= 50","Not enough coins for dispense","Canceled. Returned all coins in currentBin"],
    ["Bin >= 50","Bin >= 50","Dispense product. Empty bin to bank","Canceled. Returned all coins in currentBin"]
]

state = 0 # currentBin = 0 is init state
while(True) :
    cmd = (input('Enter cmd: d = dime, q = quarter, D = dispense product, C = cancel : \n'))
    if(cmd == 'd') :
        cmd = int(0)
    elif(cmd =='q') :
        cmd = int(1)
    elif(cmd == 'D') :
        cmd = int(2)
    elif(cmd == 'C') :
        cmd = int(3)
    else :
        print("Invalid command")
    print(output[state][cmd])
    state = table[state][cmd]

