## COSTRUTTORE LOA39
## Obiettivo
Il modulo A39 è un'intefaccia che permette di pubblicare webservice, pertanto è un costruttore che permette di rendere pubbliche delle funzioni Sme.UP, eseguibili dall'esterno.

Il costruttore A39 è costituto da 3 entità : 
-  una scheda :  LOA39
-  una servizio base :  LOA39_SE
-  script SCP_SET specifici Sme.UP o utente :  LOA39_xx

## Funzionamento
Lo Sme.UP Provider tramite il servizio LOA39_SE, interpreta gli script di interfaccia alle funzioni Sme.UP attribuendo un nome al webservice, che identifica univocamente una funzione.

Negli script vengono definite le istanze della classe SESUB.A39 nel formato xx.yyy.zzz : 
-  xx è il gruppo, corrisponde al nome dello script LOA39_xx
-  yyy è la sezione definita all'interno dello script
-  zzz è la subsezione definita all'interno dello script

All'interno dello script vengono pertanto indicate le funzioni pubblicate come web service e le relative variabili di input, che possono essere trasformate dal provider, come definito nella pre trasformazione. L'output restituito al provider è il risultato della funzione stessa e può essere dal provider trasformato come definito nella post trasformazione.

## Definizione nello script SCP_SET
Nel dettaglio questi sono i tag previsti nello script ed i relativi attributi principali : 


| 
| .COL Cod="COL001" Txt="Tag" LunAut="1" |
| ---|----|
| 
| .COL Cod="COL002" Txt="Descrizione" LunAut="1" |
| SEZ       |nell'attributo Cod viene indicata la sezione |
| SUB       |nell'attributo Cod viene indicata la subsezione |
| A39.SUBMET|l'attributo Name indica il nome attribuito alla funzione |
| A39.SUBFUN|l'attributo Value contiene la funzione che deve essere eseguita |
| A39.PRETRS|l'attributo Value contiene la classe che si occupa della pre trasformazione |
| A39.PREVAR|l'attributo Name contiene la relativa variabile prevista e Value il relativo valore |
| A39.PSTTRS|l'attributo Value contiene la classe per si occupa della post trasformazione |
| A39.PSTVAR|l'attributo Name contiene la relativa variabile prevista e Value il relativo valore |
| 

E' infine possibile tramite il tag A39.VAR definire delle variabili di contesto G91 (&CO.xxx..).

# SPECIFICHE TECNICHE
Il costruttore A39 ha lo scopo di mettere a disposizione una configurazione, e la relativa interfaccia per l'utilizzo, che permette di definire **ALIAS** di funzioni da poter esporre attraverso webservice REST su HTTP/S pubblicati dal Provider.

Con **ALIAS** di funzioni s'intende un nome da associare ad una FUN, con un meccanismo automatico di mappatura dei parametri richiesti da questa funzione in parametri della richiesta HTTP e la possibilità di definire variabili di configurazione.
E' anche possibile definire particolari gestori dell'input o dell'output della funzione.
Un esempio è la possibilità, prima che la funzione venga eseguita, di estrarre dalla richiesta HTTP un file dati e metterlo a disposizione del servizio richiamato nella funzione.
Altro esempio è modificare l'XML prodotto dalla funzione, vuoi estrandone solo una parte piuttosto che convertirlo in un altro formato.

Questi comportamenti da tenere prima della richiesta di funzione o successivamente a questa sono gestibili tramite delle particolari classi java definite **Transformer** : 
-  **TransformerPre** qualora impattino a livello di richiesta
-  **TransformerPost** qualora impattino a livello di risposta

Esempi di TransformerPre disponibili : 
-  Estrattori di file contenuti nella chiamata POST effettuata dal clientt (es :  file degli ordini da fare elaborare al servizio che gestisce la FUN, file immagine o documento da archiviare nel sistema)

Esempi di TransformerPost disponibili : 
-  Convertitore del formato xml di matrice in CSV
-  Convertitore del formato xml di matrice in JSON
-  Estrattore di CDATA dalla risposta del servizio che gestisce la FUN ed inoltro al client richiedente
.
## La configurazione
La configurazione si basa sugli script con prefisso LOA39_ contenuti nel file SCP_SET.
ereditando la struttuta dagli script dei LOA, la struttura riproposta è quella di Sezione e Subsezione.

## La sezione
La sezione permette un raggruppamento logico delle funzioni

