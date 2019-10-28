### **Sai quali sono i file coinvolti nella gestione dei documenti Sme.up?**

I files coinvolti sono : 
V5TDOC0F - Testate documenti
V5RDOC0F - Righe documenti
V5BATC0F - Archivio per la gestione di acquisizione di documenti in modo batch

### **Sai quali sono le tabelle necessarie per la gestione documenti Sme-up? (quelle principali)**

Le tabelle principali sono : 
V5D - Tipo documenti
V5A - Modello documenti
V5B - Tipo riga documenti
V51 - Parametri ciclo attivo
V5S - Spese/Maggiorazioni/Sconti
B£Y - Gruppi flag
B£W - Stati documento
### **I documenti vengono memorizzati tutti nello stesso file, sai spiegare come si identificano i diversi documenti?**

I documenti sono identificati dal Tipo documento (tabella V5D)
### **Sai qual'è il legame tra la testata documento e le righe documento (chiavi primarie dei file)?**

Le testate e le righe documento sono identificaate in modo univoco dal campo TIPO DOCUMENTO e dal campo NUMERO DOCUMENTO.
Le righe documento poi hanno un numero riga progressivo.
### **Sai come capire se un documento è di ciclo passivo o attivo?**

Un documento può essere identificato di ciclo passivo o attivo in funzione del campo TIPO MODELLO (T§TIPM).
Tale campo viene assegnato nella tabella V5A Modello documento.
### **Sai quanti sono e che funzioni hanno gli enti gestiti sulla testata documento?**

Sulla testata documento sono gestiti 4 enti : 
- Ente intestatario :  ente a cui l'ordine viene emesso. E' l'ente selezionato all'atto dell'inserimento dell'ordine.
- Ente di conferma :  ente per la conferma dell'ordine (presente solo in testata)
- Ente di spedizione :  ente a cui è destinata la merce. E' selezionabile all'atto dell'emissione dell'ordine.
- Ente di fatturazione :  ente a cui dovrà essere intestata la fattura, che verrà preso come ente anche per la contabilizzazione (presente solo in testata)
### **Sai quanti sono e che funzioni hanno gli enti gestiti sulla riga documento?**

Sulla riga documento sono gestiti 3 enti : 
- Ente intestatario :  ente a cui l'ordine viene emesso. Viene ereditato dalla testata documento e non è modificabile.
- Ente di spedizione :  ente a cui è destinata la merce. Viene ereditato dalla testata documento ed è possibile modificarlo. Possono essere inserite righe con enti di spedizione differenti.
- Ente di destino :  ulteriore ente utilizzbile sui movimenti di magazzino per gestioni specifiche
### **Sai dove viene memorizzato il TIPO ENTE di default per gli enti gestiti sul documento?**

Nella tabella V5D, che definisce i tipi documento è possibile specificare, per ciascun tipo documento, il tipo di ogni ente gestito sul documento.
Tali tipi ente saranno proposti all'atto inserimento documenti, ma saranno cmq modificabili.
### **Sai se è possibile derivare un documento generandolo da uno di tipo diverso?**

Esiste la possibilità di generare un documento derivandolo da un documento esistente.
Si deve eseguire un flusso che permette di generare testata e riga partendo da documenti già inseriti.
Si rimanda alla documentazione Gesstione Flussi per determinare come e quali parametri impostare per eseguire un flusso.
### **Sai come determinare il numero di un documento?**

Il numero documento, inteso come Chiave primaria, quindi numero riferimento interno, è assegnabile attraverso un numeratore.
Il legame con il numeratore (tabella CRNV5) è definito nella tabella V5A.
### **Sai come sono legati due documenti se il secondo è derivato dal primo?**

Il legame tra due documenti origine e derivato è scritto nei campi di riga del documento derivato : 
Tipo documento Origine
Numero documento Origine
Numero riga origine
### **Sai cos'è lo stato del documento, e che legame ha con il livello?**

Lo stato è la condizione in cui si trova il documento : 
Può essere Attivo, Chiuso o Annullato.

Lo stato del documento (presente sia sulle testate che sulle righe) è un campo di due posizioni che fa riferimento alla tabella B£W; è strettamente connesso al livello :  uno stato può avere uno ed un solo livello. Per esmpio lo stato attivo (nello standard sme.up 10) ha il livello 2=attivo.
Il livelllo invece può essere assegnato a più stati. Per esmpio gli ordini di livello 2=attivo, si possono trovare in stati diversi :  10 aperto, 20 approvato, 30 in evasione.
Su un documento può essere modificato lo stato, ma non il livello. Il livello sul documento viene assunto dallo stato assegnato.
### **Sai come viene gestito lo stato del documento?**

