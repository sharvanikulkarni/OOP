import CoinClass as c

def show_coin_status(coin_obj):
    print("This side of the coin is up", coin_obj.get_sideup())
    print(coin_obj.get_sideup())
def flip(coin_obj):
    coin_obj.toss()
    print(coin_obj.toss())
my_coin = c.Coin()

for i in range(10):
    flip(my_coin)
    show_coin_status(my_coin)
