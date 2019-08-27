- **Sollecito**

 :  : VOC Id="000001" Txt="Sollecito"
Per sollecito in smeup si intende un archivio ben identificato completamente separato da quello delle scadenze. In questo archivio confluiscono, riprendendone le informazioni rilevanti, le scadenze attive scadute che rispecchiano certe caratteristiche di età/tipologia pagamento, tali per cui può risultare opportuna una notifica al cliente che inviti alla risoluzione del credito.

- **Estrazione**

 :  : VOC Id="000002" Txt="Estrazione"
L'estrazione dei solleciti è quella fase tramite la quale vengono analizzati le scadenze attive scadute e viene valutato (secondo i criteri previsti) se sia necessario estrarre (o riestrarre) la scadenza nell'archivio dei solleciti.

- **Notifica**

 :  : VOC Id="000005" Txt="Notifica"
Sotto il termine notifica si intende, quell'azione tramite la quale a partire da uno o più solleciti estratti, viene stampata o stampata ed inviata una lettera ad un cliente avente per oggetto l'invito alla soluzione del crediti in essere.

- **Solleciti da notificare**

 :  : VOC Id="000010" Txt="Solleciti da notificare"
I solleciti da notificare sono quei solleciti estratti che non sono ancora stati notificati al cliente. Una volta che è stata prodotta la stampa il sollecito non sarà più in stato "da notificare", ma confluirà nella massa dei solleciti aperti. NOTA BENE :  quando stampo una lettera di sollecito vengono sempre inclusi tutti i solleciti aperti di un cliente, che siano da notificare o già notificati.

- **Solleciti aperti**

 :  : VOC Id="000020" Txt="Solleciti aperti"
I solleciti aperti sono quei solleciti che non sono ancora passati a stato chiuso. I solleciti possono passare a stato chiuso a seguito dell'avverarsi di una delle seguenti azioni : 
- Saldo della rata collegata al sollecito (parziale o totale)
- Estrazione di un livello di sollecito superiore a quello in essere, sulla medesima scadenza
- Intervento manuale dell'utente, sullo stato del sollecito

- **Responsabile**

 :  : VOC Id="000025" Txt="Responsabile"
Per responsabile si intende colui che a in carico la gestione della riscossione del credito in sollecito. Tale informazione nasce assumendo il responsabile indicato sull'archivio delle scadenze (a sua volta derivato dal tipo rata).

- **Richieste di definizione**

 :  : VOC Id="999999" Txt="Richieste di definizione"
- Cliente non sollecitabile
