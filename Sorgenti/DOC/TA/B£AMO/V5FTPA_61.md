# Il Cruscotto di Invio Fatture

## Operatività
Il Cruscotto di Invio Fatture è lo strumento che permette l'invio delle fatture all'intermediario (es. Abletech) il quale si occuperà di inoltrare il flusso al Sistema di Interscambio (SdI) e gestire l'informazione di ritorno dell'esito dell'invio.
La scheda è richiamabile dalla voce di menù "Cruscotto invio fatture" del modulo V5FTPA "Fatturazione Elettronica"

Attualmente si compone di 7 sezioni : 

-  La dashboard di riepilogo
-  La scheda di invio ed il cruscotto d'avanzamento invio
-  La scheda di visualizzazione dei tracciati (USRLVL 01)
-  La scheda dei log di integrazione con il webservice (USRLVL 02)
-  La scheda del log della coda dati (USRLVL 02)
-  La scheda di controlli di sistema
-  La scheda del provider (USRLVL 02)

**Prerequisito all'invio è l'impostazione di alcuni parametri la cui mancata o non corretta compilazione sarà segnalata direttamente nel cruscotto sopra le linguette di selezione delle 6 sezioni sopra elencate.
Nel caso di parametri mancanti o di componenti necessari non correttamente configurati, sarà opportuno verificare il problema tramite la tab "Controllo di sistema" e correggerlo prima di effettuare l'invio.


### La dashboard di riepilogo
In questa dashboard è presente un grafico a barre di riepilogo sullo stato di invio delle fatture elettroniche.
Su ogni record di EDSEND utilizzato per l'invio, infatti, è presente l'indicazione dello stato dell'invio della fattura stessa.

Al momento, gli stati possibili sono 6 : 

-  **0** - Da elaborare :  Rappresentano le fatture per le quali non è ancora stato generato l'XML
-  **1** - XML errato :  Rappresentano quelle fatture per le quali l'XML è stato generato ma presenta errori formali ed quindi necessario ricreare l'XML in questione, dopo aver controllato le stampe di errore e aver sistemato le cause.
-  **2** - Da inviare :  Sono le fatture con XML generato e pronte per essere inviate
-  **3** - Invio in corso :  sono le fatture per cui è stata lanciata la procedura di invio, ma che sono ancora in attesa di essere trasmesse.
-  **4** - Errore nell'invio :  Sono quelle fatture per le quali è stato tentato l'invio ma è fallita la trasmissione all'intermediario.
-  **5** - Inviate :  Sono le fatture correttamente trasmesse e ricevute dall'intermediario

La dashbord riepilogativa in questione mostra, in forma di grafico a barre, il numero complessivo di fattura con XML errato e quelle in attesa di essere inviate.


### La scheda di invio
Questa scheda permette di avere un riepilogo generale su tutte le fatture estratte (inviate, da inviare, in errore, etc...) mediante l'impostazione dei filtri nonché di procedere materialmente all'invio delle fatture stesse.
I filtri selezionabili, anche in abbinamento, sono : 
-  **Tipo selezione**. Permette di filtrare sugli stati di invio visti al punto precedente
-  **Data iniziale e finale**. Filtra tutte le fatture la cui data fattura è nel range specificato. Se impostata solo la data finale, si comporta come un 'fino a'. Se impostata solo la data iniziale si comporta come un 'da'
-  **Tipo ente fattura** e **codice ente fattura**. Corrispondono all'ente di fatturazione dei documenti da cui è composta la fattura.
-  Registro iva
-  **Numero fattura da** e **numero fattura a**. Filtra, con lo stesso criterio sopra espresso per le date, sul numero fattura
-  **Anno**. E' l'anno di emissione della fattura

