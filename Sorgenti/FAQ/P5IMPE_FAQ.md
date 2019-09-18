- **Sai come si chiama l'archivio degli Impegni materiali?**

 :  : VOC Id="SKII0005" Txt="Sai come si chiama l'archivio degli Impegni materiali?"
L'archivio è il P5IMPE0F.
- **Sai quali sono le Tabelle principali per l'attivazione ed implementazione **

 :  : VOC Id="SKII0010" Txt="Sai quali sono le Tabelle principali per l'attivazione ed implementazione degli Impegni materiali?"
Le Tabelle principali sono : 
P5I Tipo Impegno materiali
V5L Parametri di C/Lavoro e Kit
- **Sai come si legano gli Impegni ad un Ordine di produzione?**

 :  : VOC Id="SKII0015" Txt="Sai come si legano gli Impegni ad un Ordine di produzione?"
Per legare gli Impegni materiali ad un Ordine di produzione è necessario : 
1. impostare nella tabella P5T (Tipo ordine di produzione) il tipo imoegno (Tabella P5I) precedentemente definito;
2. impostare, se non già creati, nei flussi dell'Ordine di produzione le azioni di Creazione, Nettificazione e Annullamento impegni.
- **Sai come si legano gli Impegni ad un Ordine di C/lavoro?**

 :  : VOC Id="SKII0020" Txt="Sai come si legano gli Impegni ad un Ordine di C/lavoro?"
Per legare gli Impegni materiali ad un Ordine di C/lavoro è necessario : 
1. impostare nella tabella V5B XX, per il tipo riga relativo ad un C/lavoro, l'elemento di V5L precedentemente creato;
2. impostare nell'elemento della tabella V5L (Parametri di C/lavoro e Kit) il tipo impegno (Tabella P5I) di c/lavoro definito;
2. impostare, se non già creati, nei flussi della riga dell'Ordine di c/lavoro le azioni di Creazione, Nettificazione e Annullamento impegni.
- **Sai se è possibile non creare l'impegno per un codice articolo?**

 :  : VOC Id="SKII0025" Txt="Sai se è possibile non creare l'impegno per un codice articolo?"
Affinchè per un codice articolo non venga creato l'impegno, anche se presente nella distinta base dell'assieme di riferimento, è necessario intervenire sulla Tecnica di gestione definita fra i parametri Articolo / Magazzino.
In questo specifico caso la Tecnica di gestione (tabella GMT) associata dovrà avere come modalità di scarico il valore 'A' Nessuno scarico/impegno.
- **Sai quali sono le modalità con cui vengono creati gli impegni di component**

 :  : VOC Id="SKII0030" Txt="Sai quali sono le modalità con cui vengono creati gli impegni di componenti per l'assieme di un Ordine di produzione o di una riga di Ordine di C/lavoro?"
Le principali modalità con cui vengono creati gli impegni per un assieme sono : 
'DB'  :  a partire dalla Distinta dell'oggetto
'D1'  :  a partire dalla Distinta del documento, e se fosse assente dalla Distinta dell'oggetto
'D2'  :  a partire dalla Distinta del documento
'D3'  :  a partire dalla Distinta del documento, e se fosse assente dalla Distinta dell'oggetto più l'oggetto stesso
'OJ'  :  l'oggetto Stesso (esempio per rilavorazioni)
Per le altre modalità si rimanda all'Help della tabella P5I.
- **Sai come si crea la Distinta di un documento di Produzione o di C/lavoro?**

 :  : VOC Id="SKII0035" Txt="Sai come si crea la Distinta di un documento di Produzione o di C/lavoro?"
La Distinta di un Ordine di produzione è la Distinta base associata a quello specifico Ordine. In particolare l'assieme della distinta è l'ordine di produzione stesso e il tipo distinta è definito nell'elemento di P5I corrispondente al tipo ordine di riferimento.
Per creare la distinta è necessario impostare fra i passi del Flusso di Inserimento Ordine di produzione l'azione Creazione Distinta base, con programma P5FUDDC, Funzione 'CRE' e Metodo : 
CIE :  Creazione cieca
RIC :  Creazione con Richiesta
CIEGES :  Cieca con successiva gestione
RICGES :  Con richiesta e successiva gestione
- **Sai come si introducono in un' Analisi di disponibilità gli impegni materi**

 :  : VOC Id="SKII0040" Txt="Sai come si introducono in un' Analisi di disponibilità gli impegni materiali?"
