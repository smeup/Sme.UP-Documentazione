### **Nel caso in cui un cliente sia al tempo stesso anche fornitore, è possibile visualizzare all'interno del suo scadenzario anche le partite negative (quindi quelle del fornitore)+
**

?"
 Sì, per ottenere questo risultato è necessario impostare nella tabella BRE la modalità di determinazione dell'ente complementare che può essere effettuata compilando l'ente
 corrispondente presente sull'anagrafica oppure in modo automatico tramite il confronto delle partite IVA. compilata questa tabella all'interno dell'interrogazione dello scadenzario
 è necessario compilare il campo 'Scadenze ente complementare'.

### **Nella colonna 'Documenti' che valore è riportato?**

 All'interno di questa colonna è riportato il valore fatturato al cliente all'interno dello specifico documento.

### **Il calcolo dei giorni di ritardo come viene calcolato?**

 Il calcolo dei giorni di ritardo viene calcolato a partire dalla scadenza originale del documento. Quindi se emetto una fattura con scadenza 31/12/xxxx e a partire da questa fattura vengono generati uno o più insoluti,
 i giorni di ritardo vengono sempre calcolati tenedo come riferimento il 31/12/xxxx e non la scadenza di eventuali nuovi effetti emessi a copertura dell'insoluto.
 In particolare, i giorni di ritardo teorici vengono calcolati prendendo come data inizio la data inizio pagamento, se presente, oppure la data documento, mentre come data fine
 viene presa la data di scadenza indicata sulla rata della fattura. I giorni effettivi invece vengono calcolati utilizzando come data fine la data di scadenza dell'effetto (in caso di effetti)
 oppure la data valuta o registrazione dell'incasso.

### **Cosa significano le Date Documento e Incasso/Registrazione presenti nelle impostazioni?**

 Impostando un range come Data Documento, verranno letti tutti i movimenti relativi a documenti aventi data compresa all'interno dei limiti.
 L'obiettivo di questo tipo di interrogazione è quello di vedere la situazione delle fatture emesse in un certo periodo o esercizio. Impostando invece una Data incasso/registrazione
 vengono analizzati tutti gli incassi avvenuti nelle date limite. Questa data non è una data fissa, ma viene determinata secondo questa risalita : 
 \* se l'incasso è un effetto, essa è la data di scadenza dell'effetto (se ci sono più effetti cumulati, come data scadenza viene sempre presa la scadenza trasmessa alla banca);
 \* in tutti gli altri casi, se è indicata una data valuta viene presa in considerazione questa, altrimenti viene presa in considerazione la data registrazione.


### **Sai cosa sono le rate?**

Sono il derivato principale delle registrazioni contabili, quando queste contengono delle righe inerenti gli enti. Sono scritte nel file C5RATE0F e consentono ad esempio la consultazione degli estratti conto e degli scadenzari.
### **Sai quali sono le tabelle che consentono di generare le scadenze di un documento?**

Fondamentali la tabella codici di pagamento PAG e la sua appendice delle rate variabili C5I.
Nella tabella C5E possono essere codificati vari tipi di rate, che si collegano alle registrazioni contabili sulle tabelle casuali C5V e tipi registrazioni C5D.
### **Sai quali tipi di rate vengono generate?**

Nel registrare dei documenti (con IVA o senza) vengono generate rate di DOVUTO, mentre gli incassi e pagamenti generano rate di PAGATO, come pure le registrazioni di abbuono e oscillazione cambi.
### **Sai come provare un codice di pagamento ed il suo funzionamento?**

Dalla riga comadi mediante la funzione T G01.
### **Sai quali vincoli ci sono tra la registrazione e le rate da essa derivate?**

Deve esserci totale quadratura tra l'importo della riga registrazione origine e le sue rate, sia di dovuto che di pagato.
### **Sai come bloccare una rata?**

In modifica sulla rata immettendo un valore valido (tabellato) nel primo campo a destra.
### **Sai cos'è uno scadenzario e come interrogarlo?**

Elenco ordinato per data scadenza delle partite aperte di un ente, ottenibile nelle interrogazioni soggetti sia per singolo ente che per lista enti con funzione S e metodo R (nella versione a residuo).
### **Sai cos'è un partitario e come interrogarlo?**

Elenco suddiviso per partita dei documenti relativi ad un ente e loro eventuali incassi/pagamenti già avvenuti, oppure abbuoni o oscillazioni cambi rilevati, ottenibile nelle interrogazioni soggetti sia per singolo ente che per lista enti con funzione P e il metodo A.
### **Sai cos'è il saldaconto?**

E' il sistema con il quale effettuare registrazioni di incasso/pagamento e derivate utilizzando causali contabili dedicate. Si tratta in sostanza di una scelta di partite da saldare da una lista simile allo scadenzario, eseguibile anche per più enti su un'unica registrazione, che termina poi su un conto bancario o di cassa/attesa liquidità.
### **Sai cos'è una pratica bancaria?**

E' un oggetto di Sme.Up (PA), cioè una lista di rate omogenee che, selezionate sotto una certa banca di destinazione, consentono poi di effettuare tutta l'attività documentativa, contabile e dispositiva verso la banca stessa.
### **Sai come configurare le registrazioni automatiche da pratiche bancarie?**

