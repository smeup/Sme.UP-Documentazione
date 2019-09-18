- \*\*Applicazione\*\*

 :  : VOC Id="APP01" Txt="Applicazione"
Una applicazione in SME.up è un insieme di moduli applicativi che sono riferiti ad un argomento.
Esempi di applicazioni sono la contabilità, la gestione del magazzino ecc. Molto spesso una applicazione coincide con l'oggetto software venduto.

- \*\*Modulo\*\*

 :  : VOC Id="MOD01" Txt="Modulo"
Insieme omogeneo di programmi che definiscono un ambito applicativo quale ad esempio la gestione degli articoli, la gestione dell'inventario, il calendario ecc.

- \*\*Programma\*\*

 :  : VOC Id="PGM01" Txt="Programma"
Insieme di istruzioni che implementano un algoritmo. Tali istruzioni possono prevedere una interazione con un utente mediante l'emissione di un formato video.
[http://en.wikipedia.org/wiki/Computer_program](http://en.wikipedia.org/wiki/Computer_program)

- \*\*Azione\*\*

 :  : VOC Id="AZI01" Txt="Azione"
Si dice funizzato un programma con una interfaccia (modo di chiamata) standard, definito all'interno di SME.up
Tali programmi vengono anche genericamente chiamati "azioni".
Sono accessibili mediante il comando breve "UP AZI".
Possono essere associati ad un passo di un flusso applicativo nella tabella B£J.

- \*\*Funzione\*\*

 :  : VOC Id="FUN01" Txt="Funzione"
Chiamiamo funzione una stringa con un formato standard, necessaria e sufficiente ad ottenere dal server specificato una risposta in XML utilizzabile per l'emissione.

- \*\*Servizio\*\*

 :  : VOC Id="SER01" Txt="Servizio"
Chiamiamo servizio un programma con una interfaccia (modo di chiamata) standard definito all'interno di SME.up. È del tutto simile ad una azione (o programma funizzato) ma specifico per le chiamate eseguite da LOOC.up e che si attendono come risposta un XML

I servizi sono accessibili mediante il comando breve "UP SER".
In LOOC.up vengono chiamati da una funzione del tipo F(xx;SERVIZIO;xx) 1(;;)

- \*\*Web service\*\*

 :  : VOC Id="WEB01" Txt="Web service"
[http://en.wikipedia.org/wiki/WebService](http://en.wikipedia.org/wiki/WebService)

- \*\*Fonte\*\*

 :  : VOC Id="FON01" Txt="Fonte"
Per fonte si intende una disponibilità (di materiale o finanziaria)
presente (giacenza di magazzino o saldo del conto cassa) :  in questo caso va codificata come fonte presente.
 :  : DEC T(ST) K(M5E) O(DK)
 :  : DEC T(ST) K(C6E) O(DK)
oppure una disponibilità o impegno futuro, datato (uscita per vendita, entrata per il pagamento di una fattura) :  in questo caso essa va codificata come fonte futura.
 :  : DEC T(ST) K(M5F) O(DK)
 :  : DEC T(ST) K(C6F) O(DK)
- \*\*Vuoi continuare?\*\*

 :  : VOC Id="000001" Txt="Vuoi continuare?"
- \*\*L'operazione richiesta potrebbe richiedere \n un tempo di esecuzione \*\*

 :  : VOC Id="000002" Txt="L'operazione richiesta potrebbe richiedere \n un tempo di esecuzione molto lungo. \n Continuare?"
