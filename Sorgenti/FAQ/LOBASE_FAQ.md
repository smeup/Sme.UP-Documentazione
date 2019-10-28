### **Dove si trova il programma di installazione di Looc.UP?**

 \* Il programma di installazione in Smea si trova sul server in {SERVER_ROOT}\smea\installazione Looc.UP\. Cercare l'ultimo rilascio di Looc.UP. Per le istruzioni operative vedere "LOOC Documentazione attiva" al capitolo "ANALISI DEL FUNZIONAMENTO"
 \* Da internet :  test.smea.it\loocup

### **L'installazione su client prevede la **

 Looc.UP può essere disinstallato dal Pannello di Controllo :  Start ->Impostazioni -> Pannello di Controllo -> Installazione applicazioni
 Cercare nell'elenco Looc.UP e premere sul tasto rimuovi.

### **Dopo l'installazione di Looc.UP il browser non funziona più correttamente, perchè?**

 L'installazione di Looc.UP carica l'ultima versione di JAVA 2 V1, che viene automaticamente attivata sul browser e può causare problemi.
 Per la risoluzione : 
 \* Aprire il Browser
 \* Selezionare Strumenti --> Opzioni internet --> Avanzate
 \* Ricercare la voce Java Plug-In
 \* Selezionare la sezione Browser, disabilitare la voce relativa al browser interessato e premere "Applica"
 \* Chiudere la finestra, il browser e riprovare.

### **Perchè sul client resto all'infinito in attesa dei menù?**

 Verificare i prerequisiti lato SERVER
 1. TSTJAC per ricevere il nome della connessione
 2. TSTJASF per simulare la chiamata
 __Verifiche__
 1. Esiste SMEUPUIDQ?
 2. Si creano le code specifiche per questa connessione
 3. I lavori vengono immessi in coda (WRKJOBQ)
 4. La coda rilascia i lavori nel sottosistema (Es. QBATCH)
 __
 Possibili cause
 1. Non compilata la tabella UI1
 2. Manca la coda definita (CRTJOBQ)
 3. La coda è definita ma non attaccata  (ADDJOBQE)

# UTILIZZO DI Looc.UP
### **Come posso verificare/ottimizzare le performance?**

 1. Verificare la velocità della rete (10/100 MPS)
 2. Vedere nei prerequisiti lato server installazione e attivazione PTF di accelerazione code

### **Come si devono chiudere i lavori con esito negativo?**

 Le seguenti istruzioni sono destinate al CED
 Eseguire le seguenti azioni : 
 1. Cercare i lavori attivi-> wrkusrjob 'nome utente'.
 2. Per ogni lavoro SMEUPUIEXT e SMEUPUISTD fare 5 di gestione.
 3. Fare 11 per visualizzare lo stack di richiamo dei programmi.
 4. La coda dovrebbe essere nello stato QRCVDTAQ.
 5. Se non è possibile capire lo stato dalla Gestione Lavori Utente fare 4 sui lavori finiti male.

### **Possono restare allocati i record da Looc.UP? Come sbloccarli?**

 Nel momento in cui sblocco un programma in MSGW, vengono anche deallocati i record.
 Al riguardo si veda la domanda precedente.

### **Quali sono i pre-requisiti del profilo utente grafico su As-400?**

 Per i prerequisiti vedere la documentazione attiva in LOBASE_11 Prerequisiti

### **Quali sono le funzioni grafiche?**

 Le funzioni grafiche derivano dal nuovo oggetto applicativo J1 introdotto con Looc.UP, le cui funzioni grafiche sono recuperabili attraverso l'oggetto : 
 V2 JAGRA oppure J1 GRA

### **GLI SCRIPT ATTRIBUTO PER LA SCHEDA OGGETTO**

 **Linea (Termometro)**
 F(ANG) P(valore da visualizzare | valore min | valore max | Punto 1|
 Punto 2 | Punto 3 | Punto 4)
 Il valore da visualizzare è quello su cui si posizionerà la freccia del termometro.
 Il Valore Min è il valore minimo della scala (di solito 0).
 Il valore Max è il valore massimo della scala.
 I Punti rappresentano dei punti di riferimento in cui la scala cambia colore.
 10
 8 <--
 5
 3
 0

 **Angolo (Tachimetro)**
 F(ANG) P(valore da visualizzare | valore min | valore max | Punto 1|
 Punto 2 | Punto 3 | Punto 4)
 Il valore da visualizzare è il valore su cui si posizionerà la freccia del tachimetro.
 Il Valore Min è il valore minimo della scala (di solito 0).
 Il valore Max è il valore massimo della scala.
 I Punti rappresentano dei punti di riferimento in cui la scala cambia colore.
 5
 3     8
 0           10

 **Semaforo della scheda**
 F(SEM) P(label | label | label | numero)
 Le label vanno sopra le luci del semaforo partendo dall'alto.
 Numero invece è : 
 O 4
 O 2
 O 1
 Quindi con numero=1 accendo il verde, ma posso anche fare 3 5 6 per accendere insieme le corrispondenti.

