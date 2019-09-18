- **Sai spiegare quando un'azienda deve utilizzare gli Ordini di Produzione?**

 :  : VOC Id="SKIA0010" Txt="Sai spiegare quando un'azienda deve utilizzare gli Ordini di Produzione?" Als="comm"
Un azienda quando attraverso un insieme di uomini, macchine, attrezzature ed organizzazione trasforma e/o assembla materiali necessita di un documento di lavorazione che chiamiamo ordine di produzione.

L'ordine di produzione è il documento attraverso il quale la fabbrica conosce : 
1. Cosa deve produrre
2. Quando deve produrre
3. I componenti e/o le materie prime necessari con le relative quantità
4. Le risorse necessarie all'attuazione del ciclo di trasformazione o assemblaggio dell'ordine di produzione


- **Sai spiegare cosa sono gli impegni materiali  di un ordine?**

 :  : VOC Id="SKIA0030" Txt="Sai spiegare cosa sono gli impegni materiali  di un ordine?" Als="comm"
Gli impegni materiali rappresentano i componenti con i relativi dati di quantità che devono essere utilizzati per fabbricare l'articolo intestatario dell'ordine di produzione.
Gli impegni materiali sono costruiti scandendo la distinta del documento ordine di produzione.
- **Sai spiegare cosa sono gli impegni Risorse di un ordine?**

 :  : VOC Id="SKIA0040" Txt="Sai spiegare cosa sono gli impegni Risorse di un ordine?" Als="comm"
Gli impegni risorse sono il fabbisogno in termini di risorse necessario alle lavorazioni di un ordine di produzione.
Le risorse sono i centri di lavoro che vengono utilizzate  come  tempo e sequenza secondo quanto definito dal ciclo di lavorazione dell'ordine di produzione.
- **Sai che si possono fare Ordini di Produzione senza Articolo,se si a cosa s**

 :  : VOC Id="SKIA0050" Txt="Sai che si possono fare Ordini di Produzione senza Articolo,se si a cosa servono?"
Si è possibile fare ordini di produzione senza articolo.

Sono utili per descrivere ad esempio ordini di manutenzione in cui consumiamo materiale e risorse senza fabbricare un oggetto fisico.
- **Sai dove normalmente nascono gli ordini di produzione in Sme.up?**

 :  : VOC Id="SKIA0060" Txt="Sai dove normalmente nascono gli ordini di produzione in Sme.up?"
L'ordine di produzione normalmente in Sme.up nasce come rilascio di un suggerimento di pianificazione materiali(Mrp).

L'ordine di produzione può naturalmente essere immesso manualmente dall'operatore autorizzato.

- **Sai che è possibile creare ordini di produzione collegati 1 ad 1 ad una ri**

 :  : VOC Id="SKIA0070" Txt="Sai che è possibile creare ordini di produzione collegati 1 ad 1 ad una riga di vendita?" Als="comm"

Nei casi in cui l'ordine di produzione  deve essere collegato alla riga dell'ordine cliente è possibile generare in modo automatico l'ordine di produzione nei flussi dell'oggetto riga documento.
- **Sai consigliare quando è utile memorizzare la distinta materiali o il cicl**

 :  : VOC Id="SKIA0080" Txt="Sai consigliare quando è utile memorizzare la distinta materiali o il ciclo per il singolo ordine di produzione?" Als="comm"
E' utile memorizzare la distinta ed il ciclo di lavorazione di un ordine di produzione quando : 
1. Le date di validità  di distinta e ciclo o le modifiche per esponente di modifica  non sono gestite dall'ufficio tecnico
2. Il  prodotto presenta variazioni rispetto alla distinta e ciclo standard (ordini speciali , riparazione o trasformazione)
3. Produzioni per commessa

Nel  caso 1 consiglio di memorizzare distinta e ciclo per evitare che le attività dell'ufficio tecnico impattino sulle lavorazioni corso e per consentire il reperimento della distinta e del ciclo standard come dato storico dell'ordine. E' chiaro che questa impostazione è cautelativa ed in alcuni casi potrebbe essere necessario strutturare processi più o meno complessi che trasferiscono le modifiche tecniche su ordini già rilasciati.

Nei casi 2 e 3  la memorizzazione è obbligatoria in quanto per loro natura stiamo gestendo ordini di produzione che presentano una descrizione del processo di fabbricazione che non si ripete.



- **Sai che differenza c'e' tra distinta documento e distinta memorizzata?**

 :  : VOC Id="SKIA0090" Txt="Sai che differenza c'e' tra distinta documento e distinta memorizzata?"
