class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title 
    self.medium = medium
    self.year = year
    self.owner = owner
    
# String Representation method for Art
  def __repr__(self):
    return '%s. "%s" %s, %s. %s, %s.' % (self.artist, self.title, self.medium, self.year, self.owner.name, self.owner.location)
  
##class 2 = Marketplace Class  
class Marketplace:
  def __init__(self):
    self.listing = []
  
  def add_listing(self, new_listing):
    self.listing.append(new_listing)
  
  def remove_listing(self,expire_listing):
    self.listing.remove(expire_listing)
  
  def show_listings(self):
    for i in self.listing:
      print(i)
    
##Class No:3 = Client Class
class Client:
  def __init__(self, name, location, is_museum):
    self.name = name 
    self.location = location
    self.is_museum = is_museum
    if is_museum:
      self.location = location 
    else:
      self.location = "other buyer"
      
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
  
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
    for i in veneer.listing:
      if i.art == artwork:
        art_listing = i
        break
    if art_listing != None:
      art_listing.art.owner = self
      veneer.remove_listing(art_listing)
    
## Class No: 4 = Listing
class Listing:
  def __init__(self, art, price, seller):
    self.art = art 
    self.price = price 
    self.seller = seller
  
  def __repr__(self):
    return '%s %s.' %(self.art.title,self.price)
  
veneer = Marketplace()  
veneer.show_listings()

edytta = Client("Edytta Halpirt", None, False)
moma = Client("The MOMA","New York",True)

girl_with_mandolin = Art('Picasso, Pablo',"Girl a Mandolin (Fanny Tellier)", 1910, 'oil on canvas',edytta)
print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin,", 6M(USD)")
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