Tramite la tabella C5U negli elementi PAD\*.
### **Sai come gestire le proposte di incasso/pagamento?**

Utilizzando l'apposita funzione della gestione pratiche, creando una pratica '\*\*' che può essere poi utilizzata per generare una pratica vera e propria.
### **Sai cosa sono i rapporti bancari?**

Codificati nella tabella C5J, sono un derivato della tabella C5F usata per codificare le banche aziendali, e rappresentano i tipi di operazioni dispositive da effettuarsi sulla singola banca.
Ad esempio :  gestione conto corrente, gestione SBF, gestione anticipi su fatture, ecc.
Consentono di creare apposite pratiche, di contabilizzare movimenti se collegate correttamente a conti contabili, di scaricare file di flusso per invio telematico verso la banca, ecc.
### **Sai cosa sono le coordinate bancarie di un ente?**

Sono i parametri tramite i quali è possibile disporre verso l'ente operazioni di incasso/pagamento, formate da un codice ABICAB (sportello bancario) e numero di conto corrente.
### **Sai cos'è il codice IBAN di un ente e come codificarlo?**

Il codice IBAN è una stringa alfanumerica di caratteri che qualificano univocamente un conto corrente residente su un qualsiasi sportello bancario, calcolato da un algoritmo che viene alimentato da due informazioni basilari, il codice ABICAB della banca e il numero di conto corrente.
E' obbligatorio per effettuare bonifici bancari per via telematica, non ancora per le riba.
### **Sai come impostare il codice SIA aziendale?**

Nei parametri azienda.
### **Sai come creare una pratica bancaria?**

Vista la complessità dell'operazione riferirsi alla documentazione attiva del modulo incassi/pagamenti.
### **Sai cos'è il cumulo di rate in una pratica bancaria?**

E' una funzione che, se utilizzata selezionando più rate con la stessa scadenza e banca d'appoggio, ne ottiene una sola per il valore totale.
Per le pratiche di bonifico a fornitore non è necessaria, in quanto il programma svolge automaticamente il cumulo al momento della creazione del file di invio con home-banking, per gli altri tipi di pratica va utilizzata se necessaria. Nell'anagrafica ente un apposito parametro ne condiziona la possibile effettuazione sulla successiva gestione pratiche.
### **Sai come si elabora una pratica bancaria una volta codificata?**

Utilizzando le funzioni opzionali raggiungibili nel campo opzione, ad esempio per stampare una distinta o lettera, per contabilizzare la pratica, per preparare un file di trasmissione da scaricare e inviare in banca tramite home-banking.
### **Sai come trasferire una pratica bancaria in un flusso inviabile in banca tramite home-banking?**

Scaricando il file C5RR12TF dopo aver eseguito la funzione di trasmissione sulla pratica da inviare.
### **Sai come si importano flussi e di che tipo da home-banking?**

Tramite la funzione 'Ricezione dati remote' si possono importare i seguenti flussi : 
- Movimenti c/c;
- Avvisi Pagamento (riba fornitori);
- Esito Effetti Attivi (insoluti riba clienti).
### **Sai come si contabilizza un insoluto clienti?**

Tramite la funzione apposita, sia manualmente ricercando le riba insolute per cliente o per numero rata, oppure importando un flusso proveniente dalla banca.
### **Sai come ottenere una statistica sugli insoluti?**

Mediante l'apposita funzione nel menu incassi/pagamenti.
### **Sai cos'è l'esito effetti e come attribuirlo?**

Una rata di pagato dovuta a emissione di riba a cliente viene considerata automaticamente pagata il giorno dopo la data scadenza (oppure n giorni dopo, tramite parametro nella tabella C51).
Se la riba torna insoluta, mediante l'apposita funzione può essere contabilizzata come non pagata.
### **Sai cos'è il rischio clienti e come interrogarlo?**

E' l'ammontare delle riba presentate ma non ancora giunte a scadenza, interrogabile dallo scadenzario previa impostazione di un parametro nelle impostazioni (F17).
### **Sai cos'è l'esposizione di un cliente e come interrogarla?**

E' l'ammontare delle riba presentate ma non ancora giunte a scadenza e delle partite aperte, interrogabile dallo scadenzario previa impostazione di un parametro nelle impostazioni (F17).
### **Sai come registrare il richiamo di una riba cliente?**

Dalla opzione di contabilizzazione insoluti, utilizzando il metodo dedicato al richiamo.
### **Sai come prorogare la scadenza di una riba cliente?**

Mediante l'apposita opzione dalla gestione di una pratica, indicando la nuova data scadenza della riba prescelta.
### **Sai come personalizzare e stampare una lettera di estratto conto cliente?**

Dalla gestione lettere (G69) per il tipo lettera C51. La stampa può essere eseguita come opzione dall'interrogazione e.c. cliente, oppure con apposita funzione/metodo S/E dalla lista clienti.
### **Sai come effettuare un riallineamento di massa su tutte le rate aperte di un ente se cambiano le coordinate bancarie?**

Mediante la funzione/metodo V/B della lista clienti, eseguita anche automaticamente dopo la conferma di modifica alle coordinate bancarie nell'anagrafica ente.
