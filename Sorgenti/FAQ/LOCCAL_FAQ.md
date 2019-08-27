- **C'è un numero massimo di date gestite?**

 :  : VOC Id="10001" Txt="C'è un numero massimo di date gestite?"
 A :  tecnicamente no, rimane il limite di non superare i dati relativi ad un mese, in quanto set massimo di dati graficamente visualizzabili.

- **Se emetto una matrice che copre un intervallo di 6 o 12 mesi, come appare gra**

 :  : VOC Id="10002" Txt="Se emetto una matrice che copre un intervallo di 6 o 12 mesi, come appare graficamente? Vedo più mesi e posso spostarmi tra di essi?"
 A :  si vede il mese relativo alla data impostata nel G.SET.CAL. o in mancanza di quest'ultima, viene mostrato solo il mese relativo
 alla prima data ricevuta nella matrice.
 E' ipotizzabile utilizzare un LOA08 come filtro iniziale per popolare il calendario

- **Come  è gestito il posizionamento iniziale nel calendario? Nel G.SET.CAL non **

 :  : VOC Id="10003" Txt="Come  è gestito il posizionamento iniziale nel calendario? Nel G.SET.CAL non c'è una proprietà per la data di posizionamento."
 A :  è l'attributo G.SET.CAL DatCol="yyyymmdd"

- **Quanti eventi o oggetti posso mettere in una giornata? c'è un numero massimo?**

 :  : VOC Id="10004" Txt="Quanti eventi o oggetti posso mettere in una giornata? c'è un numero massimo?"
 A :  tecnicamente no, va fatto un test, al netto comunque dell'usabilità.

- **Oltre agli orari, alla descrizione, ai colori e alle icone ci sono altre cara**

 :  : VOC Id="10005" Txt="Oltre agli orari, alla descrizione, ai colori e alle icone ci sono altre caratteristiche visualizzabili?"
 A :  gli stili dei font (grassetto, sottolineatura...)

- **Qual è il modello di interazione per la visualizzazione/gestione di un evento**

 :  : VOC Id="10006" Txt="Qual è il modello di interazione per la visualizzazione/gestione di un evento? l'apertura di una scheda modale sopra o altro?"
 A :  attualmente l'agenda di SmeUP è l'unico esempio d'utilizzo e viene gestito un input panel modale all'evento di click sul giorno.

- **Quali sono i dinamismi supportati dal calendario?**

 :  : VOC Id="10007" Txt="Quali sono i dinamismi supportati dal calendario?"
 A :  Gli eventi gestiti sono : 
 Click  :  alla selezione (click) su un evento di un giorno.
 Drop  :  al rilascio del trascinamento di un evento (drag&drop)
 Dateselect  :  alla selezione (click) su un giorno (non su un evento).
 Le variabili istanziate a fronte dei dinamismi sono :  *CAL.DAT, *CAL.INI, *CAL.FIN, FROM.T1, FROM.P1, FROM.K1, TO.T1, TO.P1, TO.K1

- **Se non specifico nel setup la colonna con la data o quelle degli orari quali **

 :  : VOC Id="10008" Txt="Se non specifico nel setup la colonna con la data o quelle degli orari quali prende? le prime che trova con l'oggetto corretto?"
 A :  mostra il calendario del mese relativo alla prima data utile che trova.

