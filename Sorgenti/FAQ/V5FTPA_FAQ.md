# Fatturazione Elettronica
## Normativa Processo e Sdi
- **Sono subappaltatore della PA al secondo livello e il mio fornitore (che è a**

 :  : VOC Id="10001" Txt="Sono subappaltatore della PA al secondo livello e il mio fornitore (che è al primo livello) mi ha emesso fattura elettronica :  devo procedere con la conservazione lettronica dell'XML o posso conservare la fattura cartacea?"
 In questo caso si è obbligati a procedere con la conservazione eletronica del file XML.
- **Nel caso in cui un mio fornitore decida di partire con la fatturazione **

 :  : VOC Id="10002" Txt="Nel caso in cui un mio fornitore decida di partire con la fatturazione elettronica su base volontaria prima del 01/01/19 dovrò conservare le sue fatture in modalità elettronica o cartacea?"
 Questo punto non è stato ancora chiarito dall'Agenzia delle Entrate. Ad oggi sembra che sia facoltà del cliente scegliere se effettuare la conservazione elettronica o cartacea. Per non avere nessun problema, in ogni caso, il suggerimento è quello di procedere con la conservazione elettronica.
- **Per le fatture d'acquisto in reverse charge come posso indicare l'imposta **

 :  : VOC Id="10003" Txt="Per le fatture d'acquisto in reverse charge come posso indicare l'imposta integrata?"
 Per queste fatture è possibile procedere con due modalità : 
 * generare il documento autofattura (che andrà poi comunicato al sdi come qualsiasi altra fattura di vendite)
 * integrare all'interno dei metadati l'informazione dell'imposta versata e mandare il dato in conservazione sostitutiva
- **Nel caso in cui abbia optato per la generazione della fattura elettronica **

 :  : VOC Id="10004" Txt="Nel caso in cui abbia optato per la generazione della fattura elettronica anche verso i clienti esteri cosa devo conservare e cosa ha valore fiscale/civilistico?"
 Nelle cessioni verso soggetti esteri la generazione e l'invio al Sdi della fattura elettronica ha sole finalità dichiarative (quindi mi evita l'esterometro) ma ai fini civilistico/fiscali il documento che farà fede è la fattaura analogica inviata al cliente. Quindi, per queste cessioni, si consiglia di conservare elettronicamente sia il PDF che il file XML.
- **Qual è il termine per la conservazione elettronica?**

 :  : VOC Id="10005" Txt="Qual è il termine per la conservazione elettronica?"
 La conservazione elettronica delle fattura d'acquisto/vendita va eseguita entro la fine dell'anno solare successivoa  quello di registrazione della fattura stessa. Quindi, ad esempio, le fatture registrate nel 2018 andranno mandate in conservazione sostitutiva entro il 31/12/19.
- **Ho correttamente inserito nella FE il codice destinatario del mio cliente m**

 :  : VOC Id="10016" Txt="Ho correttamente inserito nella FE il codice destinatario del mio cliente ma ho ricevuto un messaggio di mancata consegna :  come mai?"
Le cause potrebbero essere due : 
 * Se è stata inserita una PEC potrebbe trattarsi di un problema sulla casella di posta (potrebbe essere piena o riconoscere la mail ricevuta dallo Sdi come spam) che quindi blocca l'invio della FE
 * Se, invece, è stato inserito un codice destinatario il problema potrebbe essere legato ai server dello Sdi. Ci è stato comuncato, infatti, che alcuni server dello sdi non sono dotati dei certificati di firma previsti a livello di standard FE. Per questo motivo gli intermediari si vedono recpaitare una FE da un mittente sconosciuto e la 'rifiutano' mandando al mittente il messaggio di 'Mancata consegna'

- **Ho ricevuto da un mio fornitore una notifca di mancata consegna ma non **

 :  : VOC Id="10017" Txt="Ho ricevuto da un mio fornitore una notifca di mancata consegna ma non vedo la sua fattura nel mio cassetto fiscale :  come mai?"
Le modifiche apportate dal provvedimento dell'agenzia delle Entrate del 21 dicembre 2018, divenute necessarie a seguito del parere del Garante della privacy pubblicato in data 20 dicembre 2018, hanno cambiato le modalità di consultazione delle fatture elettroniche emesse e
ricevute. Prima delle novità, i documenti in Xml erano comunque consultabili nella propria area riservata del portale "Fatture e Corrispettivi"; ora, invece, è richiesto che il contribuente abbia esercitato apposita adesione al servizio di consultazione e acquisizione deile fatture.
L'accesso a tale servizio è possibile a ciascun soggetto passivo Iva in possesso delle credenziali di accesso al portale "Fatture e Corrispettivi". Tale servizio sarà disponibile solo a partire dal 03/05/2019, in questo periodo transitorio accedendo al portale viene presentato un messaggio di accettazione temporanea di memeorizzazione delle fatture ricevute. Accettando questo messaggio le fatture verranno presentate all'utente.

