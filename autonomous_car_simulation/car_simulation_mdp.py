import numpy as np

with open("input.txt") as f:
    input_file= f.readlines()

output_file=open("output.txt","w+")

size=int(input_file[0])
no_of_cars=int(input_file[1])
no_of_obstacles= int(input_file[2])

obstacles=[]
car_start_loc=[]
car_end_loc=[]


for k in range(3+no_of_obstacles, 3+no_of_obstacles+no_of_cars):
    car_start_loc.append(input_file[k])

for k in range(3+no_of_obstacles+no_of_cars, 3+no_of_obstacles+(2*no_of_cars)):
    car_end_loc.append(input_file[k])

directions=["no","no","no","no"]

def wall(row,col):
    directions=["no","no","no","no"]
    if row== 0:
        directions[0]="yes"
    if row==size-1:
        directions[1]="yes"
    if col==0:
        directions[2]="yes"
    if col==size-1:
        directions[3]="yes"
    return directions

def valid(row,col):
    if row<0:
        return False
    elif row>size-1:
        return False
    elif col<0:
        return False
    elif col>size-1:
        return False
    else:
        return True
final_answer=[]
grid=  np.full((size,size), -1.0, dtype = 'float')

for k in range(3,3+no_of_obstacles):
    temp=input_file[k].split(",")
    i=int(temp[0])
    j=int(temp[1])
    grid[i][j]=-101
    obstacles.append(str(i)+str(j))

for z in range(no_of_cars):

    grid=  np.full((size,size), -1, dtype = 'float')
    temp=car_end_loc[z].split(",")
    i=int(temp[0])
    j=int(temp[1])
    grid[i][j]=99
    destination=str(i)+str(j)

    #____________policy_______________--
    prev=np.copy(grid)
    k=1
    while(1):
        for i in range(size):
            for j in range(size):
                current1=str(i)+str(j)
                if not destination==current1:
                        determine_wall=wall(i,j)

                        if determine_wall[0]=="yes":
                            up= prev[i][j]
                        else:
                            up=prev[i-1][j]

                        if determine_wall[1]=="yes":
                            down= prev[i][j]
                        else:
                            down=prev[i+1][j]

                        if determine_wall[2]=="yes":
                            left= prev[i][j]
                        else:
                            left=prev[i][j-1]

                        if determine_wall[3]=="yes":
                            right= prev[i][j]
                        else:
                            right=prev[i][j+1]

                        #vup=   (0.7* up) +  (0.1* (down+right+left))
                        #vdown=    (0.7* down) +(0.1* (up+right+left))
                        #vleft=   (0.7* left) +(0.1* (up+down+right))
                        #vright=   (0.7* right) + (0.1* (up+down+left))

                        vup=   (0.7* up) +  (0.1* down) + (0.1*left) + (0.1*right)
                        vdown=    (0.7* down) +(0.1* up) + (0.1*left) + (0.1*right)
                        vleft=   (0.7* left) +(0.1* up) + (0.1* down) + (0.1*right)
                        vright=   (0.7* right) + (0.1* up) + (0.1* down) + (0.1*left)


                        if str(i)+str(j) in obstacles:
                            maximum= np.float64(-101) + np.float64((0.9 * max(vup,vdown,vleft,vright)))
                        else:
                            maximum= np.float64(-1) + np.float64(( 0.9 * max(vup,vdown,vleft,vright)))

                        grid[i][j]=maximum

        current=np.copy(grid)
        k=k+1
        #((0.1*0.1)/0.9)
        if ((current-prev)<=0.1*0.1/0.9).all() :
            break
        prev=np.copy(current)

    ans_list=[]
    #print(grid)
    #------------seed--------------

    for m in range(10):
        ans=1
        directions=["no","no","no","no"]
        temp= car_start_loc[z].split(",")
        i_new=int(temp[0])
        j_new=int(temp[1])
        source=str(i_new)+str(j_new)
        np.random.seed(m)
        swerve=np.random.random_sample(1000000)
        k=0
        while(1):
            i=i_new
            j=j_new

            if source==destination and source in obstacles:
                ans=0
                ans_list.append(ans)
                break

            if source==destination:
                ans=100
                ans_list.append(ans)
                break

            if str(i)+str(j)==destination:
                ans=ans+grid[i][j]
                ans_list.append(ans)
                break


            determine_wall=wall(i,j)
            if str(i)+str(j) in obstacles:
                ans=ans-101
            else:
                ans=ans-1

            value=-10000

            if determine_wall[0]=="no":
                i0=i-1
                value0=grid[i0][j]
                if value<=value0:
                    value=value0
                    i_new=i0
                    j_new=j
            else:
                i0=i-1
                value0=grid[i][j]
                if value<=value0:
                    value=value0
                    i_new=i0
                    j_new=j


            if determine_wall[1]=="no":
                i1=i+1
                value1=grid[i1][j]
                if value<=value1:
                    value=value1
                    i_new=i1
                    j_new=j
            else:
                i1=i+1
                value1=grid[i][j]
                if value<=value1:
                    value=value1
                    i_new=i1
                    j_new=j


            if determine_wall[3]=="no":
                j3=j+1
                value3=grid[i][j3]
                #if str(i)+str(j3)==destination:
                    #ans=ans+value3
                    #print(ans)
                    #break
                if value<=value3:
                    value=value3
                    i_new=i
                    j_new=j3
            else:
                j3=j+1
                value3=grid[i][j]
                if value<=value3:
                    value=value3
                    i_new=i
                    j_new=j3

            if determine_wall[2]=="no":
                j2=j-1
                value2=grid[i][j2]
                if value<=value2:
                    value=value2
                    i_new=i
                    j_new=j2
            else:
                j2=j-1
                value2=grid[i][j]
                if value<=value2:
                    value=value2
                    i_new=i
                    j_new=j2




            if swerve[k]>0.7:
                i_top=i_new-i
                j_left=j_new-j
                if swerve[k]>0.8:
                    if swerve[k]>0.9:
                        if i_top<0:
                            i_new=i_new+2
                        elif i_top>0:
                            i_new=i_new-2
                        elif j_left<0:
                            j_new=j_new+2
                        elif j_left>0:
                            j_new=j_new-2
                        else:
                            pass

                    else:
                        if i_top<0:
                            i_new=i_new+1
                            j_new=j_new-1
                        elif i_top>0:
                            i_new=i_new-1
                            j_new=j_new+1
                        elif j_left<0:
                            i_new=i_new+1
                            j_new=j_new+1
                        elif j_left>0:
                            i_new=i_new-1
                            j_new=j_new-1
                        else:
                            pass

                else:
                    if i_top<0:
                        i_new=i_new+1
                        j_new=j_new+1
                    elif i_top>0:
                        i_new=i_new-1
                        j_new=j_new-1
                    elif j_left<0:
                        i_new=i_new-1
                        j_new=j_new+1
                    elif j_left>0:
                        i_new=i_new+1
                        j_new=j_new-1
                    else:
                        pass


            if not valid(i_new,j_new):
                i_new=i
                j_new=j


                #ans=ans-100
            k=k+1


    final_ans= int(np.floor(sum(ans_list)/ len(ans_list)))

    final_answer.append(final_ans)
    del ans_list[:]


for i in final_answer:
    if i== final_answer[-1]:
        output_file.write(str(i))
    else:
        output_file.write(str(i)+"\n")

print(final_answer)