Lo stato del documento può variare con diverse modalità.
Può essere modificato da un flusso di collegamento nel momento in cui il documento derivato viene collegato al documento origine.
Oppure può essere modificato da un flusso di workflow.
Oppure ancora può essere modificato attraverso funzioni specifiche utente.
Non da ultimo, lo stato del documento può essere modificato intervenendo manualmente direttamente sul campo Stato del documento.

Cambiando lo stato della testata del documento, i flussi standrd di sme.up fanno sì che le righe assumino lo stato della testata, se si tratta di un avanzamento.
### **Sai in che momento avviene l'avanzamento di stato?**

L'avanzamento di stato avviene per evasione di un documento (da ordine a bolla, da previsione a ordine), quindi nel momento in cui veine creato un documento derivato e collegato.
Oppure può essere modificato da un flusso di workflow.
Oppure ancora può essere modificato attraverso funzioni specifiche utente.

L'avanzamento di stato fa sì che il documento assuma lo stato successivo definito nella tabella B£W per lo stato esistente sul documento al momento di una delle azioni precedenti.
### **Sai cosa accade quando un documento derivato viene collegato al suo documento origine?**

Il documento origine viene modificato registrando la quantità evasa tipicamente nella qnaità 2 di riga del documento.
Inoltre se l'evasione fosse totale viene anche cambiato lo stato della riga e se tutte le righe del documento origine venissero processate ed evase totalmente, anche lo stato della testata cambierebbe.
### **Sai se è possibile che un documento derivato non abbia effetto sul documento da cui è derivao? Come?**

Se nel flag 08 di riga documento (Stato collegam. Doc. origine ) è impostato il valore '9' il documento derivato non verrà colelgato al documento origine. Quindi non si avrà l'effetto di registrazione della quantità evasa e l'avanzamento di stato.
### **Sai a cosa serve il criterio ordinamento documento presente sulla testata documento?**

Il criterio di ordinamento documento ha molteplici funzioni in conseguenza allo stato in cui si trova il documento : 
- Documento non fatturato :  il criterio ordinamento documento ha la funzione principale di organizzare i documenti in funzione della fattruazione
- Documento fatturato e contabilizzato :  il criterio ordinamento documento riporta i dati contabili principali.
### **Sai  come si gestiscono e che significato hanno le date Richiesta e Confermata sulla testata/riga documento?**

In termini generali la data RICHIESTA esprime la data di consegna richiesta dal destinatario della merce/servizio oggetto del documento (es. in ordine la data richiesta dal cliente), mentre la data CONFERMATA esprime la data che il fornitore conferma al cliente in base alla propria disponibilità.
Le suddette date hanno caratteristiche di obbligatorietà diverse tra testata e riga : 
- testata, richiesta obbligatoria, confermata si compila solo se opportuno
- riga, sia la richiesta che la confermata sono obbligatorie, se non determinata la confermata si imposta come la richiesta
Le date compilate in testata vengono proposte come date assunte durante l'immissione di una nuova riga.
### **Sai su che applicazioni hanno principalemnte effetto le date Richiesta/Confermata presenti sulle testate e righe documento??**

La data confermata nella riga è determinante per tutte le considerazioni di disponibilità materiali (sia positive che negative), motivo per la quale è obbligatoria.
La data confermata è utilizzata anche nel calcolo della disponibilità finanziaria (ADF) per determinare il momento presunto della fatturazione in documenti come previsioni ed ordini.
### **Sai quali sono i tipi oggetto che identificano i documenti?**

DO = Testate documento
DR = Righe documento
Per entrambi gli oggetti, il parametro è rappresentato dal tipo documento, ed è obbligatorio nella determinazione dell'oggetto.
### **Sai dove leggere il significaoto dei flag fi testata e righe ed i valori possibili che essi possono assumere?**

Esitono due moetodi per leggere i flag ed il loro significato : 

