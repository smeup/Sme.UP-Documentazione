- \*\*Sai com'è composta una registrazione contabile?\*\*

 :  : VOC Id="SKIA0010" Txt="Sai com'è composta una registrazione contabile?"
Seguendo la struttura della gestione documenti, una registrazione contabile ha una testata (file C5TREG0F) e delle righe (file C5RREG0F).
- \*\*Sai quali sono le tabelle fondamentali che condizionano la compilazione di\*\*

 :  : VOC Id="SKIA0020" Txt="Sai quali sono le tabelle fondamentali che condizionano la compilazione di una registrazione?"
Il piano dei conti (tab.C5B)
Le causali contabili (tab.C5V e C5D)
I registri IVA (tab.C5R)
I codici IVA (tab.IVA)
I codici di pagamento (tab.PAG)
Le registrazioni automatiche (C5U)
- \*\*Sai che cosa sono la pertinenza e la condizione di una registrazione?\*\*

 :  : VOC Id="SKIA0030" Txt="Sai che cosa sono la pertinenza e la condizione di una registrazione?" Als="comm"
La pertinenza attribuisce un significato preciso alla registrazione (fiscale, gestionale, ecc.), la condizione ne stabilisce lo stato (attivo, simulato, ecc.).
- \*\*Sai perchè una registrazione inizia immettendo l'anno e la data registrazi\*\*

 :  : VOC Id="SKIA0040" Txt="Sai perchè una registrazione inizia immettendo l'anno e la data registrazione separati?" Als="comm"
Perchè l'anno stabilisce la competenza fiscale della registrazione (al fine di utilizzarla per formare il bilancio dell'esercizio in questione), mentre la data registrazione ne stabilisce la collocazione temporale (ad esempio, il giornale di contabilità viene ordinato per data registrazione).
- \*\*Sai a cosa servono le registrazioni di pertinenza gestionale?\*\*

 :  : VOC Id="SKIA0050" Txt="Sai a cosa servono le registrazioni di pertinenza gestionale?" Als="comm"
Servono per immettere o far generare automaticamente delle registrazioni di natura non fiscale, utili però all'ottenimento di bilanci gestionali infrannuali. Si possono identificare come tali, ad esempio : 
- ratei e risconti;
- ammortamenti mensili;
- movimenti di simulazione/previsionali (stanziamenti);
- ...
- \*\*Sai cosa sono le registrazioni di pura IVA?\*\*

 :  : VOC Id="SKIA0060" Txt="Sai cosa sono le registrazioni di pura IVA?" Als="comm"
Sono registrazioni particolari, ottenibili mediante l'uso di un'apposita causale, composte da una testata e da sole righe IVA :  servono per effettuare scritture sui registri IVA ma non vengono prese in esame da bilancio, mastrini, ecc.
Esempio classico di registrazioni di pura IVA sono le bolle doganali, oppure alcuni tipi di autofatture.
- \*\*Sai se è possibile aggiungere descrizioni estese a una registrazione?\*\*

 :  : VOC Id="SKIA0070" Txt="Sai se è possibile aggiungere descrizioni estese a una registrazione?"
