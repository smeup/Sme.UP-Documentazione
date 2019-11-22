### **Sai in che ordine l'MRP analizza gli articoli?**

In ordine di LLC, ossia di livello minimo di distinta, partendo dagli articoli finiti di acquisto, poi i finiti di produzione o conto lavoro.
### **Sai come si definisce un gruppo fonti?**

In interrogazione di disponibilità, selezionando con la X il campo a dx del gruppo fonti , si accede alla lista delle fonti. Se si selezionano con X e si esce salvando la memorizzazione, viene definito il gruppo fonti , che è un record delle memorizzazioni multiple, ossia un record del file MEDAV00F.
### **Sai quando compaiono i magazzini nel gruppo fonti?**

Quando l'ambiente è multiplant, ossia nella tabella B£2 non è specificato un magazzino unico ed esistono più magazzini
### **Sai come si imposta il tipo distinta che deve essere utilizzato per il calcolo del livello minimo di distinta?**

In tabella M51 è impostato il tipo distinta per il calcolo del livello minimo di distinta
### **Sai cos'è il livello minimo di distinta?**

Il livello minimo di distinta è un attributo dell'articolo che viene letto dal file BRARDT0F. Questo file è scritto da un calcolo che analizza tutte le distinte base per trovare il livello più basso (nei legami di distinta) a cui si trova  ogni articolo. Quindi gli articoli che non sono componenti di nessun assieme sono a livello 0, mentre un articolo che è legato ad un solo assieme di livello N, si trova un livello minimo uguale a N+1
### **Sai come si calcola il livello minimo di distinta in caso di distinte configurate?**

In caso di distinte configurate , dove quindi i legami di distinta non sono predefiniti a livello di distinta base ma dipendono dalle possibili configurazioni, il livello minimo di distinta deve essere calcolato ipotizzando tutte le possibili configurazioni che si potrebbero manifestare.
Il punto di questo calcolo è il programma di aggiustamento specifico che si trova sulla tabella tipi distinta (BRL).
### **Sai cos'è lo scenario di un MRP?**

E' un lemento della tabella M5B. Serve per contenere un MRP, in questo modo possono coesistere N MRP diversi in scenari diversi.
### **Sai come si fa a fare un mrp senza utilizzare i criteri di lotto minimo , multiplo, massimo?**

Per fare un MRP senza la lottizzazione bisogna definire uno scenario in cui si seleziona l'esclusione dai criteri di lottizzazione (tab M5B)
### **Sai come si fa ad impostare per un articolo un gruppo fonti specifico (diverso da quello dell'MRP,  da utilizzarsi durante l'MRP ?**

Si assegna una politica di pianificazione che contiene un gruppo fonti specifico.
### **Sai come si fa ad escludere dall'MRP i cambi di gruppo fonti?**

