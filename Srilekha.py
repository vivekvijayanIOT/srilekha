print("** Network Stimulation code starts **")
# VivekIOT - Python code : date-> 24-3-2018
# NS - Srilekha
import sys
import os
import time
import math

home=[]
near=[]
ec_xpos=[]
ec_ypos=[]
nodes=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
node_path=[]

set_x=[]
set_y=[]

def action():
    try:
        for x in range(-20,21):
            ec_xpos.append(x)
            y=(x*x)-2
            ec_ypos.append(y)
        return True
    except:
        return False

def time_slot(times):
    time.sleep(times)

class node:
    xpos=0
    ypos=0
    data_buffer=""
    my_neigh=[]

    def __init__(self,x_pos,y_pos,name):
        global update_x
        global update_y
        self.xpos=x_pos
        self.ypos=y_pos
        self.name=name

    def add_node(self,n):
        self.my_neigh.append(n)

    def add_neigh(self,n):
        my_neigh.append(n)

    def setbuffer__(self,encrypt):
        self.data_buffer=encrypt

# Creating Ellipse
_init_=action()

# node initialisation
n1,n2,n3,n4,n5=node(0,-2,"A"),node(-1,-1,"B"),node(-2,2,"C"),node(-3,7,"D"),node(-4,14,"E")
n6,n7,n8,n9,n10=node(2,2,"F"),node(3,7,"G"),node(4,14,"H"),node(-2,9,"I"),node(2,14,"J")
n11,n12,n13,n14,n15=node(2,8,"K"),node(-1,3,"L"),node(4,2,"M"),node(-4,5,"N"),node(-3,14,"O")

objects=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15]

def get_class(name):
    class_ID=nodes.index(name)
    return objects[class_ID]

def show_my_table():
    global home
    global near
    for a in nodes:
        print("Node "+str(a)+" table:\n---------------------")
        for x,y in zip(home,near):
            if(x==a):
                print("\t"+x+" --> "+y)
        print("\n")
    file=open("table.html","w")
    top='''
    <html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
    <div class="container">
    <h2>Table maintained by the nodes</h2>
    '''

    middle=""
    for a in nodes:
        middle+="<h2 >Node "+str(a)+" table </h2>"
        middle+="<table class='table table-hover'><tr><th align='center'> Source </th> <th> Destination </th></tr>"
        for x,y in zip(home,near):
            if(x==a):
                middle+="<tr><td align='center'>"
                middle+=x+"</td>"
                middle+="<td>"
                middle+=y+"</td></tr>"
        middle+="</table>"
    end='''
    </body>
    </html>'''
    file.write(top)
    file.write(middle)
    file.write(end)
    file.close()

def _main_fun(ranges):
    global home
    global near
    #node neighbour identification
    if ranges<0:
        print ("Invalid range")
        sys.exit()
    else:
        for a in nodes:
            row_class=get_class(a)
            for b in nodes:
                if row_class!=b:
                    col_class=get_class(b)
                    x1=row_class.xpos
                    y1=row_class.ypos
                    x2=col_class.xpos
                    y2=col_class.ypos
                    dist=float(math.sqrt((x2-x1)**2 + (y2-y1)**2))
                    if dist < ranges and dist != 0.0:
                        row_class.add_node(b)
                        home.append(a)
                        near.append(b)
                        print(home)
                        print(near)

# Main Execution
print("\tNetwork Stimulation - Nodes : 15")
print("Enter the PATH from source to destination ( eg: a-b-c-d)")
node_path=input().split('-')
print("Reading node path.....")
time.sleep(1)
print("Status: ")
l=len(node_path)
q=set(node_path)
if len(q)==l:
    print ("\t* No cycle found")
    time.sleep(0.5)
    print ("\t* Number of nodes in path: "+str(l))
    time.sleep(0.5)
    print ("\t* SOURCE NODE : "+str(node_path[0]))
    time.sleep(0.5)
    print ("\t* DESTINATION NODE :"+str(node_path[l-1]))
else:
    print ("\t* Cycle path found ")
    sys.exit()
last_node=str(node_path[l-1])
print("\t* PATH EXPLORED\n")
ranges=float(input("Enter the range to identify"))
_main_fun(ranges)
show_my_table()
#print (n1.my_neigh)
'''
node_range=input("Enter the node range: ")
data=input("Enter the data to be transmited from NODE: "+str(node_path[0])+" to NODE: "+str(node_path[l-1])+" :\n")
# data encryption starts here


# encryption ends here
# @ node traversal
try:
    print ("\nStarting from Node "+str(node_path[0]))

    for node in node_path:
        if node != last_node:
            print ("\t----------NODE "+str(node)+"-----------")
            print ("\tNode number :"+str(int(node_path.index(node))+1))
            node_name=node.upper()
            obj=get_class(node_name)
            obj.setbuffer__(data)
            index=int(node_path.index(node))
            print ("\tNode position: X = "+str(obj.xpos)+ " Y = "+str(obj.ypos))
            try:
                temp_id1=ec_xpos.index(obj.xpos)
                temp_id2=ec_ypos.index(obj.ypos)
                if temp_id1==temp_id2:
                    print ("\tFound in Elliptical curve")
                else:
                    print ("\tReplica node")

            except:
                print ("\tReplica node !!! Not in Elliptical curve")
                print ("\tData not sent to Destination\n\t\tSending Failed !")
                sys.exit()

            print ("\tData sending to Node:"+str(node_path[index+1])+"")
            for a in range(0,20):
                b = "\t\tSending [" + "*" * a +"]"
                print(b,end="\r")
                time.sleep(0.1)
            print("\n")
            time_slot(1)
        else:
            print ("last node")
            print ("\t----------NODE "+str(node)+"-----------")
            print ("\tNode number :"+str(int(node_path.index(node))+1))
            node_name=node.upper()
            obj=get_class(node_name)
            obj.setbuffer__(data)
            index=int(node_path.index(node))
            print ("\tNode position: X = "+str(obj.xpos)+ " Y = "+str(obj.ypos))
            try:
                temp_id1=ec_xpos.index(obj.xpos)
                temp_id2=ec_ypos.index(obj.ypos)
                if temp_id1==temp_id2:
                    print ("\tFound in Elliptical curve")
                else:
                    print ("\tReplica node")

            except:
                print ("\tReplica node !!! Not in Elliptical curve")
                print ("\tData not sent to Destination\n\t\tSending Failed !")
                sys.exit()

            for a in range(0,20):
                b = "\t\tDecrypting [" + "+-" * a +"]"
                print(b,end="\r")
                time.sleep(0.1)
            print("\n")
            time_slot(1)
except:
    print("")
    '''
