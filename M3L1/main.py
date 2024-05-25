from flask import Flask
from random import choice,randint #random.choice yerine doğrudan choice fonksiyonu kullanabilmeyi sağlar.

#import random
app = Flask(__name__)

@app.route("/")
def index():
    return " <a href='/rastgele_gercek'>Rastgele bir gerçeği görüntüle!</a>"

@app.route("/rastgele_gercek")
def rastgele_gercek():
    #r_int = randint(1,5)
    facts_list = ["""Teknolojik bağımlılıktan mustarip olan çoğu kişi, 
                  kendilerini şebeke kapsama alanı dışında bulduklarında veya 
                  cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.""",
                  """2018 yılında yapılan bir araştırmaya göre 
                  18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.""",
                  "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
                  "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
                  ]
    return f'<br/><br/> <h1>Teknoloji hakkında bir gerçek</h1> <p>{choice(facts_list)}</p>'

app.run(debug=True)
