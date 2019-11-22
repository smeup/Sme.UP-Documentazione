# Scheda Autorizzazioni Applicative

## Interpretare la scheda di Analisi
La scheda di analisi del file AUTOAP00F mostra in ROSSO i campi non validi.
 \* _2_AA£UTE (Utente) :   è in errore se non contiene il nome di utente o di un gruppo utenti.
 \* _2_AA£CAA (Classe) :  è in errore se non contiene un valore contenuto nella B£P.
 \* _2_Da AA£O01 a AA£O10 (Valore 1 - Valore 10) :  sono in errore se il loro valore non è coerente con la B£S o se non esiste l'elemento di B£P contenuto in AA£CAA.
 \* _2_Mancanza Default :  controlla che esista il default per quel record. Il default esiste se è presente un altro record che ha per classe la stessa classe, per utente '\*\*' e per funzione '\*\*'.
 \* _2_Presenza Errori :  segnala che è stato riscontrato almeno un errore nei vari controlli.


## Formato principale

![M5CMRP_029](http://localhost:3000/immagini/MBDOC_SCH-B£AUTO/M5CMRP_029.png)
- [Autorizzazioni](Sorgenti/MB/SCP_SCH/B£AUTOES)
