# JA1 - Parametri java
## OBIETTIVO
Permettere la personalizzazione del collegamento a JAVA
## CONTENUTO DEI CAMPI

 :  : FLD T$JA1A __Utente default__
Si imposta il profilo utente che verrà utilizzato all'atto della connessione da JAVA. È opportuno creare un utente apposito, con le seguenti caratteristiche : 
_7_INLMNU(\*SIGNOFF)
PWDEXPITV(\*NOMAX)
INLPGM(\*NONE)
In questo modo si impedisce che questo utente possa collegarsi dalla mappa di collegamento. Inoltre la password non ha scadenza, quindi essa non segue l'impostazione della variazione del
password definita a livello di sistema.
**IMPORTANTE** :  Questo Utente viene utilizzato come utente FTP di AS400 nella funzione FTP dello SMENS (£G53).
In particolare è indispensabile per la fase di creazione cubi (CUBE_UP)

 :  : FLD T$JA1B __Password__
È la password dell'utente definito in precedenza, utilizzata anch'essa all'atto della connessione da JAVA. Per ragioni di riservatezza, è presentata non visualizzata.

 :  : FLD T$JA1C __Log comunicazioni JA__
Consente di scrivere un log delle varie comunicazioni effettuate, mediante l'uso della routine £jac. I valori possibili sono : 
- ' ' nessuna registrazione di log;
- '1' viene registrato un evento per ogni chiamata all'AS400;
- '2' Vengono aggiornati i campi della tabella jau con delle informazioni riguardanti i collegamenti;
- '3' entrambe le opzioni '1' '2' contemporaneamente.

 :  : FLD T$JA1F __Attivazione LOG__
Se impostato, attiva la gestione della scrittura log per la comunicazione Looc.UP / Web.UP
Sono previsti i seguenti valori : 
' ' = Nessun log attivo
'1' = Log attivo in base a quanto definito in tabella JAL (OBSOLETO)
'2' = Attivo solo per errori
'3' = Attivo per info collegamento ed errori
'9' = Attivo per tutte le info
La registrazione dei log avviene sul databases JALOGT0F con origine LOC e con i seguenti tipi : 
S Se funzione, Ping o Azioni
C se collegamento
D se dettaglio
X in tutti gli altri casi

 :  : FLD T$JA1H __Password protezione PDF con £G53__
Se impostata, viene utilizzata come password master di default nella protezione dei PDF creati con la £G53.
Viene sostituita solo se gestita a livello di creazione del singolo documento (£G53MP).

 :  : FLD T$JA1I __Path Specifico £G53__
Questo è il campo che definisce la cartella dell'IFS da cui vengono eseguiti lo Smens e lo Smedg.
Se tale campo è blank, allora lo Smens e lo Smedg vengono eseguiti dal percorso : 
**/SmeExt/Smeup**
Se tale campo non è blank, allora lo Smens e lo Smedg vengono eseguiti dal percorso : 
**/SmeExt/xxxxx/Smeup**
dove xxxxx è il contenuto del campo.

 :  : FLD T$JA1J __Exit JAJAC0_SM (SV)__
Questo campo permette di impostare il suffisso del programma di exit del JAJAC0_SM.
Il nome del programma di exit sarà JAJAC0_SM + il suffisso.

 :  : FLD T$JA1K __Attiva notifica £G53__
Attiva il fatto che in caso di errore, la G53 invia una notifica, utilizzando i parametri successivi.
-  " " - le notifiche non sono attive.
-  "1" - invia la notifica solo all'utente che esegue la g53
-  "2" - invia la notifica all'utente che esegue la g53 ed agli utenti della lista indicata nel campo "Lista notifica £G53" di questo elemento di tabella

 :  : FLD T$JA1L __Tipo notifica £G53  __
Se attiva la notifica della £G53, questo campo indica che tipo notifica utilizzare.
A standard è predisposto il tipo notifica 01.01.P01.

 :  : FLD T$JA1M __Lista notifica £G53 __
Se si sceglie di attivare le notifiche nella modalità 2 qui è possibile indicare a quali utenti inviare la notifica oltre all'utente che esegue la G53 in errore.

 :  : FLD T$JA1N __Notifica errori £G53__
Indica che tipi errori della g53 devono essere notificati. Di default vengono notificati solo gli errori sull'esecuzione delle mail, ma indicando qui "1" è possibile notificare gli errori su tutte le metologie della g53.

 :  : FLD T$JA1O __Attivazione log £G64__
La registrazione dei log, se attivata, avviene sul databases JALOGT0F con tipo record LOG.G64

 :  : FLD T$JA1P __Attiva log sessione __
La registrazione dei log, se attivata, avviene sul databases B£QQFL0F con tipo record SES.LOG

 :  : FLD T$JA1Q __Attiva log £K11     __
Può assumere i sequenti valori : 
  Solo per errori
1 Log dettagliato
2 Log dettagliato+file temp provider
La registrazione dei log avviene sul databases JALOGT0F con tipo record LOG.K11

 :  : FLD T$JA1R __Attiva log £Q06     __
Può assumere i sequenti valori : 
1 Attivo, verranno registrati i log di traccia e di esecuzione
2 solo traccia, verranno registrati i soli log di traccia
3 solo esecuzione, verranno registrati i soli log di esecuzione
  Disattivo, non saranno registrati i log
La registrazione dei log avviene sul database B£LQ060F

 :  : FLD T$JA1S __Disattiva i log     __
Se impostato disabilita la scrittura dei log relativi ai database : 
JALOGT0F Log comunicazione Client/Server, di solito gestito tramite K05 o JALOG3
B£LQ060F Log trace esecuzioni, di solito gestito tramite Q06 attivata durante le compilazioni.
L'attivazione avverra dopo essersi ricollegati.