La distinta documento è la distinta che rappresenta i componenti da consumare nell'ordine di produzione secondo le impostazioni di risalita impostate nella tabella degli impegni materiali.

La distinta del documento è quella legata all'ordine di produzione, oppure (se questa manca ed in fase di customizzazione si è impostata la risalita) è la distinta base dell'articolo.

La distinta memorizzata è la distinta istanziata sull'oggetto ordine di produzione.



- **Conosci  tre modalità di scarico degli impegni materiali previste in Sme.u**

 :  : VOC Id="SKIA0100" Txt="Conosci  tre modalità di scarico degli impegni materiali previste in Sme.up?"
Le tre modalità di scarico previste in Sme.up sono le seguenti : 

1. BackFlushing
2. Prelievo da impegno manuale
3. Prelievo contestuale alla dichiarazione di avanzamento che può essere cieco o visualizzato
- **Sai spiegare cosa è il BackFlushing?**

 :  : VOC Id="SKIA0110" Txt="Sai spiegare cosa è il BackFlushing?" Als="comm"
E' una tecnica con la quale, al momento del versamento del prodotto finito a
magazzino, sono prelevati e scaricati contabilmente dal magazzino stesso i
componenti dei livelli inferiori della distinta base. In tal modo si evita di dovere
eseguire il prelievo e lo scarico di ciascuno di essi. Questa tecnica può
essere usata se il momento del versamento non è troppo distante nel tempo
da quello dell'utilizzo reale, perché in caso contrario non può essere garantito
la corrispondenza tra giacenze contabili e fisiche
- **Conosci i prerequisiti di applicabilità del prelievo alla fase?**

 :  : VOC Id="SKIA0120" Txt="Conosci i prerequisiti di applicabilità del prelievo alla fase?" Als="comm"
I prerequisiti per il prelievo alla fase sono : 

1. La definizione a livello di distinta materiale della fase di prelievo
2. La consuntivazione delle dichiarazioni di attività

- **Sai che differenze comporta nella valorizzazione del magazzino il Backflus**

 :  : VOC Id="SKIA0130" Txt="Sai che differenze comporta nella valorizzazione del magazzino il Backflushing rispetto al prelievo alla fase ?" Als="comm"
La gestione a Backflushing  dato che consuma i componenti solo all'atto del versamento valorizza i componenti come valore di magazzino mentre lo scarico alla fase porta il valore dei componenti consumati nel valore del Wip.

Questo significa che la somma della volorizzazione del magazzino e del Wip è uguale ma i due addendi presentano valori differenti a seconda della tecnica utilizzata.
- **Sai che la giacenza alla fase di un ordine è scritta nel file impegni riso**

 :  : VOC Id="SKIA0140" Txt="Sai che la giacenza alla fase di un ordine è scritta nel file impegni risorse?"
Si la giacenza alla fase è scritta negli impegni risorse ed è interrogabile nell'analisi disponibilità
- **Sai come impostare che un articolo è escluso dall'analisi coperture di un **

 :  : VOC Id="SKIA0150" Txt="Sai come impostare che un articolo è escluso dall'analisi coperture di un ordine?"
Si è possibile escludere un impegno dall'analisi coperture impostando il flag  Q§FL03 ='1' del file impegni materiali.


- **Sai dove si impostano modalità di prelievo specifiche per magazzino/artico**

 :  : VOC Id="SKIA0160" Txt="Sai dove si impostano modalità di prelievo specifiche per magazzino/articolo?"

Nei dati di magazzino articolo si possono impostare tecniche di gestione specifiche(a consumo etc..)

Nei parametri £P1 è possibile specializzare causali di prelievo , recupero, scarto per risorsa/articolo.
- **Sai come valorizzare il Work in Progress della Produzione?**

 :  : VOC Id="SKIA0170" Txt="Sai come valorizzare il Work in Progress della Produzione?"
E' possibile valorizzare il Wip tramite la scheda di loocup D5WIP.

Prerequisiti per la valorizzazione sono : 
1.La dichiarazione delle attività di avanzamento
2.La memorizzazione dei costi standarda alla fase dell'articolo
- **Sai che si possono con una exit specifica salvare i dati pre-rifasatura si**

 :  : VOC Id="SKIA0200" Txt="Sai che si possono con una exit specifica salvare i dati pre-rifasatura sia per impegni materiali che risorse?"
La exit è impostabile nella tabella P5S e consente di salvare dati utente memorizzati nel file impegni risorse.

