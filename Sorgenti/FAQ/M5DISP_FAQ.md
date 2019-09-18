- **Sai come si fa a modificare un gruppo fonti senza cambiare il codice?**

 :  : VOC Id="SKID0010" Txt="Sai come si fa a modificare un gruppo fonti senza cambiare il codice?"
Si accede col comando M nell'opzione a destra del gruppo fonti e dopo aver compilato la scelta fonti si presenta la richiesta di conferma aggiornamento
- **Sai come si fa ad ordinare le fonti a parità di data?**

 :  : VOC Id="SKID0020" Txt="Sai come si fa ad ordinare le fonti a parità di data?"
Si utilizza il campo "ordinamento fonte" nella tabella delle fonti. ATTENZIONE :  a parità di data ed ordinamento si ottiene la sintesi in una unica fonte di tutte le quantità fonti. Ad esempio, se diverse fonti indicanti diverse aree di giacenza hanno lo stesso codice ordinamento, la quantità totale di giacenza viene riportata sulla prima fonte.
- **Sai come si fa a leggere la disponibilità che riguarda solo un fornitore, **

 :  : VOC Id="SKID0030" Txt="Sai come si fa a leggere la disponibilità che riguarda solo un fornitore, oppure una commessa?"
Si utilizza la parte inferiore dei parametri di lancio analisi disponibilità, dove si possono indicare i limiti dell'analisi, tra cui il fornitore, la commessa, il lotto, la configurazione, l'ubicazione , etc.
NOTA :  ovviamente la analisi ha successo se le fonti sono definite con la spaccatura sul campo che si vuole isolare :  per fornitore, per comemssa, etc
- **Sai come si fa a vedere la disponibilità su una griglia di date, in orizzo**

 :  : VOC Id="SKID0040" Txt="Sai come si fa a vedere la disponibilità su una griglia di date, in orizzontale, a partire da una certa data?"
Usando il metodo SIN e defininendo sia la data di inzio che una periodicità desiderata, onde definire la griglia temporale (per settimane, mesi, etc)
- **Sai come si fa a vedere la disponibilità ad una certa data?**

 :  : VOC Id="SKID0050" Txt="Sai come si fa a vedere la disponibilità ad una certa data?"
Ponendo il limite di data nel lancio disponibilità
- **Sai come si fa a vedere la disponibilità libera?**

 :  : VOC Id="SKID0060" Txt="Sai come si fa a vedere la disponibilità libera?"
Basta interrogare la disponibilità senza uno schema preciso (campo schema non valorizzato) o introducendo nello schema desiderato la colonna disponibilità libera?
- **Sai come si fa a vedere dall'analisi disponibilità la stessa situazione ch**

 :  : VOC Id="SKID0070" Txt="Sai come si fa a vedere dall'analisi disponibilità la stessa situazione che l'MRP ha fotografato quando ha girato?"
Bisogna fare un gruppo fonti che utilizza delle fonti di tipo "fotografato", ossia che siano deviate su analoghe fonti di uno scenario  MRP
- **Sai come si fa a veder la disponibilità raggruppata per giorno, o per font**

 :  : VOC Id="SKID0080" Txt="Sai come si fa a veder la disponibilità raggruppata per giorno, o per fonte ?"
Ci sono diversi metodi per interrogare la disponibilità. Tra questi diversi raggruppano. Di seguito la lista dei metodi.
DET       Dettaglio per data
DFO       Dettaglio per fonte
DMD       Dettaglio per mag.data
DMF       Dettaglio per mag.fonte
RDT       Riepilogo per giorno
RFO       Riepilogo per fonte
RMF       Riepilogo per mag.fonte
SMG       Sintesi   per magazzino
SIN       Sviluppo su griglia date
SOG       Sintesi su oggetto
SOR       Sviluppo orizzontale
- **Sai come si fa a stampare una lista di articoli la cui disponibilità sia i**

 :  : VOC Id="SKID0090" Txt="Sai come si fa a stampare una lista di articoli la cui disponibilità sia in negativo?"
Nella stampa analisi disponibilità c'è la possibilità di chiedere la stampa dei soli articoli che hanno disponibilità finale negativa.
- **Sai come impostare le fonti utente che leggano dati da altri gestionali?**

 :  : VOC Id="SKID0100" Txt="Sai come impostare le fonti utente che leggano dati da altri gestionali?"
- [Fonti utente per interfacciare altri sistemi](Sorgenti/DOC/TA/B£AMO/M5DISP_N8)
- **Sai qual'è la classe di autorizzazione per proteggere la gestione dei grup**

 :  : VOC Id="SKID0110" Txt="Sai qual'è la classe di autorizzazione per proteggere la gestione dei gruppi fonte?"
La classe di autorizazione è B£MDV5, da usarsi con la funzione M5FO01G
