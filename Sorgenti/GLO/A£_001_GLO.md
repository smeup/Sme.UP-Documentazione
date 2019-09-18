- **UPP**

 :  : VOC Id="00001" Txt="UPP"
Chiamiamo UPP l'insieme di tutti gli oggetti che nell'ecosistema applicativo di Sme.UP sono utili alla soluzione di un tema applicativo. Come per le APP avremo un nome, una icona, ecc.
L'obiettivo all'interno del sistema Sme.UP è quello di favorire la collaborazione di più persone con competenze diverse per raggiungere un obiettivo applicativo che possa anche essere un oggetto commerciale.

- **Codice Univoco**

 :  : VOC Id="00002" Txt="Codice Univoco"
La codifica delle UPP ha una struttura ben precisa :  codiceapplicazione_codiceunivoco (es. A£_001, C5_002).
Il codice univoco è univoco per tutte le UPP al di là dell'applicazione (quindi non ci sarà mai l'UPP A£_002, se esiste già l'UPP C5_002).
Il codice univoco può essere composto da numeri e lettere senza significato particolare, se non la prima lettera impostata ad "X", questa identifica in modo preciso il fatto che si tratta di un UPP sviluppata per un cliente e non per essere distribuita a standard.
Il codice univoco può (deve) essere calcolato in modo automatico dall'interfaccia di inserimento di una nuova UPP (oggetto Sme.UP SU).

- **Oggetto SU**

 :  : VOC Id="00003" Txt="Oggetto SU"
L'oggetto SU è il codice oggetto Sme.UPP che identifica le UPP.

- **Enabler**

 :  : VOC Id="00004" Txt="Enabler"
Indica una funzionalità proprietaria dell'UPP che può essere nativamente sfruttata per la costruzione dell'UPP. Ciò che le accomuna è l'utilizzo del codice dell'UPP o del codice univoco dell'UPP nella codifica della funzione stessa (ad esempio la scheda base dell'UPP si chiama come l'UPP). Tutti gli enablers sono fruibili / gestibili dalla voce di menù "gestione enabler". Solo i responsabili posso gestire l'attivazione e la manutenzione di tali enabler.

- **Responsabile**

 :  : VOC Id="00005" Txt="Responsabile"
Identifica la persona a cui fa riferimento la responsabilità dell'UPP. Questa informazione è imputabile nella gestione dell'oggetto SU.

- **Collaboratori**

 :  : VOC Id="00006" Txt="Collaboratori"
Indica i collaboratori, con possibili, differenti gradi di responsabilità, cui il responsabile può fare affidamento. L'elenco è memorizzato all'interno dello script SCP_UPP che è fruibile dalla voce "Controllo Responsabili" o dagli Enabler.

- **Sketch**

 :  : VOC Id="00007" Txt="Sketch"
In ambito UPP corrisponde all'UPP A£_000. In essa sono stati implementati tutti gli enabler applicabili ad una UPP. Quando dalla voce del menù di sviluppo "Gestione Enabler" si attiva una voce, questa voce viene automaticamente proposta tramite copia dell'equivalente funzionalità dell'UPP di sketch.

- **Custom**

 :  : VOC Id="00008" Txt="Custom"
Si intende un UPP sviluppata per un cliente e non per lo standard.

- **Variabili di script KU**

 :  : VOC Id="00009" Txt="Variabili di script KU"
Le variabili dallo script delle proprietà (UPP.VAR) generano le variabili &KU.upp%codicevariabile, dove upp è il codice intero della UPP e codicevariabile è il codice attribuito alla variabile nello script SCP_UPP. la variabile dello script di configurazione della UPP A£_000, avente codice D01, può essere impiegata in tutti gli altri script tramite la codifica _&_KU.A£_000%D01.
Si ricorda che nei programmi queste variabili posso essere fruite tramite la chiamata con funzione/metodo vuoti, dell'API £K45.

- **Wiki**

 :  : VOC Id="00010" Txt="Wiki"
Sotto questo termine finiscono una serie di documenti scrivibili secondo le tecniche di linguaggio di markup.

- **Upp Store**

 :  : VOC Id="00011" Txt="Upp Store"
E' la vetrina delle UPP che hanno una valenza commerciale.

- **Scheda della UPP**

 :  : VOC Id="010"   Txt="Scheda della UPP"