## La subsezione
Nella subsezione ci sono diversi tipi di istruzioni.
Nella istruzione che la definisce è presente il timeout di attesa del completamento della funzione. Al raggiungimento del timeout la richiesta viene considerata persa da parte del framework A39 e viene risposto di conseguenza all'interlocutore HTTP/S
Es :   :  : SUB Cod="A00" Txt="Matrice in formato JSON" Timeout="300"
E' presente poi l'istruzione che definisce l'alias con cui la funzione potrà essere richiamata dall'interlocutore HTTP/S
Es :   :  : A39.SUBMET Value="SAMPLEJSON" Txt="Nome che identifica la funzione"
E' poi necessario dichiarare la vera a propria funzione che verrà invocata
Es. :   :  : A39.SUBFUN Name="Funzione" Value="F(EXB;LOSER_03;SER) INPUT([\*USER])" Txt="Funzione"
Da notare che la variabile utilizzata **\*USER** potrà essere valorizzata nella Request HTTP e il suo valore verràa automaticamente veicolato alla funzione.

L'istruzione che permette di dichiarare un TransformerPre da modo di chiamare la classe java che manipolerà la richiesta.
Es :   :  : A39.PRETRS Name="Transformer Pre" Value="Smeup.smeui.loa39.interaction.transformer.TransformerFtpDataUpload" Txt="Classe per pre trasformazione"
e può essere supportata da variabili di configurazione a lei destinate
Es :   :  : A39.PREVAR Name="FTP_DIR" Value="/Smedoc/TST"

Stesso discorso si può fare per i TransformerPost
Es :   :  : A39.PSTTRS Name="Transformer Post" Value="Smeup.smeui.loa39.interaction.transformer.TransformerGridToJSON" Txt="Classe per post trasformazione"
e le sue potenziali variabili
Es :   :  : A39.PSTVAR Name="XXXXX" Value="AAAAAA"

Sono nativamente presenti alcuni TransfomerPre e TransformerPost nelle installazioni standard : 
-  TransformerPost
- \* TransformerFtpDataRetrieve che permette di rispondere, invece che l'XML ottenuto dalla funzione eseguita, il contenuto di un file il cui percorso è presente nella risposta alla funzione
- \* TransformerGridToJSON che permette di rispondere, invece che un XML di matrice ottenuto dalla funzione eseguita, lo stesso contenuto in formato JSON
- \* TransformerGridToJSON che permette di rispondere, invece che un XML di matrice ottenuto dalla funzione eseguita, lo stesso contenuto in formato CSV
-  TransformerPre
- \* TransformerFtpDataUpload che permette di estrarre dalla richiesta HTTP, i file eventualmente contenuti in essa e metterli a disposizione della funzione che poi verrà eseguita

## L'attivazione
L'infrastruttura A39 si avvia automaticamente negli avvii di Smeup Provider. Qualora non si voglia avviarla va bloccata attraverso una variabile in SCP_CLO con nome **PROVIDER_LOA39_ENABLED** e valore _7_false
.
## La pagina di benvenuto
E' disponibile una pagina Web all'indirizzo TCP del provider che riporta gli estremi delle funzioni disponibili.
L'indirizzo è http[s]://<indirizzo_provider>[:<porta-tcp>]/A39Service?FUN=FUN_LIST
## Interrogazione del server
Le chiamate al web service prevendono una procedura a tre passi : 
-  autenticazione e ottenimento connessione al sistema
-  richiesta/e dati utilizzando la connessione ottenuta al punto precedente
-  chiusura connessione
### L'autenticazione e connessione al sistema
Implementare l'autenticazione prevede che il chiamante abbia a disposizione un set di credenziali di collegamento valide :  indirizzo sistema, utente, password, ambiente. Attraverso queste credenziali viene richiamato un URL che fornirà la funzione di autenticazione ed in risposta il chiamante otterrà : 
-  il codice della sessione di collegamento messagli a disposizione
-  un timestamp che indica l'istante di creazione della sessione
-  una chiave

i tre dati di cui sopra servono per la codifica dei dati per tutte le richiesta dati vere a proprie che dovranno usare il codice di connessione fornito.
Una volta realizzata la codifica dei dati questi potranno essere passati alla richiesta dati vera e propria.

La sessione può essere riutilizzata per varie chiamate evitando l'overhead provocato dalla creazione di una nuova sessione, può essere esplicitamente chiusa attraverso una chiamata apposita di disconnessione quando si ritiene di non averne più bisogno, oppure scade dopo un tempo gestito dal sistema ERP.

### La richiesta dati
Sulla base dei dati ottenuti nella fase di autenticazione la richiesta dovrà essere fatta sulla base di un meccanismo di sicurezza che prevedere la presenza di un token generato al momento dal cliente, valido solo per quella richiesta.

### La disconnessione
Nel momento in cui la connessione al sistema non sia più necessaria si può richiamare esplicitamente la disconnessione, qualora non ci si disconnetta esplicitamente la sessione non più utilizzata scadrà.


