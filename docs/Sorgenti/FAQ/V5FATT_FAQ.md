### **Come impostare la fatturazione PERIODICA?**

 \* Creare dei codici di periodicità di fatturazione, attribuendoli ai vari clienti in modo da formare una sorta di gruppi di clienti, organizzati per periodicità di fatturazione.
 \* I codici di periodicità di fatturazione vengono catalogati nella tabella **BR\*CF** (solo descrittiva) e assegnati ai clienti mediante l'estensione £08 del BRESCO.
 \* Nella tabella **V51** è presente un campo che permette di determinare il calendario di fatturazione, mediante il quale si indica il tipo risorsa di riferimento. Ne è esempio l'elemento FAT della tabella TRG.
 Il calendario di fatturazione, basato sul tipo risorsa definito quindi nella V51, si gestisce come un normale calendario di disponibilità risorse, riportando nel giorno di fatturazione prescelto un turno lavorativo :  in altre parole dovrò ottenere una disponibilità risorse nei soli giorni di fatturazione.
 \* La stampa fatture dovrà infine essere lanciata nella "scelta tipo fatture" non normale, ma "solo gruppo XXX".

### **TABELLE DA IMPOSTARE**

 __Tabella calendario fatturazione__
 :  : DEC T(ST) K(BR\*CF) I(·)

 __Tabella impostazione tipo risorsa per calendario di fatturazione__
 :  : DEC T(TA) P(V51) K(\*)

 __Tabella tipo risorsa__
 :  : DEC T(ST) K(TRG) I(·)

 __Esempio tabella TRG da SMETAB__
 :  : DEC T(TA) P(TRG) K(FAT) I(elemento)
### **Sai dove e come è possibile definire il numeratore delle Fatture di vendita?**

Il numeratore delle fatture è assegnabile : 
1. nell'elemento della tabella V5A XX, che corrisponde al modello di documento da fatturare, nel campo "Numero fattura"; il campo punta alla tabella CRN V5;
2. direttamente nella stampa fattura qualora non si desiderino creare più modelli di Documento di vendita e si voglia aggiornare direttamente il numeratore del Registro IVA.

Il secondo caso è spesso utilizzato per non dover diversificare fra Bolle vendita Italia, CEE o ExtraCEE, dove il numeratore della Bolla potrebbe essere unico, mentre quello della Fattura diverso.
### **Sai come si chiama il programma di stampa fattura e dove si imposta?**

Il programma di stampa fattura si chiama V5FA01S e non si imposta in alcuna tabella (a differenza del programma di Stampa Ordine o di Stampa Bolla).
### **Sai come si definisce la modalità di raggruppamento delle Bolle di vendita per ottenere il documento fattura?**

La modalità di raggruppamento delle Bolle di vendita per ottenere una fattura è definita attraverso due informazioni : 
1. il valore del campo T§FDTA (Raggruppamento bolle/fatture) della testata della Bolla di vendita; se ad esempio tale campo è valorizzato con '2' significa che per ogni bolla si deve estrarre una fattura; tale campo può essere impostato manualmente sul documento, oppure essere ereditato dal flag 3 del cliente intestatario;
2. dal Criterio di ordinamento calcolato per la bolla di vendita; il citerio di ordinamento è un insieme di codici che valorizza il campo T§CORD della testata della Bolla; il campo T§COR2, unitamente al campo T§CORD viene valorizzato a livello di ordine e può essere utilizzato per definire il raggruppamento/rottura durante la creazione della Bolla, ma il passaggio dalla Bolla alla Fattura viene gestito in raggruppamento/rottura dal solo campo T§CORD.
I valori che esso può assumere sono a standard : 
'1' - Ciclo attivo :  Modalità pagamento + Valuta
'2' - Ciclo passivo :  Data bolla + Numero bolla
'3' - Ciclo attivo :  Codice di spedizione + Modalità di pagamento + Valuta + Modlaità di consegna + Modello documento
'4' - Ciclo attivo :  Numero fattura + Data fattura + Numeratore stampa fatture
oppure, nel caso utilizzi le lettere, calcolati attraverso il programma V5DO01O_X, dove X è la lettera indicata nella tabella V5A XX.
Quindi se più bolle possono finire nella stessa fattura, verranno scelte quelle con T§CORD e T§COR2 uguali.
### **Sai come si definisce fatturabile un documento?**

