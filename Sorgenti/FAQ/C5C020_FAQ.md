- **Come vanno trasmesse le note credito rettificative di movimenti già trasmessi**

 :  : VOC Id="10001" Txt="Come vanno trasmesse le note credito rettificative di movimenti già trasmessi?"

 Sui modelli predisposti dall'Agenzia delle Entrate è predisposto il riquadro 'Note di variazione di periodi precedenti' all'interno del quale, però, non è possibile indicare il segno. Pertanto pare opportuno evidenziare solo note di segno negativo, imputando quelle in aumento come nuove operazioni attive o passive (si veda Il sole 24 Ore del 02/11/10).

- **Come ci si deve comportare in caso di Rappresentanti Fiscali?**

 :  : VOC Id="10002" Txt="Come ci si deve comportare in caso di Rappresentanti Fiscali?"

 Nel caso in cui si eseguano operazioni con rappresentanti fiscali di soggetti passivi stabiliti in paesi Black List è necessario comunicare l'operazione anche nel caso in cui il rappresentante fiscale sia localizzato in un paese non Black List. Ipotizziamo, ad esempio, il caso di un trasportatore avente sede in Svizzera e con rappresentante fiscale francese. Anche nel caso in cui il servizio di trasporto venga fatturato dal rappresentante francese sarà necessario trasmettere l'operazione all'interno del modello Black List.
 Per risolvere la casistica è stata inserita l'estensione £42 - Soggetto economico rappresentato che dovà essere compilata sull'anagrafica del rappresentante fiscale. All'interno di questa estensione sarà necessario indicare il soggetto rappresentato.
 Nell'esempio fatto sopra sarà necessario procedere come segue : 
 * Codificare il soggetto economico svizzero
 * Codificare il soggetto francese (rappresentante fiscale) indicando nell'estensione £42 il codice dell'operatore svizzero.
 Fatto ciò il sistema determinerà la validità delle operazioni da trasmettere analizzando la nazione dell'ente riportato nell'estensione £42 e non quella del fornitore riportato sulla registrazione contabile.

- **Come ci si deve comportare in caso di identificazione diretta?**

 :  : VOC Id="10003" Txt="Come ci si deve comportare in caso di identificazione diretta?"

 Nel caso in cui la società intrattenga raporti con un operatore avente sede in paesi a fiscalità privilegiata ma con identificazione diretta in nazioni non Black List, è necessario comunicare le operazioni indicando nei dati anagrafici del quadro A come Codice IVA estero la Partita IVA con cui l'operatore è identificato 8e in genere con cui viene emessa la fattura), mentre come Codice Fiscale estero dovrà essere indicato il codice identificativo del soggetto Black List.
 Si sottolinea che nel caso in cui lo stesso soggetto Black List emetta fatture con diverse partite IVA poichè identificato in diverse nazioni dovrà essere compilato un quadro A per ciascuna delle partite IVA con cui vengono emesse le fatture.

- **Il file estratto deve avere una particolare nomenclatura/estensione?**

 :  : VOC Id="10004" Txt="Il file estratto deve avere una particolare nomenclatura/estensione?"

 Non è stata per ora indicata una specifica nomenclatura/estensione del file da trasmettere all'Agenzia delle Entrate. E', infatti, il software stesso dell'Agenzia che elaborando il primo record riconosce la tipologia di dati contenuti.

- **Dove vengono ripresi i dati dell'intermediario?**

 :  : VOC Id="10005" Txt="Dove vengono ripresi i dati dell'intermediario?"

 I dati dell'intermediario vengono letti all'interno dei parametri fissi aziendali.

- **Cosa sono e come vanno trasmesse le comunicazioni 'Correttive nei termini' e **

 :  : VOC Id="10006" Txt="Cosa sono e come vanno trasmesse le comunicazioni 'Correttive nei termini' e 'Integrative'?"

 Nel caso in cui vengano omessi uno o più record all'interno di una trasmissione è possibile inviare all'Agenzia delle Entrate una nuova comunicazione che sarà : 
 * Correttiva nei termini nel caso in cui si sia già provveduto all'invio di una comunicazione ma non sia ancora passata la scadenza di legge. Esempio :  il 20 Dicembre viene fatto un invio dei dati di Novembre e il 28 dicembre ci si accorge di aver omesso dei record sempre con data registrazione Novembre -> in questo caso sarà possibile inviare una comunicazione correttiva nei termini entro il 31 Dicembre.
 * Integrativa nel caso in cui ci si accorga di aver omesso dei record e sia già scaduto il termine di presentazione. Nell'esempio precedente, quindi, ci si accorge dell'omissione dei record dopo il 01 Gennaio.

 All'interno di SmeUP la tipologia di trasmissione viene indicata all'interno della funzione 'Trasmiss. Mov.IVA Black List' compilando il campo 'Tipo Elaborazione' che potrà essere vuoto per le normali trasmissioni, compilato con 1 per trasmissioni correttive e con 2 per trasmissioni integrative.

 Si sottolinea che in caso di comunicazione correttiva o integrativa vanno comunque trasmessi tutti i record del periodo e non solo quelli omessi.