Oltre alla possibilità di alterare la descrizione standard associata alla causale prescelta, è possibile immettere delle note di testata (tasto funzione F8) e/o delle note di riga (opzione 'NO' sulla riga o 'X' ed invio nel campo all'estrema destra della riga stessa). Possono esistere entrambi i tipi di note sulla stessa registrazione.
Le note vengono come di consueto scritte nel file NTSTRU0F legate all'oggetto E4 (testata) o E5 (riga).
- \*\*Sai come è possibile ottenere una lista di registrazioni contabili?\*\*

 :  : VOC Id="SKIA0080" Txt="Sai come è possibile ottenere una lista di registrazioni contabili?"
Esiste una funzione apposita, configurabile nelle informazioni salienti (F17), che consente di ottenere una lista parzializzabile delle registrazioni contabili.
- \*\*Sai come eseguire una registrazione con IVA?\*\*

 :  : VOC Id="SKIA0090" Txt="Sai come eseguire una registrazione con IVA?"
Utilizzando tipi di registrazioni con modello 01.
- \*\*Sai cos'è il saldaconto?\*\*

 :  : VOC Id="SKIA0100" Txt="Sai cos'è il saldaconto?" Als="comm"
E' un tipo di registrazione che consente di effettuare incassi e pagamenti su clienti e fornitori, ivi compresi abbuoni attivi e passivi, oscillazioni cambi attive e passive, incassi e pagamenti anticipati.
- \*\*Sai quali consolidamenti vengono eseguiti sulle registrazioni?\*\*

 :  : VOC Id="SKIA0110" Txt="Sai quali consolidamenti vengono eseguiti sulle registrazioni?"
La stampa definitiva dei registri IVA pone un flag che protegge gran parte della registrazione, lasciando in sostanza libere le contropartite e le rate.
La stampa definitiva del giornale protegge tutta la registrazione lasciando libere solo le rate.
- \*\*Sai cosa sono e a cosa servono le rate?\*\*

 :  : VOC Id="SKIA0120" Txt="Sai cosa sono e a cosa servono le rate?" Als="comm"
Le rate sono un 'di cui' della riga ente su una registrazione che ne prevede l'uso, in particolare le registrazioni con IVA e quelle di incasso e pagamento. Nel primo caso si hanno delle rate di dovuto, nel secondo di pagato. Sono la base per le interrogazioni di partitario e scadenzario enti, per la creazione di pratiche bancarie, per tutte le statistiche su debiti e crediti.
- \*\*Sai cos'è un insoluto?\*\*

 :  : VOC Id="SKIA0130" Txt="Sai cos'è un insoluto?" Als="comm"
E' una registrazione contabile da effettuare dietro segnalazione della propria banca, nel caso un cliente non paghi una ricevuta bancaria emessa a fronte di una fattura a lui inviata.
- \*\*Sai cos'è e a cosa serve la data competenza iniziale/finale presente sulla\*\*

 :  : VOC Id="SKIA0140" Txt="Sai cos'è e a cosa serve la data competenza iniziale/finale presente sulla testata e su ogni riga?" Als="comm"
Serve per attribuire un costo (solitamente) al periodo in cui esso viene sostenuto, dato che normalmente viene addebitato con una fattura in un periodo successivo.
Ad esempio, una fattura di energia elettrica emessa in data x può riferirsi al bimestre precedente, quindi nella data competenza inizio/fine viene riportata questa indicazione (rilevabile sul documento). Se attiva la gestione automatica dei ratei/risconti, l'indicazione darà modo al programma di fare la corretta elaborazione della quota parte di costo per il periodo di competenza.
- \*\*Sai che cos'è il protocollo IVA assegnato alle registrazioni IVA?\*\*

 :  : VOC Id="SKIA0150" Txt="Sai che cos'è il protocollo IVA assegnato alle registrazioni IVA?"
E' il numero progressivo assegnato che ne determina, tra l'altro, l'ordinamento nella stampa delle informazini sul registro IVA a cui la registrazione stessa viene assegnata. Per i documenti di vendita coincide con il numero di fattura emessa, per quelle di acquisto è un numero progressivo gestito da un numeratore (se si sceglie l'assegnazione automatica) oppure viene immesso manualmente.
- \*\*Sai se una registrazione è annullabile o modificabile liberamente?\*\*

 :  : VOC Id="SKIA0160" Txt="Sai se una registrazione è annullabile o modificabile liberamente?" Als="comm"
