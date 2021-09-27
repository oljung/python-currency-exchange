import requests
from bs4 import BeautifulSoup
from tkinter import *

class Gui:
    def __init__(self, root, size='', bg=''):
        self.root = root
        self.size = size
        self.bg = bg
        root.title('Valutaomvandlare')
        root.geometry(self.size)
        root.config(bg=self.bg)


def dollar(sek, rate):
    change = sek/rate
    eResult.delete(0, END)
    eResult.insert(0, f'${change:.2f}')


def sek(dollar, rate):
    change = dollar*rate
    eResult.delete(0, END)
    eResult.insert(0, f'{change:.2f}SEK')

root = Tk()
GUI = Gui(root, '500x200', 'dark slate gray')
r = requests.get('https://www.di.se/valutor/usdsek-26491/')
soup = BeautifulSoup(r.text, 'html.parser')
result = soup.find('div', attrs={'class':'js_instrument-details__price instrument-details__price-main'})
rateRaw = (result.contents[0])
rateStr = rateRaw.replace(',', '.')
rate = float(rateStr)

label1 = Label(root, text='Ange SEK för omvandling till $', bg='navajo white')
label1.place(x=40, y=20)
eSek = Entry(root, width=10, bg='navajo white')
eSek.place(x=20, y=55)
bDollar = Button(root, text='Omvandla SEK -> $', bg='navajo white', fg='black', font=('bold', 10),
              command=lambda:dollar(float(eSek.get()), rate))
bDollar.place(x=100, y=50)
label2 = Label(root, text='Ange $ för omvandling till SEK', bg='navajo white')
label2.place(x=290, y=20)
eDollar = Entry(root, width=10, bg='navajo white')
eDollar.place(x=270, y=55)
bSek = Button(root, text='Omvandla $ -> SEK', bg='navajo white', fg='black', font=('bold', 10),
              command=lambda:sek(float(eDollar.get()), rate))
bSek.place(x=350, y=50)
label3 = Label(root, text='Resultat av omvandling:', bg='navajo white')
label3.place(x=200, y=100)
eResult = Entry(root, width=50, bg='navajo white')
eResult.place(x=100, y=130)
root.mainloop()
print(rate)