Si intende la scheda intestataria della UPP. Il nome del membro ha il medesimo nome della UPP.
In essa si concentra l'operatività corrispondente alla funzionalità espressa dalla UPP.
Alla scheda intestataria se ne possono poi affiancare altre che prendono lo stesso codice ma con l'aggiunta di una desinenza (es. _01).

- **Documentazione Scheda**

 :  : VOC Id="020"   Txt="Documentazione Scheda"
Corrisponde al documento che descrive l'operatività utente di una particolare scheda.

- **Documentazione Applicativa**

 :  : VOC Id="030"   Txt="Documentazione Applicativa"
Corrisponde al documento che descrive nel dettaglio la struttura ed i passi di installazione dell'UPP.

- **Script Proprietà UPP**

 :  : VOC Id="040"   Txt="Script Proprietà UPP"
Corrisponde allo script che identifica l'UPP, lo script SCP_UPP tramite cui l'UPP viene ad esistere ed in cui vengono memorizzati i principali dati anagrafici della UPP.

- **Script Variabili UPP**

 :  : VOC Id="050"   Txt="Script Variabili UPP"
Per il funzionamento della UPP può risultare necessario settare una serie di parametri obbligatori (senza la loro indicazione l'UPP non può funzionare) o facoltativi (a seconda di cosa vi indico l'UPP, si comporta secondo alcune varianti alternative).
Nel caso in cui siano scelte da effettuare solo una tantum, tali parametri possono essere fissati in un apposito script di definizione. Si tratta di uno script contenuto in SCP_UPP ed avente codice :  codiceupp_var. Lo script fa parte degli Enabler della UPP.
Le variabili qui settate potranno essere poi fruibili tramite la £K45 nei programmi e tramite le variabili KU (si veda apposita voce di glossario).
Se invece le scelte da effettuare devono poter essere variabili di volta in volta dall'utente, si può utilizzare il configuratore.

- **Wiki Applicativa**

 :  : VOC Id="060"   Txt="Wiki Applicativa"
E' la documentazione tramite la quale viene descritto il funzionamento dell'UPP ed i passi necessari alla sua attivazione.

- **Valori Fissi**

 :  : VOC Id="070"   Txt="Valori Fissi"
E' lo script tramite il quale è possibile definire una serie di oggetti di tipo V4 ad uso specifico della UPP.

- **File Fisico**

 :  : VOC Id="080"   Txt="File Fisico"
E' un archivio creato per memorizzare dati secondo una struttura specifica necessaria al funzionamento dell'UPP.
La sua attivazione, attiva la voce del menù tecnico "Scheda del file codiceupp0F.

- **File Logico**

 :  : VOC Id="090"   Txt="File Logico"
E' una particolare vista logica applicata al file specifico fisico dell'UPP.

- **Programma Oav**

 :  : VOC Id="100"   Txt="Programma Oav"
E' un programma che permette di definire degli attributi per più di un oggetto, la cui presenza risulta necessaria solo nel caso in cui la UPP intestataria venga attivata. Ad eccezione del fatto che il programma gestisce più di un oggetto, la struttura è del tutto simile a quella di un normale programma di oav oggetto.
La gestione del programma, attiva nel menù tecnico dell'UPP, la voce "Controllo Costruzione OAV Specifici", tramite cui è possibile generare, controllare ed eventualmente riallineare la definizione di questi OAV.

- **Script Dati di Installazione**

 :  : VOC Id="110"   Txt="Script Dati di Installazione"
E' uno script che permette di definire un elenco di istanze da creare in fase di installazione della UPP. Questo enabler attiva la voce del menù tecnico "Dati di installazione", da cui è possibile lanciare il controllo e la creazione di questi dati.

- **Script Dati Dimostrativi**

 :  : VOC Id="120"   Txt="Script Dati Dimostrativi"
E' uno script che permette di definire un elenco di istanza da creare al solo fine di dimostrare il funzionamento dell'UPP. Sono dati meramente dimostrazioni che probabilmente dopo la dimostrazione è opportuno cancellare.
Questo enabler attiva la voce del menù tecnico "Dati demo", da cui è possibile lanciare il controllo e la creazione di questi dati.

- **Cartella**

 :  : VOC Id="130"   Txt="Cartella"
E' la cartella di documenti intestata all'UPP.

- **Cartella Azienda**

 :  : VOC Id="140"   Txt="Cartella Azienda"
E' una particolare sottocartella della cartella intestata all'UPP pensata per contenere dati o documenti specifici per l'UPP nel particolare contesto aziendale in cui viene utilizzata.

