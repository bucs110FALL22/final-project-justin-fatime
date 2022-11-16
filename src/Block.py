class Block:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.color = "brown"
    self.visible = True
    self.health = 10

  def destroyed(self):
#	makes destroyed block no longer visible
#	args: self
#	return: makes block invisible
    self.visible = False
    return self.visible

  def hitBlock(self):
#	takes health away from block when hit
#	args: self
#	return: lowers health
    self.health = self.health - 5
    return self.health