La classe di autorizzazione C5E401G consente di autorizzare utenti e/o gruppi utenti alla manutenzione delle registrazioni. Se l'utente è autorizzato, i flag di stampa definitiva registri IVA e giornale bloccano eventualmente la modifica di parte o tutta la registrazione.
- \*\*Sai come fare per assegnare ad un ente un conto di costo/ricavo preferenzi\*\*

 :  : VOC Id="SKIA0170" Txt="Sai come fare per assegnare ad un ente un conto di costo/ricavo preferenziale?"
Tramite la gestione delle estensioni enti, nell'elemento £17 è possibile impostare la contropartita contabile preferenziale.
- \*\*Sai come gestire la ritenuta d'acconto di un percipiente durante una regis\*\*

 :  : VOC Id="SKIA0180" Txt="Sai come gestire la ritenuta d'acconto di un percipiente durante una registrazione?"
Impostando correttamente nell'anagrafica il rapporto fiscale e le estensioni £40 e £41 si configura un ente come percipiente. Durante la registrazione contabile del documento il programma riconoscerà tali impostazioni, aggiungendo una richiesta parametri precompilata con calcolo della ritenuta d'acconto al termine della registrazione stessa. Al momento del pagamento/incasso della partita, se le impostazioni della tabella C5U sono correttamente impostate, si vedrà rilevare automaticamente la ritenuta applicata precedentemente.
- \*\*Sai se è possibile registrare il pagamento di una fattura di un percipient\*\*

 :  : VOC Id="SKIA0190" Txt="Sai se è possibile registrare il pagamento di una fattura di un percipiente senza averne ricevuto la fattura?"
Con una registrazione di saldaconto è possibile registrare un anticipo, che poi si può collegare alla fattura con un pareggio appena questa verrà registrata. Dalla gestione pratiche è possibile generare una rata di anticipo e pianificare quindi un bonifico con invio di un flusso con home-banking, e poi si contabilizza la pratica. Si procede poi al pareggio con la fattura come per il saldaconto.
- \*\*Sai collegare la registrazione di acquisto di un cespite alla gestione ces\*\*

 :  : VOC Id="SKIA0200" Txt="Sai collegare la registrazione di acquisto di un cespite alla gestione cespiti?"
Il conto contabile usato come contropartita all'acquisto deve essere una immobilizzazione, cioè avere il flag 'Rilevanza cespiti' acceso nella tabella C5B. Nella tabella C51 il flag 'Collegamento automatico cespiti' deve avere valore '2'. Devono essere impostate le tabelle cespiti, in particolare la A5F che stabilisce il legame tra causale contabile e causale cespite.
- \*\*Sai configurare correttamente le registrazioni IVA Intracee e/o Reverse Ch\*\*

 :  : VOC Id="SKIA0210" Txt="Sai configurare correttamente le registrazioni IVA Intracee e/o Reverse Charge?"
Sulla tabella IVA c'è un flag apposito che stabilisce se un certo codice deve dar seguito a registrazioni con IVA Intracee oppure Reverse Charge, concettualmente identiche.
Nella tabella C5U vanno codificati dei record con codice IVAACxx, dove xx è il codice IVA di cui sopra, indicando il codice del conto IVA acquisti da utilizzare in presenza di registrazioni con quel codice IVA. Devono inoltre esserre presenti gli elementi IVACE e IVARE, che determinano quale conto di contropartita va impiegato per generare automaticamente la riga di IVA a debito.
- \*\*Sai collegare la registrazione di acquisto Intracee alle gestione Intrasta\*\*

 :  : VOC Id="SKIA0220" Txt="Sai collegare la registrazione di acquisto Intracee alle gestione Intrastat?"
Nella tabella C51 il flag 'Collegamento automatico Intra' va posto a '2', poi deve essere attiva la gestione Intracee.
- \*\*Sai cosa sono i modelli di registrazioni?\*\*

 :  : VOC Id="SKIA0230" Txt="Sai cosa sono i modelli di registrazioni?"