Per definire un documento fatturabile si deve agire sul Gruppo flag di testata e sul Gruppo flag di riga.
TESTATA :  il flag interessato è il flag 19 (T§FL19) che se assume valore "\*blanks" indica che il documento non è fatturabile (es. Bolla di c/visione), altrimenti, affinchè il documento sia fatturabile, deve assumere i valori 'B' per le Fatture di vendita, 'N' per le Note di accredito clienti, 'b' per le Fatture di Acquisto, 'n' per le Note di accredito fornitori. Gli altri possibili valori sono interrogabili con il comando UP FLG, archivio V5TDOC0F.
RIGA :   il flag interessato è il flag 19 (r§FL19) che se assume valore "9" indica che la riga non è fatturabile, altrimenti, affinchè il documento sia fatturabile, deve assumere valore '\*blanks' per una riga di vendita normale,  '7' per un Omaggio imponibile con IVA Cliente etc etc.  Gli altri possibili valori sono interrogabili con il comando UP FLG, archivio V5RDOC0F.

Inoltre deve essere definito il numeratore delle Fatture (vedi domanda F0005).
### **Sai come si definisce contabilizzabile un documento?**

Per definire un documento contabilizzabile si deve : 
1. agire sul Gruppo flag di testata; il flag interessato è il flag 8 (T§FL08) che se assume valore "\*blanks" indica che il documento è contabilizzabile, se assume valore '9' indica che il documento non è contabilizzabile;

2. definire la casuale contabile (Tabella C5A) associata al documento da contabilizzare; questa causale viene solitamente definita nell'impostazione del modello del documento (Tabella V5A XX);

3. definire le regole per assegnare i corretti Conti contabili al documento; la principale tabella interessata è la COA.
### **Sai come si capisce se un documento è fatturato?**

Un documento è fatturato se non è annullato (Livello della testata diverso da '9') e se sono valorizzati i campi della testata Numero e Data fattura (T§NFAT e T§DFAT).
### **Sai come si capisce se un documento è contabilizzato?**

Un documento è contabilizzato se è fatturato (nel caso delle vendite) e se il flag 19 della testata (T§FL19) è valorizzato a : 
'E' per una fattura di vendita
'Q' per una Nota di accredito cliente
'e' per una fattura di acquisto
'q' per una Nota di accredito fornitore
### **Sai qual è la differenza fra una prefattura e una fattura proforma?**

La prefattura è la stampa di una fattura di vendita senza che sia stato assegnato il numero di fattura definitivo.
La fattura proforma è un documento senza alcuna valenza fiscale, utilizzato quando si rende necessario presentare al cliente un facsimile della fattura finale senza incorrere negli obblighi fiscali e mantenendo la certezza che il documento non possa far insorgere, in caso di controlli, la presunzione di fatturazione, generando tutte le conseguenze per la mancata registrazione dello stesso. Normalmente viene ottenuta stampando la conferma Ordine cliente con le corrette diciture.
### **Sai come si lancia una fatturazione di massa?**

Ci sono due modalità di lancio della fatturazione di massa.
1. La prima è la semplice stampa fattura (call V5FA01A) dove posso impostare una parzializzazione, ad esempio per cliente o per data bolla.
2. La seconda è la Fatturazione interattiva (call V5FA02A), che ha il vantaggio, rispetto alla precedente, di visualizzare tutti i documenti fatturabili prima di lanciare la stampa.
### **Sai se un documento fatturato può essere modificato?**

