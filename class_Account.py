from datetime import datetime
import pytz

WHITE= '\033[00m'
GREEN='\033[0;92m'
RED='\033[1;31m'


class Account:
    def __init__(self,name,balanse=0):
        self.name=name
        self.__balanse=balanse
        self._history = []

    @staticmethod
    def _get_curren_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self,amount):
        self.__balanse+=amount
        self._history.append([amount,self._get_curren_time()])
        print(f'вы пополнились на {amount}')

    def withdrow(self,amount):
        if self.__balanse > amount:
            self.__balanse -= amount
            self._history.append([-amount,self._get_curren_time()])

            print(f'вы сняли {amount}')
        else:
            print('У вас недостаточно денег для снятия')
            

    def show(self):
        print(f'Баланс {self.__balanse}')

    def show_history(self):
        for  amount,date in self._history:
            if amount<0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdrown'
                color =RED
            print(f'{color} {amount} {WHITE} {transaction} on {date.astimezone()}')


    
x=Account('Kirill')

x.deposit(100)

x.show()
x.withdrow(20)
x.show()

x.show_history()