Per ottenere questo riusultato pè necessario creare un elemento nella Tabella M5F (Fonti Future) che abbia come origine fonte IM - Impegni e come parametro il tipo impegno che mi interessa visualizzare nella Disponibilità.
- **Sai come vengono datati gli Impegni materiali in un'Analisi di disponibili**

 :  : VOC Id="SKII0045" Txt="Sai come vengono datati gli Impegni materiali in un'Analisi di disponibilità?"
Quando viene creato un impegno materiali questo ha come data di riferimento la data di inizio produzione per l'Ordine di produzione e la data di consegna per la riga di C/Lavoro.
Se esiste un lead time di rettifica sul legame di distinta la data è invece : 
- per gli ordini di produzione :  data di fine arretrata del lead time
- per la riga di c/lavoro :  data di consegna confermata arretrata del lead time.
- **Sai se per creare gli Impegni è sufficiente definire correttamente le tabe**

 :  : VOC Id="SKII0050" Txt="Sai se per creare gli Impegni è sufficiente definire correttamente le tabelle?"
Non è sufficente intervenire solo sulle tabelle, ma bisogno aggiungere i passi di gestione degli impegni materiali sul flussi di inserimento, post-modifica e pre-annullamento degli ordini di produzione e delle righe di c/lavoro.
- **Sai dove si definice la modalità di scarico degli Impegni?**

 :  : VOC Id="SKII0055" Txt="Sai dove si definice la modalità di scarico degli Impegni?"
La modalità di scarico degli Impegni è definita sia sulla Tabella P5I per tutti gli articoli della Distinta base. In particolare le modalità di scarico previste sono : 
'IM' :   Scarico di tutti gli impegni
'IC'  :   Scarico di tutti i componenti su residuo
'ID'  :   Scarico di tutti i componenti alla fase
'DO' :   Scarico da Documento, senza creazione impegni

Se non si definisce la modalità è possibile definire una modalità di scarico diversa per singolo componente attraverso la Tecnica di gestione (tabella GMT) definita sui parametri Magazzino / Articolo.
- **Sai che impostazioni fare per prelevare in automatico i componenti di un c**

 :  : VOC Id="SKII0060" Txt="Sai che impostazioni fare per prelevare in automatico i componenti di un c/lavoro senza creare i relativi Impegni?"
E' necessario per i relativi impegni definire una modalità scarico uguale a 'DO'.
In questo modo non verranno creati gli impegni, ma verranno solo scaricati in automatico i documenti attraverso la Distinta del documento.
- **Sai qual è la differenza fra Impegno pianificato ed Impegno rilasciato?**

 :  : VOC Id="SKII0065" Txt="Sai qual è la differenza fra Impegno pianificato ed Impegno rilasciato?"
Un impegno pianificato (archivio M5CONS0F) è un impegno potenziale creato attraverso l'esecuzione dell'MRP, e ai relativi Ordini di produzione pianificati.
Un impegno rilasciato (archivio P5IMPE0F) è l'impegno legato ad un Ordine di produzione reale.
- **Sai come viene associata la causale di prelievo ad un impegno?**

 :  : VOC Id="SKII0070" Txt="Sai come viene associata la causale di prelievo ad un impegno?"
La causale di prelievo è associabile in almeno due modi : 
1. attraverso la tabella P5I, definendola nell'apposito campo Causale di prelievo;
2. attraverso i Parametri logistici, in particolare la categoria £P1 Parametri di impegno/prelievo/consumo.
- **Sai perchè se modifico un Ordine di produzione non vengono automaticamente**

 :  : VOC Id="SKII0075" Txt="Sai perchè se modifico un Ordine di produzione non vengono automaticamente aggiornati anche gli Impegni?"
La causa può essere : 

1. non sono stati attivati i flussi di gestione relativi all'Ordini di produzione che gestiscono i relativi impegni;
2. è stato erroneamente impostata la modalità di scarico degli impegni ('DO');
3. a tutti gli articoli è stata associata una Tecnica di gestione con moalità di scarico ='A'.
- **Sai come si imposta un flusso di spedizione componenti di c/lavoro?**

 :  : VOC Id="SKII0080" Txt="Sai come si imposta un flusso di spedizione componenti di c/lavoro?"