Ricordo che tutti i dati necessari alla schedulazione BCD sono automaticamente reimpostati dal programma standard e pertanto non è necessario salvarli con la exit.
- **Sai che si possono nettificare gli impegni materiali anche con i movimenti**

 :  : VOC Id="SKIA0210" Txt="Sai che si possono nettificare gli impegni materiali anche con i movimenti neutri?"
Si tramite apposito flag in tabella P5I,  nella nettificazione degli impegni vengono considerati anche i
movimenti di magazzino neutri (che hanno in bianco l'azione sulla giacenza). Se la quantità è positiva è un prelievo, se negativa è un recupero.
- **Sai che è possibile impostare una modalità di scarico tale per cui la dich**

 :  : VOC Id="SKIA0220" Txt="Sai che è possibile impostare una modalità di scarico tale per cui la dichiarazione dell'ultima fase dichiara le precedenti"
Si è possibile impostando apposito flag nella tabella P5S.
L'ultima fase del ciclo verrà considerata milestone standard (tipo milestone 1) e tutte le  fasi precedenti  verranno considerate milestone Automatica precedente (milestone P). Questa impostazione  dichiarerà automaticamente TUTTE le fasi del ciclo (con tempi standard) al momento della
dichiarazione dell'ultima fase. Questo comportamento è analogo a quello che si otterrebbe impostando il flag Tipo Milestone nelle singole
fasi del ciclo di lavorazione. In questo modo si evita di dover gestire tale flag su ogni fase del ciclo.
- **Sai che è possibile impostare un visualizzatore del dettaglio Ordine di pr**

 :  : VOC Id="SKIA0230" Txt="Sai che è possibile impostare un visualizzatore del dettaglio Ordine di produzione?"
Si è possibile impostare il visualizzatore degli ordini di produzione in cui definire controlli e visualizzazioni customizzate per tipo ordine di Produzione.

Deve essere impostata la gestione con visualizzatore nella tabella P51.

E' possibile impostare un visualizzatore specifico per tipo ordine di produzione nella tabella P5T.
- **Sai come impostare un ordine monofase senza ciclo di lavorazione?**

 :  : VOC Id="SKIA0250" Txt="Sai come impostare un ordine monofase senza ciclo di lavorazione?"
E' possibile impostare un ordine di produzione a fase unica in cui i dati del ciclo di lavorazione (tempi) sono scritti sul file p5teop0f.
L'attivazione avviene impostando nella tabella P5S degli impegni risorse collegati il modo di costruzione "L1"
- **Sai che esiste un flag che mi indica se ordine rilasciato da Mrp?**

 :  : VOC Id="SKIA0260" Txt="Sai che esiste un flag che mi indica se ordine rilasciato da Mrp?"
Si è il flag K§FL08 dell'ordine di produzione
- **Sai se e' possibile cancellare movimenti prelievo o versamento dalla revis**

 :  : VOC Id="SKIA0270" Txt="Sai se e' possibile cancellare movimenti prelievo o versamento dalla revisione movimenti di magazzino?"
E' possibile se l'utente è autorizzato  ma è fortemente sconsigliato.

Prelievi e versamenti devono essere modificati e cancellati dalle funzioni specifiche di revisione partendo dall'ordine di produzione.
- **Sai se è possibile generare ordini tra loro dipendenti?**

 :  : VOC Id="SKIA0280" Txt="Sai se è possibile generare ordini tra loro dipendenti?"
Si è possibile costruire ordini dipendenti tramite specifico programma funizzato richiamabile nei flussi di inserimento e/o Pop.up dell'oggetto ordine.
Questa funzione è utile quando si devono creare dato un ordine di produzione gli ordini di produzione dei livelli di distinta più bassi.
Il programma consente di specificare : 
\* Tipo di distinta da esplodere
\* Tipo Esplosione
\* Modo Scelta componenti per cui costruire ordine produzione dipendente

Dato un ordine di produzione è possibile interrogare/gestire i sui ordini dipendenti in formato di lista.

Esempi applicativi sono per esempio rilasci massivi di ordini extra -mrp di articoli i cui ordini non devono essere raggruppati per fabbisogno.
- **Sai a cosa serve il campo Priorità sull'ordine di produzione?**

 :  : VOC Id="SKIA0290" Txt="Sai a cosa serve il campo Priorità sull'ordine di produzione?"
Il campo priorità presente nel dettaglio della testata dell'ordine di produzione serve per ordinare gli impegni risorse degli ordini di produzione.

E' un campo pertanto significativo per le interrogazioni di Work-list delle attività residue sui centri di lavoro e per chi utilizza la schedulazione a capacità finita.

Ricordo che il campo priorità si antepone al campo CORD (precedentemente calcolato) solo  se nella tabella dello scenario impegni risorse si è attivato lo specifico flag.
Nello scenario è inoltre possibile inserire un valore di priorità "normale" che viene assunta nella composizione del CORD se è stata lasciata in bianco quella dell'ordine di produzione. In tal modo si risove il problema che il campo bianco è il valore più basso, e quindi inserendo un valore nella testata dell'ordine di produzione se ne può solo "peggiorare" la priorità.
Inserendo in tabella un valore "medio", è possibile quindi, nell'ordine, sia migliorarne sia peggiorarne la classifica (inserendo rispettivamente valori più bassi e più alti).


- **Sai a cosa serve la matricola nel dettaglio ordine produzione?**

 :  : VOC Id="SKIA0300" Txt="Sai a cosa serve la matricola nel dettaglio ordine produzione?"
E' la matricola proposta nel versamento dell'ordine di produzione
- **Sai a cosa serve il  lotto nel dettaglio ordine di produzione?**

 :  : VOC Id="SKIA0310" Txt="Sai a cosa serve il  lotto nel dettaglio ordine di produzione?"
Il campo lotto nella testata dell'ordine di produzione è  : 

\* il lotto della qualità a cui vengono normalmente collegati i dati di collaudo    dell'ordine di produzione.
\* il lotto che viene scritto nei movimenti di versamento dell'ordine di produzione
\* il lotto che viene stoccato a magazzino nel caso di giacenza per lotto
\* il lotto (opzionale) per il calcolo del costo a consuntivo per lotto




- **Sai a cosa serve l'ubicazione nel dettaglio ordine di produzione?**

 :  : VOC Id="SKIA0320" Txt="Sai a cosa serve l'ubicazione nel dettaglio ordine di produzione?"
Viene utilizzata come ubicazione proposta all'atto del versamento dell'ordine di produzione.
- **Sai che impostata  la data di fine viene ricalcolata  la data di inizio se**

 :  : VOC Id="SKIA0330" Txt="Sai che impostata  la data di fine viene ricalcolata  la data di inizio se abblencata e viceversa?"
Impostando una tra la Data di inizio e quella di fine la data viene ricalcolata sulla base dei dati di pianificazione (lead time) scritti nella testata dell'ordine di produzione e reperiti all'atto della creazione dell'ordine dai dati di pianificazione dell'articolo
- **Sai cosa è una produzione MFP?**

 :  : VOC Id="SKIA0340" Txt="Sai cosa è una produzione MFP?"

La produzione mfp (material flow production) si introduce  quando si vuol trattare ad un livello logistico più vicino alla realtà l'avanzamento della
produzione.
All'ordine di produzione si abbinano n contenitori, che venono gestiti
singolarmente (come "minordini", con il loro eventuale ciclo).
Al centri di lavoro si assegnano ubicazioni pre e post :  l'avanzamento
produzione si traduce nello spostamento da un'ubicazione pre ad una post.
La giacenza di wip è ottenuta dalla giacenza dei singoli contenitori.
Esistono funzioni di spostamento del contenitore fuori linea, o da un
ordine all'altro. Le quantità globale dell'odine viene rifasata
automaticamente.
- **Conosci quali metodi di valorizzazione di  un ordine sono implementati?**

 :  : VOC Id="SKIA0370" Txt="Conosci quali metodi di valorizzazione di  un ordine sono implementati?"
Un ordine può essere valorizzato con
o Ciclo e distinta standard (Articolo)
Costo Standard Ordine
o Ciclo e distinta pianificati (Legati all'ordine in fase di emissione)
Costo Pianificato Ordine
o Ciclo e distinta consuntivi (consuntivo movimenti ed Attività)
Costo Medio consuntivo ordine

- **Sai cosa si intende per raccolta dati della produzione?**

 :  : VOC Id="SKIA0380" Txt="Sai cosa si intende per raccolta dati della produzione?" Als="comm"
La raccolta dati è la raccolta dei dati della Fabbrica.
La raccolta dati serve per monitorare in tempo reale l'avanzamento della produzione in termini di quantità e tempo.

Disporre della raccolta dati consente di registare automaticamente in Sme.up  le quantità prodotte ed i tempi di attrezzaggio, lavorazione.


- **Sai se è possibile versare un ordine di produzione generando una giacenza **

 :  : VOC Id="SKIA0390" Txt="Sai se è possibile versare un ordine di produzione generando una giacenza negativa dei componenti?"
Si è possibile versare un ordine di produzione generando una giacenza negativa sui componenti prelevati se non attivato il controllo della versabilità dell'ordine di produzione.

Il controllo di  versabilità dell'ordine presenta la lista dei componenti che non hanno disponibilità dato il gruppo fonti impostato.
Se avanzamento alla fase il controllo si attiva con flag nella tabella P5C della causale di avanzamento.
Se prelievo BackFlushing o manuale nella B£J del Prelievo/versamento


- **Sai cosa sono le  date di inizio/fine ordine a capacita infinita al piu pr**

 :  : VOC Id="SKIA0410" Txt="Sai cosa sono le  date di inizio/fine ordine a capacita infinita al piu presto?" Als="comm"
Sono le date di inzio e fine schedulando l'ordine a capacità infinita partendo dalla data di inzio dell'ordine di produzione.

Queste date sono ottenute datando le singole fasi del ciclo di lavorazione dell'ordine di produzione a capacità infinita supponendo quindi che sia l'unico ordine ad utilizzare le risorse necessarie alla sua lavorazione.
La data di inzio quindi coincide con la data di inzio dell'ordine e la fine è ottenuta sommando i tempi delle lavorazioni delle singole fasi e gli eventuali tempi di coda impostati per centro di lavoro.

- **Sai cosa sono le  date di inizio/fine ordine a capacita infinita al piu ta**

 :  : VOC Id="SKIA0420" Txt="Sai cosa sono le  date di inizio/fine ordine a capacita infinita al piu tardi?" Als="comm"
Sono le date di inzio e fine schedulando l'ordine a capacità infinita partendo dalla data di fine dell'ordine di produzione.

Queste date sono ottenute datando le singole fasi del ciclo di lavorazione dell'ordine di produzione a capacità infinita supponendo quindi che sia l'unico ordine ad utilizzare le risorse necessarie alla sua lavorazione.
La data di fine  quindi coincide con la data di fine dell'ordine e l'inizio è ottenuto sottraendo  i tempi delle lavorazioni delle singole fasi e  gli eventuali tempi di coda impostati per centro di lavoro.
- **Sai cosa sono le  date di inizio/fine ordine a capacita finita?**

 :  : VOC Id="SKIA0430" Txt="Sai cosa sono le  date di inizio/fine ordine a capacita finita?" Als="comm"
Sono le date di fine ed inzio di un ordine di produzione ottenute dalla schedulazione delle sue fasi di lavorazioni tramite la schedulazione a capacita finita.
- **Sai  come impostare causali di prelievo specifiche per componente?**

 :  : VOC Id="SKIA0440" Txt="Sai  come impostare causali di prelievo specifiche per componente?"
Nei parametri £P1 per Risorsa/Articolo.
Se si vuole impostare una causale specifica per articolo non si deve impostare la causale di prelievo nell'elemento di P5I collegato all'ordine di produzione

- **Se un componente è impegnato in una fase esterna i suoi impegni sono di ti**

 :  : VOC Id="SKIA0400" Txt="Se un componente è impegnato in una fase esterna i suoi impegni sono di tipo PP o PE?"
Sono di tipo PE per tutti i tipi di lavorazione esterna
- **Sai dove impostare la causale di versamento ?**

 :  : VOC Id="SKIA0450" Txt="Sai dove impostare la causale di versamento ?"
Nei parametri logistici £P2 dove è definibile per Tipo ordine/Articolo.

Si possono impostare eventuali risalite utilizzando le normali funzionalità della gestione parametri
- **Sai come  verificare se un ordine è coperto ?**

 :  : VOC Id="SKIA0460" Txt="Sai come  verificare se un ordine è coperto ?"
E' possibile verificare la copertura di un ordine : 
1.  Interrogazione Copertura impegni nelle funzioni previste dalla sintesi ordine di produzione
2.  Interrogando Mrp dal consiglio di pianificazione
- **Sai che  una fonte futura di tipo ordine di produzione può essere datata c**

 :  : VOC Id="SKIA0470" Txt="Sai che  una fonte futura di tipo ordine di produzione può essere datata con le date della schedulazione?"
Si impostando nella tabella M5F il flag data fonte possiamo datare l'ordine di produzione usando i risultati della shedulazione a capacità infinita o finita
- **Sai che la giacenza alla fase di un ordine di produzione è possibile impos**

 :  : VOC Id="SKIA0490" Txt="Sai che la giacenza alla fase di un ordine di produzione è possibile impostarla nell'analisi disponibilità?"
Si è possibile impostare nelle fonti presenti l'orgine 'GF' giacenza alla fase che restituisce le giacenze alla fase degli ordini di produzione dell'articolo oggetto dell'analisi disponibilità.

Può essere utile nelle interrogazioni di disponibilità impostarla come fonte neutra per esplicitare lo stato di avanzamento delle lavorazioni.
