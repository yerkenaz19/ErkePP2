def solve(numheads, numlegs):
    num_chicks=0
    num_rabbits=0
    for i in range(1, numheads+1):
        num_chicks=i
        num_rabbits=numheads - i
        if(num_chicks*2 + num_rabbits*4==numlegs):
            break
        
    print(f"Number of rabbits={num_rabbits} and Number of chicks ={num_chicks}")
solve(35,94)