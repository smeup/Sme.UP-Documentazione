### **Conosci l'archivio costi?**

Archivio D5COSO0F
### **Conosci la tabella che gestisce la struttura delle chiavi dell'archivio costi, definita tema dei costi?**

La tabella è la D5O che come impostazione oltre ad avere la struttura della chiave (3 chiavi + periodo) ha assegnato anche la tabella che definisce il significato dei 99 valori
### **Conosci qual'è la tabella del tipo costo?**

La tabella è la TCO.
### **Sai qual'è la specificità, possibile, nella chiave dell'archivio costi, per l'archiviazione di un costo?**

Se il tema impostato in questa tabella è uguale al tipo costo, si potrà ommettere la chiave "tipo costo" (TCO) nella tabella delle chiavi (tabella D5O), così da recuperare un elemento di chiave.
### **Conosci la tabella che specifica la struttura del costo?**

La tabella è la IGI
### **Conosci il nuovo calcolo dei costi definito per oggetto?**

Il nuovo calcolo dei "Costi Oggetto" permettere di calcolare i costi non solo per articolo ma per una serie di oggetti diversi : 
- AR  Articolo
- OR  Ordine di Produzione
- DR  Documento (acq o cto lav)
- LO  Lotto
- CZ  Collo
Questo calcolo ha la caratteristica, se richiesto, di conservare tutta la documentazione di come è stato calcolato il costo.
### **Sai come è possibile mappare la struttura del costo per riportare i costi da livello a livello inferiore?**

Genericamente la mappatura degli indici viene garantita dalla tabella D0C per le aliquote (lavorazioni interne) e dalla tabella D0D per gli altri elementi.
Con la nuova versione del calcolo dei "Costi Oggetto" si può impostare la risalita della mappatura degli indici direttamente nella tabella IGI.
### **Conosci la tabella che gestisce la gravità di un errore nel calcolo del costo per oggetto?**

La tabella è la D0E che può essere impostata specificatamente per il cliente e che determina se quello specifico errore deve essere evidenziato oppure no, e se evidenziato se deve determinare un errore "vincolante" nel calcolo, così da non permettere l'aggiornamento dell'archivio costi.
### **L'archivio costi è popolato solo con costi unitari o anche costi a totale?**

Anche costi a totale
### **Conosci la /COPY che garantisce il reperimento del costo?**

La /COPY è la £G55, essa può restituire sia costi unitari che costi a totale in base al "metodo".
### **Sai se nel calcolo costi posso usare politiche specifiche per i costi superando le politiche logistiche?**

Si è possibile, si deve usare la gestione dei listini in particolare l'area £D, dove è stato approntato il listino specifico per le politiche £D0 ed una sezione standard £DP.
### **Sai come è consigliato ripristinare /impostare le tabelle necessarie al calcolo dei costi?**

Se genericamente l'utilizzo delle tabelle impostate come modello (per cui il comando UP FTB) era lo strumento più adeguato alla generazione di una struttura dei costi, nella gestione dei "Costi Oggetto" è a disposizione un Set'n Play che permette l'installazione anche di "Costi Complessi" ed della generazione sia delle tabelle che degli MDV necessari all'impostazione. Tale generazione permette anche di rinominare dei costi nel caso vi fossero già presenti delle codifiche standard.
### **Conosci la nomenclatura standard, del tipo costo, proposta dal set'n play?**

La nomenclatura propone uno standard con il nome del tipo costo diviso in due parti : 
- X Tipologia costo
- YY Progressivo

Dove per X si hanno i seguenti significati : 
- A Costi Aliquote
- I Costi di Item / Articolo
- J Costi Medi di Articolo
- R Costi di Rimanenza
- P Costi Preventivi
- O Costi Ordine Produzione
- D Costi Documento
- L Costi di Lotto
- Z Costi di Collo
- K Costi Commessa (fase analisi)
- V Rim. Commessa (Fase analisi)

Mentre le YY possono indicare : 
Da 01 a 30 - Costi generici
Da 31 a 40 - Costi Consuntivi
Da 41 a 50 - Costi Manuali
Da 51 a 99 - Costi di completamento ai precedenti ma per FASE.
### **Conosci l'archivio per la documentazione dei costi**

L'archivio specifico è il D0DOCU0F, che può essere popolato solo a richiesta, nel calcolo dei costi per oggetto.
### **Sai se nel calcolo del costo questo risulta errato, l'archivio della documentazione viene popolato comunque?**