Un documento fatturato, ma non contabilizzato, può essere modificato, salvo la stampa della fattura non sia già stata inviata al cliente.
Bisogna prestare particolare attenzione se le modifiche comportano una variazione nelle condizioni di pagamento, nell'aliquota IVA o nell'importo della fattura, in generale se è prevista la ristampa della fattura.
Se il documento è già stato inviato al cliente bisognerà prendere particolari accordi con esso.
Se il documento è già stato contabilizzato è necessario seguire una procedura diversa.
### **Sai se un documento contabilizzato può essere modificato?**

Un documento contabilizzato può essere modificato ma prima bisogna procedere alla : 
1. cancellazione della corrispondente registrazione in contabilità;
2. modifica del flag 19 da Contabilizzato a In attesa di contabilizzazione.

Per procedere alla modifica del flag si può utilizzare l'azione di Menu 'Azioni su documenti fatturabili'.
### **Sai se è possibile definire una periodicità diversa di fatturazione per un cliente (ad esempio mensile a fronte di una fatturazione standard settimanale)?**

Per la fatturazione differita è possibile diversificare, per alcuni clienti, la periodicità di fatturazione utilizzando il Calendario di fatturazione (Tabella BR\* CF).
Questa informazione deve essere poi associata al cliente attraverso l'informazione estesa £08.
### **Sai che impostazioni fare se un cliente chiede per ogni bolla un'unica fattura?**

E' necessario indicare tale modalità di accorpamento bolle / fatture nell'anagrafica cliente alla voce "Raggruppamento documenti" (E§FL03).
### **Sai come si imposta una riga omaggio?**

Affinchè una riga sia di tipo omaggio è necessario impostare il corretto Gruppo flag di riga nella tabella V5B XX.
In particolare è necessario impostare correttamente il flag 19 (R§FL19) : 

'1'         Omaggio non imponibile
'7'         Omaggio imponibile - Iva cliente
'8'         Omaggio non imponibile - autofattura
'A'         Omaggio con IVA a Carico
### **Sai come si ottiene un' Autofattura?**

L'Autofattura è un documento che l'azienda intesta a se stessa per adempiere agli obblighi fiscali relativi al pagamento dell'IVA.
Un esempio è emettere autofattura per gli Omaggi ai clienti dove l'imponibile non è a carico del cliente (flag 19 della riga = '8').
La tabella da compilare è la V53 :  è necessario creare un elemento per ogni modello di documento di vendita che possa contenere righe Omaggio non imponibili.
Per estrarre il documento di Autofattura in automatico è presente nel Menu fatturazione l'azione "Generazione documento Autofattura" (programma V5FA10A).
### **Sai come si blocca un documento fatturabile?**

Per bloccare un documento fatturabile è necessario utilizzare la voce del Menu fatturazione, "Azioni su documenti fatturabili".
Individuato il documento è sufficiente utilizzare l'opzione 30 = Stato -> Bloccato :  questa opzione porta il flag 19 della testata (T§FL19) al valore 'D' per le fatture di vendita, 'P' per le Note accredito Clienti, 'd' per le fatture di acquisto e 'p' per le Note di accredito Fornitori.
### **Sai come si trasfoma un documento fatturabile in non fatturabile?**

Per rendere un documento fatturabile non fatturabile è necessario utilizzare la voce del Menu fatturazione, "Azioni su documenti fatturabili".
Individuato il documento è sufficiente utilizzare l'opzione 34 = Stato -> Non fatturabile :  questa opzione porta il flag 19 della testata (T§FL19) al valore '\*blanks'.
### **Sai se è possibile gestire con unico documento di vendita più numeratori di fattura?**

Non è possibile.
E' vero il contrario che più documenti di vendita possono essere riferiti alla stessa fattura.
### **Sai cos'è la fatturazione interattiva?**

La fatturazione interattiva è una funzionalità che mi consente di effettuare la PRESTAMPA, STAMPA e RISTAMPA di documenti fatturabili o già fatturati e/o contabilizzati, presentando a video l'elenco dei documenti selezionati tramite i parametri di ingresso.

