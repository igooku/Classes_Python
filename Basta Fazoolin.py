##Class No 1 = Menu Class with 1 Calculate bill Method

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items 
    self.start_time = start_time
    self.end_time = end_time
  
  def calculate_bill(self,purchased_items):
    bill = 0
    for i in purchased_items:
      #print(i)
      if i in self.items:
        print(i)
        bill += self.items[i]     
    return bill
  
  def __repr__(self):
    return self.name +" menu availble from "+ str(self.start_time)+ " to "+ str(self.end_time)

## class No 2 = Franchise class which have available Menu method

class Franchise:
  def __init__(self,address,menu):
    self.address=address
    self.menu=menu
  def available_menus(self,time):
    menu_book=[]
    for i in self.menu:
      if (time>=i.start_time) and (time <= i.end_time):
        menu_book.append(i) 
    return menu_book
  
  def __repr__(self):
    return self.address
  
## Class No 3 = control all franchises  
class Business:
  def __init__(self,name,franchises):
    self.name=name
    self.franchises=franchises
  
## All available menus  
brunch_item = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu("brunch",brunch_item,1100,1600)

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu('early_bird',early_bird_items, 1500, 1800)

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu('dinner', dinner_items, 1700, 2300)

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu('kids', kids_items, 1100,2100)


## All menus in one list 
menu1=[brunch,early_bird,dinner,kids]

## creating 2 franchise store with the help of Franchise class

flagship_store = Franchise("1232 West End Road",menu1)
new_installment = Franchise("12 East Mulberry Street",menu1)

Basta =Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])

arepas_items={
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu=Menu("Take a’ Arepa",arepas_items,1000,2000)
arepas_place=Franchise("189 Fitzgerald Avenue",arepas_menu)

arepa =Business("Take a' Arepa",arepas_place)
print(arepa.Menu[0])



