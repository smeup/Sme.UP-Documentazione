- **I componenti (Provvisorio per forzare l'utilizzo delle F.A.Q.)**

 :  : VOC Id="10001" Txt="I componenti (Provvisorio per forzare l'utilizzo delle F.A.Q.)"

- **Perché c'è la forma START e cosa significa?**

 :  : VOC Id="10002" Txt="Perché c'è la forma START e cosa significa?"

 Il comando "START" portava ad una modalità di ingresso agli oggetti di Sme.UP
 Sono rappresentati solo i concetti. La forma dovrebbe essere adeguata da nuove possibilità grafiche
 In particolare si vuole far emergere concetti generali del tipo seguente : 
 \* Io entro a vedere le cose che "preferisco". Adesso ci sono tanti TAB (Io, il mio gruppo, ecc) ma questi TAB dovrebbero diventare una icona che mi consente di dire quale iniseme (LISTA) voglio vedere. Ad esempio sui componenti (ma il concetto è generale) vedo solo quelli cu cui voglio valorare.
 \* All'interno ci sono N forme di scelta (Albero, riga di scelta, immagini). Anche qui mi dovrebbe apparire la forma che preferisco e la forma dipende da due cose : 
 \*\* Le caratteristiche della classe
 \*\* Le mie preferenze (Questo è il concetto FONDAMENTALE che chiamiamo (MDV). Potete guardare il video del componente "Activity Timeline" di Saleforce per vedere un esempio (ma ne è pieno l'WEB) di come io fisso in una sezione le mie preferenze di elaborazione
 \* Dato un componente (ma START lavora su qualsiasi oggetto) vengono presentate altre possibilità ma l'intenzione è quella di far emergere i concetti. Ne cisto solo due (per brevità)
 \*\* Descrizioni. Vengono estratte tutte le parole utilizzate per descrivere gli elementi della classe (In questo caso componenti) al fine di scrivere in modo normalizzato, riutilizzando le parole, eliminando le abbreviazioni. Ciò per tanti ovvi motivi (esempio traduzioni)
 \*\* Valutazioni. E' IMPORTANTISSIMO arrivare ad una dichiarazione di "chi sa cosa". Io dichiaro di conoscere ad un livello la matrice (quindi ad esempio parteciperò agli eventi formativi di quel livello).

- **Cosa significano gli attributi della matrice dei componenti?**

 :  : VOC Id="10003" Txt="Cosa significano gli attributi della matrice dei componenti?"
 Sono già state tolte da Giovanni alcune colonne.
 Questa matrice giaceva (pressoché inutilizzata) da circa 15 anni.
 E' importante comprendere che dobbiamo guardare ad una classe (insieme di istanze) da due prospettive che chiamo "Singolare" e "Plurale". In una filtro scelgo, nell'altra gestisco. Poi devo poter passare sempre da una a tutti e viceversa.
 Possiamo migliorare a piacere questa tabella di informazioni
 Queste informazioni non devono essere portate nella documentazione.
 La cosa giusta sarebbe avere la documentazione di scheda che descrive il significato delle colonne

 Se fossimo bravi dovremmo trattare la colonna device associati come una lista di oggetti che consentirebbero decodifiche ecc.

 Le proprietà (compresa la classe ABC) sono sotto la responsabilità dell'owner del componente stesso

- **Cosa sono i **

 :  : VOC Id="10004" Txt="Cosa sono i "Setup associati""
 Parliamo al plurale ma nel nostro caso abbiamo un solo setup. Si tratta dell'insieme delle proprietà del componente che consentono all'utente (in fase di sviluppo o di uso) di definire le preferenze
 Ogni proprietà deve essere documentata (se non è ovvia)
 In aggiunta abbiamo deciso di permettere di associare una o più di queste proprietà agli esempi.
 In tal modo io potrò vedere l'esempio che spiega come si comporta una proprietà. La proprietà è un campo di un configuratore. Il risultato è concettualmente la configurazione ovvero la risposta ad un questionario

- **Perché alcune scelte grafiche?**

 :  : VOC Id="10005" Txt="Perché alcune scelte grafiche?"
 Ribadito che ieri avevate alcuni comportamenti per mancato rilascio, voglio precisare che quella che si presenta NON E' ASSOLUTAMENTE il risultato desiderato.
 Su questo conto sul vostro contributo e nell'WEB il risultato dovrebbe essere molto migliore.
 Qui mi premono due cose fondamentali : 
 1. I concetti (Descrizioni normalizzate, preferenze, singolare/plurale, MDV, FAQ e documentazione di una parola, esempi utilizzabili, ecc.)
 2. Il completamento dei dati dei componenti (il più velocemente possibile) al fine di forzare l'accesso, la contribuzione ecc. dei vostri colleghi. Questo è l'unico modo per far apprezzare il vostro lavoro e per ridurre i disturbi. A quel punto abbiamo contributi (Test, documentazione, formazione)

- **Dove sono scritti i responsabili di un componente?**

 :  : VOC Id="10006" Txt="Dove sono scritti i responsabili di un componente?"
 Il concetto di responsabilità è molto importante. Mediante il tasto F1 arrivo agli oggetti che stanno sotto il mio contesto. Da qui scegliendo ? alla spiegazione di un oggetto qualsiasi e da qui alle responsabilità. Su tale scheda (Che deve molto completarsi) devo arrivare a tutto quanto riguarda la responsabilità.
 Il responsabile è un normale OAV di qualsiasi istanza quindi posso aggiungerlo come colonna aggiuntiva ovunque (OAV Generali!)

- **Al click su un componente, perché non passo alla scheda?**

 :  : VOC Id="10007" Txt="Al click su un componente, perché non passo alla scheda?"
 Qui io passo in pratica al "cruscotto" del componente, ossia ad una sua funzione.
 Da qualsiasi funzione su un oggetto potrei/dovrei risalire alle funzioni (Sempre singolare (una funzione) plurale (menù))
 Esattamente come da una istanza dovrei passare a istanze

- **Non comprendo alcuni termini?**

 :  : VOC Id="10008" Txt="Non comprendo alcuni termini?"
 La costruzione di un "vocabolario" comune è uno degli obiettivi.
 Ditemi tutte le parole che non si capiscono e le poniamo nel glossario. Ogni parola è un oggetto che mi consente di passare alla sua "scheda". In WEB questa cosa potrebbe essere fantastica
 Tutto il tema dei "GLOSSARI" è da approfondire.

 Come si caratterizzano gli esempi?
 \* Tutti gli esempi dovranno essere sezioni della scheda CMP_xxx in SCP_SCHESE
 \* La proprietà "SubNote" della sezione conterrà le seguenti proprietà
 \*\* Dev() = Device supportati (W, C, ecc.)
 \*\* Liv() = Livello 0,2,8
 \*\* Tag() = Tag associati
 \*\* Doc() Documento specifico (Capitolo della documentazione specifico per questa funzionalità)
 \*\* Fld() = Campo specifico della documentazione
 In tal modo io potrò accedere agli esempi a partire dalla proprietà. Ad esempio tutti quelli attivi e validi per il device che sto utilizzando oppure tutti quelli di questa funzionalità ecc.

- **Sai quali sono i requisiti software minimi per l'installazione di Looc.Up**

 :  : VOC Id="SKIAB0010" Txt="Sai quali sono i requisiti software minimi per l'installazione di Looc.Up su un PC?" Als="comm"
Per l'installazione di Looc.Up su un PC sono necessari i seguenti requisiti software : 

1) Un sistema operativo Windows in versione XP o superiore
2) Una Java Virtual Machine (JVM) a 32 bit in versione 1.6 o successive.

Sulle machine a 64 bit è comunque richiesta l'installazione di una JVM a 32 bit.
- **Sai se Looc.Up è eseguibile su PC con sistema operativo a 64 bit?**

 :  : VOC Id="SKIAB0020" Txt="Sai se Looc.Up è eseguibile su PC con sistema operativo a 64 bit?" Als="comm"
Looc.Up è un prodotto sviluppato nei linguaggi Java e Delphi con tecnologia a 32 bit. Sui sistemi Windows a 64 bit viene normalmente installata la versione a 64 bit della Java Virtual Machine, che però non è compatibile con il client Looc.Up. Quindi, per il corretto funzionamento di Looc.Up su macchina a 64 bit è necessario installare manualmente una versione a 32 bit della JVM, che può essere affiancata liberamente alla versione a 64 bit già presente.
- **Sai verificare se un PC è compatibile con l'esecuzione di Looc.Up?**

 :  : VOC Id="SKIAB0030" Txt="Sai verificare se un PC è compatibile con l'esecuzione di Looc.Up?" Als="comm"
A partire dalla versione V3R2M120301, nel pacchetto Looc.Up è contenuto un tool per il controllo della compatibilità di un PC con l'esecuzione di Looc.Up. Il tool è costituito dall'eseguibile "LoocupNetTester.exe", collocato nella directory di installazione di Looc.Up ed avviabile direttamente (con un doppio click sul file eseguibile) o indirettamente da console di connessione.

Il tool esegue una serie di controlli sul PC in esame : 

1) Fornisce un riepilogo delle risorse del sistema
2) Esegue una serie di misure sulle prestazioni
3) Controlla i prerequisiti necessari al funzionamento di Looc.Up