- **Spesometro**

 :  : VOC Id="10007" Txt="Spesometro"

- **Quali sono gli step da seguire per effettuare la comunicazione?**

 :  : VOC Id="10008" Txt="Quali sono gli step da seguire per effettuare la comunicazione?"

 Il processo da seguire per effettuare la comunicazione è il seguente : 
 - Controllare l'anagrafica aziendale avendo particolare attenzione ai campi della Ragione sociale, partita IVA, codice fiscale, indirizzo mail e fax
 - Controllare i parametri fissi azienda avendo particolare attenzione ai campi codice attività, Rappresentante legale (tipo, codice e codice carica) e Intermediario (tipo e codice)
 - Controllare l'anagrafica del rappresentante legale
 - Controllare l'anagrafica di chi effettuerà la comunicazione (soggetto riportato come intermediario nei parametri fissi azienda)

 Per gli step successivi che riguardano la parametrizzazione necessaria all'esclusione di alcuni movimenti dallo spesometro si ricorda che il sistema effettua già automaticamente l'esclusione di : 
 * Corrispettivi
 * Movimenti di pura IVA
 * Assoggettamenti indicati come Fuori campo IVA e quindi non stampati sui registri IVA
 * Soggetti con nazione black list (anche se non viene effettuata la comunicazione dei movimenti black list con SmeUP)
 * Movimenti intrastat :  vengono esclusi solo nel caso in cui la singola registrazione contabile risulti come trasmessa all'interno dell'archivio dei movimenti intrastat (la ricerca viene effettuata proprio con il numero registrazione). Quindi se i dati intrastat non vengono comunicati con SmeUP sarà necessario agire sui codici IVA per ottenere l'esclusione dei movimenti
 * Movimenti intestati ad enti cha abbiano come codice nazione SM (San Marino)

 - Controllare la tabella dei codici IVA avendo premura di compilare i campi Esc.Elenco Clienti e/o Esc.Elenco Fornit. per tutti quegli assoggettamenti le cui operazioni non dovranno confluire nello spesometro
 - Controllare le anagrafiche di particolari soggetti per i quali le operazioni sono già comunicate in altro modo o non vadano in nessun caso comunicate (es. Fornitori pagati esclusivamente a mezzo carta di credito, fornitori di utenze elettriche, idriche e gas, contribuenti minimi, ecc.). In particolare per questi soggetti andrà gestita l'estensione £44 attraverso cui è possibile agire sia sull'estraibilità che sulla modalità di pagamento fissa che sull'informazione che si tratti di una società di noleggio/leasing

 Terminata la fase di controllo di base è possibile procedere con le tra azioni di elaborazione : 
 - Estrazione dei dati tramite la voce Ripresa   Mov. Spesometro
 - Eventuale manutenzione tramite la voce Gestione Mov. Spesometro
 - Creazione del file tramite la voce Trasmiss. Mov. Spesometro
 Per ognuna di queste funzioni è disponibile la relativa documentazione a cui potete accedere digitando F2 seguita da F1 nella videata di lancio della funzione stessa

- **Da dove vengono reperite le informazioni del Soggetto a cui si riferisce la c**

 :  : VOC Id="10009" Txt="Da dove vengono reperite le informazioni del Soggetto a cui si riferisce la comunicazione sul frontespizio del modulo?"

 I Dati del soggetto a cui si riferisce la comunicazione vengono lette dal contatto Azienda da cui si effettua l'estrazione dei dati. Quindi se estrarrò i dati dello spesometro collegandomi all'ambiente dell'azienda 01 il sistema leggerà queste informazioni dai dati di base dell'azienda 01.
 Per manutenerli basta andare nei dati di base del modulo della contabilità e scegliere Anagrafica azienda nel menù 'Azienda'.

