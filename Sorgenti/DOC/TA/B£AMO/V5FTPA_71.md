# Cruscotto esito fatture

## Operatività
Il Cruscotto esito fatture è lo strumento che permette all'utente di mantenere sotto controllo la situazione delle fatture emesse una volta effettuato l'invio al Sistema di Interscambio (SdI) dell'Agenzia delle Entrate.
La scheda è richiamabile dalla voce di menù "Controllo Esiti" del modulo V5FTPA "Fatturazione Elettronica".

Verranno qui presentate una serie di funzionalità di seguito descritte.

### Situazione Esiti
In questa scheda è presente l'elenco dei documenti inviati al SdI e che sono ancora in uno stato transitorio.

Vengono considerate fatture in stato transitorio : 
-  Fatture di cui non è conosciuto l'esito (valore 1)
-  Consegnata ad SDI (valore A). Quando c'è di mezzo un intermediario, questo stato indica il fatto che la fattura ha passato i controlli dell'intermediario ed è stata veicolata all'SDI.
-  Scartate (valore 2). Scartata non è considerato come uno stato definitivo in quando sarà necessario verificare il motivo dello scarto ed operare poi in modo opportuno al fine di gestire il problema.
-  Rifiutata da ufficio PA (valore 6). Valgono le medesime considerazioni del punto precedente.
-  Mancata consegna a ufficio PA (valore 3) e Impossibilità recapito (8). Questi stati dovranno evolvere negli stati X e Y, che indicano il fatto l'emissione delle fatture è stata notificata al cliente. Per il passaggio a tale stato c'è l'apposita voce che verrà a descritta a seguire, ma nulla vieta di sviluppare anche specifiche procedure interne atte a gestire tale indicazione.

Sono invece considerati stati definitivi : 
-  Consegnata a destinatario (valore 4)
-  Accettata da ufficio PA (valore 5)
-  Decorrenza termini (valore 7)
-  Notificata da mancata consegna PA (valore X)
-  Notificata da impossibilità recapito (valore Y)

In alto è presente un grafico a torta che rappresenta un riepilogo sulla situazione in cui si trovano le fatture già trasmesse all'intermediario o al Sistema di Interscambio, accanto al grafico troviamo i valori dai quali è composta e che vengono acquisiti dalla matrice sottostante.