In caso di problemi viene mostrato un report contenente alcuni suggerimenti per la risoluzione del problema.
- **Conosci le possibili modalità di installazione di Looc.Up?**

 :  : VOC Id="SKIAB0040" Txt="Conosci le possibili modalità di installazione di Looc.Up?" Als="comm"
Looc.Up può essere installato in tre diverse modalità : 

1) Come client, installato su tutti i PC su cui è necessario
2) Come server condiviso, con Looc.Up installato su una cartella del server condivisa da tutti i PC della rete.
3) Come client sincronizzato :  Looc.Up è installato sui singoli PC ma ogni volta che parte si sincronizza automaticamente con una copia di riferimento presente su una cartella del server. La sincronizzazione è garantita dal plugin RSync.
- **Conosci i requisiti richiesti sul server per una installazione Looc.Up co**

 :  : VOC Id="SKIAB0050" Txt="Conosci i requisiti richiesti sul server per una installazione Looc.Up condivisa?" Als="comm"
Nell'installazione di tipo condivisa sul server, Looc.Up viene installato su una cartella del server visibile da tutti i PC della rete. Però una volta avviato gira (e consuma risorse) sul PC locale.
Per questo motivo sul server non è richiesto alcun prerequisito software; in particolare non è richiesta l'installazione sul server della Java Virtual Machine, visto che in questa configurazione Looc.Up non girerà mai sul server.
E' però necessario che la cartella sul server che contiene Looc.Up sia condivisa ed accessibile sia in lettura che in scrittura da tutti i PC su cui si vorrà usare Looc.Up.
- **Sai come si avvia Looc.Up?**

 :  : VOC Id="SKIAB0060" Txt="Sai come si avvia Looc.Up?"
