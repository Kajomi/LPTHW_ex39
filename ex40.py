class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics 
		
	def favorate_songs_band(self):
		for line in self.lyrics:
			print (line) 
			
# Instantiating/ creating objects by calling the class a lot like a function,
# Similar to the Constructor in Java:
beatles = Song(['In My Life', 'A Day In Life', 'Nowhere Man'])
zeppelin = Song(['Trampled Under Foot', 'Gallows Pole', 'In The Evening'])

# Getting/ applying the functions of the class:
beatles.favorate_songs_band()
zeppelin.favorate_songs_band()

# Study Drills:

#Put the lyrics in a separate variable and pass that variable to the class to use instead:

bee_gees_songs = ['Nights on Broadway', 'You Win Again', 'Islands in the Stream']

bee_gees = Song(bee_gees_songs)

bee_gees.favorate_songs_band()