- **Wiki Sviluppo**

 :  : VOC Id="150"   Txt="Wiki Sviluppo"
E' la documentazione in cui vengono messe le note per il processo di sviluppo dell'UPP.

- **Scheda Prototipo**

 :  : VOC Id="160"   Txt="Scheda Prototipo"
E' una particolare scheda intestata all'UPP, che va utilizzata nella fase di sviluppo dell'UPP.
Questa scheda può essere utilizzata, sfruttando i prototipi, per descrivere l'operatività finale della scheda, prima che i servizi ed i dati necessari al suo utilizzo siano stati prodotti.
La scheda a senso che esista in maniera separata rispetto alla scheda intestataria al fine anche di poter effettuare un confronto, fra la scheda prototipale e la scheda reale.
La sua attivazione, attiva la voce del menù tecnico "Scheda Prototipo".

- **Script Prototipi**

 :  : VOC Id="170"   Txt="Script Prototipi"
E' un particolare script che permette di definire degli insiemi di dati prototipali. Tali dati possono essere originati in vari modi (da istruzioni di script, ma anche da fogli excel esterni).
Lo script di definizione si trova in SCP_SET ed ha codice uguale a codiceupp_PRO e permette di definire degli oggetti
La fruizione di tali dati può essere poi possibile attraverso chiamate al servizio B£SER_46.
Per vedere nel dettaglio un loro utilizzo si rimanda ai prototipi impiegati nella scheda dell'UPP di sketch.
La sua attivazione, attiva la voce del menù tecnico "Prototipi".

- **Cartella Prototipi**

 :  : VOC Id="180"   Txt="Cartella Prototipi"
E' una particolare sottocartella della cartella intestata all'UPP pensata per contenere i dati da impiegare nei prototipi.

- **Cartella Sviluppo**

 :  : VOC Id="190"   Txt="Cartella Sviluppo"
E' una particolare sottocartella della cartella intestata all'UPP pensata per contenere i dati o la documentazione a supporto del processo di sviluppo dell'UPP.

- **Nice To Have**

 :  : VOC Id="200"   Txt="Nice To Have"
Indica un elenco di domande che si possono porre al responsabile dell'UPP, su funzionalità che il richiedente desidera vedere implementate nell'UPP. Per abilitare tale funzionalità è necessario che il responsabile abiliti il relativo Enabler.

- **Forum**

 :  : VOC Id="210"   Txt="Forum"
Attiva la voce del menù tecnico per l'accesso al forum intestato all'UPP.
La sua attivazione, attiva la voce del menù tecnico "Forum".

- **Servizi**

 :  : VOC Id="220"   Txt="Servizi"
Programmi con struttura di servizio (atti a rispondere ad una "funzione" Sme.UP). Per convenzione viene attribuito il codice codiceupp_nn dove nn è numero progressivo di due cifre.

- **Configuratore**

 :  : VOC Id="230"   Txt="Configuratore"
Per il funzionamento della UPP può risultare necessario settare una serie di parametri obbligatori o facoltativi. Se tali scelte non vanno effettuate una tantum, ma devono poter essere risettabili ogni volta dall'utente, si possono utilizzare gli script di configurazione (SCP_CFG) impiegati nella struttura delle istruzioni G.SET.UCF/SUB.UCF e D.FUN.UCF.
Si veda inoltre la voce "Exit Controllo Configuratore" per l'implementazione di logiche più complesse rispetto a quelle dello script da implementare nell'interazione con l'utente.

- **Exit Controllo Configuratore**

 :  : VOC Id="240"   Txt="Exit Controllo Configuratore"
Si abbina all'utilizzo del configuratore. Permette di aggiungere delle logiche più articolate rispetto a quelle possibili tramite script. La sua attivazione va poi indicata anche nello script SCP_CFG tramite le istruzioni iniziali  :  : A08.

- **Documentazione Configuratore**

 :  : VOC Id="250"   Txt="Documentazione Configuratore"
E' la documentazione in cui viene descritto il significato dei campi utilizzati nel configuratore.

- **Script Menù**

 :  : VOC Id="260"   Txt="Script Menù"
E' lo script che permette di definire un elenco di azioni, da impiegare poi nelle schede dell'UPP tramite il costruttore LOA12.

- **Programmi**

 :  : VOC Id="270"   Txt="Programmi"
Si differenziano per i servizi perchè a differenza di quest'ultimi che hanno una funzionalità specifica (rispondere ad una 'funzione Sme.UP') i programmi possono essere impiegati in tutti i modi per cui risulta necessario il loro utilizzo.
Per convenzione viene attribuito il codice codiceupp_An dove n è numero progressivo di una cifra.

