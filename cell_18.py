#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class stack:

  def __init__(self):
    self.stack = []
    self.TOS = -1
    self.x = 0
    print("class stack activated")

  def size(self,size):
    self.stack = [None] * size

  def push(self,data):
    self.TOS +=1
    self.stack[self.TOS] = data

  def pop(self):
    while self.TOS > -1:
      self.x = self.stack[self.TOS]
      self.TOS -=1
      self.stack[self.TOS+1] = None
      return self.x

  def status(self):
    return self.stack

s = stack()
y = int(input("What Size stack would you like "))
s.size(y)
s.push('hello')
s.push('true1')
s.push('true2')
s.push('true3')
s.pop()
s.pop()
s.pop()
print(s.pop())
print(s.pop())
print(s.status())