Assolutamente SI, in quanto tale archivio serve, oltre ad evidenziare come è stato calcolato il costo, anche ad individuare nello specifico l'errore nel calcolo, evidenziando l'oggetto in errore.
### **Sai se la documentazione ha un consumo di spazio disco che potrebbe diventare un elemento critico nel sistema?**

Si, tale documentazione salvando tutti i dati relativi a qualsiasi evento che determina quel costo, ha un consumo di byte che potrebbe risultare critico.
### **Sai se esistono strumenti che forniscono indicazioni sull'occupazione disco della documentazione?**

Si, nella scheda del menu dei costi, D0MENU, esiste una sessione specifica che segnala lo spazio occupato da tutte le documentazioni conservate per tutti i calcoli del costo eseguiti nel tempo.
### **Sai se esiste uno strumento, massivo, di cancellazione / ripristino documentazione?**

Si, nella scheda del menu dei costi, D0MENU, esiste una scheda specifica dove si può SALVARE, CANCELLARE, RIPRISTINARE i dati relativi alla documentazione.
### **Sai perchè è importante la definizione della 'Natura costo' nella tabella TCO?**

Perché permette di evitare di generare dei costi non desiderati, con il calcolo dei costi per oggetto, così da evitare spiacevoli inconvenienti.
### **Sai se nel calcolo del costo base si possono avere flussi PRE calcolo o POST calcolo?**

Si, ed è stato predisposto un deviatore (D0CO99F_P) che permette il lancio sia dei flussi standard che dei flussi "D5" (D5AP00G).
### **Conosci il sisnificato di 'Costo manuale'?**

E' definito così quel costo che viene inserito a mano in archivio, o popolato con programmi che non siano il calcolo del "Costo per Oggetto" e/o "Costo Medio Articolo".
### **Conosci il significato di 'Costo Dinamico'?**

### **Conosci il significato di 'Costo Base'?**

Il costo BASE di un OGGETTO è il calcolo tradizionale del costo su Ciclo e Distinta considerando la sua politica standard
### **Conosci quali exit possono essere attivate sul calcolo del costo base?**

Nello specifico possiamo attivare : 
- Exit in estrazione
- Exit in calcolo
- Exit in fase di documentazione costo
### **Sai come si chiama e cosa puoi gestire nella exit di estrazione nel calcolo del costo base?**

Exit di Estrazione : 

Nominativo exit D0CExx_y dove : 
-  xx = Oggetto (exit diverse per AR - DR - OR - LO - CZ)
- y   = Estensione della exit yP (parametri exit)

Esempi di circostanze da gestire nella exit
- Selezione degli oggetti
- Modifica chiave del calcolo (D5COSO)
- Creare più chiavi di calcolo per lo stesso oggetto, così da generare calcoli diversi (es. per configurazione).
### **Sai come si chiama e cosa puoi gestire nella exit di calcolo nel calcolo del costo base?**

Exit di Calcolo : 

Nominativo exit D0CC01_x dove : 
- x = Estensione della exit xP (parametri exit)

Esempi di circostanze da gestire nella exit
- Assunzione del lotto, prima del calcolo, per condizioni particolari
- Incremento dei vari indici del costo, dopo il calcolo
- Calcolo di costi generali NON derivanti da ciclo e distinta da assegnare all'oggetto, come costi fissi, dazi doganali, spese generiche di trasporto e/o varie.
- In generale completamento del costo dell'oggetto specificatamente per ogni chiave del costo (D5COSO).

### **Sai come si chiama e cosa puoi gestire nella exit in fase di generazione della documentazione del calcolo del costo base?**

Exit documentazione ed Errori  : 

Nominativo exit D0CO01F_x dove : 
- x = Estensione della exit xP (parametri exit)
- B£DP01_U programma dove assegnare la exit per ricorsioni con estensione D0CO01F_xA

Esempi di circostanze da gestire nella exit
- Eliminare un errore
- Modificare la tipologia dell'errore (es :  da vincolante a warning), anche se il consiglio è sostituirlo con errore personalizzato.
- Immissione di un errore (es :  superamenti % di soglia)
### **Sai come si chiama e cosa puoi gestire nella exit nella fase di completamento della struttura del costo del calcolo del costo base?**

La exit è denominata D0CS01_x (dove "x" è una lettera a piacere) e lo scopo di attivarla è quello di poter modificare l'indice di confluenza del costo in base alle caratteristiche dell'oggetto.
Per ottimizzare i tempi si può attivare oppure no, questa exit, utilizzando metodi diversi.
### **Sai se nel calcolo dei costi oggetto tutti i dati tipici del costo sono salvati nella tabella TCO (tabella del tipo costo)?**