- **Script Setup Standard**

 :  : VOC Id="280"   Txt="Script Setup Standard"
E' un script la cui struttura è di libera definizione ed è prettamente contestuale all'impiego che se ne vuole fare nella UPP specifica. In sostanza ci si possono strutturare tutte quelle informazioni atte a far funzionare l'UPP, per le quali uno script può risultare idonee.
Per una maggior comprensione si legga anche la voce "Wizard Script Setup Specifico".
Nello script standard stanno quelle impostazioni che verranno distribuite a tutti i clienti.
L'utilizzo degli script non è automatico, i servizi/programmi della UPP dovranno impiegarli poi modo che risulterà utile.

- **Script Setup Utente**

 :  : VOC Id="290"   Txt="Script Setup Utente"
E' un script la cui struttura è di libera definizione ed è prettamente contestuale all'impiego che se ne vuole fare nella UPP specifica. In sostanza ci si possono strutturare tutte quelle informazioni atte a far funzionare l'UPP, per le quali uno script può risultare idonee.
Nello script standard stanno quelle impostazioni che verranno impiegate dal particolare cliente.
L'utilizzo degli script non è automatico, i servizi/programmi della UPP dovranno impiegarli poi modo che risulterà utile.

- **Wizard Script Setup Specifico**

 :  : VOC Id="300"   Txt="Wizard Script Setup Specifico"
In questo script vengono definite le istruzioni che potranno essere utilizzare nello script di setup (standard ed utente). In sostanza è qui che per questi script di setup viene definito che cosa posso descrivere.

- **Documentazione Wizard Script Setup Specifico**

 :  : VOC Id="310"   Txt="Documentazione Wizard Script Setup Specifico"
E' il documento che permette di descrivere il significato delle istruzioni e degli attributi del wizard dello script di setup specifico.

- **Script Oggetti Aggiuntivi**

 :  : VOC Id="320"   Txt="Script Oggetti Aggiuntivi"
In questo script vengono definite le istruzioni che potranno essere utilizzare nello script di setup (standard ed utente). In sostanza è qui che per questi script di setup viene definito che cosa posso descrivere.

- **Script Distribuzione**

 :  : VOC Id="330"   Txt="Script Distribuzione"
In questo script è possibile descrivere l'elenco dei sorgenti e le istruzioni di installazione per permettere la distribuzione e l'aggiornamento dell'UPP su altri sistemi.
L'attivazione dei questo enabler comporta la compilazione automatica dello script con tutti i sorgenti associati all'UPP (sia che siano enabler sia che siano indicati nello script degli oggetti aggiuntivi). Una volta creato sarà sempre possibile intervenire poi a mano nello script per aggiungere altre indicazioni.
La sua attivazione, attiva la voce del menù tecnico "script di distribuzione".

- **Script Workflow**

 :  : VOC Id="340"   Txt="Script Workflow"
E' lo script che permette di attivare la descrizione di processi di workflow, da impiegare nell'uso dell'UPP.

- **Messaggi e voci**

 :  : VOC Id="350"   Txt="Messaggi e voci"
E' lo script che permette di definire delle voci da utilizzare nel modo che può risultare più utile. In presenza dello script di menù, se in questo script vengono descritte delle voci con codice uguale a quello della voce di menù, è possibile descrivere la voce di menù.

- **Scheda Cruscotto**

 :  : VOC Id="360"   Txt="Scheda Cruscotto"
E' una particolare scheda intestata all'UPP, che può essere utilizzata per dare una panoramica sintetica dei dati dell'UPP.
Se presente è la scheda che viene presentata per prima, nella scheda del menù tecnico.

- **Scheda Esempi**

 :  : VOC Id="370"   Txt="Scheda Esempi"
E' una particolare scheda intestata all'UPP, che può essere utilizzata per evidenziare delle applicazioni esemplificative dell'UPP.
La sua attivazione, attiva la voce del menù tecnico "Scheda Esempi".

- **Scheda di Test**

 :  : VOC Id="380"   Txt="Scheda di Test"
E' una particolare scheda intestata all'UPP, che può essere utilizzata per gestire l'esecuzione di funzioni di test della funzionalità dell'UPP.
La sua attivazione, attiva la voce del menù tecnico "Scheda di Test".

- **Layout**

 :  : VOC Id="390"   Txt="Layout"
