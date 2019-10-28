## OBIETTIVO

Tracciare le performance del client nelle elaborazioni dell'emulatore e della scheda.

## ATTIVAZIONE

Per l'emulatore il log è sempre attivo.

Per la scheda, invece l'attivazione è opzionale.
La sua gestione è richiamabile dal setup della scheda.
Il setup della scheda è richiamabile dall'icona verde in alto a sinistra di tutte le finestre di scheda di loocup.
Da li con tasto destro, va richiamata la voce "Carica/Gestisci Configurazione"
Si aprirà quindi la schermata con le configurazioni al momento presenti. Da questa schermata si può evincere il fatto che l'attivazione può essere fatta a livello di utente/ambiente o per tutti gli utenti/tutti gli ambienti (tramite l'indicazione nell'apposito campo del codice \*\* piuttosto che dell'istanza precisa (va comunque considerato che queste scelte vengono memorizzate nel file B£MEDE0F e che quindi l'attivazione su più ambienti dipende anche dal posizionamento di questo file).
Entrano inserimento o modifica della configurazione il log potrà essere gestito tramite il campo "Abilita Log Utente" sotto l'etichetta "Debug".

## GESTIONE DATI DEL LOG

- [Regole di Denominazione File di Log del Client](Sorgenti/DOC/TA/B£AMO/B£LOGG_01)

I log di performance sono identificati fra gli altri tramite l'estensione ".PR".

I dati in essi contenuti saranno interrogabili e gestibili tramite le schede specifiche.

In base a quanto descritto è importante notare questi due aspetti : 
-  Visto che i dati vengono memorizzati sul client, anche se la configurazione viene attivata per tutti gli utenti, nelle interrogazioni avrò la possibilità di vedere solo i log del client su cui sono.
-  I dati pur essendo manutenzionabili tramite le schede vengono comunque automaticamente eliminati ogni 7 giorni.

Per questi motivi è possibile utilizzare nella scheda una  funzione che permette di copiare i file di log dalla cartella dell'utente ad una cartella di installazione di loocup (nell'assunzione che loocup sia installato su un server disponibile a più utenti). Per questo motivo nelle interogazioni è predisposta sia l'interrogazione della cartella di log dell'utente che quella di installazione di loocup.



