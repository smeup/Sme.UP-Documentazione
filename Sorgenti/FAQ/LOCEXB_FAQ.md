## AAA
### **Quanti decimali visualizza la matrice nei campi numerici?**

 Il numero di decimali viene impostato al numero massimo di decimali presenti nell'Xml relativamente ai campi di tipologia NR o NP.

### **Come si mettono le date non valorizzate?**

 A \*BLANKS, non 00/00/0000.

### **Come è possibile salvare una stampa realizzata da matrice?**

 Il modo più comodo per salvare una matrice su file non è attraverso la stampa della medesima, ma attraverso l'opzione "Stampa Sezione", all'apertura del menù contestuale, premendo il tasto destro del mouse sull'etichetta della sottosezione. Viene creato un pdf che può essere salvato oltre che stampato.

## BBB
### **Ho una matrice abilitata all'inserimento, con un solo campo modificabile che induce un dimanismo su una altra sezione allo scattare dell'evento **

mismo non viene indotto?"
 Affinchè possa scattare l'evento "Cambio cella", in questo caso è necessaria la presenza di più celle modificabili.
 Per indurre il dinamismo è consigliato utilizzare un altro evento, ad esempio il "Click" o il "Doppio click" del mouse.
 In alternativa è possibile scatenare l'evento "Cambio cella" alla pressione del tasto "TAB".
### **Sai come impostare uno o più raggruppamenti come default nel setup della griglia?**

E' sufficiente impostare l'attributo DftGroup del setup del componente EXB.
Il valore dell'attributo è una stringa contenente i campi (i nomi delle colonne) in ordine di raggruppamento divisi dal carattere '|' più un eventuale ",H" se si vuole che il campo/i campi per cui si raggruppa non rientrino nelle colonne visualizzate in matrice.

Riferirsi all'Help contestuale dell'attributo per maggiori dettagli.
### **Sai come selezionare un filtro multiplo di 3 o più elementi su una colonna?**

Semplicemente, aprendo il menù a tendina del filtro premendo sull'apposita icona nella intestazione della colonna. E' possibile apporre la spunta su un numero qualsiasi di elementi nella lista dei filtri.
### **Sai eseguire una selezione multipla di record nella griglia?**

E' possibile eseguire una selezione multipla di record in due modi diversi.

1) Con la tastiera :  posizionarsi su un record e premere CTRL+INVIO. Il record viene aggiunto alla lista dei record selezionati ed assume una colorazione ocra. Ripetere l'operazione per tutti i record che si desidera selezionare oppure per definire un intervallo di selezione posizionarsi sull'ultimo record del gruppo che si desidera selezionare e premere CTRL+SHIFT+INVIO.

2) Con il mouse :  tenere premuto CTRL e cliccare sull'intestazione del record (rettangolo in testa al record prima della prima colonna della griglia). Il record viene aggiunto alla lista dei record selezionati ed assume una colorazione ocra. Ripetere l'operazione per tutti i record che si desidera selezionare oppure per definire un intervallo di selezione tenere premuto CTRL+SHIFT e cliccare sull'intestazione dell'ultimo record del gruppo che si desidera selezionare.
### **Sai eseguire una selezione multipla di celle (stile excel) nella griglia?**

 Als="comm"
E' possibile effettuare una multiselezione rettangolare tenendo premuto il tasto SHIFT e cliccando (o spostandosi con le frecce) sulle celle che si vuole includere nella selezione.
Questa procedura non seleziona record o oggetti, ma solo celle. E' molto utile per copiare il contenuto di gruppi di celle o per incollare contenuti dagli appunti in gruppi di celle (se la matrice permette l'aggiornamento dei dati).
### **Sai selezionare un asse e una o più serie tra le colonne visibili e poi visualizzarne il grafico?**

E' sufficiente selezionare una colonna come Asse, cliccando con il tasto destro del mouse sulla intestazione della colonna desiderata, e scegliendo la voce "Marca colonna come asse".
Successivamente, eseguire la medesima operazione sulle colonne numeriche da utilizzare come serie (avendo cura di scegliere la voce "Marca la colonna come serie").

Una volta impostati asse e serie, selezionare la voce "Visualizza grafico associato" presente nel menù contestuale dell'intestazione di qualsiasi colonna.
### **Sai come modificare l'ordine delle colonne visualizzate?**

Tramite drag&drop è possibile modificare a piacimento l'ordine delle colonne visualizzate.
Basta trascinare la colonna prima o dopo una altra colonna per cambiarne l'ordine.
### **Sai come ottenere la matrice dei totali a partire dalla matrice corrente?**

 Als="comm"
Se sono presenti delle totalizzazioni e dei raggruppamenti nella matrice, è sufficiente cliccare con il tasto destro del mouse su una riga di raggruppamento e selezionare la voce "Matrice dei totali".
### **Sai come ottenere la matrice di un raggruppamento di una griglia corrente?**

Se sono presenti dei raggruppamenti nella matrice, è sufficiente cliccare con il tasto destro del mouse sulla riga di raggruppamento desiderata e selezionare la voce "Matrice del raggruppamento".
### **Sai come abilitare la visualizzazione dei totali di una griglia?**

m"
Nel menù contestuale di ogni intestazione di colonna è presente la voce "Totalizzazioni". Scegliere il sottomenù "Abilita" per abilitare la visualizzazione dei totali.
### **Sai come aggiungere un totale su una colonna numerica?**