L' MRP è in grado di cambiare il gruppo fonti di pianificazione di un articolo se nella sua politica (tabella M5A) viene inserito un gruppo fonti specifico (chiamato anche "gr fonti da politica").
Ovviamente questa forzatura da politica potrebbe dar fastidio se si volesse eseguire un MRP con un gruppo fonti determinato, da utilizzarsi per tutti gli articoli (ad esempio quando un MRP è utilizzato per valorizzare il budget dell'anno prossimo).

Ecco che per "inibire" il cambio fonti da politica si esegue un MRP in uno scenario diverso (tabella M5B) che è caraterizzato con il parametro "No gr.fonti politica" = 1.

L'MRP eseguito su tale scenario NON cambierà il gruppo fonti di lancio con quello delle politiche.
### **Sai come si fa a datare la scorta minima?**

Ci sono due modi :  o si imposta nella tabella M51 il flag che dice di datare la scorta minima, o si definisce direttamente la fonte scorta minima come fonte futura di origine SD (scorta datata).

Nota :  è sempre opportuno datare la scorta minima perchè i suggerimenti per la copertura del sottoscorta NON nascano scaduti, ossia la data del suggerimento NON sia inferiore all'oggi.
### **Sai come si fa a trascurare un riordino?**

Per trascurare un riordino bisogna definire sulla politica di pianificazione (tabella M5A) una fonte trascurata ed un criterio di trascuratezza (leggere l'help di tabella per capire i metodi possibili)
### **Sai come si fa a fare un MRP senza leadtimes?**

Per fare un MRP senza leadtimes, ossia che produca suggerimenti con data suggerimento = data pianificata = data fonte, basta eseguirlo in uno scenario (tab M5B) in cui è stato impostato uno, o tutti, dei seguenti flags : 
No tempi ord.prod.
No tempi ord.acq.
No tempi ord.lav.
### **Sai come si fa a scrivere gli impegni di risorsa per i suggerimenti pianificati al termine dell'MRP?**

Una delle caratteristiche dello scenario di pianificazione (tabella M5B) è quella di lanciare la costruzione degli impegni di risorsa, ottenuti esplodendo il ciclo di produzione e memorizzati sempre nel file S5IRIS0F , con tipo impegno M5. Leggere l'help di tabella per capire come parametrizzare opportunamente.
### **Sai come si fa ad assegnare un fornitore ad un suggerimento di acquisto o di conto lavoro?**

Sulla politica M5A si valorizza il metodo di assegnazione ente
### **Sai  perchè il lotto massimo può essere inferiore al lotto minimo?**

Il lotto massimo viene spesso utilizzato per spaccare il riordino di materiale in N suggerimenti in parallelo, generalmente per avere un ordine diverso per ogni bancale, cesta, pallet, ossia per ogni contenitore utilizzato per muovere i materiali lungo la produzione. Questo avviene se non si vuole avere uno stesso ordine su più bancali. In altre parole, per avere una identificazione del bancale con il numero ordine.
In questo caso, mentre il lotto minimo rappresenta la quantità minima sotto di cui non si vuole produrre in quanto non risulterebbe economico (generalmente è il rapporto tra tempo di attrezzaggio e tempo di lavorazione che definisce il lotto minimo..) , il lotto massimo rappresenta la quantità per contenitore. Quindi il lotto massimo può essere inferiore al lotto minimo.

Nota :  il trattamehto che l'MRP fa del lotto massimo non è quello che erroneamente si potrebbe dedurre dal nome, ossia NON si limita mai a riordinare al di sotto del lotto massimo! L' MRP copre sempre il fabbisogno!
### **Sai quando è indispensabile utilizzare politiche a punto di riordino?**

Quando i fabbisogni dell'articolo non sono descritti da altre fonti. Succede quando l'articolo non è inserito in nessuna distinta base.
### **Sai cos'è una metafonte?**

Una metafonte (dal greco meta = dopo)  è una fonte che per essere definita abbisogna di un'altra fonte o di un  gruppo fonti. Per esempio una fonte di orgine DL = diponibilità libera abbisogna di un gruppo fonti per esistere in quanto è funzione di una funzione diponibilità. E' analogo al concetto (in analisi matematica ) della derivata di funzione.
Sono metafonti le fonti di origine : 
DL= Disponibilità Libera
BL= Disponibilità Bilanciata
FG= Fabbisogno Giornaliero
FF= Fonte Fotografata
QG=Quantità Giornaliera
### **Sai cos'è una fonte bilanciata?**

E' una metafonte che è in grado di ritornare un bilanciamento di fonti , con diversi operatori di bilanciamento (differenze, maggiore, delta solo se positivo, etc..) all'interno di periodi temporali , definiti da una fonte guida di tipo MP. Riferirsi all'help di tabella M5F per capire le possibilità applicative.

Nota :  è generalmente utilizzata per nettificare gli ordini dalle previsioni.
### **Sai come si fa ad impostare un MRP che pianifichi per ordine gli assiemi finiti e per previsione i componenti?**

Per pianificare con diversi fabbisogni i finiti ed i componenti, bisogna cambiare il gruppo fonti a queste classi di articoli. Ciò si ottiene facendo prendere ai Finiti una politica di pianificazione caratterizzata da un gruppo fonti diverso da quello con cui si lancia l'MRP.
Specificatamente a questa domanda, il gruppo fonti della politica dei finiti conterrà gli ordini di vendita ma non le previsioni, mentre il gruppo fonti con cui si lancia l'MRP conterrà le previsioni .

Nota :  la fonte previsioni che si inserisce nel gruppo fonti dell'MRP potrebbe essere sostitutiva degli impegni , sia rilasciati che pianificati, oppure essere integrativa degli impegni. In quest'ultimo caso bisogna preparare una nettificazione specifica delle previsioni rispetto agli impegni . Leggere l' help della tabella M5F che riguarda le fonti di origine BL = fonte bilanciata
### **Sai cos'è la disponibilità libera?**

La disposnibilità libera è quella funzione che, partendo dall'analisi di disponibilità, ritorna la quantità nel tempo che può essere prelevata senza inficiare la prelevabilità degli impegni già inseriti nel sistema
### **Sai quando è indispensabile utilizzare la disponibilità libera ?**

Senza fonti di tipo DL= Disponibilità Libera non saremmo in grado di far funzionare l'ATP, in quanto non sapremmo se una quantità disponibile ad una data sia prelevabile.
### **Sai cos'è una fonte di origine PM ?**

Una fonte di orgine PM è una fonte che prende dai parametri dell'articolo l'informazione quantità e data per comporre una fonte di disponibilità . Può essere sia fonte esistente (M5E) che fonte futura (M5F). Nel caso di fonte futura, ovviamente, il parametro deve essere definito con data.
### **Sai cos'è una fonte deviata?**

Una fonte deviata è una fonte che legge i dati su un altro sistema informativo.
### **Sai cos'é una fonte di altra applicazione**

Una fonte di altra applicazione è una fonte che legge i dati da una altra applicazione conosciuta e catalogata.
### **Sai cos'é una fonte fotografata?**

Una fonte fotografata è una fonte che legge i dati di un MRP, ossia i records scritti nel file M5CONS0F, in un determinato scenario.
### **Sai cos'è una fonte fissa?**

Una fonte fissa è una fonte su cui l'MRP non è abilitato a suggerire o spostamenti e/o cancellazioni. Leggere l'help della tabella M5F per comprendere appieno la parametrizzazione possibile.
### **Sai come si fa ad impedire i suggerimneti di riduzione?**

C'è un campo nella tabella delle fonti , identificato come "fonte fissa", che permette di limitare i tipi di suggerimenti che l'MRP può fare su una fonte copertura rilasciata (ordini di acquisto, produzione, conto lavoro, ..) .
Con questo campo si possono evitare sia i suggerimenti di spostamento di date, che i suggerimenti di riduzione.
### **Sai come si fa a definire una fonte che legga gli ordini di vendita?**

Bisogna definire una fonte di origine V5 e parametrizzarla opportunamente.
### **Sai come si fa ad escludere un singolo ordine di vendita, anche se attivo,  dalla lettura della disponibilità?**

Sulle righe di ordini di vendita è previsto il flag 28 che ha i seguenti significati, se valorizzato : 

1         Riga esclusa da analisi disponibilità
2         Riga esclusa se fonte neutra
3         Riga esclusa se fonte non neutra

per cui per escludere uan riga di ordine dall'analisi dipsonibilità basta valorizzare questo flag e poi indicare sulla fonte che legge la riga di essere sensibile a questo flag (help tabella M5F, origine V5)
### **Sai dove si trova la documentazione che permette di attivare velocemente un MRP ?**

Nella documentazione del modulo M5CMRP, ma anche in google, cercando con le parole chiave "SMEUP" e "MRP"
### **Sai come si fa a rilasciare alcuni suggerimenti di acquisto in RDA oppure in ordini di acquisto direttamente?**

Sulla fonte pianificata si immette il pgm di rilascio M5PNV5_SM (per gli ordini di acquito) o il pgm M5PNRA_SM (per le RDA) . Quest0ultimo è valido se le RDA sono gestite con l'applicazione GA. Se invece sono gestite con l'applicazione V5, allora si utilizza il pgm M5PNV5_SM, seguito da un opportuna parametrizzazione per il rilascio (tabella M5V)
### **Sai come si fa a rilasciare tutti i suggerimenti di acquisto sotto una stessa testata?**

Impostando sulla fonte pianificata, oltre al pgm M5PNV5_SM, anche un elemento della M5V che preveda l'accodamento ad una testata documento
### **Sai come si fa a rilasciare un suggerimento di annullamento che modifichi solo lo stato del rilasciato, senza cancellazione fisica?**

Il metodo di applicazione dei suggerimenti è descritto nella tabella M5V (per i rilasci in ordini di acquisto o rda) e M5P (per i rilasci in ordini di produzione). In entrambe le tabelle è prevista la condizione di annullamento che agisce sullo stato, tipicamente lo porta a 90 (annullato).
Per agire con queste logiche sulle fonti rilasciate bisogna ovviamente valorizzare sulle fonti sia il programma di applicazione che il metodo di applicazione.
### **Sai come si fa ad impostare un MRP multiplant?**

Leggere la documentazione relativa :  si trova anche in google, SMEUP MRP MULTIPLANT
### **Sai cos'è un ordine di trasferimento?**

E' un ordine tra 2 plant e serve per trasferire il materiale dal magazzino di competenza al magazzino che ne ha bisogno
### **Sai come si impostano i magazzini sull'ordine di trasferimento?**

Il magazzino principale è quello che riceve, il magazzino di trasferimento è quello che spedisce.
### **Sai cos'è il magazzino di competenza in un MRP multiplant ?**

E' il magazzino responsabile di produrre (o acquisire) l'articolo :  è impostato nell'anagrafica articoli (Ente responsabile)
### **Sai come si imposta il leadtime di trasferimento tra magazzini?**

Nella tabella M5J
### **Sai come si impostano i magazzini sulla bolla di trasferimento?**

Si impostano inversamnete ai magazzini sull'ordine di trasferimento :  quindi il magazzino principale è quello che spedisce mentre quello di trasferimento è quello che riceve.
### **Sai come si fa ad esplicitare in una analisi di disponibilità sia gli ordini di vendita, che le bolle estratte, che le richieste di movimentazione estratte?**

Bisogna impostare delle fonti ordine che siano sempre al netto delle bolle estratte ed al netto delle richieste estratte. Poi bisogna ggiungere le fonti "bolle estratte e non collegate" e le fonti "RIM estratte"
### **Sai utilizzare un MRP per analizzare il Budget di un anno ?**

Si imposta un MRP in uno scenario diverso, con un gruppo fonti che abbia solo il budget come fonte principale, e le fonti pianificate. Poi conviene sviluppare anche gli impegni di risorsa al termine dell'MRP (leggere help tabella M5B) di modo che l'analisi del modulo P5IRIS mostri il workload relativo al budget.
### **Sai lanciare 3 MRP in coda l'uno all'altro con un comando solo?**

L'MRP prevede sia un flusso di azioni pre MRP che un flusso di azioni Post MRP. Se nel flusso di azioni post MRP si inseriscono azioni di lancio MRP , se ne possono lanciare quanti se ne vuole.
### **Sai fare in modo che un MRP legga il risultato dell'altro e lo tratti come fonte?**

Tramite le fonti fotografate. Attenzione :  una fonte positiva in un MRP può essere fotografata e vista nell'altro MRP ma non può essere cambiato il segno della fonte !
### **Sai fare in modo che un riordino per mancanza di copertura scorta minima si generi solo quando la scopertura è maggiore del 66 %**

Nella tabella M5A delle politiche di pianificazione si possono impostare due metodi di trascuratezza. Uno per i riordini normali, ed un'altro per i riordini da sottoscorta. In questo caso, la politica per la trascuratezza si basa su una percentuale di sottoscorta (percentuale di scopertura accettata ) impostabile in tabella M5A.

Questa funzione serve per non partire a riordinare il lotto di riordino non appena la giacenza è inferiore di una unità rispetto alla scorta minima, ma si ritiene di poter sopportare una scopertura del 40 o 60 % prima di fare il riordino.
### **Sai rilasciare in blocco una serie di suggerimenti?**

Dalla scheda M5CMRP, si selezionano i suggerimenti cliccando sulla colonnina grigia a destra dell'identificativo e tenendo premuto il tasto Ctrl. Poi si trascinano (drag) sul bottone del rilascio
### **Sai lanciare un MRP solo per una serie di articoli?**

Se si crea una lista di articoli si può lanciare l'MRP solo per quella lista impostando opportunamente la schermata di lancio
### **Sai cancellare uno scenario MRP e tutto il suo contenuto?**

Dall'Hypermenu si trova la funzione F-funzioni su scenari sotto il gruppo ACTIONS che permette la gestione degli scenari
### **Sai capire in che data/ora/minuto/secondo un articolo è stato pianificato?**

Solo se si è impostato il log della pianificazione nella tabella M51, allora viene mostrato per ogni articolo data, ora, minuto e secondo della pianificazione
### **Sai perchè l'MRP di smeup può girare mentre la fabbrica lavora?**

Perchè l'MRP legge la disponibilità di un articolo un istante prima del calcolo. In questo modo le probabilità che la situazione dell'articolo si modifichi tra il momento in cui viene fotografata ed il momento del calcolo è infinitesima
### **Sai impostare il calcolo indici dell'MRP?**

Nella tabella M5B degli scenari c'è l'impostazione del calcolo indici. NOTA :  fasare prima opportunamente gli indici ed il contesto, utilizzare il pgm D5FS01A !
### **Sai capire se un suggerimento di produzione ha gli impegni coperti?**

Con la funzione E1 (altre funzioni - esplosione) lanciata dal pop up del suggerimento ordine di produzione.
### **Partendo da un suggerimento di acquisto, sai capire a quali assiemi finiti serve**

Con la funzione I1 (altre funzioni - implosione) lanciata dal pop up del suggerimento
### **Sai cos'è l'analisi di copertura di Smeup?**

E' quell'analisi che permette di capire le relazioni tra i fabbisogni e le coperture, ossia quale fonte positiva soddisfa quale fabbisogno negativo.
E' una analsi che si svolge sia a livello (orizzontalmente sul bilancino di un articolo) , sia verticalmente attraverso la distinta base (in questo caso viene chiamata pegging)
### **Partendo da un ordine di vendita, sai capire se è producibile internamente o deve aspettare la consegna di materiale dall'esterno?**

Faccio una analisi E1 e vedo se esiste qualche ramo della distinta che è coperto da fonti future
### **Sai cambiare il programma di applicazione suggerimenti per una fonte ?**

Nella tabella della fonte pianificata campio il pgm di rilascio
### **Sai perchè è utile raggruppare la fonte impegno ?**

Gli impegni sono molto numerosi, al punto che possono essercene centinaia a parità di data ed articolo. Per diminuire il numero di righe che l'MRP registra è utile raggruppare per data gli impegni.
### **Sai cosa si perde quando si raggruppa la fonte impegno?**

Si perde la possibilità di analisi pegging quando passa per un articolo che ha gli impegni raggruppati.
### **Sai cos'è un Home Made MRP ?**

E'possibile demandare totalmente la costruzione dei suggerimenti pianificati alla exit di
assegnazione enti, sia come raggruppamento dei fabbisogni, sia come loro datazione.
Si può realizzare quindi un H(ome made) MRP.
In tal modo si possono, ad esempio, ottenere raggruppamenti diversi in funzione dell'ente, oppure
in funzione della data o della quantità.
### **Sai cos'é un MRP per destino?**

E' un MRP che ha come secondo codice di rottura il fornitore e che serve per descrivere un sistema logistico in cui la composizione di un prodotto tramite composizione dei suoi diversi livelli di distinta , avviene su un parco terzisti (conto lavoro pieno) . In questo caso è opportuno descrivere le scorte minime di siscurezza tra un terzista e l'altro ed utilizzare l'MRP per far partire le "chiamate" (ossia i suggerimenti di conto lavoro) che hanno come fornitore il produttore e come "destino" il terzista a cui debbono essere direttamente conseganti. leggere la documentazione specifica per capire la complessità dell'impianto tabellare a supporto dell'MRP per destino.
### **Sai quando un MRP sbaglia?**

L'MRP sbaglia quando non copre totalmente i fabbisogni che sono rappresentati. Si capisce perchè la disponibilità finale è negativa!

Questo succede per due possibili motivi : 

1- il più frequente è quando il gruppo fonti utilizzato per pianificare non include gli impegni pianificati. Quindi il calcolo non li considera, pianifica solo per gli altri fabbisogni, ma quando si interroga il bilancino dell'articolo si vede una disponibilità finale diminuita dalla quantità degli impegni pianificati (perchè sono stati scritti comunque!)
2- se il livello minimo di distinta non è aggiornato (perchè non impostato l'aggiornamento nella M51.., e non impostato l'aggiornamento interattivo sul tipo distinta...) può capitare che il calcolo di un articolo venga eseguito prima che tutti i suoi impegni pianificati siano stati scritti. Quindi li ignora al momento del calcolo ma si evidenziano nel bilancino dell'articolo
### **Sai definire i leadtimes in giorni di calendario per i fornitori ed in giorni lavorativi per la produzione?**

In tabella M51 è possibile diversificare tra acquisto, conto lavoro e produzione il criterio di lettura leadtimes
### **Sai definire un calendario per i fornitori che l'MRP possa considerare per applicare il leadtime?**

In tabella M51 si definisce il tipo calendario da utilizzarsi per conto lavoro ed acquisto, ovviamente scegliendo un calendario per fornitori. Poi si gestisce questo calendario.
### **Sai dove si definiscono il punto di riordino e la scorta minima?**

Nei dati magazzino / articolo, file GMARMG0F
### **Sai rifasare gli impegni di risorsa di un MRP?**

Da hypermenu del modulo M5CMRP, con l'opzione R-Rifasatura impegni risorse .
### **Sai vedere una matrice , con una riga per articolo e nelle colonne le quantità delle fonti ad una certa data?**

La scheda di consulatazione dell'MRP mostra in basso a destra un bottone chiamato "analisi per gruppi". Utilizzando questa funzione si ottiene una matrice con righe per articolo e nelle colonne le quantità delle singole fonti, o dei raggruppamenti di fonti .
### **Sai vedere una matrice, con una riga per articolo e nelle colonne la disponibilità per periodi mensili a partire da una certa data?**

La scheda di consulatazione dell'MRP mostra in basso a destra un bottone chiamato "analisi per data". Utilizzando questa funzione si ottiene una matrice con righe per articolo e nelle colonne disponibilità per date.
### **Sai cos' è una fonte eccedente futura?**

E' quella fonte che rappresenta l'eccedenza che si va a creare a seguito di vincoli di lottizzazione o a seguito di ordini rilasciati eccedenti.
### **Sai come si fa ad impostare un secondo codice di rottura in MRP?**

Si agisce sulla tabella M51, valorizzando il campo opportuno.
Poi bisogna anche valorizzare l'analogo campo sulle politiche (tabella M5A).
Infine, bisoganrendere le fonti sensibili (separate) al secondo codice di rottura.
### **Sai quali possono essere i secondi codici di rottura in MRP?**

I secondi codici di rottura possono essere : 
CF Configurazione
CM Commessa
CN  Enti (tipicamente il fornitore nell'MRP per destino)
EM Esponente di modifica

Nota :  Per utilizzare in MRP un secondo codice di rottura, le fonti debbono essere separate coerentemente.
### **Sai perchè l'MRP parzlale può dare risultati diversi dal totale?**

Perchè rinfresca la situazione dei soli articoli toccati dalla parzialità, ossia eplode le distinte solo degli articoli parzializzati. I cambiamenti provenienti anche da altri articoli si rendono evidenti solo con un MRP totale
### **Sai come tracciare a stampa tutti i codici elaborati da un MRP parziale?**

Impostando nella tabella PGM il log per il programma M5MRP0A, mettendo 1 nel campo LOG.
### **Sai se è necessario, per un MRP parziale, avere il LLC corretto?**

No, per un MRP singolo codice non è necessario.
### **Conosci la modalità di pianificazione make or change?**

E' la modalità con cui l'MRP decide se anticipare un ordine in corso o proporre un nuovo suggerimento
### **Conosci la differenza tra politica master, specifica e del riferimento?**

La politica master per un articolo è la prima che incontra tra quelle di produzione, acquisto e conto lavoro. Quella specifica è quella che è stata applicata per proporre un suggerimento (diversa dalla master solo se esistono almeno 2 politiche per l'articolo), quella del riferimento è quella ottenuta sui parametri di pianificazione di riferimehto (esempio per Fornitore) se quella master accetta la deviazione a quella di riferimento. Leggere help di tabella M5A
### **Sai ottenere periodi di raggruppam.fissi (es : settim.da lunedi a venerdi)?**

Nella polita di pianificazioen, tabella M5A, bisogna impostare un raggruppamento con periodicità.
### **Sai come far sì che un ordine di produzione pianificato non generi impegni?**

Nella politica (tab M5A) non si mette la fonte degli impegni pianificati.
### **Sai perchè l'MRP potrebbe escludere alcuni articoli?**

Se non è prevista la ricostruzione del livello minimo in pre-Mrp, ma è fasato dinamicamente durante la manutenzione della distinta, dopo aver scandito tutti gli articoli presenti nell'archivio del livello minimo, viene scandito, tramite interfaccia, l'archiivio anagrafico degli articoli, e vengono pianificati i codici assenti dall'archivio del LLC. Questa interfaccia deve essere realizzata correttamente anche per la scansione, se non è realizzata correttamente alcuni articoli potrebbero risultare esclusi dall'MRP
### **Sai quale comportamento si può far assumere agli ordini pianificati scaduti?**

E' possibile escludere dalla lottizzazione gli ordini scaduti, impostando il flag specifico di
tabella M51, che prevede anche la modalità per cui un ordine pianficato si classifica come
scaduto (rispetto alla data suggerimebto, o alla data fine pianificata, o alla data fonte...).
L'esclusione dalla lottizzazione per i suggerimenti scaduti è utile per evitare di creare disponibilità libera di improbabile realizzazione.
### **Sai come è possibile utlizzare giorni solari e di calendario per ordini di diverso tipo?**

Nella tabella M51 è possibile impostare giorni solari o di calendario per suggerimenti di acquisto, produzione o conto lavoro.
### **Sai dove si impostano i tempi di transito tra due plant?**

Nella tabella M5J :  questo significa che i leadtimes presenti nei parametri di pianificazione nella colonna dedicata ai trasferimenti, NON hanno effetto sulla datazione dei suggerimenti di trasferimento.
### **Sai se 2 MRP possono girare simultaneamente senza disturbarsi?**

Solo se non è impostato il ricalcolo del livello minimo di distinta in tabella M51. Altrimenti, un mrp potrebbe cancellare il llc di un articolo e l'altro mrp lo considererebbe a zero....., ottenendo informazioni sbagliate. Un'altra condizione affinchè non si disturbino è che non ci siano nei gruppi fonte delle fonti fotografate che leggono dati dall'altro MRP.
Quindi, se si vuole lanciare 2 o più MRP contemporaneamente, bisogna disattivare in tabella M51 il ricalcolo del low level code, e schedularlo di notte (pgm BRRLCA), oppure definire nel tipo distinta (tabella BRL) l'aggiornamento automatico del low level code (è raccomandato se non si hanno distinte troppo complesse, altrimenti rallenta troppo l'aggiornamento ).
