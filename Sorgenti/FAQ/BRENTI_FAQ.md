- \*\*Sai quali sono i file principali che intervengono nella gestione enti?\*\*

 :  : VOC Id="SKIE0010" Txt="Sai quali sono i file principali che intervengono nella gestione enti?"
File BRENTI0F per memorizzare i dati principali degli enti.
File BRESCO0F per la memorizzazione delle estensioni ai dati anagrafici.
- \*\*Sai quali enti vengono memorizzati sul file BRENTI0F e come si distinguono\*\*

 :  : VOC Id="SKIE0030" Txt="Sai quali enti vengono memorizzati sul file BRENTI0F e come si distinguono?"
Il file BRENTI0F è il file dove vengono memorizzate tutte le anagrafiche necessarie al gestionale SME.up, quindi è funzionale per tutti i moduli. Gli enti si differenziano per il TIPO ENTE, le cui caratteristiche sono definite dalla tabella BRE Tipo ente.

Troviamo quindi iscritte nel file BRENTI0F le informazioni dei fornitori, dei clienti, ma anche i dati dell'azienda o di altre tipologie di enti necessarie per l'attività aziendale.
- \*\*Sai quali sono le tabelle principali che è necessario impostare per la ges\*\*

 :  : VOC Id="SKIE0020" Txt="Sai quali sono le tabelle principali che è necessario impostare per la gestione enti?"
BR2  :  Impostazioni Base Contatti
Questa tabella è la base per poter impostare e gestire le anagrafiche enti secondo le esigenze specifiche.
BRE :  definisce i tipi contatti gestiti e le caratteristiche di tali tipi contatti. Attraverso questa tabella è possibile anche condizionare il comportamento della visualizzazione e dei controlli specifici sulla gestione enti (attraverso vari programmi di exit)
BRX :  definisce il rapporto fiscale del soggetto ed i controlli ad esso correlati
BRZ :  Categoria Enti che identifica delle caratteristiche specifiche delle anagrafiche (Categoria parametri impliciti ed espliciti, domande a cui eventualmente rispondere per la costruzione
automatica del codice), campi assunti in modo predefinito (livello-stato, gruppo flag, rapporto fiscale, codice nazione, assoggettamento IVA, Listino) ed anche l'esecuzione di programmi specifici per il controllo dei campi.
BRI Estensioni
BRG Scenari contatti
- \*\*Sai cos'è il Nominativo e se è obbligatorio?\*\*

 :  : VOC Id="SKIE0040" Txt="Sai cos'è il Nominativo e se è obbligatorio?"
La gestione del Nominativo è facoltativa ed attivabile attraverso le tabelle BR2 (tipo nominativo) e BRE (Gestione nominativo).
Se è attiva la gestione del nominativo è possibile storicizzare le informazioni base di un soggetto (Ragione sociale, indirizzo, partita IVA codice fiscale...) in un record base che verrà poi utilizzato per la gestione della posizione Cliente o Fornitore o altra posizione che tale soggetto assumerà nell'azienda in cui viene gestito.

Lo scopo dell'utilizzo del codice Nominativo è di gestire i dati base in modo centralizzato ed univoco.
E' così possibile modificare o storicizzare un'informazione sul nominativo e tale azione si ripercuoterà sugli enti ad esso collegati.
- \*\*Sai cos'è e a cosa serve lo scenario?\*\*

 :  : VOC Id="SKIE0050" Txt="Sai cos'è e a cosa serve lo scenario?"
lo scenario permette di differenziare informazioni a parità di tipo contatto e codice contatto.
Tipicamente lo scenario identifica l'azienda, ma è stato pensato anche per definire dimensioni differenti dall'azienda (esempio linee o divisioni).

- \*\*Sai se il codice del soggetto è univoco in diversi scenari?\*\*

 :  : VOC Id="SKIE0060" Txt="Sai se il codice del soggetto è univoco in diversi scenari?"