Per l'avvio di Looc.Up è necessario selezionare uno dei tre eseguibili di avvio forniti con l'installazione : 

1) Loocup_w.exe, per l'avvio di Looc.Up da linea di comando senza finestra di console
2) Loocup.exe, per l'avvio di Looc.Up da linea di comando con visualizzazione della finestra di console (utile per il debug)
3) Loocup_con.exe (disponibile dalla versione V3R2M120301), per l'avvio di Looc.Up attraverso ilmodulo di gestione delle connessioni

Nel caso Looc.Up venga installato in locale sul PC, vengono creati sul desktop i link a questi eseguibili. Viene inoltre creata la voce specifica nel menù di Windows.
- **Sai avviare Looc.Up passando a linea di comando i parametri di connession**

 :  : VOC Id="SKIAB0070" Txt="Sai avviare Looc.Up passando a linea di comando i parametri di connessione?"
Il formato di avvio a linea di comando di Looc.Up è il seguente : 

Loocup.exe SYSTEM USER PASSWORD ENVIRONMENT \*

dove : 

SYSTEM :  indirizzo del sistema AS400 da collegare
USER :  utente di connessione
PASSWORD :  password
ENVIRONMENT :  ambiente Sme.Up
--parms :  parametri opzionali

E' possibile lasciare uno dei campi obbligatori vuoto indicando \*NONE. Il campo verrà richiesto alla partenza.
- **Sai cos'è il modulo connessioni di Looc.Up?**

 :  : VOC Id="SKIAB0080" Txt="Sai cos'è il modulo connessioni di Looc.Up?"
