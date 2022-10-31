
class Node:
    def __init__(self,key,val):
        self.key,self.val = key ,val
        self.prev = self.next =None
class LRUCache:
    def __init__(self,capacity:int):
        self.cap =capacity
        self.cache ={}

        self.left, self.right =Node(0,0), Node(0,0)
        #connecting two nodes doubly 
        self.left.next , self.right.prev= self.right,self.left

        #remove node from list
    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next,nxt.prev = nxt,prev

    def insert(self,node):
        prev,nxt = self.right.prev,self.right
        prev.next=nxt.prev=node
        node.next,node.prev=nxt,prev
         

    def put(self,key:int,value:int):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        #check the len(cache) after inserting, if len exceeds capacity then evict lru
        if len(self.cache)>self.cap:
            lru =self.left.next
            self.remove(lru)
            del self.cache[lru.key]



    def get(self,key:int):
        if key in self.cache:
            #make this node as most recent by removing and re-inserting at right
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