L'introduzione dello scenario permette di differenziare anche il codice di un soggetto.
La gestione del nominativo garantisce l'univocità delle informazioni base.
La diversificazione del codice è attivata da un flag da parametrizzare nella tabella BRE a livello di tipo contatto.
- \*\*Sai se e come è possibile attivare la storicizzazione per data delle infor\*\*

 :  : VOC Id="SKIE0070" Txt="Sai se e come è possibile attivare la storicizzazione per data delle informazioni di un contatto?"
La gestione della data validità permette di memorizzare le informazioni per cui si desidera tenere uno storico.
Tale gestione è attivabile dalla tabella BR2 ed i campi che si intendono storicizzare sono da inserire nello script CN_F(Tipo Ente) nel file SCP_SET, aggiungendo il parametro  "Sto=1"
- \*\*Sai dove si attiva lo scenario e se è obbligatorio per tutti i tipi enti?\*\*

 :  : VOC Id="SKIE0055" Txt="Sai dove si attiva lo scenario e se è obbligatorio per tutti i tipi enti?"
E' necessario compilare la tabella BRG codificando gli scenari che si intendono gestire (nel caso standard vanno codificate le aziende con i rispettivi ambienti) e successivamente attivare sulla tabella BR2 il flag deputato. E' poi possibile decidere se un tipo ente è da gestire su diversi scenari oppure è trasversale. Tale definizione avviene nella tabella BRE tipo contatto.
- \*\*Sai se è possibile definire quali campi gestire nello scenario e dove avvi\*\*

 :  : VOC Id="SKIE0058" Txt="Sai se è possibile definire quali campi gestire nello scenario e dove avviene questa scelta?"
I campi da gestire in uno scenario vengono stabiliti all'interno dello script CN_F(tipo ente) definendo il parametro "Sce=1".
- \*\*Sai cosa sono i parametri impliciti?\*\*

 :  : VOC Id="SKIE0080" Txt="Sai cosa sono i parametri impliciti?"
I parametri impliciti sono i campi liberi presenti sul file BRENTI0F.
Esistono 10 campi alfanumerici e 10 campi numerici a disposizione dell'utente.
- \*\*Sai come vengono definiti e assegnati i parametri implciti?\*\*

 :  : VOC Id="SKIE0090" Txt="Sai come vengono definiti e assegnati i parametri implciti?"
I parametri impliciti sono definiti dalla tabella C£I e vengono assegnati attraverso la tabella BRZ (categorai enti).
Se ne deduce che tali parametri possono essere differenti in funzione della categoria enti assegnata al tipo contatto oppure scelta per il contatto specifico al momento della codifica.
- \*\*Sai se sono gestibili altri parametri oltre ai parametri implciti?\*\*

 :  : VOC Id="SKIE0100" Txt="Sai se sono gestibili altri parametri oltre ai parametri implciti?"
E' possibile definire nella tabella C£E una categoria parametri per poter memorizzare sul file C£CONR0F informazioni specifiche aggiuntive per ciascun soggetto codificato.
Il legame tra i parametri esterni ed il soggetto sarà memorizzato nella tabella delle categorie enti (BRZ) oppure più specificamente nella tabella del tipo contatto (BRE).
- \*\*Sai cosa sono le estensioni di un contatto?\*\*

 :  : VOC Id="SKIE0110" Txt="Sai cosa sono le estensioni di un contatto?"
Le estensioni di un contatto sono tutte quelle informazioni che vengono memorizzate sul file BRESCO0F.
- \*\*Sai come sono organizzate le estensioni di un contatto e se è possibile co\*\*

 :  : VOC Id="SKIE0120" Txt="Sai come sono organizzate le estensioni di un contatto e se è possibile codificarne di specifiche?"