No, in questo calcolo i parametri presenti nella tabella TCO si devono completare con le "memorizzazioni" assegnate al calcolo stesso, che in alcuni casi sopravanzano le stesse impostazioni presenti nella tabella TCO, vedi ad esempio : 
- Distinta base da cui prendere i componenti
- Ciclo da cui prendere le fasi
### **Sai se possono essere assegnate delle ricariche ai vari oggetti?**

Si
### **Sai che tabella devo impostare per assegnare delle ricariche nel calcolo del costo base?**

La tabella di riferimento è la CSR
### **Sai che tipo di ricariche posso assegnare sulla tabella CSR?**

Le tipologie di ricarica sono le seguenti : 
- Una Ricarica sul materiale
- Una Ricarica su Lavorazioni esterne
- Nove Ricariche sull'oggetto
### **Sai se posso assegnare delle ricariche che sono gestite da exit e avere così, oltre a dei metodi standard anche dei metodi di calcolo specifici per il cliente?**

Si, il programma da implementare è uno specifico D0CR01_UT
### **Sai che  logiche regolano la 'Ricarica Materiale'?**

- Se non definisco alcuna exit, per assegnare l'indice del materiale viene assunto da tabella D0D, in base alla classe del materiale, con risalita all'elemento "\*\*\*", nel sotto-settore ricariche impostato nel lancio del calcolo costi; la ricarica assumerà indice D0D se materiale assunto indice D0D.
- Se nel calcolo del costo del materiale viene attivata la exit «D0CS01_X» per definire un indice diverso dalla D0D, le ricarica sul materiale assume lo stesso indice "ridefinito" per il materiale.
Se utilizzo il metodo "Utente", nel calcolo della ricarica, posso impostare, oltre al costo della ricarica, anche il suo indice separando eventualmente il valore della ricarica dal valore del materiale.
- In ultima istanza posso attivare la exit sulla struttura della "ricarica del materiale" (D0CS01_X) dove potrò ulteriormente modificare l'indice della ricarica stessa.
- Questa impostazione permettere di modificare l'indice in particolare dove calcolo delle ricariche con metodi diversi da quello "Utente" e voglio impostare indici diversi rispetto alla D0D.
- Questa ricarica nella documentazione sarà evidenziata sulla stessa riga del materiale a prescindere dall'indice a cui verrà assegnata.
- Posso avere una sola ricarica legata al materiale
- Anche questa ricarica, se impostata in altro indice, potrà essere riportata ai livelli inferiori utilizzando la nuova struttura del costo previsto in tabella IGI
### **Sai che logiche regolano la 'Ricarica sulle lavorazioni esterne'?**

- Stesse logiche che per la ricarica del materiale, in quanto anche per queste ricariche si può determinarne un indice specifico, in base alle caratteristiche dell'oggetto, così come per il suo costo.
- Questa ricarica, nella documentazione, verrà identificata come ricarica legata alla lavorazione.
### **Sai che logiche regolano la 'Ricarica sull'oggetto'?**

- Sono definite, in prima istanza, nella tabella D0D
- Se presente un programma di calcolo "Utente" sulla tabella CSR relativa, può essere impostato un indice specifico direttamente nella fase di calcolo ricarica (D0CR01_UT), superando così l'impostazione della D0D.
- In ultima istanza posso attivare la exit sulla struttura della "ricarica oggetto" (D0CS01_X) dove potrò ulteriormente modificare l'indice in particolare per ricariche non calcolate con metodo "Utente".
- Queste ricariche, nella documentazione, saranno evidenziate in una riga specifica dedicata alle ricariche.
- Posso avere sino a nove ricariche oggetto, calcolate con metodi misti.
- Anche queste ricariche, se impostate in indici che prevedono indici di livello inferiore, utilizzando la nuova struttura del costo previsto in tabella IGI, possono essere gestite con "livello proprio" e "livello inferiore".

### **Conosci il significato di Costo Medio Articolo?**

Il costo MEDIO di un ARTICOLO è la media ponderata del costo degli eventi, presenti in vari archivi, che concorrono alla sua
determinazione in quel periodo.
### **Conosci una definizione di Costo Medio Articolo?**

NON è il calcolo di un costo ma : 
- Una selezione degli eventi con possibilità di determinare quale tipo e per quale oggetto scatenare il calcolo (exit D0CJ01_x)
- Un sistema di generazione, di uno o più calcoli, rispetto ad un evento relativamente ad un oggetto (Passi B£J/D0)
- La valorizzazione di ogni singolo evento per un suo costo totale, a valore e quantità (Calcolo base oggetto - D0CO01A)
- La sommatoria dei valori e quantità degli eventi, per determinare la media ponderata di articolo
### **Conosci i principi per la selezione degli eventi che determinano il costo Medio di articolo?**

