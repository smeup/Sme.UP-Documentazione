- \*\*Configurazione del server Databeacon\*\*

 :  : VOC Id="10001" Txt="Configurazione del server Databeacon"
 Al fine di permettere a Looc.UP di sfruttare il motore di generazione di consultazione dei cubi, è necessario, sulla macchina ove risiede il server di Databeacon, predisporre una condivisione di rete (le autorizzazioni devono essere almeno di lettura ed esecuzione) sulla cartella di installazione di Databeacon (di solito _B_C : \Programmi\Databeacon).

- \*\*Configurazione di Looc.UP\*\*

 :  : VOC Id="10002" Txt="Configurazione di Looc.UP"
 Looc.UP deve sapere dove trovare il motore di di generazione di consultazione dei cubi. Per far ciò va inserito nel file di configurazione di Looc.UP il percorso di rete della condivisione creata al punto precedente.

- \*\*Dove trovo il file di configurazione di Looc.UP?\*\*

 :  : VOC Id="10003" Txt="Dove trovo il file di configurazione di Looc.UP?"
 Nella cartella _7_LOOCUP_SET\CFG contenuta nella cartella di installazione di Looc.UP. Qui è presente il file _7_application.xml.

- \*\*Come identifico la voce di configurazione che determina il funzionamanto del \*\*

 :  : VOC Id="10004" Txt="Come identifico la voce di configurazione che determina il funzionamanto del modulo?"
 Aprite il file identificato al punto precedente con un editor per XML (o all'estremo con notepad). Trovate l'elemento _7_Module con _7_Name="UICube". Eventualmente cercate la seguente stringa :  _B_Module Name="UICube".

- \*\*Come modifico il file di configurazione di Looc.UP?\*\*

 :  : VOC Id="10005" Txt="Come modifico il file di configurazione di Looc.UP?"
 L'elemento XML identificato al punto precedente contiene un attributo _7_databeacondir. Al valore presente nel file di configurazione sostituire il percorso di rete che punta alla cartella condivisa precedentemente creata. Ora è necessario, qualora sia aperto, riavviare Looc.UP.
