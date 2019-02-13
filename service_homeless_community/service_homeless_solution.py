from collections import defaultdict
import operator
import sys
import time
import collections
start=time.time()
d=defaultdict(list)
class Node(object):
    def __init__(self, id_):
        self.id = id_
        self.children = []
        self.check_lst=[]
        self.del_lst=[]

    def __repr__(self):
        return "Node: [%s]" % self.id

    def add_child(self, node):
        self.children.append(node)

    def del_child(self,node):
        self.children.remove(node)

    def add_node(self,node):
        current_node = self.id
        self.check_lst.append(node)
        self.del_lst.append(node)

    def del_node(self,node):
        current_node = self.id
        self.del_lst.remove(node)

    def del_check(self,node):
        current_node=self.id
        self.check_lst.remove(node)

with open("test/input0215.txt") as f:
    input_file= f.readlines()
output_file=open("output.txt","w+")
t=3+int(input_file[2])
app= input_file[5+int(input_file[2])+int(input_file[t]) : len(input_file)]
lahsa_used=input_file[3: 3+int(input_file[2])]
lahsa_used_id = [i[0:5] for i in lahsa_used]
spla_used=input_file[4+int(input_file[2]) : 4+int(input_file[2])+int(input_file[t])]
spla_used_id=[i[0:5] for i in spla_used]
both=lahsa_used_id+spla_used_id
pool=[]
pool_sort=[]
ans_path=[]
total=-10000000000
total0=-1000000000
spla_ans={}
lahsa=[]
spla=[]
all_values=[]
all_values1=[]
ans_dict={}
backtrack=False
answer=[]
b=int(input_file[0])
p=int(input_file[1])
x=[]
y=[]
mon=mon1=tue=tue1=wed=wed1=thu=thu1=fri=fri1=sat=sat1=sun=sun1=0
for i in app:
    t=i[0:5]
    if t not in both:
        if i[5]=='F' and int(i[6:9])>17 and i[9]=='N' and i[10]=='N' and i[11]=='Y' and i[12]=='Y':
            pool.append(i)
        if i[5]=='F' and int(i[6:9])>17 and i[9]=='N':
            lahsa.append(i)
        if i[10]=='N' and i[11]=='Y' and i[12]=='Y':
            spla.append(i)
    if t in lahsa_used_id:
        t=i
        mon1=mon1+int(t[13])
        tue1=tue1+int(t[14])
        wed1=wed1+int(t[15])
        thu1=thu1+int(t[16])
        fri1=fri1+int(t[17])
        sat1=sat1+int(t[18])
        sun1=sun1+int(t[19])
    if t in spla_used_id:
        t=i
        mon= mon+int(t[13])
        tue=tue+int(t[14])
        wed=wed+int(t[15])
        thu=thu+int(t[16])
        fri=fri+int(t[17])
        sat=sat+int(t[18])
        sun=sun+int(t[19])

s1=mon
s2=tue
s3=wed
s4=thu
s5=fri
s6=sat
s7=sun

p1=p-s1
p2=p-s2
p3=p-s3
p4=p-s4
p5=p-s5
p6=p-s6
p7=p-s7

l1=mon1
l2=tue1
l3=wed1
l4=thu1
l5=fri1
l6=sat1
l7=sun1

b1=b-l1
b2=b-l2
b3=b-l3
b4=b-l4
b5=b-l5
b6=b-l6
b7=b-l7


def week_count(e):
    t= [int(k) for k in e[13:len(e)-1]]
    return sum(t)

if len(pool)==0:
    spla_sort=sorted(spla,key=week_count,reverse=True)
    A = Node("A")
    A.add_node(A)
    for i in spla_sort:
        A.add_child(Node(i))
    ptr=A
    while(len(A.del_lst)):
        count=1
        while(count):
            if len(ptr.children)==0:
                count=0
            for l in ptr.children:
                count=0
                if l not in A.check_lst:
                    count=1
                    A.add_node(l)
                    name=l.id
                    index=spla_sort.index(name)
                    for i in range(index+1,len(spla_sort)):
                        l.add_child(Node(spla_sort[i]))
                    ptr=l
                    break

        current=time.time()
        if current-start>170:
            output_file.write(min(answer)[0:5])
            sys.exit()
        mon=0
        tue=0
        wed=0
        thu=0
        fri=0
        sat=0
        sun=0
        for i in A.del_lst[1:len(A.del_lst)]:
                t=i.id
                if mon+int(t[13])<=p1 and tue+int(t[14])<=p2 and wed+int(t[15])<=p3 and thu+int(t[16])<=p4 and fri+int(t[17])<=p5 and sat+int(t[18])<=p6 and sun+int(t[19])<=p7:
                    mon= mon+int(t[13])
                    tue=tue+int(t[14])
                    wed=wed+int(t[15])
                    thu=thu+int(t[16])
                    fri=fri+int(t[17])
                    sat=sat+int(t[18])
                    sun=sun+int(t[19])
        total_temp = mon+tue+wed+thu+fri+sat+sun
        if total_temp>total:
            total=total_temp
            ans_path=[i.id for i in A.del_lst[1:len(A.del_lst)]]
            answer=ans_path
            #print(ans_path) #tree traversal
        if len(A.del_lst)>0:
            ptr=A.del_lst[-1]
            for i in ptr.children:
                A.del_check(i)
            A.del_node(A.del_lst[-1])
        if len(A.del_lst)>0:
            ptr=A.del_lst[-1]
            backtrack=True
            while(backtrack):
                for l in ptr.children:
                    if l not in A.check_lst:
                        backtrack=False
                if backtrack==True:
                    if len(A.del_lst)>0:
                        ptr=A.del_lst[-1]
                        for i in ptr.children:
                            A.del_check(i)
                        A.del_node(A.del_lst[-1])
                    if len(A.del_lst)>0:
                        if len(A.del_lst)==1:
                            ptr=A.del_lst[-1]
                current=time.time()
                if current-start>170:
                    output_file.write(min(answer)[0:5])
                    sys.exit()