I costi dei vari eventi possiamo determinarli in base alla impostazione presente sulla tabella B£J/D0 passi rispetto al flusso del calcolo del costo medio, e sono : 
1 - Calcolo del Costo a totale
2 - Lettura di un Costo a totale per quello stesso periodo di calcolo
3 - Lettura di una Costo a totale relativo ad un periodo precedente (genericamente usato per le rimanenze)
4 - Lettura di un Costo Unitario di quel periodo.
5 - Lettura di un Costo a totale del periodo, scatenando prima un PREcalcolo.
### **Conosci quali archivi possono concorrere, a standard, alla determinazione del costo Medio?**

Archivio per eccellenza è il file dei movimenti di magazzino (GMMOVI) mentre per eccezione si possono generare movimenti di costo anche da : 
- V5RDOC Documenti
- CQLOTT Lotti
- P5TEOP Ordini produzione
### **Conosci la tabella per estrazione movimenti, per generare costo medio?**

La tabella è la D0J
### **Sai se nel calcolo dei costo medio tutti i dati tipici del costo sono salvati nella tabella TCO (tabella del tipo costo)?**

No, in quanto il costo medio, più che un calcolo è un totalizzatore di costi (che poi sommando quantità e valori ne determinano un valore medio), e la sua impostazione è condizionata da : 
- Impostazioni di calcolo dei costi base eseguiti
- Tabella B£J/D0 con gli elementi specifici che caratterizzano il lancio del calcolo
- Impostazioni delle memorizzazioni tipiche del costo medio
Praticamente i dati impostati nella tabella TCO di un costo medio non ricoprono nessuna importanza se non nella determinazione del tema e dell'eventuale costo di risalita.
### **Sai come si chiama e cosa puoi gestire nella exit nella fase di estrazione dei movimenti nel calcolo del costo medio di articolo?**

Exit di Estrazione : 

Nominativo exit D0CJ01_x dove : 
- x = Estensione della exit x

Esempi di circostanze gestibili con metodo MOV
- Escludere un movimento di magazzino, (es verificare causale rispetto ad un parametro non gestendo così la «lista causali».)
- Modificare l'oggetto dell'analisi rispetto a quanto impostato a standard
- Modificare la quantità che deve contribuire al costo medio

Esempi di circostanze gestibili con metodo B£J
- Escludere il passo B£J rispetto alle caratteristiche del movimento di magazzino
### **Sai come si chiama e cosa puoi gestire nella exit nella fase di calcolo del costo medio di articolo?**

La exit è denominata D0CO10C_x (dove la "x" è l'estensione personalizzabile) e, una volta calcolato il costo medio, quale sommatoria dei vari eventi, si possono aggiungere elementi di costo necessari, che non permetteranno, chiaramente, una quadratura tra i costi dei singoli eventi ed il costo medio determinato.
### **Sai come si chiama e cosa puoi gestire nella exit nella fase di generazione della documentazione del calcolo del costo medio articolo?**

Exit documentazione ed Errori  : 

Nominativo exit D0CO01F_x dove : 
- x = Estensione della exit xP (parametri exit)
- B£DP01_U programma dove assegnare la exit per ricorsioni con estensione D0CO01F_xA

Esempi di circostanze da gestire nella exit
- Eliminare un errore
- Modificare la tipologia dell'errore (es :  da vincolante a warning), anche se il consiglio è sostituirlo con errore personalizzato.
- Immissione di un errore (es :  superamenti % di soglia)

Evidenziamo che gli errori gestibili in questa exit sono SOLO quelli specifici per il costo medio articolo e non quelli relativi ai vari eventi che hanno concorso alla sua determinazione.
### **Conosci il significato di 'Costo di Rimanenza'?**

E' il costo, in genere dell'oggetto articolo, a fine periodo per la sua quantità di giacenza.
### **Sai perché si è definito di avere delle rimanenze sull'archivio costi, pur avendo un archivio 'Fiscale' per le rimanenze standard?**

Pur avendo l'archivio GMSIAN (giacenze fiscali fine anno / periodo) si mantiene anche la giacenza sull'archivio costi per "preservare" la struttura del costi che può essere suddivisa fino a 99 elementi.
### **Conosci il significato di 'Costo Preventivo'?**

