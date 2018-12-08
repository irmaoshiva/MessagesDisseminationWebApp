import building
import pickle

class buildingDB:

	def __init__(self, campus):
		self.campus = campus.upper()
		try:
			f = open(self.campus + 'buildingsDB', 'rb')
			self.buildings = pickle.load(f)
			f.close()
		except IOError:
			self.buildings = {}


''' podem haver 2 buildings com o esmo nome se tiverem id diferente? '''
	def insertBuildings(self, filename):
		try:
			f = open(filename, 'rt')

			for line in f.readlines():
				[id, name, latitude, longitude] = line.split(',')
				if id in self.buildings:
					print('There is already a building with id', id, 'in the database')
					continue
				self.buildings[id] = building.building(id, name, latitude, longitude)
			
			f.close()
		except:
			print('Error uploading file', filename)

		f = open(self.campus + 'buildingsDB', 'wb')
		pickle.dump(self.buildings, f)
		f.close()
	
	def showBuilding(self, *ids):
		if(len(ids) == 0):
			result = self.buildings
		else:
			result = {k: self.buildings[k] if k in self.buildings else None for k in ids}
		
		return list(result.values())