### **GLI SCRIPT DOCUMENTI PER LA SCHEDA OGGETTO**

 **;;LOO F(IMM)**
 Serve per poter visualizzare tutte le immagini di un documento e viene configurato attraverso la tabella JAN, dove, per
 ogni oggetto è presente un sottosettore.
 Es. :  JAN AR
 **;;DEC T(TA) P(JANAR) I(tabella JAN AR)**
 __Uso dei livelli__
 Nella tabelle e nei suoi elementi è possibile l'uso dei livelli attraverso il "."
 Es. : 
 \* DOC           documentazione
 \* DOC.A         documentazione tecnica
 \* DOC.A.ING     documentazione tecnica inglese
 __I tipi di modello__
 I modelli che possono essere usati nella tabella JAN sono : 
 \* XML    XML
 \* HTM    Html
 \* DOC    Testo formattato
 \* RUL    Regole di Configurazione
 \* TXT    Testo libero
 **;;DEC T(V2) P(JATXT) I(V2 jatext)**

### **Come posso evitare di digitare ogni volta l'indirizzo IP dell'AS400?**

 Per non digitare ogni volta l'indirizzo IP dell'AS400 bisogna modificare il file host c : \windows\system32\drivers\ecc...
 Per esempio deve essere inserita una riga del tipo :  172.16.2.11 s4431cfa, dove il primo è l'indirizzo IP del AS400 e il secondo è un nome mnemonico.

### **Come sono gestite le icone e le immagini?**

 Le icone vengono gestite nella seguente maniera :  nella directory sul server sono presenti due sotto-directory chiamate rispettivamente ObjIcons
 e ObjImage.
 Nella prima vanno messe tutte le immagini delle icone degli oggetti applicativi di Sme.UP, quindi ci troveremo le gif di tutti gli oggetti come :  AR, CN, D8,TA, ecc...
 Nella seconda sotto-directory troviamo invece l'insieme di tutte le immagini usate nella scheda oggetto.
 Entrambe le directory hanno una struttura molto ricca per permettere la risalita degli oggetti.
 ES :  vogliamo recuperare l'immagine dell'articolo oggetto=AR Parametro=ART
 Codice=A01. Nella scheda oggetto verrà eseguita la seguente ricerca : 
 Cerco in ObjImage\AR\ART\ l'immagine A01; se la trovo mi fermo, altrimenti cerco sempre in ObjImage\AR\ART l'immagine "default.jpg" che rappresenta tutti gli AR ART.
 Se la trovo mi fermo, altrimenti cerco in ObjImage\AR\ l'immagine "default.jpg" che rappresenta tutti gli AR.

### **Come avvio il Client di Looc.UP?**

 Per avviare Looc.UP con la finestra DOS attivata, utilizzare Loocup.exe che si trova nella directory di installazione, mentre per la modalità che non prevede la finestra DOS, utilizzare Loocup_w.exe . Le funzionalità del client non cambiano.

### **Come posso cancellare un lavoro da PC?**

 __Le seguenti istruzioni sono destinate agli utenti.__
 1. Assumendo di lavorare su una macchina Windows, premere CTRL+ALT+CANC -> Task Manager
 2. Cercare i processi : 
 java.exe o javaw.exe interpreti linguaggio java;
 SmeTray.exe componente delphi per la parte grafica;
 SmeUiClt.exe componente delphi per emulazione 5250.
 3. Se il lavoro finisce male vanno terminati prima di lanciare di nuovo Looc.UP

### **Come posso attivare la finestra DOS della JAVA VIRTUAL MACHINE?**

 Andare sul collegamento di Looc.UP -> pulsante destro del mouse -> Proprietà -> Scegliere il tab Collegamento -> come Destinazione : 
 java.exe -jar Loocup.jar sistema utente password
 Come DA : 
 {SERVER_ROOT}\smea\Programmi\Loocup, sostituendo opportunamente la share del server su cui è installato Looc.UP.

### **Come si può usare Looc.UP?**

 Le modalità di utilizzo di Looc.UP sono principalmente due : 
 \* Installata sul pc localmente
 \* Installata su un server di rete

### **Come posso velocizzare Looc.UP?**

 E' possibile velocizzare Looc.UP non utilizzando le icone nell'albero o nell'emulatore.
 Le opzioni sono rispettivamente : 
 \* Nell'albero -> Config -> Mostra icone negli alberi
 \* Nell'emulatore -> Visualizzazione icone Oggetto su campo oppure CTRL+F12

### **Tabulando l'ordine dei campi non è corretto? Perchè?**

 E' necessario effettuare l'ordinamento dei campi del formato video mediante l'SDA e ricompilarlo.
 Per ordinare i campi automaticamente è necessario fare F4 nella videata e apparirà la lista dei campi. Poi premere F6 per far automaticamente l'ordinamento.

### **Cosa si intende per componente base?**

 Come componente base di Looc.UP si intende il componente che si occupa della comunicazione e che comprende le parti AS400 e quelle di Looc.UP.

### **La scheda è definita come componente base?**

 No.

### **Dove si trovano i preferiti?**

 I preferiti si trovano nella cartella di installazione di Looc.UP -> cartella LOOCUP_DAT -> PRE.

### **Come sono organizzati i preferiti?**

 I preferiti sono salvati per utente e ambiente.
 All'interno della cartella PRE c'è una cartella per ogni utente, contenente un file dei preferiti per ogni ambiente.

### **Se installo una nuova versione di Looc.UP perdo i preferiti?**

 No, è necessario non cancellare la cartella LOOCUP_DAT\PRE

### **Come posso spostare i preferiti da un pc a un'altro o in una nuova installazione?**

 E' sufficiente copiare la cartella LOOCUP_DAT\PRE.
