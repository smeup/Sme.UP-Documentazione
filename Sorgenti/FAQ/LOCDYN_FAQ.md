- \*\*Che differenza c'è tra un componente SUB, SCH e un DYN?\*\*

 :  : VOC Id="00001" Txt="Che differenza c'è tra un componente SUB, SCH e un DYN?"
In uno script di scheda, una sezione può essere composta da una o più subsezioni (sub), ognuna contenente un componente specifico.
Una scheda stessa SCH, anche se composta da più sezioni e subsezioni (e quindi da più componenti), non è altro che un componente contenuto come sottoscheda all'interno di una sub.
Una volta definito il tipo contenuto di una sub, questo non ouò cambiare, in quanto al client viene detto esplicitamente di aspettarsi un determinato componente
Ad esempio una sub A definita come G.SUB.TRE conterrà sempre un albero, la sub B (G.SUB.SCH) una scheda .. e così via ..

A volte però si vuole fare in modo che il contenuto di una sub possa contenere un componente diverso a seconda della selezione di un utente.
In questo caso si susa il componente DYN.
Definendo un seub come G.SUB.DYN il client sa che la sua forma dovrà cambiare a seconda dei dati che verranno inviati dal server.
Può essere visto come una specie di segnaposto per un altro componente.
Questo componente potrà essere diverso nel tempo :  prima un albero, poi una scheda .. etc

- \*\*Perchè non tutte le sub contengono componenti DYN?\*\*

 :  : VOC Id="00002" Txt="Perchè non tutte le sub contengono componenti DYN?"
Il componente DYN fornisce una grande possibilità in alcune soluzioni, ma introduce una complessità maggiore da gestire sia nella definizione delle schede che nella visualizzazione lato client.
Spesso il comportamento voluto di una scheda può essere definito con componenti specifici e bene definiti, senza sfruttare il meccanismo introdotto dal componente DYN.

- \*\*Posso evitare di utilizzare un componente DYN?\*\*

 :  : VOC Id="00003" Txt="Posso evitare di utilizzare un componente DYN?"
La scelta di utilizzare un componente rispetto ad un altro, dipende dalla funzionalità che si vuole ottenere nella scheda e da come si struttura l'interazione da parte dell'utente.
Tramite dinamismi si può cambiare la funzione che carica il contenuto di una scheda.
E' un meccanismo simile a quello che verrebbe utilizzato con il componente DYN, si perderebbe però il vantaggio di poter usare qualunque fun :  si dovranno utilizzare solo funzioni che restituiscono xml di scheda.