Sono dei settaggi predefiniti per causale contabile, che possono essere utilizzati per definire una serie di conti da impiegarsi sempre per determinate registrazioni particolari, che si ripetono sempre identiche (esclusi importi e date, ovviamente) periodicamente.
- \*\*Sai come configurare i modelli di registrazioni?\*\*

 :  : VOC Id="SKIA0240" Txt="Sai come configurare i modelli di registrazioni?"
Dalla immissione registrazioni contabili, premendo l'F11 sulla finestra di inizio registrazione, si può compilare una registrazione fittizia che se confermata verrà memorizzata come modello.
- \*\*Sai dove e come configurare i meccanismi che eseguono registrazioni automa\*\*

 :  : VOC Id="SKIA0250" Txt="Sai dove e come configurare i meccanismi che eseguono registrazioni automatiche?"
Nella tabella C5U.
- \*\*Sai cos'è e a cosa può servire una registrazione autostornante?\*\*

 :  : VOC Id="SKIA0260" Txt="Sai cos'è e a cosa può servire una registrazione autostornante?"
Serve per eseguire registrazioni che, il giorno o il mese successivo la data registrazione, vengono stornate automaticamente con una registrazione uguale e contraria.
Un esempio tipico di tale registrazione potrebbe essere quello di una rilevazione di ammortamenti periodici ad un certo trimestre, che servono per i bilanci gestionali infrannuali.
- \*\*Sai cos'è la quota di IVA indetraibile rilevabile su una registrazione?\*\*

 :  : VOC Id="SKIA0270" Txt="Sai cos'è la quota di IVA indetraibile rilevabile su una registrazione?"
E' una parte dell'IVA acquisti che, per definizione normativa, è stabilito non possa essere detratta interamente e quindi deve essere destinata a costo.
- \*\*Sai come codificare i conti IVA che il programma utilizza automaticamente?\*\*

 :  : VOC Id="SKIA0280" Txt="Sai come codificare i conti IVA che il programma utilizza automaticamente?"
Nella tabella C5U gli elementi IVA\* sono tutti dedicati alla gestione dell'IVA e alla configurazione di eventuali automatismi.
- \*\*Sai cosa significa gestire un conto a documenti/partite?\*\*

 :  : VOC Id="SKIA0290" Txt="Sai cosa significa gestire un conto a documenti/partite?"
Significa assegnare ad un certo conto delle caratteristiche del tutto simili a quelle di un cliente o fornitore, ovvero poter effettuare delle registrazioni dove numero e data documento sono dati obbligatori, perchè necessari alla successiva interrogazione di un estratto conto a partite.
- \*\*Sai a cosa serve l'immissione batch?\*\*

 :  : VOC Id="SKIA0300" Txt="Sai a cosa serve l'immissione batch?"
Può servire sia per l'immissione di movimenti durante una conversione, che per la generazione automatica di movimenti da altri sistemi conferenti. Durante l'esecuzione di procedure che prevedono la generazione di movimenti automatici, nell'ingresso batch si fermano quelle scritture che, per un verso o per l'altro, hanno dei problemi che non consentono il corretto riepimento di tutti i dati obbligatori componenti la registrazione o ne rendono impossibile la quadratura. Tramite la 'Gestione ingresso batch' è possibile gestire tali movimenti ed eventualmente completarli e applicarli.
- \*\*Sai cos'è l'archivio transazioni?\*\*

 :  : VOC Id="SKIA0310" Txt="Sai cos'è l'archivio transazioni?"
E' un file temporaneo nel quale si 'ferma' una registrazione in gestione (immissione, modifica). Si svuota se al termine dell'elaborazione il movimento viene confermato, mentre rimane sospesa se, per qualsiasi motivo, il movimento non viene confermato e l'elaborazione si interrompe.
- \*\*Sai come funziona il collegamento delle fatture di vendita alle registrazi\*\*

 :  : VOC Id="SKIA0320" Txt="Sai come funziona il collegamento delle fatture di vendita alle registrazioni?"
