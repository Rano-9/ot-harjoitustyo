```wsd
title HSL
participant Main
participant laitehallinto as laite

Main->*laite: HKLLaitehallinto()
note left of laite : _lataajat = [] \n _lukiajat = []
laite --> Main :
Main->*rautatientori: Lataajalaite()
rautatientori --> Main:
Main->*ratikka6: Lukijalaite()
ratikka6 --> Main:
Main->*bussi244: Lukijalaite()
bussi244 --> Main:
Main->laite: lisaa_lataaja(rautatientori)
note left of laite : _lataajat.append(rautatientori)
laite --> Main:
Main->laite: lisaa_lukija(ratikka6)
note left of laite : _lukijat.append(rautatientori)
laite --> Main:

Main->laite: lisaa_lukija(bussi244)
note left of laite : _lukijat.append(rautatientori)
laite --> Main:

Main->*lippu_luukku : Kioski()
lippu_luukku --> Main :
Main->+lippu_luukku : osta_matkakortti("Kalle")
lippu_luukku ->* kallen_kortti: Matkakortti("Kalle")
note left of kallen_kortti : nimi = Kalle
kallen_kortti --> lippu_luukku :
note left of lippu_luukku: arvo = None
lippu_luukku -->- Main : 
Main->+rautatientori : lataa_arvoa(kallen_kortti,3)
rautatientori ->+ kallen_kortti: kasvata_arvoa(3)
note left of  kallen_kortti: arvo +3
kallen_kortti -->- rautatientori :
rautatientori -->- Main:
Main ->+ ratikka6 : osta_lippu(kallen_kortti,0)
note left of ratikka6 : tyyppi == 0 \n hinta = 1.5
ratikka6 ->+ kallen_kortti : arvo()
kallen_kortti ->- ratikka6 : 3
note left of  ratikka6 : arvo > hinta 
ratikka6 ->+ kallen_kortti : vahenna_arvoa(1.5)
note left of  kallen_kortti : arvo -1.5
kallen_kortti -->- ratikka6 :
ratikka6 ->- Main : True
Main ->+ bussi244 : osta_lippu(kallen_kortti, 2)
note left of  bussi244 : tyyppi == 2 \n hinta = 3.5
bussi244 ->+ kallen_kortti : arvo()
kallen_kortti ->- bussi244 : 1.5
note left of bussi244 : arvo < hinta
bussi244 ->- Main : False
```