Sono script di tipo SCP_LAY intestati all'UPP, che ad esigenza possono essere impiegati in BOX o input panel richiamati nelle schede dell'UPP.

- **Report come Pdf**

 :  : VOC Id="400"   Txt="Report come Pdf"
Sono script di tipo SCP_G53 intestati all'UPP, che ad esigenza possono essere impiegati nella produzione di particolari report di stampa strutturati.

- **Analisi tabellare**

 :  : VOC Id="410"   Txt="Analisi tabellare"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A03.

- **Matrice due oggetti**

 :  : VOC Id="420"   Txt="Matrice due oggetti"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A06.

- **Raccoglitore di funzioni**

 :  : VOC Id="430"   Txt="Raccoglitore di funzioni"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A07.

- **Flussi**

 :  : VOC Id="440"   Txt="Flussi"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A11.

- **Reportistica**

 :  : VOC Id="450"   Txt="Reportistica"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A15.

- **Albero dinamico**

 :  : VOC Id="460"   Txt="Albero dinamico"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A16.

- **Gestione Mail**

 :  : VOC Id="470"   Txt="Gestione Mail"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A17.

- **Sql preparati**

 :  : VOC Id="480"   Txt="Sql preparati"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A25.

- **Gestione batch**

 :  : VOC Id="490"   Txt="Gestione batch"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A27.

- **Mappe**

 :  : VOC Id="500"   Txt="Mappe"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A29.

- **Dati di campo**

 :  : VOC Id="510"   Txt="Dati di campo"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A37.

- **Integrazione con webservice**

 :  : VOC Id="520"   Txt="Integrazione con webservice"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A38.

- **Funzioni pubbliche**

 :  : VOC Id="530"   Txt="Funzioni pubbliche"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A39.

- **Dashboard**

 :  : VOC Id="540"   Txt="Dashboard"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A41.

- **Notifiche**

 :  : VOC Id="550"   Txt="Notifiche"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A60.

- **Navigazione**

 :  : VOC Id="560"   Txt="Navigazione"
Sono script SCP_SET che possono essere impiegati per l'utilizzo del costruttore A66.

- **Wiki Operativa**

 :  : VOC Id="570"   Txt="Wiki Operativa"
E' una documentazione atta a descrivere il funzionamento dell'UPP.
Una volta attivata la wiki sarà disponibile alla voce "Imparare" dell'UPP.

- **Tutorial**

 :  : VOC Id="580"   Txt="Tutorial"
E' uno script che mi permette di definire un elenco di esercizi da svolgere a scopo formativo.
Una volta attivato il video sarà disponibile alla voce "Imparare" dell'UPP.

- **Video**

 :  : VOC Id="590"   Txt="Video"
E' uno script che mi permette di accedere ad un video formativo relativo al funzionamento dell'UPP.
Una volta attivato il video sarà disponibile alla voce "Imparare" dell'UPP.

- **Corsi**

 :  : VOC Id="600"   Txt="Corsi"
E' uno script che mi permette di descrivere i passi da seguire per tenere un corso atto a formare sul funzionamento della UPP.
Una volta attivato il contenuto dello script sarà disponibile alla voce "Imparare" dell'UPP.

- **Skill**

 :  : VOC Id="610"   Txt="Skill"
E' uno script che mi permette di descrivere un percorso formativo con autovalutazione.
Una volta attivato il contenuto dello script sarà disponibile alla voce "Imparare" dell'UPP.

- **F.A.Q.**

 :  : VOC Id="620"   Txt="F.A.Q."
E' uno script che mi permette di definire un elenco di domande, con relativa risposta, volte a dare un'indicazione rispetto alle domande più frequenti.
Una volta attivato le faq saranno disponibili alla voce "Imparare" dell'UPP.

- **Glossario**

 :  : VOC Id="630"   Txt="Glossario"
E' uno script che mi permette di definire l'elenco dei termini specifici impiegati nell'UPP.
Una volta attivato i termini saranno disponibili alla voce "Imparare" dell'UPP.

- **Cartella documentazione**

 :  : VOC Id="640"   Txt="Cartella documentazione"
E' una particolare sottocartella della cartella intestata all'UPP pensata per contenere dati o documenti specifici atti ad integrare la comprensione dell'UPP.

- **Figure Documentazione**

 :  : VOC Id="650"   Txt="Figure Documentazione"
E' un particolare script che permette di definire le figure da impiegare nei vari script di documentazione.

