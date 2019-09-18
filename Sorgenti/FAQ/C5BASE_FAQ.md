- \*\*Come gestire gli ambienti paralleli di produzione e di test?\*\*

 :  : VOC Id="10001" Txt="Come gestire gli ambienti paralleli di produzione e di test?"
 Non è possibile testare le conversioni nell' ambiente di produzione perchè tabelle fondamentali come la
 B£1 PAG IVA C5B sono deviate in ambiente ACG.
 E' necessario dunque creare un ambiente parallelo dove testare le conversioni e continuare ad allineare le tabelle
 nell'ambiente di test e nell'ambiente di produzione ad eccezione di quelle deviate.
 Solo in fase di partenza sarà possibile allineare anche queste ultime.
 Nella maggior parte dei casi le tabelle interessate sono : 
 \* B£1
 \* VAL
 \* PAG
 \* IVA
 \* C5B
 \* BAN
 \* AGE

- \*\*Non trova elementi in tabella?\*\*

 :  : VOC Id="10002" Txt="Non trova elementi in tabella?"
 E' possibile che elementi di tabella non vengano trovati nel relativo sottosettore.
 E' necessario verificare gli eventuali sottosettori esistenti e controllare la metodologia di risalita
 definita nalla definizione di tale tabella con sottosettore 'bianco' secondo la documentazione 'Definizione tabelle'.

- \*\*Con che logica definire gli esercizi?\*\*

 :  : VOC Id="10003" Txt="Con che logica definire gli esercizi?"
 Es. Data di impostazione esercizio :  30/09/2001

 Caso 1 :  ho già generato per l'anno 2000 le registrazioni di chiusura/riapertura
 Nella tabella PER dovrò indicare le seguenti : 
 Stato periodo anno 2000 = 'C' Chiuso;.
 Stato periodo anno 2001 'A' Attivo.

 Caso 2 :  non ho ancora generato per l'anno 2000 le registrazioni di chiusura/riapertura
 Nella tabella PER dovrò indicare le seguenti : 
 Stato periodo anno 2000 = 'S' In Sovrapposizione;
 Stato periodo anno 2001 'A' Attivo.

- \*\*Ci sono differenze tra partitario e scadenzario?\*\*

 :  : VOC Id="10004" Txt="Ci sono differenze tra partitario e scadenzario?"
 La differenza è giustificata dal fatto che : 
 \* l'analisi del partitario prende in considerazione sia eventi già verificatisi (pagamenti parziali su partite aperte) sia eventi ancora da verificarsi (rate aperte) per cui media qualcosa già successo con qualcosa ancora da verificarsi;
 \* l'analisi dello scadenzario considera soltanto eventi futuri, per cui, non guardando mai al passato, ignora fattori presenti invece nel partitario.

- \*\*Perchè dopo il lancio della creazione l'elaborazione va subito in errore?\*\*

 :  : VOC Id="10005" Txt="Perchè dopo il lancio della creazione l'elaborazione va subito in errore?"
 L'errore può essere dovuto alla composizione della tabella PER, che deve contenere solo gli elementi dei mesi e degli
 anni che possibilmente dovrebbero essere stati creati tramite la funzione MAN/CRE della £PE8.

- \*\*Perchè scrive le rate nel C5BATC, ma non le applica e se applico manualmente \*\*

 :  : VOC Id="10006" Txt="Perchè scrive le rate nel C5BATC, ma non le applica e se applico manualmente vanno?"
 Controllare che l'ambiente di contabilizzazione nella tabella V51 corrisponda all'azienda delle fatture che si stanno contabilizzando.