else:
    mon=mon1=tue=tue1=wed=wed1=thu=thu1=fri=fri1=sat=sat1=sun=sun1=0
    pool_sort=sorted(pool,key=week_count,reverse=True)
    spla_sort=sorted(spla,key=week_count,reverse=True)
    lahsa_sort=sorted(lahsa,key=week_count,reverse=True)
    A = Node("A")
    A.add_node(A)
    for i in spla_sort:
        A.add_child(Node(i))
    ptr=A
    level=1
    while(len(A.del_lst)):
        count=1
        while(count):
            if len(ptr.children)==0:
                count=0
            for l in ptr.children:
                count=0
                if l not in A.check_lst:
                    count=1
                    A.add_node(l)
                    t=l.id
                    del_lst_nodes=[i.id for i in A.del_lst]
                    flag_lahsa=0
                    flag_spla=0
                    level=len(A.del_lst)
                    if level%2==0:
                        mon=mon+int(t[13])
                        tue=tue+int(t[14])
                        wed=wed+int(t[15])
                        thu=thu+int(t[16])
                        fri=fri+int(t[17])
                        sat=sat+int(t[18])
                        sun=sun+int(t[19])
                    else:
                        mon1=mon1+int(t[13])
                        tue1=tue1+int(t[14])
                        wed1=wed1+int(t[15])
                        thu1=thu1+int(t[16])
                        fri1=fri1+int(t[17])
                        sat1=sat1+int(t[18])
                        sun1=sun1+int(t[19])
                    flag_lahsa=flag_spla=0
                    if level%2==0:
                        for i in lahsa_sort:
                                if i not in del_lst_nodes:
                                    t=i
                                    if mon1+int(t[13])<=b1 and tue1+int(t[14])<=b2 and wed1+int(t[15])<=b3 and thu1+int(t[16])<=b4 and fri1+int(t[17])<=b5 and sat1+int(t[18])<=b6 and sun1+int(t[19])<=b7:
                                        flag_lahsa=flag_lahsa+1
                                        l.add_child(Node(i))
                        if flag_lahsa==0:
                            for i in spla_sort:
                                    if i not in del_lst_nodes:
                                        if mon+int(t[13])<=p1 and tue+int(t[14])<=p2 and wed+int(t[15])<=p3 and thu+int(t[16])<=p4 and fri+int(t[17])<=p5 and sat+int(t[18])<=p6 and sun+int(t[19])<=p7:
                                            l.add_child(Node("00000F020NNYY0000000"))
                                            break;
                    else:
                        for i in spla_sort:
                                if i not in del_lst_nodes:
                                    t=i
                                    if mon+int(t[13])<=p1 and tue+int(t[14])<=p2 and wed+int(t[15])<=p3 and thu+int(t[16])<=p4 and fri+int(t[17])<=p5 and sat+int(t[18])<=p6 and sun+int(t[19])<=p7:
                                        flag_spla=flag_spla+1
                                        l.add_child(Node(i))
                        if flag_spla==0:
                            for i in lahsa_sort:
                                    if i not in del_lst_nodes:
                                        if mon1+int(t[13])<=b1 and tue1+int(t[14])<=b2 and wed1+int(t[15])<=b3 and thu1+int(t[16])<=b4 and fri1+int(t[17])<=b5 and sat1+int(t[18])<=b6 and sun1+int(t[19])<=b7:
                                            l.add_child(Node("10000F020NNYY0000000"))
                                            break;
                    ptr=l
                    break

        total_temp0 = mon+tue+wed+thu+fri+sat+sun
        total_temp1= mon1+tue1+wed1+thu1+fri1+sat1+sun1

        if total_temp0>=total0:
            ans_path=[i.id for i in A.del_lst[1:len(A.del_lst)]]
            total0=total_temp0

        if total_temp1>=total:
            if total_temp1==total:
                total=total_temp1
                ans_path=[i.id for i in A.del_lst[1:len(A.del_lst)]]
                x.append(total_temp0)
                y.append(total_temp1)

            else:
                total=total_temp1
                ans_path=[i.id for i in A.del_lst[1:len(A.del_lst)]]
                del x[:]
                del y[:]
                x.append(total_temp0)
                y.append(total_temp1)


            #print(A.del_lst) #tree traversal
        current=time.time()
        if current-start>160:
            spla_ans.update({ans_path[0]:total0})
            ans_dict.update({ans_path[0]:max(x)})
            del A.del_lst[:]
            break
        if len(A.del_lst)>0:
            ptr=A.del_lst[-1]
            for i in ptr.children:
                A.del_check(i)
            l=len(A.del_lst)
            t=ptr.id
            if len(A.del_lst)>1:
                if l%2==0:
                    mon=mon-int(t[13])
                    tue=tue-int(t[14])
                    wed=wed-int(t[15])
                    thu=thu-int(t[16])
                    fri=fri-int(t[17])
                    sat=sat-int(t[18])
                    sun=sun-int(t[19])
                else:
                    mon1=mon1-int(t[13])
                    tue1=tue1-int(t[14])
                    wed1=wed1-int(t[15])
                    thu1=thu1-int(t[16])
                    fri1=fri1-int(t[17])
                    sat1=sat1-int(t[18])
                    sun1=sun1-int(t[19])

            A.del_node(A.del_lst[-1])
        if len(A.del_lst)>0:
            if len(A.del_lst)==1:
                spla_ans.update({ans_path[0]:total0})
                total0=-100000000
                mon=mon1=tue=tue1=wed=wed1=thu=thu1=fri=fri1=sat=sat1=sun=sun1=0
                ans_dict.update({ans_path[0]:max(x)})

                total=-100000000
                del x[:]
                del y[:]
            ptr=A.del_lst[-1]
            backtrack=True
            while(backtrack):
                for l in ptr.children:
                    if l not in A.check_lst:
                        backtrack=False
                if backtrack==True:
                    if len(A.del_lst)>0:
                        ptr=A.del_lst[-1]
                        for i in ptr.children:
                            A.del_check(i)
                        l=len(A.del_lst)
                        temp=A.del_lst[-1]
                        t=temp.id
                        if len(A.del_lst)>1:
                            if l%2==0:
                                mon=mon-int(t[13])
                                tue=tue-int(t[14])
                                wed=wed-int(t[15])
                                thu=thu-int(t[16])
                                fri=fri-int(t[17])
                                sat=sat-int(t[18])
                                sun=sun-int(t[19])

                            else:
                                mon1=mon1-int(t[13])
                                tue1=tue1-int(t[14])
                                wed1=wed1-int(t[15])
                                thu1=thu1-int(t[16])
                                fri1=fri1-int(t[17])
                                sat1=sat1-int(t[18])
                                sun1=sun1-int(t[19])

                        A.del_node(A.del_lst[-1])
                    if len(A.del_lst)>0:
                        if len(A.del_lst)==1:
                            spla_ans.update({ans_path[0]:total0})
                            total0=-100000000
                            mon=mon1=tue=tue1=wed=wed1=thu=thu1=fri=fri1=sat=sat1=sun=sun1=0
                            total=-100000000
                            ans_dict.update({ans_path[0]:max(x)})

                            del x[:]
                            del y[:]
                        ptr=A.del_lst[-1]
                current=time.time()
                if current-start>160:
                    spla_ans.update({ans_path[0]:total0})
                    ans_dict.update({ans_path[0]:max(x)})
                    del A.del_lst[:]
                    backtrack=False
                    break


if len(answer)>0:
    output_file.write(min(answer)[0:5])
    sys.exit()

count=0
i=spla_ans
maximum_value=-10000000
for j in i:
    if i[j]>maximum_value:
        maximum_value=i[j]

key_list=[]
for j in i:
    if i[j]==maximum_value:
        count=count+1
        key_list.append(j)

if count==1:
    output_file.write(key_list[0][0:5])

if count>1:

    i=ans_dict
    dele=[]
    for j in i:
        if j not in key_list:
            dele.append(j)

    for k in dele:
        i.pop(k)

    maximum_value=-10000000
    for j in i:
        if i[j]>maximum_value:
            maximum_value=i[j]

    to_delete=[]
    for j in i:
        if i[j]!=maximum_value:
            to_delete.append(j)

    for j in to_delete:
        i.pop(j)
    output_file.write(min(i)[0:5])
