- **Servizio di aggiornamento**

 :  : VOC Id="00010" Txt="Servizio di aggiornamento"
E' il servizio che si occupa di gestire l'interazione delle modifiche che avvengono ai dati. Questo servizio è identificato dal valore del parametro di Setup "UpdSvc" e può essere un servizio differente rispetto a quello che carica i dati.
Questo servizio dovrà gestire le chiamate peculiari della comunicazione dei dati (£UIBME='\*SETUP', £UIBME='\*UPDATE", £UIBME="\*EXIT", ecc.).
Per maggiori dettagli si rimanda comunque alla documentazione applicativa.

- **XML di setup**

 :  : VOC Id="00020" Txt="XML di setup"
Per xml di setup si intende l'xml che viene caricato in risposta al metodo \*SETUP che viene eseguita nei confronti del servizio di aggiornamento come primo richiamo della sezione.
Questo xml si caratterizza per la definizione di una serie di informazioni, aggiuntive rispetto all'xml di griglia, che permettono di settare tutta una serie di comportamenti da applicare alla gestione interattiva dei dati. Fra questi si annoverano ad esempio informazioni aggiuntive : 
\* Di colonna
\* Di ricerca contestuale
\* Delle azioni di gestione possibili (es. Inserimento, Modifica, Cancellazione)

- **Layout**

 :  : VOC Id="00030" Txt="Layout"
Alla presentazione dei dati può essere associato un layout grafico (tecnicamente corrispondente ad uno script del file SCP_LAY). Attraverso questo script è possibile andare a definire come varie caratteristiche grafiche aggiuntive per la presentazione dei dati (dal posizionamento dei campi, all'attivazione di una ricerca contestuale).
Per maggiori dettagli si rimanda comunque alla documentazione applicativa.

- **Forma grafica di un campo**

 :  : VOC Id="00040" Txt="Forma grafica di un campo"
Con questo termine si far riferimento ad istanza di oggetto V2FOGOG. Le istanze di questo oggetto definiscono la forma grafica con cui i campi vengono presentati in un input panel. E' previsto un default per oggetto fissato nella K04, ma tramite il layout o la schiera di griglia £JAXSW3 è possibile sovrascrivere tale proposta. E' importante notare che ad ogni componente è associata anche una configurazione di setup.

- **Modifica di più righe**

 :  : VOC Id="00050" Txt="Modifica di più righe"
Con gli input panel è possibile gestire anche più righe. Per ottenere questo effetto è sufficiente fare in modo che nella xml iniziale vengano caricate più righe, esattamente come avviene nelle matrici. A questo punto le righe potranno essere scorse tramite i tasti di PageDown/PageUp. Propedeutico a questo tipo di gestione è l'applicazione dell'attributo di setup ShowMatrix che permette di visualizzare nella sezione, in forma matriciale, tutte le righe caricate in aggiunta all'input panel della riga su cui si ha il fuoco.

- **Autoenter o Avanzamento Record**

 :  : VOC Id="00060" Txt="Autoenter o Avanzamento Record"
E' una caratteristica che può essere attivata sulla singola cella attraverso l'attributo di colonna £JayFAR ad "1". L'effetto sarà che quando si conferma la cella viene richiamato il servizio di update con funzione \*CHECK e nome del campo nel tag FLD di £UIBSS.

- **Comandi**

 :  : VOC Id="00070" Txt="Comandi"
Tramite il servizio di aggiornamento è possibile attivare dei comandi (che si concretizzano in tasti funzione). Questi tasti hanno il solo scopo di richiamare il servizio di aggiornamento con il metodo (£UIBME) valorizzato con il codice comando (variabile £JayCmd) al fine di far svolgere al servizio di aggiornamento particolari azioni che esulano da quelle previste normalmente.
I comandi fanno parte delle istruzioni settabili dalla chiamata \*SETUP al servizio di aggiornamento.

- **Ricerche contestuali**

 :  : VOC Id="00080" Txt="Ricerche contestuali"
E' possibile tramite il layout o la schiera di griglia £JAXSW3 (attraverso i rispettivi attributi Tfk e Pmk) settare delle ricerche e dei controlli contestuali. Per contestali si intende la possibilità di far si che la ricerca del campo non si estenda a tutte le istanze della cui un cella risulta intestata, ma di limitarne le scelte secondo determinate regole (es. se a video ho regione e provincia, fisso che nella provincia posso vedere/inputare solo le province della regione indicata). Nel fissare queste regole quindi posso sfruttare tutte le variabili grafiche previste (celle di riga comprese).

- **Campi Estesi**

 :  : VOC Id="00090" Txt="Campi Estesi"
Con i campi estesi si fa riferimento ai campi che hanno una lunghezza superiore a 2560 caratteri. Questi campi presentano una gestione particolare, che va considerata nel singolo servizio di aggiornamento.