L'unico filtro obbligatorio è il tipo selezione, che condiziona anche le azioni eseguibili sull'elenco di fatture che verrà estrapolato.
Risulta infatti abilitato il pulsante per la trasmissione solo per le selezioni 'Da inviare' e 'Errore nell'invio'.
Una volta eseguito il filtro, comparirà l'elenco delle fatture che soddisfano i requisiti sopra impostati. Sono visibili tutte le principali informazioni riepilogative delle fatture e lo stato dell'invio.
Se impostato un tipo selezione che consente l'invio, nella matrice sarà visibile come prima colonna la spunta di selezione della fattura stessa.
E' possibile selezionare o deselezionare singolarmente le fatture oppure mediante i due pulsanti 'Seleziona tutto' e 'Deseleziona tutto' effettuare la sezione/deselezione di massa. Ovviamente saranno soggette ad invio le sole fatture selezionate.
L'invio delle fatture avviene tramite sottomissione batch del lavoro (pulsante 'Trasmetti (BATCH)' della scheda). Una volta lanciato l'invio verrà aperto un nuovo cruscotto che riepilogherà in tempo reale lo stato dell'invio con un grafico e con una matrice delle singole fatture da inviare.
Tale cruscotto è descritto nel paragrafo a seguire.

E' inoltre possibile visualizzare il contenuto del tracciato della fattura. Può essere utile in caso di errori o incongruenze.
Cliccando infatti sulla lente d'ingrandimento si accederà infatti ad una specifica sezione in cui sarà possibile visualizzare in dettaglio il contenuto dei dati estratti, suddiviso per tracciato. Sono tutte le informazioni che verranno trasmesse e che sono contenute nel file XML estratto.

### Il cruscotto d'avanzamento invio fatture
Una volta avviato l'invio in batch delle fatture selezionate verrà aperto la dashboard di riepilogo sull'avanzamento dell'invio.
La dashboard è suddivisa in due sezioni :  a sinistra troviamo il grafico ed a destra l'elenco delle fatture presenti nell'invio in corso.

Il grafico a torta, con refresh automatico ogni 20 secondi, mostra : 

-  In grigio la porzione di fatture in attesa di essere inviate
-  In verde la porzione di fatture inviate per le quali è stato restituito l'esito di invio positivo
-  In rosso la porzione di fatture inviate per le quali è stato restituito l'esito di invio negativo

E' possibile forzare il refresh cliccando sulla barra del titolo del grafico.
Il grafico mostra, come etichetta, la percentuale per ogni porzione mentre sotto al grafico è presente una piccola tabella riepilogativa che fornisce le stesse informazioni del grafico ma in termini numerici.
Sulla parte destra della dashboard è invece presente l'elenco delle fatture in elaborazione con i dati essenziali e riepilogativi delle fatture stesse. Inizialmente è visibile l'elenco completo, ma cliccando sugli appositi pulsanti sopra le intestazioni della matrice è possibile selezionare anche solo quelle in attesa dell'invio, quelle già trasmesse o quelle per le quali si è verificato un errore durante l'invio.
Un'icona all'inizio di ogni riga, comunque, restituirà l'informazione relativa allo stato dell'invio. Questa matrice non è in aggiornamento automatico. Per aggiornare la matrice è sufficiente agire sui pulsanti sopra la matrice stessa.
Questa scheda non verrà chiusa al termine dell'esecuzione dell'invio ma andrà chiusa manualmente (quando dal grafico si evincerà che non sono più presenti fatture in attesa di invio).
Si è scelto di non chiudere la scheda anche per consentire un analisi sulla matrice di riepilogo dell'invio.

**N.B. :  La chiusura anticipata della dashboard non pregiudicherà né interromperà il processo d'invio, che proseguirà in bacth. L'esito dell'invio, peraltro, può comunque essere visualizzato dalla scheda di partenza (quella di selezione delle fatture per l'invio) agendo sugli appositi filtri di selezione.

A chiusura della dashbord della scheda di riepilogo, si verrà riportati nella scheda di selezione delle fatture da inviare, aggiornandone il contenuto.

- [Include 01 - Sezioni di controllo sistema](Sorgenti/DOC/TA/B£AMO/V5FTPA_I01)

