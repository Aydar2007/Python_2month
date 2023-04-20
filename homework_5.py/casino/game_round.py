from decouple import config
import random
class Casino_Game:
    def __init__(self) -> None:
        self.your_money=config("MY_MONEY",cast=int,default=100)
        self.bet=0
    def round(self):
        while True:
            global total_round
            total_round =+ 1
            slot=int(input("Выбери куда поставишь 1-30 :"))
            bet=int(input("Какую сумму поставите:"))
            if bet < self.your_money:
                ost=self.your_money-bet
                print(f"Ставка принята у вас осталось{ost}")
            else:
                ne_hvataet=bet-self.your_money
                print(f"Не хватает для ставки {ne_hvataet}")
            game_point=random.randint(1,30)
            if game_point==slot:
                win=bet*30
                your_money1=win+self.your_money
                self.your_money=your_money1
                print(f"Вы выиграли ваш баланс {self.your_money}")
            else:
                your_money1=self.your_money-bet
                self.your_money=your_money1
                print(f'Вы проиграли ваш баланс {self.your_money}')
            contin=input(str(f"Ваш баланс {self.your_money}, Хотите продолжить игру?"))
            if contin=="Da":
                continue
            else:
                print(f"Ваш баланс {self.your_money}")
                break

