- **Servizio di aggiornamento**

 :  : VOC Id="00010" Txt="Servizio di aggiornamento"
E' il servizio che si occupa di gestire l'interazione delle modifiche che avvengono ai dati. Questo servizio è identificato dal valore del parametro di Setup "UpdSvc" e può essere un servizio differente rispetto a quello che carica i dati.
Questo servizio dovrà gestire le chiamate peculiari della comunicazione dei dati (£UIBME='*SETUP', £UIBME='*UPDATE", £UIBME="*EXIT", ecc.).
Per maggiori dettagli si rimanda comunque alla documentazione applicativa.

- **XML di setup**

 :  : VOC Id="00020" Txt="XML di setup"
Per xml di setup si intende l'xml che viene caricato in risposta al metodo *SETUP che viene eseguita nei confronti del servizio di aggiornamento come primo richiamo della sezione.
Questo xml si caratterizza per la definizione di una serie di informazioni, aggiuntive rispetto all'xml di griglia, che permettono di settare tutta una serie di comportamenti da applicare alla gestione interattiva dei dati. Fra questi si annoverano ad esempio informazioni aggiuntive : 
* Di colonna
* Di ricerca contestuale
* Delle azioni di gestione possibili (es. Inserimento, Modifica, Cancellazione)

- **Layout**

 :  : VOC Id="00030" Txt="Layout"
Alla presentazione dei dati può essere associato un layout grafico (tecnicamente corrispondente ad uno script del file SCP_LAY). Attraverso questo script è possibile andare a definire come varie caratteristiche grafiche aggiuntive per la presentazione dei dati (dal posizionamento dei campi, all'attivazione di una ricerca contestuale).
Per maggiori dettagli si rimanda comunque alla documentazione applicativa.

- **Forma grafica di un campo**

 :  : VOC Id="00040" Txt="Forma grafica di un campo"
Con questo termine si far riferimento ad istanza di oggetto V2FOGOG. Le istanze di questo oggetto definiscono la forma grafica con cui i campi vengono presentati in una matrice. E' previsto un default per oggetto fissato nella K04, ma tramite il layout o la schiera di griglia £JAXSW3 è possibile sovrascrivere tale proposta. E' importante notare che ad ogni componente è associata anche una configurazione di setup.

- **Autoenter o Avanzamento Record**

 :  : VOC Id="00060" Txt="Autoenter o Avanzamento Record"
E' una caratteristica che può essere attivata sulla singola cella attraverso l'attributo di colonna £JayFAR ad "1". L'effetto sarà che quando si conferma la cella viene richiamato il servizio di update con funzione *CHECK e nome del campo nel tag FLD di £UIBSS.

- **Comandi**

 :  : VOC Id="00070" Txt="Comandi"
Tramite il servizio di aggiornamento è possibile attivare dei comandi (che si concretizzano in tasti funzione). Questi tasti hanno il solo scopo di richiamare il servizio di aggiornamento con il metodo (£UIBME) valorizzato con il codice comando (variabile £JayCmd) al fine di far svolgere al servizio di aggiornamento particolari azioni che esulano da quelle previste normalmente.
I comandi fanno parte delle istruzioni settabili dalla chiamata *SETUP al servizio di aggiornamento.

- **Ricerche contestuali**

 :  : VOC Id="00080" Txt="Ricerche contestuali"
E' possibile tramite il layout o la schiera di griglia £JAXSW3 (attraveso i rispettivi attributi Tfk e Pmk) settare delle ricerche e dei controlli contestuali. Per contestali si intende la possibilità di far si che la ricerca del campo non si estenda a tutte le istanze della cui un cella risulta intestata, ma di limitarne le scelte secondo determinate regole (es. se a video ho regione e provicia, fisso che nella provicia posso vedere/inputare solo le province della regione indicata). Nel fissare queste regole quindi posso sfruttare tutte le variabili grafiche previste (celle di riga comprese).

- **Campi Estesi**

 :  : VOC Id="00090" Txt="Campi Estesi"
Con i campi estesi si fa riferimento ai campi che hanno una lunghezza superiore a 2560 caratteri. Questi campi presentano una gestione particolare, che va considerata nel singolo servizio di aggiornamento.

- **Aggiornamento Differito ed Immediato**

 :  : VOC Id="00500" Txt="Aggiornamento Differito ed Immediato"
Indicando del setup del componente l'attributo DeferUpd a "Yes", il servizio di aggiornamento verrà chiamato solo quando verrà premuto il tasto di salvataggio dei dati, mentre non verrà mai invocato durante la compilazione delle righe.

- **Aggiornamento una riga per volta**

 :  : VOC Id="00510" Txt="Aggiornamento una riga per volta"
L'attributo OneRowUpd ha implicazione grafica del caso di matrici ad aggiornamento immediato :  implica che solo la riga su cui si ha il fuoco in un dato momento verrà presentata come riga di aggiornamento, mentre le altre righe saranno visibili come normali righe di matrice.

- **Aggiornamento Monoline**

 :  : VOC Id="00520" Txt="Aggiornamento Monoline"
Per MonoLine si intende un servizio a cui arrivano una o più Line ma in cui ognuna, in maniera sequenziale, è trattata indipendentemente dalle altre (controllo / scrittura / restituzione XML). Non è possibile, inoltre, creare Line aggiuntive rispetto a quelle ricevute dal client (effettuare modifiche su righe diverse da quelle toccate dall'utente).
L'utilizzo dell'aggiornamento Monoline è indirizzato dal fatto di impiegare la /COPY £JAY_C1, nel servizio di aggiornamento.

- **Aggiornamento Multiline**

 :  : VOC Id="00530" Txt="Aggiornamento Multiline"
A differenza del caso monoline, può capitare che in un servizio si debba trattare un insieme di Line in maniera congiunta. Un esempio banale è la necessità di deferire la scrittura vera e propria solo dopo avere controllato tutte le Line e avere verificato PER TUTTE l'assenza di errori.
Rispetto al gestione monoline (la stessa prevista per gli input panel), consiste in queste differenze operative : 
a. vengono prima controlla tutte le righe (routine £JAY_LOAD e £JAY_AFTER)
b. al termine del controllo di tutte le righe viene lanciata la routine £JAY_GLOBAL (per controlli da applicare all'insieme di righe)
c. dopo la £JAY_GLOBAL verrà eseguita una sola £JAY_EXEC che si dovrà occupare dell'aggiornamento di tutte le righe.
Per maggiori dettagli si rimanda comunque alla documentazione applicativa.
L'utilizzo dell'aggiornamento Monoline è indirizzato dal fatto di impiegare la /COPY £JAY_C2, nel servizio di aggiornamento e dal fatto che la matrice sia in aggiornamento differito.

- **Celle M**

 :  : VOC Id="00540" Txt="Celle M"
Indicando tipo di input/output di colonna il valore M, la colonna verrà nascosta, ma tramite una combinazione di due cifre con valore 0 e 1 sarà possibile condizionare la protezione della cella successiva. Tramite questa funzionalità è quindi possibile condizionare sia la protezione di una cella, in base a considerazioni che possono essere fatte per la singola riga.
La prima cifra ad 1 indica che la condizione di protezione, a 0 invece di modificabilità.
La seconda cifra a 1 indica invece che la condizione della cifra precedente verrà applicata a tutte le celle successive sintanto che non si incontra un'altra cella di tipo M.
La seconda cifra 0 indica invece che la condizione della cifra precedente verrà applicata solo alla cifra successiva.

- **Riga inserimento automatica**

 :  : VOC Id="00550" Txt="Riga inserimento automatica"
Dalla chiamata *SETUP a servizio, tramite il parametro £JayFirIns, è possibile attivare il fatto che il client proponga nella matrice una riga di inserimento automatica.
Tramite l'attributo di setup del componente, InsertPosition, sarà inoltre possibile decidere dove presentare tale riga (es. in alto o in fondo alla matrice).

- **Tutta la matrice di inserimento**

 :  : VOC Id="00560" Txt="Tutta la matrice di inserimento"
Dalla chiamata *SETUP a servizio, tramite il parametro £JayAllIns, è possibile attivare il fatto che tutte le righe di matrice vengano elaborate come righe in inserimento (Utile per riprese da Excel).

- **Attivazione combo/autocomplete**

 :  : VOC Id="00570" Txt="Attivazione combo/autocomplete"
Dalla chiamata *SETUP a servizio, tramite il parametro £JayComboM, è possibile attivare l'utilizzo dei componenti grafici di combo ed autocomplete in loocup che di norma nella matrici sono invece disattivate.

- **Archivio B£SUPS0F e Salvataggio Setup di Matrice**

 :  : VOC Id="00580" Txt="Archivio B£SUPS0F e Salvataggio Setup di Matrice"
Al fine di facilitare la creazione di servizi di aggiornamento, è stata implementato in  modo automatizzato all'interno della /copy £JAY_C0 il salvataggio dei dati di setup della matrice.
Questo avviene salvando i valori della schiera dei campi gestiti (£JayFldLst), delle autorizzazioni e delle altre informazioni di setup (£JayDSSetup) e di eventuali informazioni specifiche impostate nel servizio (£JaySpecInfo) nel file di appoggio B£SUPS0F direttamente nella /copy £JAY_C0.
Per sfruttare questo file è necessario : 
* Aggiungere nella IMP0 del servizio di aggiornamento l'esecuzione della routine £JAY_SETLET .
* Aggiungere sotto la chiamata con £UIBME='*EXIT' l'esecuzione della routine £JAY_EXIT.
Per maggiori dettagli si rimanda comunque alla documentazione applicativa.

- **Ritorno ad inizio record**

 :  : VOC Id="00590" Txt="Ritorno ad inizio record"
Indica se arrivati all'ultimo campo di una riga, alla tabulazione successiva, si passa alla riga successiva o si ritorna al primo campo della riga su cui ci si trova. Questa scelta è legata all'attributo di componente CarReturn.

