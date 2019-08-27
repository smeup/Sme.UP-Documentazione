- **DASHBOARD**

 :  : VOC Id="CRU001" Txt="DASHBOARD"
DASHBOARD è il nome della sezione che permette di vedere delle informazioni considerate "fondamentali" ed "importanti" per l'oggetto in questione. Come prima cosa quando si entrerà nella scheda di un modulo o di un oggetto quindi verranno visualizzate sulla destra le informazioni del cruscotto.

Il Dashboard quindi è una sorta di visualizzatore grafico delle informazioni principali, queste informazioni possono essere rappresentate da una o più matrici, da dei semafori, da gauge, ecc. Il Dashboard quindi in sintesi è la scheda principale dell'oggetto/modulo che si sta interrogando.
In alcuni casi il cruscotto non viene interamente caricato, ma vengono visualizzati dei filtri per evitare di caricare troppi dati.

- **FLY**

 :  : VOC Id="DRI001" Txt="FLY"
FLY è il nome di quella funzione che permette,  a partire da un oggetto di origine,  di navigare trasversalmente su altri oggetti collegati e dipendenti da quello di partenza, uscendo dal contesto di origine.
Per esempio, partendo da un ordine di produzione , permette di navigare sui movimenti di magazzino dell'ordine.

Oltre ad essere messo come voce di hypermenu,  si può accedervi anche dal popup sull'oggetto.

- **INFO dell'Hypermenu**

 :  : VOC Id="INF001" Txt="INFO dell'Hypermenu"
Il concetto di INFO coincide con la lista grafica degli attributi dell'oggetto, ovvero contiene l'indicazione di tutti gli oggetti / parametri / dati / informazioni / attributi che sono collegati all'oggetto di cui stò guardando la scheda.

Tutti gli oggetti hanno l' INFO che racchiude tutte le informazioni collegate all'oggetto (può essere visto come l'F10 "lista campi" dell'oggetto).

- **FOCUS**

 :  : VOC Id="FOC001" Txt="FOCUS"
Il Focus non è una scheda legata a tutti gli oggetti ma solo ad alcuni di essi (un esempio è quello dell'ordine di produzione).
Questa scheda è una sorta di Info, più evoluta.
Nella tabella B§K si può decidere di aggiungere/togliere delle cose nel FOCUS senza abilitare le schede personalizzate ma mettendo un suffisso dell'eventuale pgm di aggiustamento.

- **SURF**

 :  : VOC Id="SUR002" Txt="SURF"
SURF è una modalità di interrogazione che parte da una informazione di origine e "naviga" sugli attributi di quella informazione di origine ma mantenendosi nel contesto originale.
Per esempio, se parto da un movimento di magazzino (l'informazione di origine) con SURF  sull'articolo di quel movimento ottengo tutti i movimenti (contesto originale) dell'articolo.

Se invece faccio SURF da un modulo, per esempio il modulo P5ORDI (ordini di produzione), mi porta ad interrogazioni del contenuto del modulo (gli ordini di produzione) tramite metodi di accesso che sono gli attributi dell'oggetto del modulo (la commessa, la data, l'articolo, etc.)

- **HYPERMENU**

 :  : VOC Id="HYP001" Txt="HYPERMENU"
L'Hypermenu è il nuovo componente che permette di gestire nuove funzionalità a livello di menu.
Questo strumento è stato spostato nella parte sinistra delle schede (di oggetti e moduli), può contenere nuove e vecchie funzionalità.
- **GO**

 :  : VOC Id="GOO001" Txt="GO"
GO permette di passare a qualcos'altro :  modulo, oggetto, applicazione, tabella e quant'altro.
- **PROPERTIES**

 :  : VOC Id="PRO001" Txt="PROPERTIES"
Properties permette di visualizzare la lista delle proprietà relative all'oggetto o modulo sul quale mi trovo.
- **ACTIONS**

 :  : VOC Id="ACT001" Txt="ACTIONS"
E' l'insieme delle azioni di gestione e consultazione sul modulo o sull'oggetto.
- **ACCORDION**

 :  : VOC Id="ACC001" Txt="ACCORDION"
E' quel componente di scheda, normalmente a sinistra, che ha la capacità di stringersi in orizzontale , scomparendo a tutto vantaggio del resto della scheda, e di raggrupare in verticale le opzioni all'interno come una fisarmonica, da cui il nome di Accordion. E' il componente di looc up che contiene l'Hypermenu.