- **Come viene effettuato il conteggio dei bolli dall'Ade? E come posso fare **

 :  : VOC Id="10022" Txt="Come viene effettuato il conteggio dei bolli dall'Ade? E come posso fare se ho emesso fatture che avrebbero dovuto riportare il bollo ma, per un errore di configurazione, il bollo non è stato esposto?"

Sulla FE ci sono dei TAG specifici per identificare che la fattura è soggetta a bollo :  l'Agenzia utilizza questi campi per il conteggio dei bolli da addebitare.
Si tratta di campi che il programma compila in modo automatico se la configurazione del bollo è stata fatta correttamente.
I Campi sono questi : 
          2.1.1.6  <DatiBollo>

  2.1.1.6.1  <BolloVirtuale>

  2.1.1.6.2  <ImportoBollo>

Nel caso in cui vengano emesse fatture soggette a bollo ma sulle quali, per un errore di configurazione, il bollo non venga rilevato è sufficiente adottare un comportamento concludente sanando l'errore con il corretto versamento in F24.Quindi ipotizziamo che l'Agenzia comunichi un conteggio di 100 bolli da pagare ma, da conteggi interni ne risultino 150 sarà sufficiente effettuare un versamento di 300¤ per sanare la situazione tramite comportamento concludente.

## Able Tech

- **Se ho sottoscritto il pacchetto con Able Tech qual è il codice **

 :  : VOC Id="10009" Txt="Se ho sottoscritto il pacchetto con Able Tech qual è il codice destinatario da comunicare ai miei fornitori/indicare come indirizzo di ricezione nella mia anagrafica del Sdi?"
 Il codice destinatario di Able Tech è A4707H7 pertanto dovremo comunicare questo valore ai nostri fornitori o, meglio ancora, indicarlo nella nostra anagrafica del sito ffatture e corrispettivi
- **E' possibile attivare con Able Tech il servizio di interfacciamento con il **

 :  : VOC Id="10010" Txt="E' possibile attivare con Able Tech il servizio di interfacciamento con il Sdi e procedere alla conservazione con un altro fornitore/ente?"
 Sì è possibile. Dovranno essere, però, definite le modalità di scambio dei file XML/metadati tra SmeUP e il conservatore.
- **Nel caso in cui Able Tech fallisca come posso recuperare i miei dati?**

 :  : VOC Id="10011" Txt="Nel caso in cui Able Tech fallisca come posso recuperare i miei dati?"
 In caso di generiche traversie dell'azienda (chiusura, fallimento, ecc.) viene nominato un procuratore che ha l'incarico di gestire la continuità del servizio ordinario. Il procuratore avrebbe, quindi, l'onere di generare i pacchetti di distribuzione dei documenti contenenti per ciascun cliente tutte le sue fatture e quant'altro conserva con Able Tech. I pacchetti di distribuzione hanno valore di copia conforme, pertanto il cliente si porterebbe in casa quanto archiviato
- **Nel caso in cui decida di cambiare fornitore qual è il costo dell'estrazion**

 :  : VOC Id="10012" Txt="Nel caso in cui decida di cambiare fornitore qual è il costo dell'estrazione dei file da Able Tech per darli al mio nuovo conservatore?"
 Il volume di conservazione è sempre disponibile ed estraibile in ogni momento senza nessun costo aggiuntivo, quindi il versamento ad un altro ente di conservazione non ha oneri aggiuntivi.
- **Quanto tempo prima è necessario dare disdetta del contratto**

 :  : VOC Id="10013" Txt="Quanto tempo prima è necessario dare disdetta del contratto"
 90 GG dalla data scadenza
- **Perché usano la firma Aruba e non hanno fatto loro una firma?**

 :  : VOC Id="10014" Txt="Perché usano la firma Aruba e non hanno fatto loro una firma?"
 Able Tech non è un ente certificatore, ma è un ente che fornisce servizi, tra cui il tramite della fatturazione elettronica.
- **Se acquisto il servizio IXCE il 01/10/18 poi posso versare in **

 :  : VOC Id="10015" Txt="Se acquisto il servizio IXCE il 01/10/18 poi posso versare in conservazione anche gli XML passivi ricevuti in luglio 2018?"
 Sì, quello che viene acquistato è uno spazio di archiviazione su cui è possibile caricare anche documenti precedenti all'apertura del contratto stesso
- **Ho inviato delle fatture estere :  mi segnala errore in conservazione per un **

 :  : VOC Id="10018" Txt="Ho inviato delle fatture estere :  mi segnala errore in conservazione per un problema sulla partita IVA."
Able Tech ci ha segnalato che è presente un errore sui loro sistemi che stanno correggendo. Non appena lo risolveranno manderanno loro in automatico in conservazione tutte le fatture estere

## Procedure SmeUP

- **Come posso forzare come 'trasmesse' le fatture elettroniche inviate prima **

 :  : VOC Id="10006" Txt="Come posso forzare come 'trasmesse' le fatture elettroniche inviate prima della partenza con il nuovo intermediario?"
 E' necessario forzare il flag 2 del file EDSEND e il flag 12 del file V5TDOC
