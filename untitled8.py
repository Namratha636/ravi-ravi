class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
def insertnode(root,value):
    if root.data==None:
        root.data=value
    elif value<root.data:
        if root.leftChild is None:
            root.leftChild=BSTNode(value)
        else:
            insertnode(root.leftChild,value)
    elif value>=root.data:
        if root.rightChild is None:
            root.rightChild=BSTNode(value)
        else:
            insertnode(root.rightChild,value)
            return str(value),"the Node as been successfully inserted"
def searchNode(root,value):
    if value<root.data:
        if root.leftChild is None:
            return str(value),"not found in the tree"
        
            
        