Le estensioni di un contatto sono elencate nella tabella BRI. Tali estensioni sono standard se iniziano con il carattere £-- e sono gestite da programmi predefiniti.
E' tuttavia possibile creare delle estensioni personalizzate da gestire attraverso programmi specifici da memorizzare nell'elemento della tabella BRI creato appositamente (di solito sono elementi che iniziano con il carattere X--)
- \*\*Sai se ci sono vincoli nella definizione di un codice contatto?\*\*

 :  : VOC Id="SKIE0130" Txt="Sai se ci sono vincoli nella definizione di un codice contatto?"
L'unico vincolo predefinito nella costruzione di un codice contatto è che deve essere lungo 15 caratteri.
E' tuttavia possibile definire dei vincoli nella tabella BRE, per esempio se il codice debba essere solo numerico e se debba avere una lunghezza fissa.
- \*\*Sai se esiste la possibilità di costruire in modo automatico o guidato il \*\*

 :  : VOC Id="SKIE0140" Txt="Sai se esiste la possibilità di costruire in modo automatico o guidato il codice di  un contatto? Come?"
E' possibile gestire delle domande di costruzione codice, associabili alla categoria enti (tabella BRZ) per avere una guida nella definizione del codice del contatto.
Si tratta della struttura di domande definite dalle tabelle B£F e B£C.
- \*\*Sai se è possibile definire controlli vincolanti durante la creazione di u\*\*

 :  : VOC Id="SKIE0150" Txt="Sai se è possibile definire controlli vincolanti durante la creazione di un nuovo contatto?"
Ci sono controlli definiti a priori sulla natura fiscale del contatto (Tabella BRX) che può essere assegnata a priori attraverso la categoria enti.
Tali controlli sono definibili in progressione in funzione della tipologia fiscale del contatto che si sta gestendo :  per esempio se si sta codificando un soggetto che è una persona fisica, è possibile chiedere obbligatoriamente la compilazione del campo codice fiscale ma non partita IVA.
Viceversa se si sta creando una società, quindi persona giuridica si può chiedere l'inserimento della partita IVA.
E' inoltre possibile, sempre parametrizzando in modo opportuno la tabella BRX che venga fatto il controllo dell'esistenza di eventuali altri contatti che abbiano informazioni duplicate (partita IVA per esempio).
E' inoltre possibile gestire dei programmi specifici di controllo campi con personalizzazioni.
- \*\*Sai se è possibile oltrepassare i vincoli fiscali stabiliti attraverso la \*\*

 :  : VOC Id="SKIE0160" Txt="Sai se è possibile oltrepassare i vincoli fiscali stabiliti attraverso la tabella BRX ?"
In inserimento/modifica dei dati del contatto è possibile utilizzare il tasto F07 = Forzatura per inibire i vincoli stabiliti a priori.
- \*\*Sai cosa sono le prospettive?\*\*

 :  : VOC Id="SKIE0170" Txt="Sai cosa sono le prospettive?"
La prospettiva è lo script CN_P----- che elenca i campi presenti nella visualizzaizone.
Ci sono prospettive di default (standard) e sono le prospettive CN_P£--.
Tuttavia è possibile stabilre prospettive specifiche per tipo contatto CN_P(Tabella BRE) e per tipo contatto e scenario CN_P(Tabella BRE)(Tabella BRG).
- \*\*Sai se è possibile autorizzare e a che livello la gestione delle anagrafic\*\*

 :  : VOC Id="SKIE0180" Txt="Sai se è possibile autorizzare e a che livello la gestione delle anagrafiche?"
La gestione dei contatti è autorizzata a livello di tipo contatto. La classe di autorizzazione che permette di gestire un contatto (Inserimento, modifica, cancellazione...etc.) è la classe BREN01.
- \*\*Sai se le estensioni contatto sono soggette ad autorizzazioni?\*\*

 :  : VOC Id="SKIE0190" Txt="Sai se le estensioni contatto sono soggette ad autorizzazioni?"