- Attraverso la /copy £G06 è possibile ottenere l'lenco dei flag gestiti su un file.
Lanciando da una riga comandti il programma TSTG06 e passandogli i parametri :  funzione DOC e metodo V, si ottiene l'elenco dei flag gestiti in un file con la   descrizione e la lista dei valori possibili che essi possono assumere.

- Attraverso il comando DSPFLD (Abbreviato F) seguito dal nome del file, si visualizza l'elenco dei campi del file, posizionandosi su ciascun campo, è possibile inserire l'ozione V nella colonna "R" e vengono visualizzati i possibili valori che il campo può assumere.
### **Sai dare una descrizione completa della funzionalità del flag 19 di testata?**

Il Flag 19 di testata documento è il flag che identifica lo stato del documento ai fini della fatturazione.
I valori che può assumere sono alfabetici e sono in carattere MAIUSCOLO se si stratta di un documento di CICLO ATTIVO, sono invece in carattere MINUSCOLO se si tratta di un documento di CICLO PASSIVO.
Se il fla 19 è  ' ' (vuoto) il documento non è da fatturare (ciclo attivo), ovvero non si vedrà nel controllo bolle fatture (ciclo passivo).
Tipicamente i documenti Previsione, Ordine, Offerta avranno il falg 19 vuoto perché per loro natura non entreranno nel ciclo di fatturazione.
Fatta eccezzione per gli ordini di acquisto, che potrebbero rientrare nel ciclo di controllo bolle fatture (per questo si rimanda all'applciazione C5, Modulo C5C040 Controllo docuemnti/Fatture).
I valori dalla  'A' 'a' alla 'E' 'e' riguardano la condizione dei documenti Fattura, mentre i valori dall 'M' 'm' alla  'Q' 'q' riguardano la posizione dei documenti Nota di Accredito.
'A' - 'a'         Non pronta
'B' - 'b'         In attesa
'C' - 'c'         In esame
'D' - 'd'         Bloccato
'E' - 'e'         Fatturato e Contabilizzato
'M' - 'm'        Non pronta
'N' - 'n'         In attesa
'O' - 'o'         In esame
'P' - 'p'         Bloccato
'Q' - 'q'         Fatturato e Contabilizzato
### **Sai indicare in che modi e in che flussi cambia lo stato del flag 19 di testata?**

A standard lo stato del flag 19 cambia quando : 
Ciclo attivo
- Viene stampata la bolla (DDT)
- Viene contabilizzata la fattura/N.C. attiva
Ciclo passivo
- Viene stampatao l'eventuale DDT di reso (sulla base del quale il fornitore emetterà nota di accredito)
- Viene registrata la fattura/N.C. passiva attraverso la procedura di controllo bolle fatture

E' possibile poi sviluppare flussi personalizzati che gestiscano anche lo stato del falg 19.
### **Sai se la testata documento è direttamente collegabile ad una registrazione contabile e come?**

Sì, è possibile rintracciare la registrazione contabile relativa ad una testata documento contabilizzata, utilizzando il campo T§CORD - Criterio ordinamento documento, oppure tramite il campo T§NRFC - Riferimento contabile.
### **Sai se il criterio ordinamento documento è personalizzabile e come?**

Nella tabella V5A (modello documento) viene definito il criterio ordinamento di partenza, associato al modello, tramite il campo T$V5AG.
Tale criterio ordinamento è calcoalto dal programma V5DO01O se il carattere inserito in questo campo è numerico. Se invece il carattere inserito è alfabetico, è necessario implementare il prgramma di exit V5DO01O_x (dove x è l'estensione scritta nel campo T$V5AG) che calcola il criterio ordinamento in modo specifico (personalizzato).
### **Sai il significato e la rilevanza dei campi Quantià in unità di misura interna e Quantità in unità di misura esterna sulle righe documento?**

Sulle righe documento è possibile gestire la doppia unità di misura, in quanto potrebbe rendersi necessario, interfacciandosi con il fornitore/cliente, gestire una unità di misura diversa rispetto a quella gestita internamente a magazzino.
Ecco quindi che la quantità in unità di misura interna registra la quantità nell'unità di misura gestita a magazzino, mentre l'unità di misura esterna registra la quanità gestita esternamente. Le due quanità sono relazionate da un fattore di conversione (definibile nella tabella UMS).
I movimenti di magazzino verranno eseguiti utilizzando la quantità in unità di misura interna.
### **Sai il significato e l'utilizzo dei Valori presenti sulle righe documento?**

### **Sai se e come una riga di documento è direttamente collegata ad una registrazione?**

Sulla riga documento è presente il campo R§NRFC - Num.Riferimento contabile che riporta il numero della testata della registrazione contabile collegata alla riga.
### **Sai se e come è possibile attribuire ad una riga documento parametri da riportare in contabilità?**

Sulle righe documento è possibile assegnare un conto contabile specifico che verrà poi utilizzato per creare la registrazione contabile.
Tale conto dovrà essere scritto nel campo R§CONT - Conto contabile.
E' anche possibile assegnare un centro di costo ed una voce di spesa specifiche, informazioni necessarie per la contabilità analitica.
I campi deputati a memorizzare tali informazioni nelle righe documento sono :  R§CRIC - Centro di ricavo (costo) e R§VODS - Voce di spesa.
### **Sai cos'è il tempo di approvvigionamento?**

### **Sai su quali applicazioni ha effetto il tempo di approvvigionamento?**

"comm"
### **Sai a cosa serve il campo - Suff.bolle DDT - nella tabella V5A?**

Il "Suffisso bolle DDT" serve per differenziare il programma di stampa bolle, è possibile quindi gestire diverse stampe di DDT attraverso un programma di exit (V5BO01Sx dove x il "Suff.Bolle DDT") che viene lanciato dal V5BO01S.
### **Sai a cosa serve il campo - Suff.vis.dett.docum - che si trova nella tabella V5A?**

Attraverso qusto campo è possibile gstire un porgramma di exit V5IN01_x (dove x è il valore presente nel campo in oggetto) per gestire la visualizzaizone del dettaglio del documento, ovvero l'esposizione delle righe nel passaggio da testata a righe (Quando si preme F07 dalla testata oppure si sceglie l'opzione RI).
### **Sai quali sono le classi di autorizzazione per la gestione dei documenti e la loro funzione?**

Le classi di autorizzazione per le testate documenti (V5TDOC0F) sono : 
V5DO01    - Gestione testate documenti
Serve per abilitare la gestione delle testate documenti (modifica, inserimento, visualizzazione etc..)

V5DO01M - Gestione testate documenti per modello
Come la precedente, con un ulteriore parametro che è il modello per gestire autorizzazioni in modo più specifico.

V5DO01D - Gestione testate Tipo documento in funzione Stato Flag
Serve per gestire le autorizzazioni in funzione dello stato, della condizione del falg 19 di testata, del flag 01 di collegamento a magazzino e del falg 02 di colelgamento a statistiche.

PLC-V5TDOC - Protezione campi testate documenti
Per proteggere la gestione e visualizzazione dei campi presentati nei visualizzatori

RIS-   - Riservatezza
Protezione campi presenti in :  Lista campi (funzione V5T-xxx), Lista numeri (funzione VL_DOxxx), Sintesi conti spese tasse (funzione V5Dxxx)

ABILITA + funzione V5DO01D - Abilitazioni SI/NO - Funzioni aggiuntive F14
Permette di vedere le funzioni presenti nell'F14 funzioni aggiuntive

B£FUN0 + funzione DO - Abilitazioni funzioni di un oggetto
Serve per permettere la visulizzazione e l'utilizzo delle funzioni di testata presenti nell'F10 Funzioni oggetto


Le classi di autorizzazione per le righe documenti (V5RDOC0F) sono : 
V5DO05    - Gestione righe documenti
Serve per abilitare la gestione delle righe documenti (modifica, inserimento, visualizzazione etc..)

V5DO05M - Gestione righe documenti per modello
Come la precedente, con un ulteriore parametro che è il modello per gestire autorizzazioni in modo più specifico.

V5DO05D - Gestione righe Tipo documento in funzione Stato Flag
Serve per gestire le autorizzazioni in funzione dello stato e della condizione del falg 24 controllo bolle fatture.

PLC-V5RDOC - Protezione campi righe documenti
Per proteggere la gestione e visualizzazione dei campi presentati nei visualizzatori

RIS-   - Riservatezza
Protezione campi presenti in :  Lista campi (funzione V5T-xxx), Lista numeri (funzione VL_DOxxx), Sintesi conti spese tasse (funzione V5Dxxx)

ABILITA + funzione V5DO05D - Abilitazioni SI/NO - Funzioni aggiuntive F14
Permette di vedere le funzioni presenti nell'F14 funzioni aggiuntive

B£FUN0 + funzione DR - Abilitazioni funzioni di un oggetto
Serve per permettere la visulizzazione e l'utilizzo delle funzioni di riga presenti nell'F10 Funzioni oggetto
### **Sai quali sono le copy principali della testata documento e sai spiegare le loro funzioni?**

£IDO - Interfaccia testate documenti ciclo esterno. Permette la ricerca ed il recupero delle informazioni di una testata documento.
Inoltre gestisce le funzioni di scrittura, cancellazione, modifica e l'esecuzione dei flussi.

£V5Y - Inizializzaione testate documenti

### **Sai dove trovare l'elenco delle classi di autorizzazione per al gestione delle testate e righe dei documetni?**

E' possibile leggere le classi di autorizzazione coinvolte nella gestione documenti, dalla documentazione per oggetto dei file V5TDOC0F e V5RDOC0F.
Vale a dire :  andare sulla lista campi del file (utilizzando il comando DSPFLD oppre il comando abbreviato F), premere F1 per visualizzare l'help da dove si potranno leggere, oltre ad una descrizione dei campi, anche le classi di autorizzaione da abilitare e la loro funzione.
### **Sai quali sono le copy principali delle righe documento e sai spiegare le loro funzioni?**

£IDR - Interfaccia righe documenti ciclo esterno. Permette la ricerca ed il recupero delle informazioni di una riga documento.
Inoltre gestisce le funzioni di scrittura, cancellazione, modifica e l'esecuzione dei flussi.

£V5Z   - Inizializzaione righe documenti
£V5L   - Informazioni collegate ad un tipo riga
£V5V\* - Calcolo valori con dati variabili
### **Sai cosa si intende per Ingresso in Lista e come si gestisce?**

L'ingresso in lista permette di gestire in un sub-file le righe di un documento.
Si attiva dalla tabella V5A (campo T$V5AK Suff.caricamento in lista) ed è possibile creare dei programmi di visulizzaione specifica attraverso il programma di exit V5DO19x (dove x assume il valroe del campo T$V5AK).
### **Sai come può essere personalizzata la visualizzazione dei dati di un documento (testata e righe)?**

Attraverso i "Visulizzatori" si può personalizzare l'esposizione dei dati sia delle testate che delle righe.
I programmi "Visualizzatori" in più possono eseguire anche delle operazioni di controllo, ricerca ed aggiornaemnto, in funzione di logiche specifiche.

Il prgramma di visualizzazione per la testata è associabile al modello documento (tabella V5A).
Il campo da valorizzare è il campo T$V5AF - Forma percorso, che fa riferimento alla tabella B£Q. L'elemto di questa tabella conterrà il nome del programma personale da usare per visualizzare la testata documento.

Il prgramma di visualizzazione per le righe è associabile al Tipo riga documento (tabella V5B).
Il campo da valorizzare è il campo T$V5BF - Forma percorso, che fa riferimento alla tabella B£Q. L'elemto di questa tabella conterrà il nome del programma personale da usare per visualizzare la riga documento.
### **Sai se e come possono essere gestiti controlli specifici sui campi delle testate e delle righe documenti?**

E' possibile gestire delle Exit per personalizzare controlli di campi sia su righe che su testate documenti.

Il prgramma di exit controllo campi per le testate, è associabile al modello documento (tabella V5A).
Il campo da valorizzare è il campo T$V5A1- Suff.Controllo campi, verrà quindi richiamato il programma V5DO01C_x dove x è il carattere inserito nel campo Suff.controllo campi.

Il prgramma di exit controllo campi per le righe, è associabile al tipo riga (tabella V5B).
Il campo da valorizzare è il campo T$V5B4- Suff.Controllo campi, verrà quindi richiamato il programma V5DO05C_x dove x è il carattere inserito nel campo Suff.controllo campi.
### **Sai se e come possono essere gestiti controlli sugli enti dei documenti?**

Per gestire controlli aggiuntivi sugli enti è possibile utilizzare un programma di exit.
Tale programma viene definito sul modello documento (tabella V5A).
Il campo da valorizzare è il campo T$V5A3- Suff.Controllo ente, verrà quindi richiamato il programma V5DO01E_x dove x è il carattere inserito nel campo Suff.controllo ente.

### **Sai se e come può essere deviata l'inizializzaiozne di un documento (testata e righe) rispetto al motore standard?**

Esiste la possibilità di intervenire durante l'inizializzazione di un documento sia sulle righe che sulla testata attraverso programmi di exit.

Il prgramma di exit per la gestione dell'inizializzazione della testata è associabile al modello documento (tabella V5A).
Il campo da valorizzare è il campo T$V5A7- Suff.inizializzazione, verrà quindi richiamato il programma V5V5Y0_x dove x è il carattere inserito nel campo Suff.inizializzazione.

Il prgramma di exit per la gestione dell'inizializzazione della riga è associabile al tipo riga documento (tabella V5B).
Il campo da valorizzare è il campo T$V5B£- Suff.inizializzazione, verrà quindi richiamato il programma V5V5Z0_x dove x è il carattere inserito nel campo Suff.inizializzazione.
### **Sai cosa sono i parametri impliciti di un dcumento?**

I parametri impliciti di un documento sono i campi liberi a disposizione dell'utente presenti sui file, da compilare in modo personalizzato.
Tali campi sono : 

TESTATE : 
10 campi numerici
10 campi alfanumerici
10 campi data

RIGHE
10 campi numerici
10 campi alfanumerici
10 cami data
### **Sai come si definiscono i parametri impliciti di un documento?**

Il significato dei parametri impiciti si stabilisce attraverso la tabella C£I che a sua volta punta alla tabella B£N per la definizione dei singoli campi.
### **Sai come si devono mappare i parametri impliciti di una testata documento?**

E' sulla tabella V5A (modello documento), campo T$V5A4 che viene memorizzato l'elemento della tabella C£I (parametri impliciti) da utilizzare per la definizione dei parametri impliciti di testata.
### **Sai come si mappano i parametri implciti delle righe documento?**

E' sulla tabella V5B (Tipo riga documento), campo T$V5B$ che viene memorizzato l'elemento della tabella C£I (parametri impliciti) da utilizzare per la definizione dei parametri impliciti di riga.
### **Sai quali sono le regole per determinare il numeratore bolle di un documento?**

Il numeratore delle bolle di un documento viene definito nella tabella V5A (modello documento) campo T$T$V5AB ed è un elemnto presente nella tabella CRN sottosettore V5.
### **Sai quali sono le regole per determinare il numeratore fatture?**

Il numeratore fatture può essere un elemento della tabella CRNV5 associato al modello documento (tabella V5A) attraverso il campo T$V5AD Numeratore base fatture.

E' possibile tuttavia gestire una risalita o determinazione del numeratore fatture in modo personalizzato, attivando l'utilizzo di un programma specifico V5FA01S_x nella tabella V51, attraverso il campo T1V51A Num.Fat.Sp.
### **Sai quali sono i flussi tipici delle testate documento?**

Flussi standard : 
I-DO  Creazione
C-DO  Copia
F-DO  Pre Modifica
M-DO Post Modifica
P-DO  Pre Eliminazione
D-DO  Post Eliminazione
V-DO  Visualizza

Flussi tipici : 
K-DO  Collegamento
S-DO  Scollegamento
E-DO  Esecuzione
J-DO  2° collegamento (CoGe)
L-DO  2° scollegamento (CoGe)
O-DO  Riferim. origine post Delete
B-DO  Batch
T-DO  Transazione (DO)

### **Sai quali sono i flussi tipici delle righe documento?**

Flussi standard oggetto : 
I-DR Post Inserimento
C-DR Copia docuemnto
F-DR Pre modifica
M-DR Post modifica
P-DR Pre cancellazione
D-DR Post cancellazione
V-DR Visualizzazione

Flussi tipici oggetto : 
K-DR  Collegamento
S-DR  Scollegamento
E-DR  Esecuzione
J-DR  2° collegamento (CoGe)
L-DR  2° scollegamento (CoGe)
O-DR  Riferim. origine post Delete
B-DR  Batch
T-DR  Transazione (DO)
### **Sai come capire se una testata documento è di conto lavoro?**

Il Flag 10 di testata indica che il documento è di conto lavoro.
### **Sai come capire se una riga è di conto lavoro?**

Attraverso il flag 10 di riga è possibile stabilire se la stessa è di conto lavoro oppure di Kit
### **Sai quali sono le impostazioni base di un tipo riga di c/lavoro?**

### **Sai il significato e l'utilizzo del campo Modello ATP?**

