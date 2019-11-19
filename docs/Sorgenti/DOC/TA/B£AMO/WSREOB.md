
## Introduzione

Il modulo oggetti remoti (WSREOB) si occupa della gestione di oggetti e OAV remoti.

Un oggetto è remoto quando le sue istanze vengono recuperate tramite webservice. Un esempio può essere l'oggetto V5GDR (File di Google Drive) le cui istanze sono la lista dei file di una determinata cartella di Google Drive.

Un OAV è remoto quando il suo valore viene recuperato da un webservice.

I webservices utilizzabili sono quelli integrati in Sme.UP tramite il costruttore A38.
 :  : DEC T(V2) P(LOCOS) K(A38) L(1)

Gli script di definizione sono nel file SCP_K47.
 :  : DEC T(OJ) P(\*FILE) K(SCP_K47)
Gli script che iniziano per V5 definiscono oggetti remoti, quelli che iniziano con OA_ definiscono OAV remoti.

Qui è presentato un diagramma di sequenza su come opera il modulo WSREOB. Il recupero delle informazioni remote viene effettuato tramite passaggio alla £OAV che richiama la £K47 che a sua volta richiama la £K11.

![0001](http://localhost:3000/immagini/WSREOB/0001.png)
- [Oggetti remoti](Sorgenti/DOC/TA/B£AMO/WSREOB_01)
- [OAV remoti](Sorgenti/DOC/TA/B£AMO/WSREOB_02)
