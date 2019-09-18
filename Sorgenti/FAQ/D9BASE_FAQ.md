- **A cosa serve il modulo Cube.UP?**

 :  : VOC Id="10001" Txt="A cosa serve il modulo Cube.UP?"
 Permette di estrarre dati da Sme.UP o altri file su As400 e metterli a disposizione di applicazioni PC (Databeacon,Excel, ecc...) per poterli visualizzare graficamente.

- **Perchè il nome **

 :  : VOC Id="10002" Txt="Perchè il nome "Cubo"?"
 Il nome cubo deriva dal fatto di poter fare un analisi multidimensionale dei dati grazie a strumenti grafici di aggregazione.

- **Quali sono i prerequisiti?**

 :  : VOC Id="10003" Txt="Quali sono i prerequisiti?"
 Il modulo Cube.UP di Sme.UP installato, il modulo di comunicazione Smens o Netserver di As400 e l'applicazione Client installata (Databeacon, Excel, ecc...)

- **Esiste una documentazione per l'installazione?**

 :  : VOC Id="10004" Txt="Esiste una documentazione per l'installazione?"
 Sul sito www.smeup.com è disponibile un'ottima guida tecnica, che vi seguirà passo passo nell'installazione di tutto il modulo (sia per la parte As400 che per la parte rete PC).
 Indirizzo: http://docs.smeup.com/ITA/masterbook/5178.htm

- **L'interrogazione dei cubi degli utenti appesantisce l'As400?**

 :  : VOC Id="10005" Txt="L'interrogazione dei cubi degli utenti appesantisce l'As400?"
 No, perchè una volta avvenuta l'estrazione, i client si collegano al server interrogando i dati presenti, senza tornare sull'as400 ad interrogare gli archivi.

- **Posso Schedulare la creazione e pubblicazione di cubi?**

 :  : VOC Id="10006" Txt="Posso Schedulare la creazione e pubblicazione di cubi?"
 Sì, basta schedulare un lavoro As400 (WRKJOBSCDE) e impostare nel comando da eseguire la chiamata al pgm D9AP00A con parametro 1 il nome del MDV dei parametri
 di lancio e parametro 2 il nome del cubo da lanciare.
 Posso anche creare un CL che contiene tutte le chiamate ai cubi e schedulare il CL nei lavori As400.

- **File creato su AS/400, ma non lo trovo sul browser. Quali sono i possibili mo**

 :  : VOC Id="10007" Txt="File creato su AS/400, ma non lo trovo sul browser. Quali sono i possibili motivi?"
 1. Utente definito in JA1 non ha autorizzazioni per eseguire l'FTP dai file D9Wxxx dell'AS/400
 2. Se utilizzato il metodo Smens, questo non è attivo sul server di arrivo
 3. Se utilizzato il metodo Smens, questo non è installato su As400

- **I file BAT/TXT/DS4 arrivano sul server, ma non si compilano. Cosa devo fare?**

 :  : VOC Id="10008" Txt="I file BAT/TXT/DS4 arrivano sul server, ma non si compilano. Cosa devo fare?"
 \* Portarsi sul SERVER oppure collegarsi tramite Terminal Client
 \* Reperire la directory contenente i file per la generazione del cubo
 \* Modificare il file .BAT mettendo PAUSE prima di EXIT
 \* Eseguire il file .bat interessato
 \* Nella finestra DOS che rimane aperta dovrebbe essere visibile un errore

 Esempi di errore tipico : 
 \* Campo di intestazione presente due volte (Zona;Agente;Zona;)
 \* Campo non definito
 \* Struttura Cubo troppo Voluminosa. La dimensione di un cubo aumenta con l'aumentare delle gerarchie strutturate e della numerosità delle dimensioni.
 Ad esempio, se la categoria Articolo contiene moltissimi elementi, si consiglia di non agganciargli direttamente tanti Oav, ma di replicare se stessa come OAV e sull'elemento base
 della gerarchia indicare di non visualizzarlo.
 Quindi se ho la gerarchia : 
 ART Articolo per codice e descrizione
 ART.01 Classificazione 1
 ART.02 Classificazione 2
 la posso trasformare in : 
 ART Articolo no visualizza
 ART.ART Articolo per codice e descrizione
 ART.01 Classificazione 1
 ART.02 Classificazione 2
- **Sai quali sono le soluzioni leader di mercato nella BI?**

 :  : VOC Id="SKIA0010" Txt="Sai quali sono le soluzioni leader di mercato nella BI?"