A partire dalla versione V3R2M120301 di Looc.Up è disponibile una nuova modalità di avvio che prevede la visualizzazione di un modulo di gestione delle connessioni alla partenza del client grafico. Attraverso questo modulo, l'utente può definire le connessioni di cui ha bisogno, organizzarle in gruppi ed associare icone specifiche.
Viene quindi semplificata la gestione di connessioni multiple, soprattutto nel caso l'utente debba usare Looc.Up su sistemi AS400 multipli o su ambienti gestionali diversi.
- **Sai come si avvia il modulo connessioni di Looc.Up?**

 :  : VOC Id="SKIAB0090" Txt="Sai come si avvia il modulo connessioni di Looc.Up?"
Per avviare Looc.Up in modo che visualizzi alla partenza il modulo di selezione delle connessioni è sufficiente invocare l'eseguibile "Loocup_con.exe" presente nella cartella di installazione oppure selezionare le voci specifiche create sul desktop o nel menù di Windows dall'installatore (solo nel caso Looc.Up sia installato direttamente sul PC).
- **Sai come si creano le connessioni del modulo connessione al primo avvio d**

 :  : VOC Id="SKIAB0100" Txt="Sai come si creano le connessioni del modulo connessione al primo avvio di Looc.Up?"
Al primo avvio di Looc.Up, il modulo connessioni non contiene alcuna connessione. Per poterle creare è necessario accedere a Looc.Up con un utente noto e andare nella scheda di gestione delle connessioni per creare le connessioni necessarie al proprio lavoro.
L'avvio di Looc.Up è possibile selezionando nel modulo connessioni il bottone "Avvia SME.Up" presente in basso a sinistra e immettendo le credenziali di un utente valido.
- **Come si accede alla scheda di gestione delle connessioni?**

 :  : VOC Id="SKIAB0110" Txt="Come si accede alla scheda di gestione delle connessioni?"
Le connessioni sono gestite da una scheda apposita che può essere invocata nei seguenti modi : 


1) Dal menù "My Loocup" selezionando la voce "Gestire il sistema". Nella scheda che si apre cercare la voce "Gestione connessioni" nella sezione "Configurazione generale"

2) Dal menù dell'applicazione "LO", selezionando il modulo "LOBASE"

3) Aprendo direttamente la scheda LOBASE_05 di gestione
- **Sai quali sono i prerequisiti di sistema per l'esecuzione di funzioni BAT**

 :  : VOC Id="SKIAB0120" Txt="Sai quali sono i prerequisiti di sistema per l'esecuzione di funzioni BATCH?"
Perchè in Looc.Up sia possibile eseguire funzioni di tipo batch, è necessario che nella rete sia presente un Looc.Up server. Le richieste di funzione da eseguire in batch saranno inviate al server ed eseguite su di esso.
- **Sai quali sono le funzioni che possono essere eseguite in modalità BATCH?**

 :  : VOC Id="SKIAB0130" Txt="Sai quali sono le funzioni che possono essere eseguite in modalità BATCH?"
Come su AS400, anche in Looc.Up le funzioni che possono essere eseguite in modalità batch sono tutte le funzioni F che non richiedono interazione con l'utente. Non possono quindi essere richieste funzioni che visualizzano finestre o messaggi, che chiedono un input dati o qualsiasi altra forma di interazione con l'utente. Un esempio tipico di funzioni immesse eseguite in modalità batch sono i flussi non presidiati.
- **Sai come si richiede l'esecuzione in modalità batch di una funzione?**

 :  : VOC Id="SKIAB0140" Txt="Sai come si richiede l'esecuzione in modalità batch di una funzione?"
All'interno di Looc.Up una funzione può essere eseguita in modalità batch specificando la notazione SERVER(BATCH) all'interno della funzione stessa. Ad esempio, data una funzione generica F(XX;YY;ZZ), l'esecuzione in modalità batch si ottiene modificando la richiesta in questo modo :  F(XX;YY;ZZ) SERVER(BATCH).