Per i documenti selezionati non ho però solo a disposizione le opzioni di stampa di cui sopra, ma, per i documenti non ancora fatturati, posso anche : 
- visualizzare e/o modificare testate e righe di tutti i documenti raggruppati;
- forzare raggruppamenti di documenti su un'unica fattura, oppure forzare separazione di documenti altrimenti raggruppati;
- gestire i flag di fatturazione del/i documento/i di una fattura.
### **Sai come si può gestire facilmente l'accorpamento o disaccorpamento di documenti di vendita prima della fatturazione?**

Utilizzando le funzionalità della Fatturazione interattiva.
### **Sai qual è la procedura corretta per annullare un documento già fatturato?**

La procedura è semplice nel caso in cui il documento ha l'ultimo numero di fattura utilizzato.
In questo caso è necessario : 
1. cancellare dalla testata il numero e la data fattura
2. annullare il documento
3. riportare indietro di un numero il numeratore delle fatture.

Nel caso il numero di fattura non è l'ultimo utilizzato è necessario verificare se è possibile riutilizzare il numero, nel qual caso va indicato manualmente sul nuovo documento emesso oppure agire come prevede la normativa fiscale.
### **Sai qual è la procedura corretta per annullare un documento già contabilizzato?**


Se si imposta il flag (previsto a standard nel modello) nella tabella C51

Scolleg.Docum.Orig.  '1'

"CANCELLANDO LA REGISTRAZIONE CONTABILE" il documento passa da Contabilizzato a "DA contabilizzare" a quel punto posso modificarlo e/o Cancellarlo.
Sempre che le autorizzazioni me lo permettano.
### **Sai se è possibile impedire la modifica di un documento fatturato?**

E' possibile impostando correttamente la Classe di autorizzazione V5DO01D per il tipo documento di roferimento e modificando lo stato del documento in caso di Fattura stampata.
In particolare, se ad esempio metto in stato 50 un documento per cui la fattura è stata stampata, è sufficente impostare il campo A_ST dello Stato a '40'.
### **Sai se è possibile impedire la modifica di un documento contabilizzato?**

E' possibile impostando correttamente la Classe di autorizzazione V5DO01D per il tipo documento do roferimento.
In particolare è sufficente impostare il campo A_FA del flag stato fattura a 'D'.
### **Sai se è possibile inserire una Fattura manuale (non derivata da Bolla di vendita)?**

E' possibile inserire manualmente una Fattura utilizzando la funzione "Manutenzione documenti" del Menu Ciclo esterno e selzionando il modello, precedentemente implementato, di Fattura manuale cliente.
Tale modello dovrà avere indicati nell'elemento di tabella V5A corrispondente, il numeratore fatture (salvo non venga impostato tramite il programma di stampa), la causale contabile e un gruppo flag di testata con flag 19 valorizzato a 'B'.
### **Sai come si imposta un modello di Nota di accredito Cliente?**

Per impostare un modello di Nota di accredito è necessario utilizzare il corretto Gruppo flag di testata. In particolare il Gruppo deve avere il Flag 19 valorizzato ad 'N'.
### **Sai qual è l'archivio delle fatture?**

Le Fatture, così come le Bolle o gli Ordini o più in generale tutti di documenti del Ciclo attivo e del Ciclo passivo sono il V5TDOC0F e il V5RDOC0F.
In particolare una fattura è esattamente l'insieme delle testate e delle righe di bolla che riportano il Numero e la data fattura nei campi T§NFAT e T§DFAT. In altre parole dalle Bolle di vendita non viene estratto alcun altro documento.
### **Sai cosa si intende per fatturazione immediata e fatturazione differita?**

La fatturazione immediata è una fattura accompagnatoria che sostituisce la bolla che quindi NON ci sarà (per far questo servono i flag  di testata (18 e 19) impostati  adeguatamente)

La fatturazione differita prevede che la stampa definitiva delle fatture avvenga con una periodicità fissa e in un momento successivo all'emissione delle Bolle. Normalmente avviene a fine mese.