In alto a sinistra, al grafico viene riportata la possibilità, tramite bottoni di : 
-  di lanciare la procedura di aggiornamento immediato degli esiti (con evidenza dell'ultimo momento in cui questo è stato effettuato)
-  di lanciare la gestione della spunta notifica delle fatture non recapitate (funzione che verrà descritta a seguire).

In basso è presentato il dettaglio delle fatture che sono sintetizzate nel grafico.
L'elenco delle fatture è raggruppato per tipologia di esito ed il documento viene descritto all'interno delle seguenti colonne : 

-  Codice ente, è il codice del destinatario documento;
-  Ragione sociale, è la ragione sociale del destinatario documento;
-  Partita IVA, è la P.IVA del destinatario documento;
-  Codice fiscale, è il codice fiscale del destinatario documento;
-  Registro IVA, è il registro IVA sul quale il documento è protocollato;
-  Numero fattura, è il numero del documento;
-  Data fattura, è la data del documento;
-  Importo, è l'importo del documento;
-  Esito, è lo stato in cui si trova il documento dopo essere stato inviato al Sistema di Interscambio;

Le colonne seguenti descrivono attraverso una rappresentazione a "semaforo" la situazione del documento.

-  Creazione XML, se rosso indica che l'xml del documento è stato generato con errori, se invece è verde indica che l'xml del documento è stato generato senza problemi. Quando il semaforo è giallo l'xml è in fase di elaborazione;
-  Invio, se rosso indica che l'xml del documento è stato inviato con errori al Sistema di Interscambio, se invece è verde indica che l'xml del documento è stato inviato senza problemi all'SdI. Quando il semaforo è giallo l'xml è in fase di invio;
-  Ricevuto SDI, se rosso indica che il SdI ha avuto problemi nel ricevere l'xml, se invece è verde indica che l'xml del documento è stato ricevuto senza problemi. Quando il semaforo è giallo il SdI non ha ancora comunicato se l'xml è arrivato a destinazione o se ha avuto problemi legati all'incorrettezza dell'xml oppure all'impossibilità di consegnare al nostro cliente il documento;
-  Ricevuta consegna, se rosso indica che il SdI ha constatato che l'xml è formalmente errato, se invece è verde indica che l'xml del documento è corretto e consegnato al cliente, in questo caso la riga di questo documento verrà spostato nella scheda "Storico documenti". Quando il semaforo è giallo il SdI ha ricevuto l'xml ma non ho ancora la ricevuta della consegna;
-  Mancata consegna, se rosso indica che il SdI ha constatato che l'xml è formalmente errato, se invece è verde indica che l'xml del documento è corretto e consegnato al cliente, in questo caso la riga di questo documento verrà spostato nella scheda "Storico documenti". Quando il semaforo è giallo il SdI ha ricevuto l'xml ma non ho ancora la ricevuta della consegna;

### Lancio procedura aggiornamento esiti
Lanciando questa procedura verrà richiesta un ulteriore conferma di esecuzione.
Confermando verrà aperto la dashboard di riepilogo sull'avanzamento dell'aggiornamento.
La dashboard è suddivisa in due sezioni :  a sinistra troviamo il grafico ed a destra l'elenco delle fatture in elaborazione (tutte le fatture che non hanno un esito definitivo).

Il grafico a torta, con refresh automatico ogni 20 secondi, mostra : 

-  In grigio la porzione di fatture in attesa di essere elaborate
-  In verde la porzione di fatture elaborate per le quali l'aggiornamento è andato a buon fine
-  In rosso la porzione di fatture elaborate per le quali l'aggiornamento non è andato a buon fine

E' possibile forzare il refresh cliccando sulla barra del titolo del grafico.
Il grafico mostra, come etichetta, la percentuale per ogni porzione mentre sotto al grafico è presente una piccola tabella riepilogativa che fornisce le stesse informazioni del grafico ma in termini numerici.
Sulla parte destra della dashboard è invece presente l'elenco delle fatture in elaborazione con i dati essenziali e riepilogativi delle fatture stesse. Inizialmente è visibile l'elenco completo, ma cliccando sugli appositi pulsanti sopra le intestazioni della matrice è possibile selezionare anche solo quelle in attesa di elaborazione, quelle già elaborate o quelle per le quali si è verificato un errore durante l'elaborazione.
Un'icona all'inizio di ogni riga, comunque, restituirà l'informazione relativa allo stato dell'invio. Questa matrice non è in aggiornamento automatico. Per aggiornare la matrice è sufficiente agire sui pulsanti sopra la matrice stessa.
Questa scheda non verrà chiusa al termine dell'esecuzione dell'invio ma andrà chiusa manualmente (quando dal grafico si evincerà che non sono più presenti fatture in attesa di invio).
Si è scelto di non chiudere la scheda anche per consentire un analisi sulla matrice di riepilogo dell'elaborazione.

**N.B. :  La chiusura anticipata della dashboard non pregiudicherà né interromperà il processo d'invio, che proseguirà in batch. L'esito dell'invio, peraltro, può comunque essere visualizzato dalla scheda di partenza (quella di selezione delle fatture per l'invio) agendo sugli appositi filtri di selezione.

A chiusura della dashboard della scheda di riepilogo, si verrà riportati nella scheda di selezione della situazione esiti, aggiornandone il contenuto.

### Spunta fatture non recapitate
Lanciando questa scheda si avrà la possibilità di gestire manualmente l'indicazione del fatto che il cliente intestatario di una fattura non recapitata sia stato effettivamente informato dell'emissione della fattura. Tale indicazione farà si che la fattura scompaia dalla scheda situazioni esiti.

Nella scheda vengono presentate due sezioni : 
-  Spunta Notifica Fatture Non Recapitate :  presenta solo le fatture che non risultano notificate. Da qui sarà possibile in modo immediato andare a spuntare quelle per cui il cliente è stato informato. La modifica è definitiva.
-  Controllo Storico :  presenta solo le fatture già spuntate e permette di effettuare un eventuale controllo o anche di annullare un'eventuale spunta erroneamente attribuita.

### Interrogazione storico
E' un interrogazione che mostra un dettaglio molto simile a quelle presente nella situazione esiti, con la sola differenza che è possibile interrogare tutto lo storico delle fatture con l'evidenza dello stato attuale (che sia definitivo o meno).

- [Include 01 - Sezioni di controllo sistema](Sorgenti/DOC/TA/B£AMO/V5FTPA_I01)