- **Da dove vengono reperite le informazioni del Soggetto che assume l'impegno al**

 :  : VOC Id="10010" Txt="Da dove vengono reperite le informazioni del Soggetto che assume l'impegno alla presentazione telematica sul frontespizio del modulo?"

 I dati di questo soggetto sono determinati leggendo nei parametri fissi azienda il codice dell'intermediario. Quindi se all'interno dei parametri fissi azienda il Tipo Contatto Interme è compilato con FOR e il Cod. Intermediario con 12345 il sistema leggerà e inserirà il codice fiscale del fornitore 12345.

- **Da dove vengono reperite le informazioni del Soggetto tenuto alla comunicazio**

 :  : VOC Id="10011" Txt="Da dove vengono reperite le informazioni del Soggetto tenuto alla comunicazione sul frontespizio del modulo?"

 I dati di questo soggetto sono determinati leggendo nei parametri fissi azienda il codice del rappresentante legale. Quindi se all'interno dei parametri fissi azienda il Tipo Rappr.Legale è compilato con COL e il Cod. Rappr.Legale con ABCD il sistema leggerà e inserirà le informazioni riportate sull'anagrafica del collaboratore ABCD. Anche il codice della carica è definito all'interno dei parametri fissi aziendali.

- **Come ci si deve comportare in caso di operazioni straordinarie (fusioni, inco**

 :  : VOC Id="10012" Txt="Come ci si deve comportare in caso di operazioni straordinarie (fusioni, incorporazioni, ecc.)?"

 In caso di fusioni, incorporazioni, ecc. il codice fiscale da indicare sul frontespizio della comunicazione è quello del soggetto attivo al momento dell'invio mentre all'interno del riquadro del soggetto a cui si riferisce la comunicazione andranno indicati gli estremi della società estinta.
 Se ad esempio Alfa SpA incorpora Beta Srl, la comunicazione andrà effettuata indicando come Codice fiscale intestatario quello di Alfa SpA mentre all'interno del riquadro 'Dati del soggetto cui si riferisce la comunicazione' andranno riportate le informazioni di Beta Srl.
 Per ottenere questo risultato in SmeUP sarà necessario collegarsi all'ambiente dell'azienda Beta srl (che probabilmente non sarà più utilizzato al momento dell'estrazione), effettuare tutte le estrazioni ed elaborazioni di dati all'interno di questo ambiente e quindi lanciare la trasmissione dei movimenti compilando il campo 'Codice Fiscale' con il codice fiscale di Alfa SpA

- **Come posso scegliere tra forma analitica e forma aggregata?**

 :  : VOC Id="10013" Txt="Come posso scegliere tra forma analitica e forma aggregata?"

 Il default all'interno di SmeUP è la trasmissione dei dati in forma analitica. Per ottenere la forma aggregata sarà sufficiente compilare il campo Dati Aggregati con 1=Sì all'interno della funzione di Trasmissione

- **Come posso escludere le importazioni/esportazioni?**

 :  : VOC Id="10014" Txt="Come posso escludere le importazioni/esportazioni?"

 Agendo sui campi Esc.Elenco Clienti e/o Esc.Elenco Fornit.  dei codici assoggettamento utilizzati

- **Come posso escludere i movimenti Intrastat?**

 :  : VOC Id="10015" Txt="Come posso escludere i movimenti Intrastat?"

 Se effettuate la comunicazione dei modelli attraverso le funzioni di SmeUP l'esclusione verrà già effettuata automaticamente per tutte quelle registrazioni che risultano nell'archivio movimenti Intrastat. In caso contrario sarà necessario agire sui campi Esc.Elenco Clienti e/o Esc.Elenco Fornit.  dei codici assoggettamento utilizzati

- **Come devo comportarmi con le operazioni con San Marino?**

 :  : VOC Id="10016" Txt="Come devo comportarmi con le operazioni con San Marino?"

 A partire dal 11/03/2014 (data in cui San Marino è stata esclusa dall'elenco delle nazioni black list) l'acquisto da un operatore sanmarinese con applicazione dell'Iva va incluso nello spesometro in quanto rilevante ai fini del tributo e non oggetto di separata comunicazione.
 Le prestazioni di servizio generiche effettuate nei confronti di operatori economici sanmarinesi provvisti di coidce identificativo IVA si considerano territorialmente rilevanti nel paese del committente e, quindi, dovrebbero essere escluse dallo spesometro. Fonte :  "L'esperto risponde" - Sole24Ore del 01/06/2015

- **Come posso escludere i movimenti fuori campo IVA?**

 :  : VOC Id="10017" Txt="Come posso escludere i movimenti fuori campo IVA?"

 Agendo sui campi Esc.Elenco Clienti e/o Esc.Elenco Fornit.  dei codici assoggettamento utilizzati oppure verificando che il campo 'Fuori Campo' all'interno dell'assoggettamento stesso sia impostato.

- **Come devo comportarmi con le Schede Carburante?**

 :  : VOC Id="10018" Txt="Come devo comportarmi con le Schede Carburante?"

 Dipende da come avviene l'acquisto : 
 * Se l'acquisto avviene tramite carta di credito il movimento non andrà comunicato. Pertanto laddove la scheda carburante venga registrata come movimento IVA su un generico fornitore 'Scheda carburante' si dovrà procedere impostando sull'anagrafica di questo fornitore nell'estensione £44 il campo Da Non Trasmettere=1 sì
 * Se l'acquisto non avviene tramite carta di credito il movimento andrà estratto e comunicato. Si tratta di una comunicazione di tipo riepilogativo non essendo il soggetto 'SCHEDA CARBURANTE'dotato di dati identificativi quali codice fiscale e partita IVA. Quindi si dovrà procedere all'inserimento manuale di un record dal menù della gestione movimenti spesometro. All'interno di questo record andrà indicato l'importo totale delle transazioni e dovrà essere impostatomanualmente il campo 'Documento Riepilogativo'

- **Come devo comportarmi con le Note di variazione?**

 :  : VOC Id="10019" Txt="Come devo comportarmi con le Note di variazione?"

 Nel momento in cui viene redatta questa documentazione permane ancora una richiesta di chiarimenti da parte dell'Agenzia delle Entrate in merito al trattamento delle note di variazione.
 In particolare, la possibilità di indicare un segno negativo sembra prevista (anche se non espressamente indicata nella struttura del record) solo nei riquadri NR e NE dedicati proprio alle note di variazione nel caso in cui si effettui la comunicazione in forma analitica. Analoga possibilità non è invece prevista nel riquadro FA da utilizzarsi in caso di forma aggregata. In tale riquadro per le operazioni attive il campo 10 parla di note a debito della controparte e per le operazioni passive il campo 15 parla di note a credito per la controparte.
 In attesa di un chiarimento SmeUP ha deciso di conformarsi al comportamento adottato da Assosoftware e consigliato anche dalla stampa specialistica secondo cui per le operazioni attive la nota di variazione è indicata nel campo 15 mentre per gli acquisti la nota di variazione è indicata nel campo 10.
 All'utente, in ogni caso, non è richiesta alcuna attività di riconciliazione o completamento.

- **Come devo comportarmi con gli omaggi?**

 :  : VOC Id="10020" Txt="Come devo comportarmi con gli omaggi?"

 Nel caso in cui l'omaggio riguardi la sola parte del corrispettivo e venga emessa al cliente regolare fattura con evidenza di imponibile ed IVA l'operazione andrà comunicata come una qualsasi altra cessione. Se invece si adotta il sistema dell'autofattura poichè non vi è rivalsa sul cessionario, all'interno dello spesometro andrà comunicata la partita IVA del cedente e compilato il flag di Autofattura. Il software compila in automatico questo campo laddove verifichi che la partita iva dell'intestatario del documento è uguale alla partita IVA dell'azienda.

- **Come devo comportarmi con i leasing?**

 :  : VOC Id="10021" Txt="Come devo comportarmi con i leasing?"

 Le istruzioni del modello prevedono per i soggetti utilizzatori di beni in leasing o in noleggio permane l'obbligo di comunicazione nello spesometro.
 Il campo "Noleggio Leasing" va valorizzato con una delle  lettere previste dal modello e corrispondenti alla tipologia del veicolo dato a noleggio. Per questo motivo è stato implementato sull'anagrafica dei soggetti all'interno dell'estensione £44 il flag relativo al noleggio e leasing (con i suoi possibili valori). L'utente dovrà quindi preoccuparsi di completare questa informazione laddove abbia fornitori di beni in leasing/noleggio.

- **Come devo comportarmi con gli acquisti in Reverse Charge (es. acquisti di rot**

 :  : VOC Id="10022" Txt="Come devo comportarmi con gli acquisti in Reverse Charge (es. acquisti di rottami, materiali ferrosi, ecc.)?"

 Le fatture assoggettate al meccanismo dell'inversione contabile (reverse charge) vanno indicate nel quadro FR-fatture ricevute barrando il campo 6  (reverse charge). L'imponibile e l'imposta vanno specificati nei campi 8 e 9 del medesimo quadro FR. In SmeUP questa compilazione si ottiene  impostando all'interno dell'assoggettamento IVA il campo Reverse Charge a 1.

- **Come devo comportarmi con i servizi da fornitori ExtraCEE per i quali è stata**

 :  : VOC Id="10023" Txt="Come devo comportarmi con i servizi da fornitori ExtraCEE per i quali è stata emessa autofattura?"

 Secondo la nota 0136693 del 19 Novembre 2013 dell'Agenzia delle Entrate in caso di compilazione dal modello per dati analitici l'operazione andrà indicata alternativamente nel quadro SE "Acquisti di servizi da non residenti" se l'impresa è in possesso dei dati identificativi del soggetto non residente oppure nel quadro FR "Fatture ricevute" se il documento ricevuto non contiene tutti i predetti dati (in tale ultima circostanza andrà barrata la casella Autofattura ed indicata quale partita Iva quella dell'impresa italiana) e nel quadro FE "Fatture emesse" barrando la casella Autofattura.
 Diversamente, qualora il contribuente scelga di presentare i dati in modalità aggregata sarà tenuto a compilare il quadro BL "Operazioni con soggetti non residfenti in modalità aggregata" unitamente al quadro FA "Operazioni documentate da fattura esposte in forma aggregata" oppure solo il quadro FA in mancanza dei dati identificativi del soggetto non residente.
 Fonte :  L'Esperto Risponde - Il Sole24Ore del 04/07/16
- **Sai quali sono le operazioni Black List? Quali categorie coinvolgono?**

 :  : VOC Id="SKIA0010" Txt="Sai quali sono le operazioni Black List? Quali categorie coinvolgono?"
Si/No.
- **Sai come capire se una nazione è Black List? In quale tabella è impostato?**

 :  : VOC Id="SKIA0020" Txt="Sai come capire se una nazione è Black List? In quale tabella è impostato?"
Nella tabella V§N (codici Nazioni).
- **Sai come e dove attribuire la natura operazione per la Black List?**

 :  : VOC Id="SKIA0030" Txt="Sai come e dove attribuire la natura operazione per la Black List?"
Nei parametri del conto (tabella C5B).
- **Sai come vengono gestite le Note di Variazione per la Black List?**

 :  : VOC Id="SKIA0040" Txt="Sai come vengono gestite le Note di Variazione per la Black List?"
Si/No.
- **Sai cosa si deve fare nel caso di operazioni legate a Rappresentanti fisca**

 :  : VOC Id="SKIA0050" Txt="Sai cosa si deve fare nel caso di operazioni legate a Rappresentanti fiscali di soggetti Black List?"
Si/No.
- **Sai dove vanno inseriti i dati dell'intermediario della comunicazione Blac**

 :  : VOC Id="SKIA0060" Txt="Sai dove vanno inseriti i dati dell'intermediario della comunicazione Black List?"
Nei parametri azienda.
- **Sai quali sono i file coinvolti per la gestione e trasmissione Black List?**

 :  : VOC Id="SKIA0070" Txt="Sai quali sono i file coinvolti per la gestione e trasmissione Black List?"
I dati estratti dalle registrazioni contabili vengono scritti nel C5MBLA0F e poi eventualmente elaborati.
- **Sai con quale periodicità si può presentare il modello Black List?**

 :  : VOC Id="SKIA0080" Txt="Sai con quale periodicità si può presentare il modello Black List?"
Mensile o trimestrale.
- **Sai qual è la scadenza per la trasmissione delle comunicazioni Black List?**

 :  : VOC Id="SKIA0090" Txt="Sai qual è la scadenza per la trasmissione delle comunicazioni Black List?"
L'ultimo giorno del mese per la dichiarazione del mese precedente.
- **Sai cos'è una comunicazione integrativa ed entro quando deve essere fatta?**

 :  : VOC Id="SKIA0100" Txt="Sai cos'è una comunicazione integrativa ed entro quando deve essere fatta?"
E' il sistema di regolarizzazione degli errori commessi in sede di prima trasmissione delle comunicazioni black list, tramite appunto l'invio di una comunicazione integrativa da presentare entro l'ultimo giorno del mese successivo alla scadenza del termine per la presentazione della comunicazione originaria.
- **In fase di trasmissione movimenti Black List, sai quali sono i vari tipi d**

 :  : VOC Id="SKIA0110" Txt="In fase di trasmissione movimenti Black List, sai quali sono i vari tipi di elaborazione che possono essere fatti?"
Invio ordinario nei termini, correttivo nei termini e invio integrativo.
- **Sai cos'è il PRO-RATA?**

 :  : VOC Id="SKIA0120" Txt="Sai cos'è il PRO-RATA?"
Il pro-rata è la percentuale di detrazione dell'IVA acquisti da applicare nel caso siano presenti vendite che non danno diritto a detrazione (art. 19/bis). Tale percentuale viene determinata una volta l'anno in funzione delle operazioni eseguite l'anno precedente.
- **Sai quali sono le principali tabelle legate alla gestione IVA?**

 :  : VOC Id="SKIA0130" Txt="Sai quali sono le principali tabelle legate alla gestione IVA?"
Si/No.
- **Sai dove viene associato il registro IVA ad un operazione?**

 :  : VOC Id="SKIA0140" Txt="Sai dove viene associato il registro IVA ad un operazione?"
Nella tabella C5D (tipi registrazioni).
- **Sai se è possibile impostare automaticamente l'assoggettamento IVA ad una **

 :  : VOC Id="SKIA0150" Txt="Sai se è possibile impostare automaticamente l'assoggettamento IVA ad una registrazione contabile?"
Nell'anagrafica ente è possibile codificare il codice IVA preferenziale.
Nei parametri del tipo registrazione (tabella C5D) è possibile codificare un codice IVA di default.
- **Sai da dove vengono salvate le date particolari di ultima stampa registri **

 :  : VOC Id="SKIA0160" Txt="Sai da dove vengono salvate le date particolari di ultima stampa registri IVA e liquidazione IVA?"
Nella tabella B£4 (date aziendali).
- **Sai quali parametri azienda devono necessariamente essere impostati in fas**

 :  : VOC Id="SKIA0170" Txt="Sai quali parametri azienda devono necessariamente essere impostati in fase di installazione IVA?"
Nei parametri azienda vanno impostati : 

- Period/Giorno Liq.IVA
- % Interesse Liquidazi
- Azienda Compens.IVA
- Dati Integr.Reg.IVA
- Sintesi Reg.Riep.IVA
- Plafond Mobile
- % Pro-Rata
- Cessione Credito IVA
- Plafond in Liq.IVA
- **In fase di passaggio da un'altro gestionale, sai come impostare il credito**

 :  : VOC Id="SKIA0180" Txt="In fase di passaggio da un'altro gestionale, sai come impostare il credito/debito IVA affinchè venga considerato all'atto della prima liquidazione con il nuovo sistema?"
Entrando in gestione nell'archivio riepiloghi IVA ed immettendo un record di tipo 'RP'.
- **Sai cos'è il plafond IVA?**

 :  : VOC Id="SKIA0190" Txt="Sai cos'è il plafond IVA?" Als="comm"
Si/No.
- **Sai quali sono le modalità di stampa registri IVA?**

 :  : VOC Id="SKIA0200" Txt="Sai quali sono le modalità di stampa registri IVA?"
Si possono stampare n volte in provvisorio, una volta in definitivo e n volte in copia.
- **Sai se e come è possibile annullare una stampa definitiva registri IVA su **

 :  : VOC Id="SKIA0210" Txt="Sai se e come è possibile annullare una stampa definitiva registri IVA su un periodo?"
Utilizzando l'opzione 'Allinea progressivi' presente nel menu di gestione IVA.
- **Sai se è possibile che la liquidazione IVA abbia dei riferimenti propri, c**

 :  : VOC Id="SKIA0220" Txt="Sai se è possibile che la liquidazione IVA abbia dei riferimenti propri, cioè non venga accodata come numerazione pagine ad un registro?"
Non indicando il parametro 'Registro di riferimento' nei filtri a video della stampa liquidazione.
- **Sai cosa succede nel caso in cui viene lanciata una stampa registri e vi s**

 :  : VOC Id="SKIA0230" Txt="Sai cosa succede nel caso in cui viene lanciata una stampa registri e vi siano degli errori?"
Se è stato scelto di eseguire il controllo errori l'elaborazione della stmpa si blocca e viene emessa una stampa di log che spiega quali errori sono presenti e su che registri.
Se invece è stata fatta una forzatura rinunciando al controllo errori la stampa registri esce comunque.
- **Sai come si può stampare la liquidazione IVA in coda ad un altro registro?**

 :  : VOC Id="SKIA0240" Txt="Sai come si può stampare la liquidazione IVA in coda ad un altro registro?"
Indicando il registro di riferimento nei filtri di selezione della stampa liquidazione.
- **Sai se è possibile avvalersi di prefincati personali nella stampa registri**

 :  : VOC Id="SKIA0250" Txt="Sai se è possibile avvalersi di prefincati personali nella stampa registri e liquidazione IVA?"
Si/No.
- **Sai interrogare e analizzare il plafond?**

 :  : VOC Id="SKIA0260" Txt="Sai interrogare e analizzare il plafond?"
Si/No.
- **Sai in quale tabella viene annotato il numero dell'ultima pagina stampata **

 :  : VOC Id="SKIA0270" Txt="Sai in quale tabella viene annotato il numero dell'ultima pagina stampata sul registro IVA?"
Nella tabella C5R (registri IVA).
- **Sai in quali modi è possibile capire se una registrazione contabile fa par**

 :  : VOC Id="SKIA0280" Txt="Sai in quali modi è possibile capire se una registrazione contabile fa parte di un periodo IVA già chiuso?"
Se in modifica i dati di testata risultano protetti.
- **Sai come fare a stabilire se una registrazione andrà o meno a concorrere a**

 :  : VOC Id="SKIA0290" Txt="Sai come fare a stabilire se una registrazione andrà o meno a concorrere alla determinazione del plafond?"
In base al flag di gestione plafond impostato sul codice IVA utilizzato per la registrazione.
- **Sai quali sono le impostazioni da applicare per gestire dei documenti con **

 :  : VOC Id="SKIA0300" Txt="Sai quali sono le impostazioni da applicare per gestire dei documenti con IVA ad esigibilità differita?"
Si/No.
- **Sai cosa si deve predisporre per ottenere delle registrazioni la cui IVA f**

 :  : VOC Id="SKIA0310" Txt="Sai cosa si deve predisporre per ottenere delle registrazioni la cui IVA finisca sia sul registro acquisti che sul registro vendite (REVERSE CHARGE)?"
Si/No.
- **Sai cos'è un autofattura?**

 :  : VOC Id="SKIA0320" Txt="Sai cos'è un autofattura?"
Si/No.
- **Sai quali sono le caratteristiche che deve avere una registrazione di acqu**

 :  : VOC Id="SKIA0330" Txt="Sai quali sono le caratteristiche che deve avere una registrazione di acquisto per essere collegata al documento di autofattura?"
Si/No.
- **Sai come si può escludere un assoggettamento IVA dalla stampa dei registri**

 :  : VOC Id="SKIA0340" Txt="Sai come si può escludere un assoggettamento IVA dalla stampa dei registri IVA?"
Impostando il flag 'Fuori campo IVA' sul codice IVA.
- **Sai su quale data ragiona il calcolo e la stampa dei registri IVA?**

 :  : VOC Id="SKIA0350" Txt="Sai su quale data ragiona il calcolo e la stampa dei registri IVA?"
Sulla data competenza IVA.
- **Sai su quale data invece ragiona il Registro Riepilogativo e la Liquidazio**

 :  : VOC Id="SKIA0360" Txt="Sai su quale data invece ragiona il Registro Riepilogativo e la Liquidazione IVA?"
Sulla data registrazione.
- **Sai se è possibile stampare parzialmente i registri IVA?**

 :  : VOC Id="SKIA0255" Txt="Sai se è possibile stampare parzialmente i registri IVA?"
Si/No.
- **Sai se è possibile chiudere definitivamente uno o alcuni registri IVA?**

 :  : VOC Id="SKIA0259" Txt="Sai se è possibile chiudere definitivamente uno o alcuni registri IVA?"
Si/No.
- **E' possibile e come si fa ad escludere un operazione IVA dalla spesometro?**

 :  : VOC Id="SKIA0370" Txt="E' possibile e come si fa ad escludere un operazione IVA dalla spesometro?"
Agendo sui due flag dedicati presenti nel codice IVA per escludere il codice dagli elenchi.
- **Sai quali file sono coinvolti nella gestione spesometro?**

 :  : VOC Id="SKIA0380" Txt="Sai quali file sono coinvolti nella gestione spesometro?"
Dopo l'estrazione dalle registrazioni viene scritto il file C5MCIV0F per essere eventualmente elaborato.
- **Sai quali dati obbligatori si devono inserire nell'anagrafica enti inerent**

 :  : VOC Id="SKIA0390" Txt="Sai quali dati obbligatori si devono inserire nell'anagrafica enti inerenti alla gestione dello spesometro?"
Oltre ai dati anagrafici completi c'è un'estensione utile a parametrizzare l'esclusione dell'ente dallo spesometro, come pure il tipo di pagamento da associare ai record eventualmente estratti.
- **Sai se è possibile escludere uno o più enti dalla gestione spesometro?**

 :  : VOC Id="SKIA0400" Txt="Sai se è possibile escludere uno o più enti dalla gestione spesometro?"
Si/No.
- **Sai quali tipi di invio sono a disposizione per lo spesometro e qual è la **

 :  : VOC Id="SKIA0410" Txt="Sai quali tipi di invio sono a disposizione per lo spesometro e qual è la loro funzione?"
L'invio ordinario, l'invio sostitutivo e l'annullamento invio.
- **Sai quali stampe sono state predisposte per aiutare l'utente ad analizzare**

 :  : VOC Id="SKIA0420" Txt="Sai quali stampe sono state predisposte per aiutare l'utente ad analizzare le inclusioni ed esclusioni dallo spesometro?"
Durante l'estrazione dei dati dalle registrazioni vengono preparate delle stampe che segnalano l'ammontare dei dati analizzati, l'elenco dei dati esclusi da estrazione e l'ammontare suddiviso per mese/registro IVA/codice IVA delle inclusioni e delle esclusioni.
- **Sai come le note di variazione vengono collegate dal sistema alle fatture **

 :  : VOC Id="SKIA0430" Txt="Sai come le note di variazione vengono collegate dal sistema alle fatture nella gestione spesometro?"
Si/No.
- **Sai come è possibile associare una nota di variazione ad una fattura nella**

 :  : VOC Id="SKIA0440" Txt="Sai come è possibile associare una nota di variazione ad una fattura nella gestione spesometro?"
In manutenzione sulla nota credito, immettendo i riferimenti a una o più fatture per ogni riga di imponibile presente.
- **Sai quali campi si possono modificare su una registrazione il cui periodo **

 :  : VOC Id="SKIA0450" Txt="Sai quali campi si possono modificare su una registrazione il cui periodo IVA è già stato chiuso definitivamente?"
Contropartite, rate e note.
- **Sai ottenere una situazione IVA da versare/a credito ad una data senza dov**

 :  : VOC Id="SKIA0460" Txt="Sai ottenere una situazione IVA da versare/a credito ad una data senza dover stampare il registro IVA?"
Interrogando i matrini dei conti IVA, oppure utilizzando le liste di analisi movimenti IVA attivi e passivi, oppure stampando una liquidazione IVA.
- **Sai come viene alimentato il plafond IVA?**

 :  : VOC Id="SKIA0195" Txt="Sai come viene alimentato il plafond IVA?"
Dalle registrazioni di vendita dell'esercizio precedente eseguite con codici IVA su cui è acceso il flag apposito.
- **Sai come viene calcolato il residuo del plafond IVA?**

 :  : VOC Id="SKIA0196" Txt="Sai come viene calcolato il residuo del plafond IVA?"
Detraendo al plafond iniziale (proveniente dall'esercizio precedente) tutti i movimenti di acquisto eseguiti con determinati codici IVA su cui è acceso l'apposito flag.
- **In caso di errori su un registro IVA, sai se è possibile procedere comunqu**

 :  : VOC Id="SKIA0237" Txt="In caso di errori su un registro IVA, sai se è possibile procedere comunque a stampare il dettaglio del registro?"
Si, forzando la stampa senza eseguire il controllo errori.
- **Sai se è possibile generare un documento di autofattura in Smeup a partire**

 :  : VOC Id="SKIA0327" Txt="Sai se è possibile generare un documento di autofattura in Smeup a partire dalla registrazione contabile della fattura di acquisto?"
Si/No.
- **Sai ottenere dal sistema le informazioni necessarie per compilare la dichi**

 :  : VOC Id="SKIA0470" Txt="Sai ottenere dal sistema le informazioni necessarie per compilare la dichiarazione IVA annuale?"
Si/No.
- **Dato un numero protocollo IVA, attraverso le interrogazioni proposte dal m**

 :  : VOC Id="SKIA0480" Txt="Dato un numero protocollo IVA, attraverso le interrogazioni proposte dal modulo contabilità, sai risalire alla registrazione contabile?"
Si/No.
- **Sai navigare sui dati IVA attraverso le schede LOOCUP?**

 :  : VOC Id="SKIA0490" Txt="Sai navigare sui dati IVA attraverso le schede LOOCUP?"
Si/No.
