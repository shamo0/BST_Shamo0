#!/usr/bin/env python3
import random
import sys

class Node:
    def __init__(self, data) :
        '''Initialize Node with data.'''
        self.data = data
        self.left = None
        self.right = None
        self.priority = random.random()

    def __str__(self) :
        '''Return string representation of data.'''
        return str(self.data)

class TreapSet:
    def __init__(self):
        self.root = None
        self.count = 0

    def leftRot(self,node):
        right = node.right
        node.right.left = right.left
        right.left= node
        node.right= node.right.left
        return right

    def rightRot(self,node):
        left = node.left
        node.left.right = left.right
        left.right= node
        node.left= node.left.right
        return left
    #
    # def balance(self,refNode):
    #     print("in")
    #     if refNode.left is None and refNode.right is None:
    #         return
    #     if refNode.left.priority<refNode.priority:
    #         refNode=self.rightRot(refNode)
    #         return balance(refNode)
    #     elif refNode.right.priority>refNode.priority:
    #         refNode=self.leftRot(refNode)
    #         return balance(refNode)
    #     return refNode

    
    # def moveUp(self,node,parent):
    #     if parent == None:
    #         return
    #     if parent != None and node.priority >= parent.priority:
    #         return
    #     if node == parent.left:
    #         self.rightRot(parent)
    #     else:
    #         self.leftRot(parent)

    def add(self,e):
        self.count+=1
        self.root=self.__add(e,self.root)

    def __add(self,e,refNode):
        new = Node(e)
        if refNode==None:
            newNode = new
            return new
        if refNode.data==e:
            return refNode
        if e<refNode.data:
            refNode.left = self.__add(e,refNode.left)
            refNode=self.moveUp(refNode.left,refNode)
            # if refNode.left.priority<refNode.priority:
            #     refNode=self.rightRot(refNode)
        else:
            refNode.right = self.__add(e,refNode.right)
            refNode=self.moveUp(refNode.right,refNode)
            # if refNode.right.priority<refNode.priority:
            #     refNode=self.leftRot(refNode)
        return refNode

    def __contains__(self,element):
        return self.__contains(self.root,element)

    def __contains(self,refNode,element):
        if (refNode==None): #BASE CASE: EMPTY SPOT
            return None
        elif (refNode.data == element):
            return True
        if (element<refNode.data):
            return self.__contains(refNode.left,element)
        elif (element>refNode.data):
            return self.__contains(refNode.right,element)
        else:
            return False

    def child(self, nodes):
        children = []
        for node in nodes:
            if node.left is not None:
                children.append(node.left)
            if node.right is not None:
                children.append(node.right)
        return children

    def height(self):
        if self.root is None:
            return 0
        height = 0
        nodes = [self.root]
        while len(nodes):
            height+=1
            nodes = self.child(nodes)
        return height

    def __len__(self):
        return self.count