- **Come posso capire se una fattura è stata estratta?**

 :  : VOC Id="10007" Txt="Come posso capire se una fattura è stata estratta?"
 Nel momento in cui una fattura viene estratta viene sempre scritto il file EDSEND. In particolare, in questo file il flag 02 verrà così valorizzato : 
 * 0 se l'XML è stato correttamente estratto
 * 1 se l'XML contiene errori (gli errori vengono dettagliati nella stampa di controllo/dettagli da matrice)
 * 2 se l'XMl è corretto ed è in attesa di invio all'intermediario
 * 3 se l'XML è già stato mandato all'intermediario e quest'ultimo non ha ancora dato esito dell'invio (non ci ha ancora comunciato se l'invio è andato a buon fine o meno)
 * 4 se l'XML è stato inviato ma l'intermediario ha dato messaggio di errore
 * 5 se l'XML è stato inviato e l'intermediario ha dato esito positivo
 Quindi, se trovo la fattura nell'EDSEND significa che è estratta, il flag 2 poi mi dirà in che stato è.
 Lo sviluppo sta comunque implementando una scheda per semplificare questa analisi
- **Ho inviato una fattura e mi è stata scartata per un errore nella partita IV**

 :  : VOC Id="10008" Txt="Ho inviato una fattura e mi è stata scartata per un errore nella partita IVA come devo procedere?"
 In questo caso è prima di tutto necessario inserire il dato corretto della partita IVA (si ricorda che tutti i codici che iniziano con 8 o 9 sono in realtà dei codici fiscali e non delle partite IVA, quindi il dato va inserito nel codice fiscale).
 Fatto questo si dovrà procedere nuovamente con l'estrazione della fattura indicando come Tipo azione 'Riestrazione già inviate'.
 In questo modo la fattura verrà presentata nuovamente tra quelle da inviare e potrà seguire il normale flusso di invio.
 Si sottolinea anche che nel caso in cui non venga modificato alcun dato e si proceda con la riestrazione delle fatture già inviate il sistema non estrarrà nulla perchè non troverà dati modificati
- **Ho emesso una fattura in valuta a un cliente estero ma allo sdi sono **

 :  : VOC Id="10019" Txt="Ho emesso una fattura in valuta a un cliente estero ma allo sdi sono erronaemente stati comunicati i valori in euro :  esempio fattura di 1000USD pari a 800¤ inviata al Sdi per 1000¤. Come posso rettificare l'invio?"
Sarà necessario procedere in questo modo : 
1- Modificare la fattura già emessa e contabilizzata forzando il cambio a 1 :  in questo modo i dati contabili e iva si allineano a quanto ricevuto dal Sdi
2- Emettere NC con la stessa struttura della fattura 1, quindi stessa valuta, stessi importi e cambio 1 (quindi nell'esempio citato la NC sarà emessa per 1000USD con cambio 1). Questa NC andrà inviata allo sdi e contabilizzata ma NON inviata al cliente poichè si tratta semplicemente di una rettifica interna.
3- Emettere una nuova fattura con valori corretti, quindi cambio e importi originali dell'operazione (nell'esempio la fattura sarà di 1000USD pari a 800¤, quindi cambio 1,25).Questa fattura andrà inviata allo sdi e contabilizzata ma NON inviata al cliente poichè si tratta semplicemente di una rettifica interna.
A questo punto in contabilità si potranno pareggiare i documenti 1 e 2 e resterà aperta la fattura 3 (che verrà saldata nel momento in cui ci sarà l'incasso)

- **Le autofatture generate in seguito a prestazioni extracee vanno comunciate?**

 :  : VOC Id="10020" Txt="Le autofatture generate in seguito a prestazioni extracee vanno comunciate?"
Le autofatture generate in seguito a prestazioni ricevute da fornitore extracee non hanno nessun obbligo di invio. E', quindi, facoltà del cessionario decidere se comunicare o meno l'autofattura. Si sottilinea che nel caso in cui il documento non venga inviato non ci sono problemi a livello di protocollazione perchè lato sdi non vengono effettuati controlli di sequenza mentre a livello di conservazione sostitutiva verrà data una segnalazione non bloccante e si potrà decidere se lasciare il buco nella numerazione oppure se effettuare un versamento del PDF ricevuto.
Nel caso in cui, invece, si decida di inviare l'autofattura si ricorda che questo documento comparirà anche tra quelli ricevuti ma non andrà ovviamente registrato in contabilità.

- **Per le fatture che ho ricevuto nel cassetto fiscale e non sul portale able **

 :  : VOC Id="10021" Txt="Per le fatture che ho ricevuto nel cassetto fiscale e non sul portale able tech come posso comportarmi?"
Questa casistica si è presentata con una certa frequenza nella prima metà di gennaio per un problema dei certificati di firma dei server dello sdi.
Per queste fatture sarà necessario procedere al download dal cassetto fiscale ed efettuare la registrazione in modo tradizionale, non è possibile includerle nel cruscotto delle FE passive di SmeUP.
Per quanto riguarda la conservazione, Able Tech ci ha comunicato che faranno un'utility che permetta di recuperare in automatico questi documenti per inviarli in conservazione sostitutiva. Non appena gli aggiornamenti saranno disponibili avviseremo i clienti.
