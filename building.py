class building:
  radius = 100

  def __init__(self, id, name, latitude, longitude)
   self.radius = radius
   self.id = id
   self.name = name
   self.latitude = latitude
   self.longitude = longitude
 
   def __str__(self):
    return "%d - %s - %d - %d" % (self.id, self.name, self.latitude, self.longitude)