Si ricorda che le funzioni batch non sono eseguite sul client stesso ma delegate ad un server Looc.Up presente sulla rete. Se il server non esiste la funzione viene sempre eseguita in modalità interattiva.
- **Sai come si capisce se in una rete esiste un server Looc.Up attivo?**

 :  : VOC Id="SKIAB0150" Txt="Sai come si capisce se in una rete esiste un server Looc.Up attivo?"
E' sufficiente eseguire all'interno di un qualsiasi Looc.Up una ricerca di oggetti di tipo V3-LSE (Looc.Up server). La lista visualizzata mostra i server configurati ed attivi presenti sulla rete a cui è connesso il sistema AS400 di riferimento.
- **Sai cosa sono i Serventi di Looc.Up?**

 :  : VOC Id="SKIAB0160" Txt="Sai cosa sono i Serventi di Looc.Up?"
I Serventi di Looc.Up sono dei moduli di interfaccia che consentono a Looc.Up di accedere a fornitori di servizi alternativi al sistema AS400. Quando in Looc.Up di esegue una funzione F(XX;YY;ZZ), la richiesta di servizio è sempre inviata per default al sistema AS400 di riferimento. Specificando il servente (attraverso il campo SERVER della funzione) è invece possibile reindirizzare la richiesta dal sistema AS400 ad un sistema alternativo.

Ad esempio, la richiesta di funzione F(XX;YY;ZZ) SERVER(KK) indica che la richiesta di servizio verrà richiesta al servente identificato dal codice KK e non al sistema AS400.

I serventi sono registrati in fase di avvio di Looc.Up e sono identificati come oggetti :  V3-CSE

- **Sai cos'è un server Looc.Up?**

 :  : VOC Id="SKIAB0170" Txt="Sai cos'è un server Looc.Up?"
Il Looc.Up Server è una macchina attiva sulla rete su cui è in esecuzione una o più istanze di Looc.Up avviate in modalità server.

Rispetto ad una normale istanza di Looc.Up, un Looc.Up Server ha alcune funzionalità aggiuntive : 

1) Funzione server :  il Looc.Up server è in grado di registrare tutti i client Looc.Up attivi sulla rete ed aprire un canale di comunicazione diretto con loro. Attraverso questo canale il Looc.Up Server può controllare tutti i client Looc.Up attivi sulla rete e gestirli in maniera diretta. Ad esempio, può inviare messaggi, spegnere o riavviare un client, inviare una richiesta FUN ecc ecc
2) Comunicazione con AS400 :  il Looc.Up Server ha una comunicazione bidirezionale con l'AS400. Nel senso che può chiedere servizi al sistema AS400 (come un normale client Looc.Up) ma può anche eseguire servizi richiesti da AS400 (cosa che normalmente un client Looc.Up non può fare)
3) Funzioni batch :  il Looc.Up server è in grado di eseguire funzioni F in modalità batch.
- **In un sistema Looc.Up client-server, sai a cosa serve il campo CLIENT del**

 :  : VOC Id="SKIAB0180" Txt="In un sistema Looc.Up client-server, sai a cosa serve il campo CLIENT della FUN?"
In un sistema Looc.Up client-server, il campo CLIENT della FUN permette di identificare il client Looc.Up su cui verrà eseguita fisicamente la funzione.

E' quindi possibile richiedere su un client A una funzione che verrà fisicamente eseguita su un client B. Unica condizione necessaria è che nella rete ci sia un Looc.Up server attivo e che i due Looc.Up client identificati dai codici A e B siano entrambi connessi al server.




- **Sai come si avvia un Looc.Up perchè si connetta come client ad un Looc.Up**

 :  : VOC Id="SKIAB0190" Txt="Sai come si avvia un Looc.Up perchè si connetta come client ad un Looc.Up server presente in rete?"
Per fare in modo che un Looc.Up sia avvii come client collegato a un server presente nella rete è sufficiente inserire in fase di avvio tutti i parametri aggiuntivi necessari a definire il collegamento.

Looc.Up può essere avviato in modalità client inserendo nella linea di comando la notazione : 

--client : IP_SERVER : PORTA : CODCLI 

dove : 

