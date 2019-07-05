#!/usr/bin/env python3

class Node:
    def __init__(self, data) :
        '''Initialize Node with data.'''
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) :
        '''Return string representation of data.'''
        return str(self.data)

class TreeSet:
    def __init__(self):
        self.__root = None

    def insert(self,phrase):
        self.__root = self.__insert(self.__root,phrase)

    def __insert(self,refNode,phrase):
        if (refNode==None): #Base Case:empty spot
            newNode = Node(phrase)
            return newNode
        if (refNode.data == phrase): #Base Case: Already in BST
            return refNode
        if (phrase<refNode.data):
            refNode.left = self.__insert(refNode.left,phrase)
        else:
            refNode.right = self.__insert(refNode.right,phrase)
        return refNode

    def __contains__(self,phrase):
        return self.__contains(self.__root,phrase)

    def __contains(self,refNode,phrase):
        if (refNode==None): #BASE CASE: EMPTY SPOT
            return None
        elif (refNode.data == phrase):
            return True
        if (phrase<refNode.data):
            return self.__contains(refNode.left,phrase)
        elif (phrase>refNode.data):
            return self.__contains(refNode.right,phrase)
        else:
            return False