- \*\*Cosa devo fare se il bilancio di verifica riporta saldi di mastro clienti/for\*\*

 :  : VOC Id="10007" Txt="Cosa devo fare se il bilancio di verifica riporta saldi di mastro clienti/fornitori diverso dalla somma dei clienti/fornitori fornita dall'allegato di bilancio?"
 Effettuare le seguenti ricerche : 
 1. verificare che nel dettaglio dei clienti/fornitori riportato dal bilancio di verifica non ci siano enti senza descrizione. In tal caso l'ente è stato
 cancellato fisicamente dal BRENTI0F. Questo comporta che nell'allegato il saldo ci sia e nel bilancio no.
 2. verificare che non ci siano registrazioni con ente valorizzato e conto \*blanks
 3. verificare che non ci siano registrazioni con mastro valorizzato e ente \*blanks

- \*\*Quali sono le analisi da fare per verificare la localizzazione in un ambiente\*\*

 :  : VOC Id="10008" Txt="Quali sono le analisi da fare per verificare la localizzazione in un ambiente straniero?"

 \*Esistono comunicazioni strutturate via Internet?
 \*\*La fatturazione dipende da un Sito Statale
 \*Vincoli in fase di registrazione
 \*\*Obbligo sequenzialità date registrazione?
 \*\*Obbligo di riportare i valori in valute diverse da quella nazionale e da quella nell'eventuale valuta del documento?
 \*\*Informazioni particolari obbligatorie all'interno della registrazione
 \*IVA
 \*\*Comunicazioni da presentare
 \*\*Periodicità presentazione (mensile, trimestrale, annuale)
 \*\*Modalità di presentazione (cartacea, tramite file, ecc.)
 \*Bilanci
 \*\*Forme di presentazione (es. bilancio CEE, bilanci in valute diverse da quella nazionale, ecc.)
 \*\*Periodicità di chiusura dei dati di bilancio
 \*\*Modalità di presentazione (cartacea, tramite file, ecc.)
 \*Procedure di chiusura periodica
 \*\*Periodicità delle chiusure
 \*\*Scritture da lanciare in fase di chiusura (es. valorizzazioni differenze cambio, fatture da ricevere, registrazione ratei/risconti, ecc.)
 \*\*Dati da presentare relativi alla chiusura dell'esercizio (es. movimentazione dei conti, elenco dettagliato delle registrazioni contabili, ecc.)
 \*Contabilità magazzino
 \*\*Obbligo tenuta?
 \*\*Periodicità di rilevazione
 \*\*Modalità rilevazione e contabilizzazione valori
 \*Flussi di cassa
 \*\*Obbligo tenuta/presentazione?
 \*\*Modalità tenuta/presentazione
 \*Immobilizzazioni
 \*\*Modalità di calcolo della quota di ammortamento
 \*\*Forme di tenuta/presentazione
 \*\*Stampe/Esportazioni obbligatorie

- \*\*Sai quali sono i passi di installazione da seguire per preparare l'ambient\*\*

 :  : VOC Id="SKIB0010" Txt="Sai quali sono i passi di installazione da seguire per preparare l'ambiente di contabilità?"
Se possibile caricare il modello, che è già un ambiente funzionante, poi se deve essere fatta una conversione il contenuto di alcune tabelle verrà sostituito dai valori convertiti.
Riferirsi alla documentazione attiva 'Passi di installazione' per avere un tracciato da seguire se serve fare una panoramica sui settaggi minimi.
- \*\*Sai come recuperare il file delle banche ABI-CAB per aggiornare l'anagrafi\*\*

 :  : VOC Id="SKIB0020" Txt="Sai come recuperare il file delle banche ABI-CAB per aggiornare l'anagrafica banche?"
Nella libreria SMEDEV è presente un savf denominato C5BANCTF, che contiene una versione più o meno aggiornata del file CBI relativo agli sportelli bancari.
Dopo averlo ripristinato, una apposita funzione nella gestione enti denominata 'Ripresa ABI CAB da esterno' ne consente il controllo di presenza ed eventualmente l'aggiornamento nel file enti.
- \*\*Sai come configurare i tipi di enti più comuni?\*\*

 :  : VOC Id="SKIB0030" Txt="Sai come configurare i tipi di enti più comuni?"