Il programma V5FA05A lancia la contabilizzazione delle fatture di vendita alla contabilità, dando modo di eseguire alcuni filtri (data e numero documento, cliente, tipo di documento) e operando in tre modi diversi : 
- solo lista di controllo;
- solo contabilizzazione movimenti;
- entrambe le precedenti opzioni.
Nel caso vi siano dei problemi con qualche documento, la lista errori ne segnalerà il motivo, dando modo di correggere il documento indicato.
Durante la contabilizzazione effettiva viene prodotta una seconda lista contenente i movimenti generati.
- \*\*Sai gestire registrazioni in divisa estera?\*\*

 :  : VOC Id="SKIA0330" Txt="Sai gestire registrazioni in divisa estera?"
Per poter effettuare registrazioni in divisa estera deve anzitutto essere correttamente gestita la tabella VAL, della quale si consiglia l'importazione completa dal modello in quanto sono già presenti tutte le valute codificate secondo il codice ISO.
Il file dei cambi giornalieri consente, opzionalmente, di tracciare uno storico dei cambi per valuta :  è opzionale perchè sulle registrazioni manuali il cambio è libero, ma è comodo perchè il programma effettua una ricerca per data documento ogni volta che si immette un codice divisa su una registrazione. Diventa fondamentale invece per la contabilizzazione delle fatture di vendita, che avviene in batch.
Per fare in modo che, per un certo cliente/fornitore, le registrazioni avvengano in divisa, si può impostare la divisa di default nell'anagrafica relativa. Anche un conto può essere configurato come conto in divisa, nella sua anagrafica in tabella C5B.
- \*\*Sai configurare il controllo fatture passive?\*\*

 :  : VOC Id="SKIA0340" Txt="Sai configurare il controllo fatture passive?"
Nella documentazione attiva del modulo sono disponibili due funzioni che, se eseguite, effettuano un settaggio minimo di tutti i parametri che regolano la gestione del controllo fatture.
Poi, in base alle caratteristiche che si vogliono dare di volta in volta, è possibile effettuare aggiunte di elementi o modifiche ai settaggi standard, includendo/escludendo parti della gestione se necessario.
- \*\*Sai come bloccare il pagamento di una scadenza fornitore?\*\*

 :  : VOC Id="SKIA0350" Txt="Sai come bloccare il pagamento di una scadenza fornitore?"
In modifica su una rata, ponendo un valore valido nel primo campo a destra.
- \*\*Sai come compensare un debito fornitore con un credito cliente?\*\*

 :  : VOC Id="SKIA0360" Txt="Sai come compensare un debito fornitore con un credito cliente?"
Tramite il saldaconto, con una causale di incasso/pagamento oppure una dedicata di pareggio partite.
- \*\*Sai come pareggiare una o più fatture con una o più note credito di un ent\*\*

 :  : VOC Id="SKIA0370" Txt="Sai come pareggiare una o più fatture con una o più note credito di un ente?"
Tramite il saldaconto, con una causale di incasso/pagamento oppure una dedicata di pareggio partite, in alternativa dall'estratto conto dell'ente mediante l'opzione 'P' di pareggio.
- \*\*Sai come configurare un calendario scadenze per tipo pagamento e/o ente?\*\*

 :  : VOC Id="SKIA0390" Txt="Sai come configurare un calendario scadenze per tipo pagamento e/o ente?"
Codificare un elemento C5G oppure CLI/FOR nella tabella TRG.
Nella tabella C53 codificare C5G nel campo 'Calendario per tipo pagamento'.
Nella tabella BRE codificare CLI/FOR nel campo 'Calendario contabile'.
Sul menu della gestione calendario andare nella 'Gestione degli anni' e codificare un nuovo elemento con tipo risorsa C5G oppure CLI/FOR e anno 3000, impostando i giorni festivi nei quali si desidera non cadano scadenze.
Sempre dalla gestione calendario impostare i 'Dati settimanali risorsa', sempre per tipo risorsa C5G oppure CLI/FOR.
Per provare il funzionamento di un codice pagamento utilizzare T G01.
- \*\*Sai cosa sono le registrazioni di stanziamento?\*\*

 :  : VOC Id="SKIA0400" Txt="Sai cosa sono le registrazioni di stanziamento?" Als="comm"