Sì le estensioni sono soggette ad autorizzazioni e la classe che gestisce tali autorizzazioni è la BRES01
- \*\*Sai se i parametri impliciti ed esterni sono soggetti ad autorizzazioni?\*\*

 :  : VOC Id="SKIE0200" Txt="Sai se i parametri impliciti ed esterni sono soggetti ad autorizzazioni?"
Essendo i parametri impliciti campi del file BRENTI0F sono soggetti alle autorizzazioni della classe BREN01 che permettono la gestione del file.
Mentre per i parametri esterni, essendo memorizzati sul file esterno C£CONR0F, sono gestiti dalle autorizzazioni del modulo C£ e precisamente dalla classe C£CR01 indicando nella funzione la categoria parametri specificata nella tabella BRZ o BRE ovvero la tabella (C£E).
- \*\*Sai se gli scenari sono sottoposti ad autorizzazione?\*\*

 :  : VOC Id="SKIE0210" Txt="Sai se gli scenari sono sottoposti ad autorizzazione?"
Gli scenari di per se no, è possibile differenziare le autorizzazioni alla gestione del contatto nei diversi scenari attraverso la classe TABRG.
Praticamente è un'estensione della classe BREN01.
- \*\*Sai se le prospettive sono soggette ad autorizzazione?\*\*

 :  : VOC Id="SKIE0220" Txt="Sai se le prospettive sono soggette ad autorizzazione?"
Sì, la classe attraverso la quale gestire le autorizzazioni sulle prospettive è la BRENPRO.
L'autorizzazione permette di stabilire se un utente può vedere i dati inseriti nella prospettiva autorizzata.
- \*\*Sai spiegare la funzione del campo Natura Ente nella tabella BRE?\*\*

 :  : VOC Id="SKIE0230" Txt="Sai spiegare la funzione del campo Natura Ente nella tabella BRE?"
Il campo Natura Ente deve essere obbligatoriamente riempito per i tipi contatti che devono essere visti dalla Contabilità come clienti/fornitori, in quanto tale definizione permette l'attivazione della gestione contabile delle partite tipica dei clienti e fornitori (saldaconto).
- \*\*Sai se è possibile gestire azioni autoamtiche successive all'inserimento o\*\*

 :  : VOC Id="SKIE0240" Txt="Sai se è possibile gestire azioni autoamtiche successive all'inserimento o modifica di un contatto?"
Come per tutti gli oggetti di SME.up è possibile gestire flussi che eseguano programmi specifici o richiamino programmi standard. La tabella da definire è la B£H ed i flussi saranno I-CN--- oppure M-CN--- etc. seguiti eventualmente dal tipo contatto.
- \*\*Sai qual'è l'utilità del campo Costru.Cod.Autom. presente sulla tabella BR\*\*

 :  : VOC Id="SKIE0250" Txt="Sai qual'è l'utilità del campo Costru.Cod.Autom. presente sulla tabella BRE?"
Se impostato presuppone che sia stata associata all'elemento una BRZ che prevede una costruzione automatica del codice ed è possibile far saltare la schermata di conferma del codice attribuito in fase di inserimento (molto utile se attiva la gesitone dei nominativi).
- \*\*Sai come assegnare ad un tipo contatto le categorie contabili da poter ass\*\*

 :  : VOC Id="SKIE0260" Txt="Sai come assegnare ad un tipo contatto le categorie contabili da poter assocaire ai codici contatto della tipologia?"
Nella tabella BRE è possibile stabilire la tabella dalla quale leggere i conti contabili da memorizzare come Categoria contabile.
E' altresì possibile definire un parametro della stessa tabella BRE che attribuisce per default ad un tipo contatto un codice di conto contabile da assegnare in automatico.
Tale campo verrà gestito sia dal programma di inserimento di una anagrafica contatto che dai programmi di contabilità per l'assegnazione del conto in sede di creazione registrazione contabile su di un cliente/fornitore.