Nella tabella BRE.
- \*\*Sai quali tabelle andrebbero gestite con sottosettore in una contabilità m\*\*

 :  : VOC Id="SKIB0040" Txt="Sai quali tabelle andrebbero gestite con sottosettore in una contabilità multiaziendale?"
In generale si potrebbe dire che tutte le tabelle C5\* (specializzate per la contabilità) andrebbero gestite con il sottosettore. Tuttavia, molto spesso, alcune di esse possono essere lasciate senza e quindi assunte come comuni a tutte le aziende. Di certo si potrebbe dire che tabella come il piano dei conti, le banche aziendali, i rapporti bancari, i registri IVA, le causali, le registrazioni automatiche, proprio perchè contenenti codifiche diverse per azienda, andrebbero sempre separate con il sottosettore.
- \*\*Sai come configurare la struttura del piano dei conti?\*\*

 :  : VOC Id="SKIB0050" Txt="Sai come configurare la struttura del piano dei conti?"
La tabella C5M consente la configurazione della struttura a livelli del piano dei conti, in seguito si codificheranno le tabelle C5NBA per i livelli sopra i conti e C5B per i conti contabili.
- \*\*Sai come si collega un cliente/fornitore al piano dei conti?\*\*

 :  : VOC Id="SKIB0060" Txt="Sai come si collega un cliente/fornitore al piano dei conti?"
Nella codifica del piano dei conti (tabella C5B) è possibile definire il tipo contatto a cui eventualmente collegare il conto stesso.
- \*\*Sai a cosa serve la tabella C5U?\*\*

 :  : VOC Id="SKIB0070" Txt="Sai a cosa serve la tabella C5U?"
Serve a codificare tutti i settaggi che regolano gli automatismi presenti nei programmi, con delle combinazioni causale/conto ricondotte alla tipologia di operazione da svolgere.
- \*\*Sai impostare un ambiente di conversione funzionante?\*\*

 :  : VOC Id="SKIB0080" Txt="Sai impostare un ambiente di conversione funzionante?"
Oltre a caricare il modello standard, se possibile, utilizzare le tabelle B£H e B£J per codificare passi di flusso da eseguire per eseguire i programmi di conversione.
- \*\*Sai come schedulare le varie operazioni da eseguire per eseguire una conve\*\*

 :  : VOC Id="SKIB0090" Txt="Sai come schedulare le varie operazioni da eseguire per eseguire una conversione?"
Per schedulare in batch le conversioni, chiamare il B£CONV con due parametri :  nel primo va indicato il gruppo azioni che si vuole eseguire (in questo caso verranno eseguite tutte le azioni del flusso che non hanno impostato il campo attivazione a "N"); il secondo parametro va invece lasciato blank.
- \*\*Sai quali controlli vanno eseguiti per controllare la correttezza e quadra\*\*

 :  : VOC Id="SKIB0100" Txt="Sai quali controlli vanno eseguiti per controllare la correttezza e quadratura di una conversione?"
Il bilancio di verifica deve essere identico a quello prodotto sul sistema origine, a parità di periodo selezionato ed inclusioni/esclusioni.
Gli scadenzari clienti/fornitori devono essere identici a quelli prodotti susl sistema origine, sia per totale che per dettaglio scadenze, a parità di periodo selezionato ed inclusioni/esclusioni.
Le liste di controllo errori clienti/fornitori (funzione/metodo L/E), devono dare risultato zero se tutto è stato convertito correttamente.
- \*\*Sai impostare le autorizzazioni di accesso ad una funzione/opzione per un \*\*

 :  : VOC Id="SKIB0110" Txt="Sai impostare le autorizzazioni di accesso ad una funzione/opzione per un utente o gruppo di utenti?"
La funzione UP AUT permette la gestione delle autorizzazioni di Sme.UP, quelle denominate C5\* sono relative alle funzioni contabili. Importarle dal modello se si dispone di una tabella autorizzazioni incompleta.
