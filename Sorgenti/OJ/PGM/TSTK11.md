

# Obiettivo
Richiamare un web service esterno al fine di integrare dati in ingresso oppure di inviarli.

## Funzione SND metodo OUT. Invia messaggio a webservice - Da server a webservice
Permette di effettuare una richiesta webservice passando in input le schiere di variabili Nome (£K11S_NM) e Valore (£K11S_VA). Le variabili devono essere definite nel relativo script LOA38. Viene restituita la chiave per la lettura dei dati di output in matrice.

## Funzione SND metodo FIL. Invia messaggio a webservice - Da server a webservice
Permette di effettuare una richiesta webservice passando in input le schiere di variabili Nome (£K11S_NM) e Valore (£K11S_VA). Le variabili devono essere definite nel relativo script LOA38.
A proposito del payload, nel parametro Pathfile indicare il percorso IFS del file contentente il payload (£K11I_PF), in alternativa passare il payload come stringa (£K11I_PL).
Viene restituita la chiave per la lettura dei dati di output CDATA.

## Funzione GRI metodo SCH. Griglia - Restituzione schiere
Restituisce la griglia di definizione delle colonne in output dal webservice, necessita della chiave restituita dal SND.OUT.

## Funzione RIG metodo POS e LET. Righe - Posizionemento e lettura
Posiziona all'inizio e legge una riga alla volta l'output dal webservice, necessita della chiave restituita dal SND.OUT.

## Funzione DAT metodo POS e LET. Righe - Posizionemento e lettura
Posiziona all'inizio e legge una riga alla volta l'output dal webservice, necessita della chiave restituita dal SND.FIL.

## Funzione INI. Reinizializza Provider
Effettua la reinizializzazione del provider per l'istanza del webservice richiesta.

## Funzione PAR. E la funzione specifica per i webservice multipart.
Prevede i metodi POS, ATR e LET.

### Funzione PAR metodo POS.
Si posiziona all'inizio di una risposta multipart, pertanto al primo part.

### Funzione PAR metodo ATR.
Legge tutti gli attributi relativi al part in cui è posizionato.
Ripetendo la funzione si leggono gli attributi del part successivo.

### Funzione PAR metodo LET.
Legge il al contenuto del part in cui è posizionato.
Ripetendo la funzione  si legge il contenuto del part successivo.

Per la definizione dei webservice si rimanda alla documentazione specifica del costruttore LOA38 : 
- [BASE Integrazione con webservice](Sorgenti/V2/LOCOS/V2LOCOSA38)
