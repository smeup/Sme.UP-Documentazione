## OBIETTIVO
Al fine di migliorare le performance e di disaccoppiare la scrittura dei log rispetto all'esecuzione delle funzioni applicative, è stata implementata una nuova struttura che prevede la scrittura dei record di log su coda dati (scrittura più veloce rispetto a quella su un file di database). I record presenti sulla coda dati vengono poi letti da un job dedicato per ambiente che si occupa di scrivere il JALOGT0F.

## ATTIVAZIONE
La scrittura dei log asincrona si attiva solo per gli ambienti presenti nello **script B£LOGG_03 nel file sorgente SCP_SET.
In caso un ambiente non sia presente nello script la scrittura dei log continua a funzionare come prima con scrittura diretta su JALOGT0F.
Lo script va messo in **libreria di gruppo**.
Nel caso sul sistema siano presenti più librerie di gruppo, ciascuna con un suo script B£LOGG_03 è necessario specificare nomi diversi per il job di monitoraggio, impostandolo tramite il tag LOG.CFG. Il default assunto è B£LOGG_03.
Per ciascun ambiente (tag LOG.AMB) va configurato il nome della coda dati da creare  e le mail mittente e destinatario utilizzate per l'invio di segnalazioni. E' possibile impostare più destinatari separati da virgola.
La coda dati viene creata nella libreria SMEUPUIDQ con dimensione massima di 2GB e riacquisizione automatica attiva.

### FUNZIONAMENTO
Schedulando l'esecuzione del programma **JALOG9** viene avviato un job B£LOGG_03 che monitora lo stato dei job che scrivono il log per ciascun ambiente.
Quindi se nello script B£LOGG_03 sono stati configurati 3 ambienti vederemo 4 job nella coda  lavori B£QQ99 :  il job B£LOGG_03 che verifica che gli altri siano attivi e funzionanti e un job per ciascun ambiente con lo stesso nome della coda dati configurata per quell'ambiente.


### GESTIONE DELLE ANOMALIE
Nello script è possibile configurare il numero di tentativi di sottomissione del job di ciascun ambiente. In caso il parametro non sia indicato viene assunto come default 50 tentativi giornalieri.
Il job di monitoraggio sottomette il job di un ambiente se questo non è attivo.
Nel caso il job sia in MSGW lo congela, manda una mail di segnalazione e ne sottomette un altro.
Nel caso il job di monitoraggio rilevi che la coda dati di un ambiente è piena, congela il job dell'ambiente, manda una mail di segnalazione e ne sottomette un altro.
Nello script è possibile anche indicare per ciascun ambiente un'ora di inizio e un'ora di fine per determinare quando dovrà chiudersi il job per ambiente e a partire da che ora il job di monitoraggio comincerà a cercare di sottomettere il job per ambiente.
