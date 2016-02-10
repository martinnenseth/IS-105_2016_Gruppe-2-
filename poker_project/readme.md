

# Kort beskrivelse av poker
Hovedfilen er poker.py
Utrengningen av poeng ligger i pointcalc_poker
utregningen av vinner skjer i calculate winner.
Testklasser kan du finne i PokerTestC.py


Programmet er skrevet 100% av gruppe 2 og vi prøver å holde det på den måten for å lære mest mulig om programmet vårt og lære python mest mulig. 

I dette programmet blir det laget objekter av player og pokercards, men isenere tidpunkt funnet ut at funksjoner er mest egnet, fordi akkurat med det å programmere til webapplikasjoner kan være problematisk med objekter. 

Poker.py
*GenerateCards* tar i utgangspunkt å generere alle kortene som trengs for å kunne gjennomføre et spill. 
*deal* oppretter spillere og deler ut kortene til spillerene

pointcalc_poker.py
*calculatePoints* Vil kjøre igjennom alle metodene fra stigende rekkefølge(altså fra royalflush og nedover), og returnere poengsummen for den hånden vedkommende har. 

CalculateWinner.py
*CalculateWinner* Vil kalkulere vinnerne bassert på hvilken poengsum hånden til spilleren har fått av pointcalc_poker.py.

## En mer detaljert beskrivelse

Før jeg begynner å forklare, er det noen nøkkelvariabler man må bemerke seg. Vi rangerer pokerhånd ved bruk av poeng. Poeng skal ikke bli vist for spilleren, men brukes av systemet til å fortelle hvilken hånd spilleren har og kan fortelle hvilken hånd som er best. Denne blir lagt til spillerobjektet når kortene blir utdelt. 

Det første som skjer er at vi oppretter x antall deck/bunker med kort på 52 kort i generateCards, vært kort blir da et objekt av PokerCard. Vært kort får da 2 ulike variabler som bestemmer hva kortet er. Det ene er Value, som måles fra 0 - 12, da 0 = 2 i kortsammenhenger (mer om dette kan man se i diagrammet under), den andre er symbol som går fra 0 - 3(også definert under).

Når dette er gjort, blir da array'en sendt videre til deal metoden, deal metoden har som hensikt å dele ut kort til spillerene, forløbig blir spillerene også generert her. Men i senere tidspunkt kommer dette til å bli en ting som blir implenetert i deal, da spillerobjektene er ønsket å bli definert allerede tidligere senere, når vi skal koble dette videre mot et virkelig spill.
I deal får man da tildelt 5 kort hver fra bunken som ble geneerert i generateCards, og blir dermed lagt inn i spillerobjektet til hver av spillerene. Her vil også Pointcalc_Poker tre inn. Denne metoden vil da finne ut hvilken poengsum som er for hver hånd. Denne metoden vil da kjøre hvor hver spiller, den returnerer da en poengsum. Denne poengsummen blir ikke synlig for spillerne, det er kun en indikasjon på hvem som vinner. Slik at man enkelt kan definere hvilken hånd man har fått, og hvem som vinner runden bassert på kortene spilleren har fått. 

Etter dette, blir da spillerene printet ut med sine kort og en vinner vil bli trukket bassert på poengscoren spilleren har fått. Det gjøres med at spillerprofilene blir sendt inn i en metode i CalculateWinner.py i metoden CalculateWinner der den da samler spillerene i en liste og printer ut høyt til lavt, og returnerer da spilleren med høyest score. Det er ikke lagt opp enda til at spillerene kan får samme score. Da den nå vil konkludere med at spilleren som havner på toppen av listen vil vinne. Dette vil nok bli endret på ganske snart.


### Value og symbol definasjoner: 

####Value
0 = 2<br />
1 = 3<br />
2 = 4<br />
3 = 5<br />
4 = 6<br />
5 = 7<br />
6 = 8<br />
7 = 9<br />
8 = 10<br />
9 = knekt<br />
10 = Dronning<br />
11 = Konge<br />
12 = Ess (ace)<br />

####Symbol
0 = Kløver<br />
1 = Spar<br />
2 = Hjerter<br />
3 = Ruter<br />

Testing er blitt gjort i modulen PokerTestC.py