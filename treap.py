#!/usr/bin/env python3
import random
import sys

class Node:
    def __init__(self, data,priority) :
        '''Initialize Node with data.'''
        self.data = data
        self.left = None
        self.right = None
        self.priority = priority

    def __str__(self) :
        '''Return string representation of data.'''
        return str(self.data)

class TreapSet:
    def generate():
        return random.random(0,1)

    def __init__(self):
        self.root = None

    def leftRot(self,node):
        right = node.right
        node.right.left = right.left
        right.left= node
        node.right= node.right.left
        return right

    def rightRot(self):
        left = node.left
        node.left.right = left.right
        left.right= node
        node.left= node.left.right
        return left

    def add(self,e):
        self.root = self.__add(e,self.root,parent=None)

    def __add(self,e,refNode,parent):
        new = Node(e,self.generate())
        if refNode==None:
            self.root=new
            return
        if refNode.data==e:
            return refNode
        if e<refNode.data:
            refNode.left = self.__add(e,refNode.left,refNode)
        else:
            refNode.right = self.__add(e,refNode.right,refNode)
        return refNode

    def __contains__(self,element):
        return self.__contains(self.__root,element)

    def __contains(sright.leftelf,refNode,element):
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

    def __len__(self):
        ...

    def height(self):
        ...
