#Copyright 2021 Kerem YEMENİCİ
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

# -*- coding: utf-8 -*-



import os 
from gtts import gTTS
import sqlite3 as sql3

class Cemile():
    def __init__(self) -> None:
        self.vt = sql3.connect('vt.sqlite3')
        self.im = self.vt.cursor()

    def konus(self, metin:str) -> None:
            print(metin)
            #tts = gTTS(text=metin, lang='tr')
            #tts.save("ses.mp3")

            #os.system('mpg321 ses.mp3 -quiet')

    def mikrofonDinle(self) -> None:
        cumle = input("Bana bir şey söyle : ")
        self.yap(cumle.lower())

    def yap(self, cumle:str) -> None:
        self.im.execute("""SELECT * FROM komutlar """)
        komutlar = self.im.fetchall()
        for komut in komutlar:
            if cumle in komut[0]:
                if komut[2]:
                    self.konus(komut[2])
                exec(komut[1])
                break

if __name__ == '__main__':
    cemile = Cemile()
    cemile.konus('Merhaba ben Cemile! Nasıl yardımcı olabilirim?')
    while True:
        cemile.mikrofonDinle()