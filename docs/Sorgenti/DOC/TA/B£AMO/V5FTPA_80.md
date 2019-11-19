### Obiettivo

In questo documento vengono descritti una serie di programmi che possono essere schedulati al fine di automatizzare vari passaggi tecnici della fatturazione elettronica. In particolare, per la fatturazione attiva, si vuole automatizzare il flusso di azioni che, solitamente, seguono la stampa della fattura, fino alla ricezione automatica di mail aventi come oggetto la segnalazione delle fatture che sono in mancata consegna. Tra i passaggi coinvolti è incluso anche il download automatico delle fatture elettroniche ricevute (cioè le passive).

Ognuno in base alle sue esigenze può valutare l'attivazione o meno di ogni singolo programma.

### NOTA BENE
Per tutte le azioni è importante notare che, in caso di presenza di errori, qualcuno deve prendersene in carico la verifica quotidiana. Solo così ci si può accorgere tempestivamente della presenza di anomalie. Una fattura che non si è contabilizzata, un xml che non è possibile produrre o l'esito di scarto/rifiuto sono eventi di particolare rilevanza, che qualcuno deve tenere sotto controllo. A seguire per ogni passaggio è ricordato come.

### 1. Contabilizzazione
Il primo passaggio schedulabile è il lancio della **contabilizzazione** delle fatture stampate, per far questo si dovrà schedulare il richiamo del programma V5FA05A_B tramite il comando CALL PGM(V5FA05A_B) PARM('3')

La schedulazione di questo passaggio va valutata con particolare cognizione di causa. Questo passo può essere attivato solo in un contesto in cui la sola stampa della fattura è sufficiente a certificare che l'emissione della fattura, senza che risultino necessarie ulteriori verifiche/controlli manuali da parte di un utente. Dove è consueto che la fattura sia normalmente controllata nel suo contenuto da un utente, è sconsigliabile prevedere l'esecuzione di questo passo per evitare l'invio di fatture il cui contenuto non è ancora stato effettivamente validato.

La verifica della corretta esecuzione dell'elaborazione può essere fatta tramite verifica della stampa di log o dalla presenza di registrazioni ferme nella "gestione immissioni batch".

### 2. Estrazione
Il secondo passaggio, sarà la procedura che permette l'**estrazione** degli XML delle fatture contabilizzate. Questo processo viene generato tramite la schedulazione del programma V5FE16. Per capire quali sono le registrazioni contabilizzate da estrarre, il programma V5FE16 verifica la presenza della registrazione contabile corrispondente. Questo comportamento permette di rilevare tutte le fatture che si sono effettivamente contabilizzate, evitando quelle che, per vari motivi, sono rimaste bloccate nel batch.

Il programma va schedulato specificando obbligatoriamente un parametro che può assumere i seguenti valori : 
-  blank :  il pgm estrae solo le fatture che non sono mai state inviate
-  2 :  il pgm estrae solo le fatture inviate che sono state poi scartate
-  6 :  il pgm estrae solo le fatture inviate che sono poi state rifiutate dalla PA
-  \*ALL :  vengono elaborati tutti i casi descriti dai punti precedenti.

Ad esclusione del primo caso è importante ricordare che, se la fattura scartata/rifiutata non verrà corretta manualmente dall'utente rispetto al motivo di scarto, il programma continuerà ad estrarre l'xml esattamente come era al momento del rifiuto/dello scarto. Va quindi valutato come sia più opportuno operare per questa casistica.

La verifica della corretta esecuzione dell'elaborazione può essere fatta tramite verifica della stampa di log o tramite le funzioni di verifica presenti nella schede della fatturazione FE.

### 3. Invio
Il terzo passaggio è rappresentato dall'**invio** delle fatture elettroniche tramite schedulazione del programma V5_061B03, l'istruzione da inserire nello schedulatore è CALL PGM(V5_061B03);
Questo programma esegue l'invio sia delle fatture in stato "da inviare" che di quelle per cui risulta lo stato "errore nell'invio".

La verifica della corretta esecuzione dell'elaborazione può essere fatta tramite verifica della stampa di log o tramite le funzioni di verifica presenti nella schede della fatturazione FE.

### 4. Esiti
Il quarto passaggio è quello che lancia la **Ricezione esiti** tramite schedulazione del programma V5_082_05 con il comando CALL PGM(V5_082_05);
Come anticipato all'inizio qui è importante ricordare che si può automatizzare la fase di download e di notifica, ma è necessario che qualcuno verifichi la presenza e poi intervenga sulle fatture che ottengono un esito di scarto o rifiuto.

La verifica della corretta esecuzione dell'elaborazione può essere fatta tramite verifica della stampa di log o tramite le funzioni di verifica presenti nella schede della fatturazione FE.

### 5. Notifiche su mancata consegna
Il quinto passaggio ha il compito di inviare al destinatario della fattura, **una pec di notifica per la mancata consegna dell'xml, questo processo viene attivato dalla schedulazione del programma V5FE15.

Il programma va schedulato specificando obbligatoriamente due parametri : 
-  Nel primo parametro va passato il valore che permette di determinare quale mail usare fra quelle del cliente. Può assumere due significati diversi a seconda che per il database delle mail sia in uso l'estensione degli enti £16 o i referenti : 
- \* Nel primo caso nel parametro va indicato il codice estensione (campo S§CEST). Le mail verranno inviate solo in presenza di una mail corrispondente al parametro qui indicato.
- \* Nel secondo caso va indicato il codice di una mailing list. Le mail verranno inviate solo in presenza di almeno un referente che risulti appartenere alla mailing list indicata.
-  Nel secondo parametro va invece passato il percorso in formato IFS a cui si può trovare la configurazione della G53 corrispondente all'invio in formato PEC.
Facoltativamente è possibile aggiungere un terzo parametro che se passato ad 1 attiva la produzione di una stampa di log.

Questo uno esempio della CALL che ci si aspetta : 
CALL PGM(V5FE15) PARM('FEPEC  ' 'smeext/V5r1/smeup/cfg/pecaz01_1.cfg' '1').

La verifica della corretta esecuzione dell'elaborazione può essere fatta tramite verifica della stampa di log o tramite le funzioni di verifica presenti nella schede della fatturazione FE.

### 6. Download Fatture passive
Come ultimo passaggio si riporta anche la possibilità di schedulare il **download delle fatture passive tramite il pgm C5_093_06.
L'esecuzione di questo passaggio comporta solo l'apparizione delle fatture ricevute, ma non ancora registrate nella relativa scheda di gestione Smeup.

La verifica della corretta esecuzione dell'elaborazione può essere fatta tramite verifica della stampa di log o tramite la funzione di verifica presente nella scheda di gestione delle FE.

