# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

class Character:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.used = False
    self.image = ""
    self.damage = 60
    self.speed = 5

## Class Interface 2

class Enemy:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.image = ""
    self.health = 100
    self.alive = True

## Class Interface 3

class Block:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.color = "brown"
    self.visible = True
    self.health = 10