Una volta abilitata la visualizzazione dei totali, nel menù contestuale di intestazione di una colonna sotto la voce "Totalizzazioni" sono presenti le voci per l'abilitazione delle funzioni base di totalizzazione della colonna.

In alternativa cliccando con il tasto destro sulla barra footer della matrice, in corrispondenza della colonna desiderata, appariranno le stesse voci per l'abilitazione delle funzioni base di totalizzazione.
### **Sai come impostare una colonna formula nel setup di una matrice?**

Tramite l'attributo Formulas che consente di definire le formule.
Le stringhe di formula contengono le colonne calcolate .
Il formato della stringa da controllare è :  DescrittoreFormula1| DescrittoreFormula2|ecc...
Il DescrittoreFormula è così definito : 
CodiceColonna;TitoloColonna;Formula;Lunghezza;
La Formula deve essere composta indicando i codici delle colonne tra parentesi quadre (Es. /)

Riferirsi all'Help contestuale dell'attributo per maggiori dettagli.
### **Sai come aggiungere una colonna attributo di una colonna oggetto?**

mm"
E' sufficiente aprire il menù contestuale della intestazione della colonna e selezionare la voce "Colonne aggiuntive".
Dal menù a tendina che apparirà selezionare la categoria desiderata e l'attributo desiderato.
### **Sai come impostare nel setup della matrice una colonna attributo di una colonna oggetto?**

E' possibile utilizzare l'attributo Formulas in modo analogo a quanto accade per le colonne formulate (riferirsi all'Help contestuale per maggiori dettagli), avendo però l'accortezza di specificare la formula in modo particolare come segue : 
ATT(Cos\<Nome colonna>\<Tipo attributo>;<Parametro attributo>;<Codice attributo>).

Esempio : 
Formulas="CALC1;NOME;ATT(Cos\AAA\OA;CNCLI;I/10);15;0;OG"
### **Sai come nascondere una colonna?**

Per nascondere una colonna è sufficiente trascinare la sua intestazione fuori dalla matrice.
### **Sai come impostare la visibilità e l'ordine delle colonne nel setup della matrice?**

E' possibile specificare l'ordine e la visibilità delle colonne della griglia tramite l'attributo Columns del setup.
Questo specifica tutte e sole le colonne della matrice che devono essere visualizzate, rendendo "invisibili" le altre.
Il valore dell'attributo è una stringa contenente i campi (nomi delle colonne della matrice) da visualizzare divisi dal carattere '|' secondo la sintassi :  Campo1|Campo2|Campo3|ecc..

Riferirsi all'Help contestuale dell'attributo per maggiori dettagli.
### **Sai come impostare delle colonne fisse (stile excel) nella matrice ?**

E' possibile, mediante gli attributi di Setup della matrice FixedLCol="N" FixedRCol="N", definire il numero di colonne da fissare partendo da Sx (attributo FixedLCol) e da Dx (attributo FixedRCol).
### **Sai come impostare le prime 'N' righe fisse (stile excel) nella matrice ?**

E' possibile, mediante l'attributo di Setup della matrice FixedTRow='N', definire il numero di righe da fissare partendo dall'alto.
### **Sai come inserire un nuovo record in una matrice di aggiornamento?**

E' possibile, in una matrice di aggiornamento, aggiungere un nuovo record, posizionandosi sull'ultimo record della stessa, e premendo il tasto Freccia Giù.
### **Sai come disabilitare l'autodimensionamento (autofit) delle colonne sulla base del testo contenuto?**

E' possibile annullare l'auto dimensionamento delle colonne sulla base del testo contenuto, impostando l'attributo di Setup della matrice AutoFit="No"
### **Sai come modificare il colore di sfondo di una matrice?**

E' possibile definire un colore di sfondo (visualizzato nell'area non contenente le celle) impostando l'attributo di Setup della matrice BackColor="RxxxGxxxBxxx".  (sostituire le tripette di x, con i valori RGB numerici corrispondenti)
### **Sai come definire dei setup personalizzati su una matrice?**

### **Sai come visualizzare un testo molto lungo in una cella della matrice, senza un riquadro esterno ?**

E' possibile per un campo definito come Memo, impostare l'attributo ShowMemoRows="False" nel setup della matrice.
### **Sai come impostare l'intera griglia a sola lettura?**

### **Sai come visualizzare il log di comunicazione XML che avviene tra una matrice di aggiornamento ed il servizio a lei associato?**

E' possibile in qualsiasi momento, visualizzare il pannello contenente il log delle transazioni che si generano tra la matrice di aggiornamento ed il relativo servizio, puntando il mouse all'interno di una matrice e premendo CTRL+F7
### **Sai come salvare localmente l'XML di una matrice?**

E' possibile in qualsiasi matrice, puntare il mouse sulla scheda contenente la matrice e mediante il tasto destro, selezionare visualizza XML
### **Sai come definire degli stili grafici personalizzati (utilizzando un criterio fisso) per una cella della matrice?**

### **Sai come costruire una matrice a partire dal suo file XML?**

E' possibile, selezionando il menu "File" e successivamente la voce "Avvio modulo da File XML" , costruire una matrice a partire dalla sua rappresentazione XML.
