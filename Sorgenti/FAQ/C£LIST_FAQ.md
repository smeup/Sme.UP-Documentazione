- \*\*Sai cos'è e a cosa serve un listino ?\*\*

 :  : VOC Id="SKIL0010" Txt="Sai cos'è e a cosa serve un listino ?" Als="comm"
E' un elenco/catalogo di prodotti, eventualmente con relativi prezzi e/o condizioni commerciali (vendita/acquisto/lavorazione).

- \*\*Sai quando è necessario codificare un listino ?\*\*

 :  : VOC Id="SKIL0020" Txt="Sai quando è necessario codificare un listino ?"
Quando si deve attribuire un valore ad un prodotto da commercializzare/acquistare/lavorare. Per Smeup, la gestione listini permette di associare dei valori numerici ad un gruppo di oggetti
(da 1 a 3). Il caso classico è il prezzo di un articolo per un cliente.

- \*\*Sai qual'è l'archivio di riferimento ?\*\*

 :  : VOC Id="SKIL0030" Txt="Sai qual'è l'archivio di riferimento ?"
C£LIST00F e relative viste logiche.

- \*\*Sai qual'è l'applicazione di Sme_up che contiene la gestione Listini...\*\*

 :  : VOC Id="SKIL0040" Txt="Sai qual'è l'applicazione di Sme_up che contiene la gestione Listini..."
C£, lo stesso di parametri, descrizioni estese, classificazioni.

- \*\*Sai quali sono le tabelle (le principali) che ne governano le funzioni di \*\*

 :  : VOC Id="SKIL0050" Txt="Sai quali sono le tabelle (le principali) che ne governano le funzioni di base ?"
- C£1 elemento \* che contiene il numeratore per attribuzione IDOJ archivio listini

- C£\* s/s CL categoria lisitini

- C£L Codici Listino (impostazione caratteristiche del listino, quali gestione listino a quantità (lotto da/a) o definizione date validità.

- C£V Definizione degli oggetti riferiti ad un listino (Articolo, Fornitore/articolo), dei valori ad essi associati (prezzo, sconti, spese) della valuta in cui sono espressi i valori

- C£H, tabella che definisce nello specifico le caratteristiche di ogni
singolo valore codificato in C£V ( sezione).

- VAL Tabella divisa, altra caratteristica codificata di un listino.



- \*\*Sai cos'e' e quando va utilizzato il lotto di validità ?\*\*

 :  : VOC Id="SKIL0060" Txt="Sai cos'e' e quando va utilizzato il lotto di validità ?"
E' possibile a livello di listino, ma anche a livello di sezione di listino (C£V), definire condizioni di validità sulla quantità da valorizzare.
Utile per codificare sconti/prezzi "a Quantità".

- \*\*Cosa sono e quando vanno utilizzate data inizio validità e data fine valid\*\*

 :  : VOC Id="SKIL0070" Txt="Cosa sono e quando vanno utilizzate data inizio validità e data fine validità ?"
Memorizzare prezzi validi ad intervalli di data diversi. Questo consente di valorizzare documenti di ciclo esterno "per data", oppure di effettuare analisi a valore nel tempo.

- \*\*Conosci le utilities per verificare la corretta impostazione della gestion\*\*

 :  : VOC Id="SKIL0080" Txt="Conosci le utilities per verificare la corretta impostazione della gestione di un listino ?"
- C£L, attraverso la quale e' possibile simulare un reperimento valore, anche analizzandone "passo passo" i criteri di determinazione

- C£T, ritorna informazioni generali di un record di listino

- \*\*Conosci  la classe di autorizzazione che regola gli accessi alla gestione \*\*

 :  : VOC Id="SKIL0090" Txt="Conosci  la classe di autorizzazione che regola gli accessi alla gestione listini ?"
C£LIS0, dove la funzione puo' contenere (in alternativa al valore di risalita \*\*, ossia tutti) il codice del listino da autorizzare.

- \*\*Conosci le possibilità offerte dalla definizione di programmi utente per a\*\*

 :  : VOC Id="SKIL0100" Txt="Conosci le possibilità offerte dalla definizione di programmi utente per aggiustare le funzioni sui listini Sme_up ?"
Come in molte funzioni Sme_up, e' possibile definire un comportamento alternativo al previsto
(standard) in alcune funzionalità. La gestione dei listini non fa eccezione. E' possibile infatti
attraverso opportuna codifica in tabella C£V  innescare programmi di aggiustamento su gestione
dettaglio scheda listino, criteri di reperimento valori, modalità di calcolo valori di listino.

I prototipi : 
C£LIS0D_Z Aggiustamento gestione scheda listino
C£LIS0O_A Aggiustamento calcolo valori listino


















