Bisogna impostare un flusso di entrata/uscita con : 
1. nella tabella V5G dovranno essere obbligatori sia il tipo documento partenza e che quello di arrivo, e il modello documento arrivo :  questo perchè è il primo modello che si assume nella catena delle priorità (se assente viene segnalato in dettaglio come errore bloccante), se si impostasse un documento con questo campo vuoto il programma tenterebbe di derivare il modello di destinazione (che è la bolla entrata merci) dal documento origine, il tipo riga è quello assunto del modello;
2. il primo passo del flusso di spedizione deve avere indicato il programma V5AT11E (passo di richiesta ente), con funzione NEWDOC e metodo NOB (se si impostassero altri metodi sarebbe lo stesso perchè non vengono sentiti dal programma successivo) il numero documento non serve;
3. il secondo passo deve essere il programma di estrazione V5AT40L, con le seguenti posizioni in £FUNPS : 
pos. 1 "blank" = presenta solo gli impegni residui
"X"       =presenta tutti gli impegni, anche quelli coperti
pos. 2 "blank" = non imposta la qtà residua da spedire
"X" imposta la qtà residua da spedire
pos. 3 Gruppo fonti per analisi disponibilità articolo (default "\*\*")
- **Sai come si imposta un flusso di prelievi di produzione da Ordine di produ**

 :  : VOC Id="SKII0085" Txt="Sai come si imposta un flusso di prelievi di produzione da Ordine di produzione?"
Quando si definisce l'attività di versamento (tabella B£J GM) si deve utilizzare il programma P5VE00G. In particolare impostando il Tipo attività a : 

'3 - Versamenti e passa a prelievi' :  avremo il prelievo manuale dopo il versamento;
'   - Versamenti e prelievi' :             avremo un prelievo automatico.
- **Sai come si imposta un prelievo backflushing degli Impegni di produzione?**

 :  : VOC Id="SKII0090" Txt="Sai come si imposta un prelievo backflushing degli Impegni di produzione?"
Il Backflushing è un metodo di prelievo automatico di tutti i componenti all'atto del versamento.
Per ottenerlo è sufficiente : 
1. impostare 'IM' come modalità di scarico degli impegni di produzione;
2. impostare una modalità di versamento con prelievo automatico.
- **Se annullo un ordine di produzione si annullano anche gli Impegni?**

 :  : VOC Id="SKII0095" Txt="Se annullo un ordine di produzione si annullano anche gli Impegni?"
Si se nel Flusso Pre Eliminazione ho inserito il passo di Cancellazione impegni (P5FUALL Funzione CAN).
- **Sai dov'è definita la modalità di scarico di un codice articolo?**

 :  : VOC Id="SKII0100" Txt="Sai dov'è definita la modalità di scarico di un codice articolo?"
Nei parametri Magazzino / Articolo alla voce Tecnica di gestione (tabella GMT).
- **Sai quali sono i motivi per cui per un componente ho prelievo manuale anch**

 :  : VOC Id="SKII0105" Txt="Sai quali sono i motivi per cui per un componente ho prelievo manuale anche se è impostato per tutti prelievo automatico?"
Se nella Tecnica di gestione è impostato un valore che prevede Scarico Manuale.
- **Sai perchè l'impegno di un articolo non viene aggiornato anche se tabelle **

 :  : VOC Id="SKII0115" Txt="Sai perchè l'impegno di un articolo non viene aggiornato anche se tabelle e flussi sono impostati correttamente?"
Se nella Tecnica di gestione dell'articolo è impostato il valore 'A' che prevede Nessun impegno e Nessuno scarico.
- **Sai dove si imposta la causale di versamento se l'ultima fase di un Ordine**

 :  : VOC Id="SKII0120" Txt="Sai dove si imposta la causale di versamento se l'ultima fase di un Ordine di produzione è una lavorazione esterna?"
Sulla Tabella V5B XX, per il tipo riga utilizzato per il C/Lavoro, nel campo "Causale versamento C/lavoro".
- **Sai dove si imposta la causale per il movimento di recupero di un Ordine d**

 :  : VOC Id="SKII0125" Txt="Sai dove si imposta la causale per il movimento di recupero di un Ordine di produzione?"
La causale di recupero si può impostare : 
1. nella tabella P5I nel campo Causale di recupero;
2. nei Parametri Logistici, categoria £P1 Parametri prelievo/impegno/consumo.
- **Sai come viene recuperata la causale di prelievo non pianficato in caso di**

 :  : VOC Id="SKII0130" Txt="Sai come viene recuperata la causale di prelievo non pianficato in caso di prelievi manuali per un Ordine di produzione?"
Durante il prelievo manuale è possibile registrare un prelievo non pianificato, utilizzando il tasto funzione F08. La causale proposta è un elemento della tabella GMC che insiste sulla stessa Area dei prelievi pianificati ma che ha tipo movimento PN (Prelievo non pianficato).