### Implementazione completa di una chiamata autenticata
Implementare il meccanismo di richiesta dati autenticata prevede i seguenti semplici passi : 
1) Definire quale FUN richiedere ed i suoi PARAMETRI

2) Richiedere autenticazione tramite http://<indirizzo provider>[ : porta]/AuthenticateService?server=<indirizzo AS400>&usr=<utente>&pwd=<password>&env=<ambiente>

3) La risposta che ti otterrà è un xml così costituito : 

<Base>
<Oggetto Codice="E7yzGNGbo4_00004" J8_HASH_KEY="dfTs9yuh0Awe0yuiMo03D4y7hwZenbsd" ProviderTime="20160526075718"/>
<Messaggi>
<Messaggio Testo="L'utente <utente> è autorizzato ad accedere al server <indirizzo AS400>, ambiente <ambiente>" Livello="20" Tipo="INFO"/>
<Messaggio Testo="Autenticato il 26.maggio.2016 09 : 57 : 18 : 902" Livello="20" Tipo="INFO"/>
<Esito Stato="OK"/>
</Messaggi>
</Base>

4) Preparare dati da hashare per la richiesta estraendoli dalla risposta precedente
4.1) concatenare Codice+FUN+ProviderTime+"SME"+J8_HASH_KEY+"UP" prendendoli dal punto 1 (il parametro FUN) e dalla risposta del punto 3 (i parametri Codice, ProviderTime e J8_HASH_KEY)

5) della stringa ottenuta al punto 4 fare getBytes("UTF-8") e, dell'array ottenuto, calcolare SHA1

6) Chiamare servlet con i seguenti parametri
6.1) FUN=SAMPLEJSON (vale a dire FUN del punto 1)
6.2) codcon=E7yzGNGbo4_00004 (vale a dire Codice del punto 3)
6.3) hash=f03c67d6f7752ce9622b2d152f5a8c8f0dec5042 (vale a dire hash SHA1 calcolata al punto 5)
6.4) timestamp=20160526075718 (vale a dire ProviderTime del punto 3)
6.5) eventuali altri parametri richiesti dalla FUN

Es: http://<indirizzo provider>[:porta]/A39Service?FUN=<punto 6.1>&codcon=<punto 6.2>&hash=<punto 6.3>&timestamp=<punto 6.4>&PARAMETRI

7) Preparare dati da hashare per la richiesta di disconnessione
7.1) concatenare Codice+ProviderTime+"SME"+J8_HASH_KEY+"UP" prendendoli dalla risposta del punto 3

8) della stringa ottenuta al punto 7.1 fare getBytes("UTF-8") e, dell'array ottenuto, calcolare SHA1

9) Richiedere la servlet per la disconnesione con i seguenti parametri
9.1) codcon=E7yzGNGbo4_00004 (vale a dire Codice del punto 3)
9.2) hash=3a5c660fc663761922a1d0b87b6f306ca54e3bb3 (vale a dire hash calcolata al punto 8)
9.3) timestamp=20160526075718 (vale a dire ProviderTime del punto 3)

Es: http://<indirizzo provider>[:porta]/DisconnectService?codcon=<punto 9.1>&hash=<punto 9.2>&timestamp=<punto 9.3>

## Client disponibili
Sono disponibili per tecnologie java o php client che è possibile utilizzare direttamente senza necessità di implementare l'algoritmo di autenticazione-richiesta-disconnessione esplicitamente.

## Problematiche possibili
Durante il processo di autenticazione-richiesta possono andare male alcune cose, di seguito le casistiche più comuni.
### Credenziali di collegamento non corrette : 
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<title>Error 401 Utente non definito, non abilitato o password non valida.</title>
</head>
<body><h2>HTTP ERROR 401</h2>
<p>Problem accessing /AuthenticateService. Reason : 
<pre>    Utente non definito, non abilitato o password non valida.</pre></p>
</body>
</html>

### Errore nel calcolo Hash
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<title>Error 406 La richiesta e' stata alterata :  hash non valido</title>
</head>
<body><h2>HTTP ERROR 406</h2>
<p>Problem accessing /A39Service. Reason : 
<pre>    La richiesta e' stata alterata :  hash non valido</pre></p><hr><i><small>Powered by Jetty : //</small></i><hr/>

</body>
</html>

### FUN non corretta e non prevista fra quelle esposte
Viene restituita la lista delle funzioni esposte

### Sessione non connessa o scaduta
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<title>Error 403 La Sessione ejcpsuhwnd_000r9 non è valida!</title>
</head>
<body><h2>HTTP ERROR 403</h2>
<p>Problem accessing /A39Service. Reason : 
<pre>    La Sessione ejcpsuhwnd_000r9 non è valida!</pre></p><hr><i><small>Powered by Jetty : //</small></i><hr/>

</body>
</html>