SAP Business Objects, IBM Cognos, Oracle OBIEE, Microstrategy, QlikView, Microsoft .......
- **Sai cosa è QlikView?**

 :  : VOC Id="SKIB0010" Txt="Sai cosa è QlikView?"
Prodotto di BI leader di mercato
- **Sai usare QlikView come utente?**

 :  : VOC Id="SKIB0020" Txt="Sai usare QlikView come utente?"
SI - NO
- **Per sviluppare con QlikView che linguaggio devi conoscere?**

 :  : VOC Id="SKIB0030" Txt="Per sviluppare con QlikView che linguaggio devi conoscere?"
Linguaggio SQL
- **Sai quale prodotto di QlikView consente accesso  web e da dispositivi mobi**

 :  : VOC Id="SKIB0040" Txt="Sai quale prodotto di QlikView consente accesso  web e da dispositivi mobile?"
QlikView Server, non da QlikView Client
- **QlikView usa la logica associativa. Sai cosa vuol dire?**

 :  : VOC Id="SKIB0050" Txt="QlikView usa la logica associativa. Sai cosa vuol dire?"
Il Database associativo non crea i cubi, ma lega i campi di differenti tabelle attraverso un legame semantico unico (stesso nome) che viene creato dallo sviluppatore rinominando i campi.
- **QlikView fa analisi in-memory. Sai cosa vuol dire?**

 :  : VOC Id="SKIB0060" Txt="QlikView fa analisi in-memory. Sai cosa vuol dire?"
L'elaborazione della richiesta fatta  dall'utente con un semplice clik avviene al volo nella memoria RAM dell'hardware. I dati non risiedono più nel disco fisso. Ne consegue che servono macchine server con almeno 32GB RAM.
- **Sai quali sono le tabelle principali di Sme.Up per l'attivazione dell'estr**

 :  : VOC Id="SKIA0100" Txt="Sai quali sono le tabelle principali di Sme.Up per l'attivazione dell'estrazione dati a scopo Business Intelligence ?"
Sono le tabelle D9B, D9C e D9D
- **Sai attraverso quale modalità vengono importati i dati nei prodotti di BI?**

 :  : VOC Id="SKIA0020" Txt="Sai attraverso quale modalità vengono importati i dati nei prodotti di BI?"
ODBC connection
- **Sai cosa significa acronimo ETL?**

 :  : VOC Id="SKIA0030" Txt="Sai cosa significa acronimo ETL?"
Extract, Trasform, Load. E' una funzione che estrae i dati dalla fonte, li trasforma e li carica nel prodotto di BI.
- **Conosci il significato di cubo?**

 :  : VOC Id="SKIA0040" Txt="Conosci il significato di cubo?"
Struttura multidimensionale che racchiude i dati visibili e interrogabili da più punti di vista
- **Conosci il significato di misura e dimensione?**

 :  : VOC Id="SKIA0050" Txt="Conosci il significato di misura e dimensione?"
Misura è il CHE COSA vuoi analizzare (es. il fatturato). Dimensione è il COME vedi il dato (es. per cliente, agente, articolo etc).
- **Sai cosa è la funzione drill-down?**

 :  : VOC Id="SKIA0060" Txt="Sai cosa è la funzione drill-down?"
E' la funzione che consente, partendo da un dato aggregato, di vedere il dato di massimo dettaglio, cioè di scendere per esempio fino alla singola riga di vendita.
- **Sai che cosa sono le Business Analytics?**

 :  : VOC Id="SKIA0070" Txt="Sai che cosa sono le Business Analytics?"
Sono tutte quelle applicazioni di BI che guardano ai consuntivi per predire comportamenti futuri :   es. Gestione del Rischio, Gestione Frodi, Gestione Reclami, Gestione del Personale,  Gestione dei Talenti, Marketing Analytics, Retail Analytics, Fidelizzazione Clienti.
- **Conosci Cube.Up?**

 :  : VOC Id="SKIA0080" Txt="Conosci Cube.Up?"
Cube.Up è l'estrattore di Sme.Up che crea un file csv che viene poi importato da QlikView nel suo Database
- **Sai a che tabella di Sme.Up ci appoggiamo per leggere i dati di fatturato,**

 :  : VOC Id="SKIA0090" Txt="Sai a che tabella di Sme.Up ci appoggiamo per leggere i dati di fatturato, ordinati, acquistato?"
V5STAT
