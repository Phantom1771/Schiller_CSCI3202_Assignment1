#Justin Schiller
#AI 3202
#Test functions located at bottom of py file (lines 129-250)
import Queue
import random
class intQueue(Queue.Queue):
	def __init__(self):
		Queue.Queue.__init__(self)
	def put(self, value,*block,**timeout):
		if (isinstance(value,int)):
			Queue.Queue.put(self,value,block,timeout)
		else:
			print("Value is not an integer")
	def get(self,*block,**timeout):
		return Queue.Queue.get(self)
class stack:
	__stackData=[]
	def __init__(self):
		self.stackData=[]
	def push(self,value):
		self.stackData.append(value)
	def checkSize(self):
		count=0
		for item in self.stackData:
			count+=1
		return count
	def pop(self):
		size=self.checkSize()
		if size!=0:
			del self.stackData[-1]	
		else:
			print("Stack is already empty")
	
	
class node:
	__ik=0
	__lc=None
	__rc=None
	__p=None
	
	def __init__(self, intKey, leftChild, rightChild, parent):
		self.ik=intKey
		self.lc=leftChild
		self.rc=rightChild
		self.p=parent
	def getKey(self):
		return self.ik
	def getLeft(self):
		return self.lc
	def getRight(self):
		return self.rc
	def getParent(self):
		return self.p
	def setKey(self,key):
		self.ik=key
	def setLeft(self,left):
		self.lc=left
	def setRight(self,right):
		self.rc=right
	def setParent(self,parent):
		self.p=parent
	def printNodes(self):
		print(self.ik)
		if self.lc != None:
			self.lc.printNodes()
		if self.rc != None:
			self.rc.printNodes()
class binTree:
	__root=None
	__nl=[]
	def __init__(self, rootNode,nodeList):
		self.root=rootNode
		self.nl=nodeList
	
	def add(self,value,parentValue):
		for nodes in self.nl:
			if (nodes.getKey()==parentValue):
				if(nodes.getLeft()==None):
					newNode=node(value, None, None, nodes)
					self.nl.append(newNode)
					nodes.setLeft(newNode)
					return
				elif(nodes.getRight()==None):
					newNode=node(value, None, None, nodes)
					self.nl.append(newNode)
					nodes.setRight(newNode)
					return
				else:
					print("Parent has two children, node not added")
					return
		print("Parent not found")
		return
	
	def delete(self, value):
		for nodes in self.nl:
			if (nodes.getKey()==value):
				if((nodes.getRight()!=None) or (nodes.getLeft()!=None)):
					print("Node not deleted, has children")
					return
				else:
					if(nodes.getParent().getLeft()==nodes):
						nodes.getParent().setLeft(None)
					else:
						nodes.getParent().setRight(None)
					self.nl.remove(nodes)
					
					return
		print("Node not found")
		return
	
	def printish(self):
		self.root.printNodes()
		
class graph:
	__vertices={}
	def __init__(self):
		self.vertices={}
	def addVertex(self,value):
		if value not in self.vertices:
			self.vertices[value]=[]
		else:
			print("Vertex already exists")
			
	def addEdge(self,value1,value2):
		if ((value1 not in self.vertices) or (value2 not in self.vertices)):
			print("One or more vertices not found")
		elif value1 in self.vertices[value2]:
			print("Edge already exists")
		else:
			self.vertices[value1].append(value2)
			self.vertices[value2].append(value1)
			
	def findVertex(self,value):
		if value in self.vertices:
			print(value,self.vertices[value])
		else:
			print("Value does not exist in graph")
		
def testQueue():
	#create queue from python queue module
	testQueue=intQueue()
	#add 15 integers
	for x in range(1,16):
		z=random.randint(1,100)
		testQueue.put(z)
	#try to add a String
	testQueue.put("fish")
	#try to add a double
	testQueue.put(3.141592)
	#print and deque all integers
	for x in range(1,16):
		print (testQueue.get())
		
def testStack():
	#create a new instance of the stack class
	testStack=stack()
	#push 20 numbers to the stack in random order
	for x in range(1,21):
		z=random.randint(1,20)
		testStack.push(z)
	#print the resulting stack
	print(testStack.stackData)
	#pop and print the values with an extra pop to show behavior if trying to pop empty stack
	for x in range(1,22):
		size=testStack.checkSize()
		if size!=0:
			print (testStack.stackData[-1])
		testStack.pop()
		
def testTree():
	#create a root node with key of 1
	test=node(1,None, None, None)
	#create a binary tree containing only the root node
	testTree=binTree(test,[test])
	#add 15 successful nodes
	testTree.add(2,1)	
	testTree.add(8,1)
	testTree.add(3,2)	
	testTree.add(5,8)
	testTree.add(4,2)
	testTree.add(17,5)
	testTree.add(12,5)
	testTree.add(14,12)
	testTree.add(19,12)
	testTree.add(11,8)
	testTree.add(33,11)
	testTree.add(13,17)
	testTree.add(100,13)
	testTree.add(42,100)
	testTree.add(43,100)
	#try to add a node to a parent with two children
	testTree.add(22,100)
	#try to add a node to a parent that doesn't exist
	testTree.add(47,48)
	#print the tree
	testTree.printish()
	#delete 3 deletable nodes
	testTree.delete(43)
	testTree.delete(42)
	testTree.delete(33)
	#try to delete a node with children
	testTree.delete(2)
	#try to delete a node that does not exist
	testTree.delete(11111)
	#print tree
	testTree.printish()

def testGraph():
	#create a new graph
	testGraph=graph()
	#add 15 vertices
	testGraph.addVertex(10)
	testGraph.addVertex(20)
	testGraph.addVertex(30)
	testGraph.addVertex(40)
	testGraph.addVertex(50)
	testGraph.addVertex(60)
	testGraph.addVertex(70)
	testGraph.addVertex(80)
	testGraph.addVertex(90)
	testGraph.addVertex(100)
	testGraph.addVertex(110)
	testGraph.addVertex(120)
	testGraph.addVertex(130)
	testGraph.addVertex(140)
	testGraph.addVertex(150)
	#add a vertex that already exists
	testGraph.addVertex(20)
	#add 20 edges
	testGraph.addEdge(20,30)
	testGraph.addEdge(20,40)
	testGraph.addEdge(20,50)
	testGraph.addEdge(70,30)
	testGraph.addEdge(60,30)
	testGraph.addEdge(130,150)
	testGraph.addEdge(120,140)
	testGraph.addEdge(120,150)
	testGraph.addEdge(110,30)
	testGraph.addEdge(60,130)
	testGraph.addEdge(120,20)
	testGraph.addEdge(60,50)
	testGraph.addEdge(100,50)
	testGraph.addEdge(100,30)
	testGraph.addEdge(60,70)
	testGraph.addEdge(140,30)
	testGraph.addEdge(110,140)
	testGraph.addEdge(90,50)
	testGraph.addEdge(80,90)
	testGraph.addEdge(60,90)
	#add an edge with a vertex that doesn't exist
	testGraph.addEdge(10000,100)
	#add an edge that already exists
	testGraph.addEdge(20,30)
	#print graph
	print(testGraph.vertices)
	#find 5 vertices
	testGraph.findVertex(20)
	testGraph.findVertex(30)
	testGraph.findVertex(40)
	testGraph.findVertex(60)
	testGraph.findVertex(70)
	#find a vertex that doesn't exist
	testGraph.findVertex(200000)
							
def main():
	testQueue()
	print(" ")
	testStack()
	print(" ")
	testTree()
	print(" ")
	testGraph()
	

if  __name__ =='__main__':main()