1) --client :  è la notazione che indica a Looc.Up di avviarsi nella modalità client
2) IP_SERVER :  è l'indirizzo IP (o il nome mnemorico) del Looc.Up Server a cui collegarsi
3) PORTA :  è la porta socket usata per il collegamento. Se non specificata vale 9999.
4) CODCLI :  è il nome univoco con cui il server identificherà questa istanza del client nella rete. Se non specificato viene assegnato dal server al momento del collegamento

Oltre alla modalità a linea di comando è possibile specificare questi parametri anche nel file di inizializzazione di Looc.Up (SCP_CLO). In questo caso nella linea comando è sufficiente inserire solo la notazione aggiuntiva --client.

Esempio di avvio Looc.Up in modalità client : 

Loocup.exe SISTEMA UTENTE PASSWORD AMBIENTE --client : 172.16.2.213 : 9990 : TSTCLI 
- **Sai come si avvia un Looc.Up in modalità server?**

 :  : VOC Id="SKIAB0200" Txt="Sai come si avvia un Looc.Up in modalità server?"
Looc.Up può essere avviato in modalità server inserendo nella linea di comando la notazione : 

--server : CODSRV : PORT

dove : 

1) --server :  è la notazione che indica a Looc.Up di avviarsi nella modalità server
2) CODSRV :  è il codice identificativo univoco che identificherà il server sulla rete
3) PORT :  è la porta socket usata dai client per il collegamento a questo server. Se non specificata vale 9999.

Regole : 

1) Nella rete non ci possono essere contemporaneamente attivi due server con lo stesso identificativo
2) Su un singolo PC non ci possono essere contemporanemente attivi due server sulla stessa porta
- **Sai come può un Looc.Up client richiedere che una funzione sia eseguita d**

 :  : VOC Id="SKIAB0210" Txt="Sai come può un Looc.Up client richiedere che una funzione sia eseguita dal server a cui è connesso?"
E' sufficiente specificare il campo CLIENT(\*SERVER) all'interno della FUN.

La notazione \*SERVER va intesa come "server a cui il client è collegato" quindi F()... CLIENT(\*SERVER) va inteso come "esegui la funzione F() sul server a cui sono collegato".
- **Sai come può un normale Looc.Up richiedere una funzione ad un server a cu**

 :  : VOC Id="SKIAB0220" Txt="Sai come può un normale Looc.Up richiedere una funzione ad un server a cui non è connesso?"
Un Looc.Up avviato in modo normale (e quindi non connesso a nessun server) può richiedere che una funzione venga eseguita da un server Looc.Up anche se non connesso al server stesso.
Per ottenere questo risultato è sufficiente la notazione : 

F() CLIENT(\*SERVER.CODSRV)

che va letta come "cerca nelle rete il server identificato dal codice CODSRV e chiedigli di eseguire la funzione F()"

Sono possibili anche notazioni più complesse : 

F() CLIENT(\*SERVER.CODSRV.A)

che va letta come "cerca nella rete il server CODSRV e chiedi al client A collegato a questo server di eseguire la funzione F()"


- **Sai come fa l'AS400 a richiedere una F() a un Looc.Up server o a un clien**

 :  : VOC Id="SKIAB0230" Txt="Sai come fa l'AS400 a richiedere una F() a un Looc.Up server o a un client ad esso collegato?"
Alla partenza di Looc.Up server vengono create su AS400 due code specifiche chiamate : 

1) ESTC+CODSRV :  per la comunicazione AS400 --> Looc.Up Server (coda semplice)
2) ECTS+CODSRV :  per la comunicazione Looc.Up Server --> AS400 (coda keyed)

dove CODSRV è il codice asseganto al server Looc.Up in fase di partenza.

Il processo di richiesta è il seguente : 

1) Il sistema AS400 scrive la F() da eseguire sulla coda ESTC, specificando un codice richiesta K1
2) Il Looc.Up Server riceve la richiesta, la esegue e scrive la risposta nella coda ECTS con chiave K1
3) L'AS400 (che nel frattempo si era messo in attesa sulla coda K1 di risposta) riceve la risposta

L'utilizzo di una coda di risposta a chiave consente di parallelizzare le richieste.
