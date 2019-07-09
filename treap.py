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
        '''Rotates the subtree to the left.'''
        newParent = node.right
        tmp = newParent.left
        newParent.left = node
        newParent.left.right = tmp
        return newParent


    def rightRot(self,node):
        '''Rotates the subtree to the right.'''
        newParent = node.left
        tmp = newParent.right
        newParent.right = node
        newParent.right.left = tmp
        return newParent

    def add(self,e):
        '''Inserts element into the tree'''
        self.count+=1
        if self.root is None:
            self.root =Node(e)
        else:
            self.root=self.__add(e,self.root)

    def __add(self,e,refNode):
        if refNode is None:
            return Node(e)
        elif e<refNode.data:
            refNode.left = self.__add(e,refNode.left)
            if refNode.left.priority>refNode.priority:
                return self.rightRot(refNode)
        else:
            refNode.right = self.__add(e,refNode.right)
            if refNode.right.priority>refNode.priority:
                return self.leftRot(refNode)
        return refNode

    def __contains__(self,element):
        '''Checks if the element is in the tree'''
        return self.__contains(self.root,element)

    def __contains(self,refNode,element):
        if (refNode==None): #BASE CASE: EMPTY SPOT
            return False
        elif (refNode.data == element):
            return True
        if (element<refNode.data):
            return self.__contains(refNode.left,element)
        elif (element>refNode.data):
            return self.__contains(refNode.right,element)
        else:
            return False

    def height(self):
        '''Used for determining the height of the tree'''
        return self.__height(self.root)

    def __height(self,node):
        if node is None:
            return 0
        else:
            return 1+max(self.__height(node.left),self.__height(node.right))

    def __len__(self):
        '''Returns the number of items in tree'''
        return self.count