Sono registrazioni di tipo gestionale, adatte per rilevare l'effettiva competenza ad esempio di un costo, ovvero immettendo alla corretta data di fruizione la quota parte di costo.
Le causali impiegate per queste registrazioni hanno gruppi flag diversi da quelle contabili, in modo da flaggare correttamente come gestionali le righe generate.
Riferirsi alla documentazione della contabilità gestionale per tutti i settaggi della gestione.
- \*\*Sai come consolidare le registrazione ad una certa data senza stampare il \*\*

 :  : VOC Id="SKIA0410" Txt="Sai come consolidare le registrazione ad una certa data senza stampare il giornale definitivo?"
Nella tabella B£4 esiste un elemento \*CG denominato 'Consolidamento gestionale' nel quale impostare una data che, di fatto, blocca l'intervento sui movimenti contabili antecedenti ad essa, senza obbligare a stampare il giornale di contabilità in definitivo.
- \*\*Sai eseguire una chiusura di esercizio e riapertura al successivo?\*\*

 :  : VOC Id="SKIA0420" Txt="Sai eseguire una chiusura di esercizio e riapertura al successivo?"
Prima di tutto verificare che nella tabella C5U siano correttamente impostati gli elementi APEPA, CHIPA, CHIEC, PARUT, PARUP, PARPP e PARPE.
Poi, dal menu 'Chiusura periodo', eseguire l'opzione 'Registrazioni chiusura/apertura/risultato', selezionando l'esercizio da chiudere e le date alle quali generare i movimenti di chiusura e apertura. La funzione può essere immessa in batch, oppure in interattivo per verificare prima a video lo sviluppo dei saldi ed il calcolo del risultato, dopo di che una doppia conferma eseguirà le scritture previste.
- \*\*Sai come annullare la stampa definitiva del giornale se eseguita per error\*\*

 :  : VOC Id="SKIA0430" Txt="Sai come annullare la stampa definitiva del giornale se eseguita per errore?"
Tramite l'opzione 'Allinea progressivi' dalla gestione del giornale.
- \*\*Sai dove vengono memorizzati i progressivi del giornale di contabilità?\*\*

 :  : VOC Id="SKIA0440" Txt="Sai dove vengono memorizzati i progressivi del giornale di contabilità?"
Nei parametri aziendali.
- \*\*Sai dove vengono memorizzate le date di consolidamento dei vari argomenti \*\*

 :  : VOC Id="SKIA0450" Txt="Sai dove vengono memorizzate le date di consolidamento dei vari argomenti contabili?"
Nella tabella B£4.
- \*\*Sai come codificare e aprire un nuovo esercizio contabile?\*\*

 :  : VOC Id="SKIA0460" Txt="Sai come codificare e aprire un nuovo esercizio contabile?"
Nella tabella PER.
- \*\*Sai cosa si intende per esercizio in sovrapposizione?\*\*

 :  : VOC Id="SKIA0470" Txt="Sai cosa si intende per esercizio in sovrapposizione?"
Se si desidera stampare il giornale di contabilità fino al 31.12.xxxx, non sarà più possibile immettere successivamente registrazioni con data minore o uguale ad essa. Pertanto le registrazioni residue ancora di competenza di quell'esercizio vanno immesse con data successiva, ma indicando come esercizio di competenza quello appena stampato. Per fare questo, l'esercizio in questione deve essere posto in sovrapposizione, agendo sull'apposito flag nella tabella PER.
