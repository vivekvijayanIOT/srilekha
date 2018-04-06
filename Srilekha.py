print("** Network Stimulation code starts **")
print("Network Developed: 15 nodes\n")
# VivekIOT - Python code : date-> 24-3-2018
# NS - Srilekha
import sys
import os
import time
import math
totalinc=0


secret_key="oiuw34h53qv5y0q9834yv50kq3984ugfvq90834mn5g9q348y"
home=[]
near=[]
element=[]
ec_xpos=[]
ec_ypos=[]
nodes=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
node_path=[]

clone_identified=[]
set_x=[]
set_y=[]

from collections import defaultdict

class Graph:
    inc=0
    def __init__(self,vertices):
        #No. of vertices
        self.V= vertices
        # default dictionary to store graph
        self.graph = defaultdict(list)
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path):
        global element
        global totalinc
        nodes=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
        visited[u]= True
        self.inc
        global element
        path.append(u)
        if u ==d:
            element.append([])
            for a in path:
#                print(nodes[a],sep=" ",end='->')
                element[self.inc].append(nodes[a])
            print("\n")
            totalinc=self.inc
            self.inc=self.inc+1
        else:
            for i in self.graph[u]:
                if visited[i]==False:
                    self.printAllPathsUtil(i, d, visited, path)
        path.pop()
        visited[u]= False

    def printAllPaths(self,s, d):
        visited =[False]*(self.V)
        path = []
        self.printAllPathsUtil(s, d,visited, path)


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
    key="82734698uy"
    def __init__(self,x_pos,y_pos,name):
        global update_x
        global update_y
        self.xpos=x_pos
        self.ypos=y_pos
        self.name=name

    def update_key(self,k):
        self.key=k
        print("Updated")

    def show_key(self):
        return self.key

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

# Main Execution




ranges=float(input("Enter the range to identify : "))
_main_fun(ranges)
show_my_table()
source_node=str(input("Enter the source node: "))
destination_node=str(input("Enter the destination node: "))

source_index=int(nodes.index(source_node))
dest_index=int(nodes.index(destination_node))

g = Graph(15)

for x,y in zip(home,near):
    g.addEdge(int(nodes.index(x)),int(nodes.index(y)))

s = source_node ; d = destination_node
print ("Following are all different paths from %s to %s :" %(s, d))
ww=[]
g.printAllPaths(source_index ,dest_index)
print("Setting up....\n\n")
try:
    print("The possible path from source to destination\n")
    for a in range(0,totalinc+1):
        for b in element[a]:
            print(b,end="-")
        print("\n")

    print("Finding shortest path")
    temp=100
    shortest_b_index=0
    for a in range(0,totalinc+1):
        temp_l=len(element[a])
        if(temp_l<temp):
            temp=temp_l
            shortest_b_index=element.index(element[a])

    print("\nShortest path is : \n")

    for b in element[shortest_b_index]:
        print(b,end="-")
    print("\n")
    print("\n")

except:
    print("NO route available => HINT: Change the range and retry !! ")
x_clone=100
y_clone=100
print("Do you want to add a clone node?")
choice=int(input("Enter 1 to add clone, 0 to do it without clone"))
if(choice==1):
    x_clone=int(input("Enter the xpos of clone"))
    y_clone=int(input("Enter the ypos of clone"))
    clone=node(x_clone,y_clone,"X")
    print("node generated")
    print("My default key:"+str(clone.key))

try:
    data=input("Enter the data to be transmited from NODE: :\n")
    # data encryption starts here
    # encryption ends here
    # @ node traversal
    node_path=list(element[shortest_b_index])
    last_node=destination_node
    print("Anchor node=> Distributed the key to "+str(source_node))
    print("KEY: "+str(secret_key))

    print ("\nStarting from Node "+str(node_path[0]))
    for node in node_path:
        if node != last_node:
            print ("\t----------NODE "+str(node)+"-----------")
            print ("\tNode number :"+str(int(node_path.index(node))+1))
            node_name=node.upper()
            obj=get_class(node_name)
            obj.setbuffer__(data)
            index=int(node_path.index(node))
            print("Distributing key to my neighbour: \n ****************")

            for a,b in zip(home,near):
                if(a==node):
                    ids=int(home.index(a))
                    class_name=get_class(b)
                    print("Sending key to node "+b+ ": Key => "+str(secret_key))
                    class_name.update_key(str(secret_key))
                    print("Getting back key : Success")
            if(x_clone<50):
                x1=obj.xpos
                y1=obj.ypos
                new_dist=float(math.sqrt((x_clone-x1)**2 + (y_clone-y1)**2))
                if(new_dist<ranges):
                    print("Getting back key: Failed \t Key :"+str(clone.key)+" doesnt match")
                    print("*** CLONE NODE IDENTIFIED ***")
                    clone_identified.append(node)

            print ("\tNode position: X = "+str(obj.xpos)+ " Y = "+str(obj.ypos))
            '''try:
                temp_id1=ec_xpos.index(obj.xpos)
                temp_id2=ec_ypos.index(obj.ypos)
                if temp_id1==temp_id2:
                    print ("\tFound in Elliptical curve")
                else:
                    print ("\tReplica node")

            except:
                print ("\tReplica node !!! Not in Elliptical curve")
                print ("\tData not sent to Destination\n\t\tSending Failed !")
                sys.exit()'''

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
            '''try:
                temp_id1=ec_xpos.index(obj.xpos)
                temp_id2=ec_ypos.index(obj.ypos)
                if temp_id1==temp_id2:
                    print ("\tFound in Elliptical curve")
                else:
                    print ("\tReplica node")

            except:
                print ("\tReplica node !!! Not in Elliptical curve")
                print ("\tData not sent to Destination\n\t\tSending Failed !")
                sys.exit()'''

            for a in range(0,20):
                b = "\t\tDecrypting [" + "*" * a +"]"
                print(b,end="\r")
                time.sleep(0.1)

            print("\n")
            print("Message recieved at destination:" +str(data))
            time_slot(1)
    print("Transimission successfull")
    if(len(clone_identified)>1):
        print("But Clone is identified at the range of ")
        for e in clone_identified:
            print("At node : "+str(e))
except:
    print("Transmission failed")
