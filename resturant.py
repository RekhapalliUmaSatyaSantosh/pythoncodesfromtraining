class Bawarchi:
    menu = {
        'starters': {
            'chilli chicken': 260,
            'chicken 65': 280,
            'chicken lolipop': 240,
            'prawns': 360,
            'crispy corn': 180,
            'paneer majestic': 240,
            'mushroom crispy': 200
        },
        'main course': {
            'chicken biryani': 320,
            'mutton biryani': 380,
            'paneer butter masala': 260,
            'kadai chicken': 290,
            'dal tadka': 180,
            'jeera rice': 150,
            'butter naan': 45,
            'garlic naan': 55,
            'veg fried rice': 220,
            'chicken noodles': 240
        },
        'desserts': {
            'gulab jamun': 90,
            'rasmalai': 120,
            'sizzling brownie': 180,
            'vanilla ice cream': 80,
            'fruit salad': 110
        }
    }
    def __init__(self):
        self.cart = {}
        self.total = 0
    def addtocart(self,item,count=1):
        if item in self.cart:
            self.cart[item]+=count
            return 'added to cart'
        for i in self.menu:
            if item in self.menu[i]:
                self.cart[item]=count
                print('Added to cart')
        print( f'{item} doesnot exist in menu')
        print(self.cart)
    def showmenu(self,t):
        a=self.menu.get(t)
        if a:
            print(f'{"menu":<25} price')
            print('-'*40)
            for i,j in a.items():
                print(f'{i:<25} {j}')
        else:
            print('menu not available')
        self.cart.clear()
u1=Bawarchi()
u1.addtocart('fruit salad')
u1.showmenu('starters')
#remove item from cart
#display the cart
