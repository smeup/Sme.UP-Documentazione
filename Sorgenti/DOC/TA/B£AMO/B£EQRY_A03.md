# Gli Schemi - Generalità

Con il termine schema si identifica l'insieme di colonne presentate nel risultato della query in scheda.

Tali colonne possono essere fissate dal pgm specifico di esecuzione della query, ma la maggior parte delle query prevede di appoggiarsi alla struttura di costruzione di schemi generica prevista dallo standard smeup (tramite la /COPY £IQ2). Quando si è in questa situazione nella richiesta parametri della query normalmente è prevista la possibilità di indicare un campo "schema".

![B£EQRY_18](https://doc.smeup.com/immagini/B£EQRY_A03/BXEQRY_18.png)![B£EQRY_19](https://doc.smeup.com/immagini/B£EQRY_A03/BXEQRY_19.png)
E' importante notare, che lo schema rappresenta la base di definizione delle colonne, ma che non è l'unico strumento a disposizione per la costruzione dell'output finale. Allo schema si affiancano infatti gli strumenti di gestione del setup. L'insieme di tali strumenti costituisce una potente funzionalità grafica che permette in modo semplice ed accessibile anche all'utente di "personalizzare" la presentazione di un particolare schema.

In questo frangente è di particolare importanza l'eventuale riordinamento/raggruppamento dei dati, che va sottolineato, viene applicato esclusivamente ai dati caricati e non ha effetto sull'ordine di caricamento effettivo dei degli stessi. Quindi qualora il risultato della query preveda un numero di righe superiori a quello previsto dalla prima pagina, il riordinamento previsto dal setup viene semplicemente applicato ai dati caricati nella prima pagina secondo l'ordinamento previsto dalla query (es. se è previsto che gli articoli vengano caricati per codice, e poi tramite gli strumenti di setup li raggruppo per tipo articolo, tale raggruppamento viene applicato esclusivamente ai codici caricati sulla prima pagina. Se vedo quindi già più gruppi, finchè la paginazione dei dati non sarà completa, tale gruppi non potranno dirsi completi).

Per la configurazione della presentazione dei dati abbiamo quindi due livelli : 
-  Lo schema, che va predisposto dal sistemista, attraverso gli strumenti tecnici.
-  Il setup di matrice, che permette di applicare al singolo schema un'ulteriore personalizzazione grafica da parte dell'utente.

# Schema di default
Salvo che per la query specifica sia stato previsto uno schema, per tutte le query viene ripreso uno schema di default (per verificarlo basta guardare se è presente questa informazione nello scheda della query, cioè dell'oggetto Q1). Questo schema viene determinato secondo la seguente risalita : 
-  Se presente, lo schema indicato nella scelta dello schema di default nelle finestra delle ricerche
-  Se presente, lo schema avente codice S/DFT
-  Se presente, lo schema avente codice Q/DFT
-  Se presente, lo schema avente codice T/DFT
-  Se l'oggetto è una Tabella \*TAB/\*ALL
-  Se l'oggetto è appartiene ad un file \*FIL/\*ALL
-  Altrimenti è T/CD\*
Per il dettaglio si veda la funzione DFT/MDE della /COPY £IQ2.

# Aggiungere nuovi schemi
A standard vengono già previsti una serie di schemi per ogni classe oggetto smeup. Questo nel pensiero di limitare al minimo la necessità di introdurre nuovi schemi. Qualora sorga tale necessità è comunque possibile inserire nuove istanze di schemi.

Di seguito viene riportata la documentazione di definizione degli schemi (oggetto Q2).

- [Documentazione Classe Q2 - Schema - Definizione](Sorgenti/DOC/OG/OG/Q201)

# Modificare il setup dello schema
Per quel che riguarda le funzionalità di setup, si rimanda alla documentazione operativa della matrice. In essa vengono esposte tutte le funzionalità grafiche disponibili per l'utente.

- [Matrice](Sorgenti/DOC_OPE/TA/B£AMO/LOCEXB)

