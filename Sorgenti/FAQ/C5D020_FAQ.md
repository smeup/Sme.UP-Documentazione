- \*\*ESTRAZIONE\*\*

 :  : VOC Id="10001" Txt="ESTRAZIONE"

- \*\*Perchè una rata di scaduto non è stata estratta come sollecito?\*\*

 :  : VOC Id="10002" Txt="Perchè una rata di scaduto non è stata estratta come sollecito?"
 I motivi possono essere questi : 
 \* Dalla scadenza non è ancora passato il numero di giorni, indicati nell'elemento di tabella C5X corrispondente al primo tipo sollecito, previsti per la gestione dell'eventuale ritardo nella registrazione o nell'effettuazione del pagamento.
 \* La rata è stata bloccata
 \* Il cliente in anagrafica è stato indicato come cliente non sollecitabile

- \*\*Perchè ho estratto e non si aggiornano date/ora ultima estrazione?\*\*

 :  : VOC Id="10003" Txt="Perchè ho estratto e non si aggiornano date/ora ultima estrazione?"
 Perchè data/ora sono quelle dell'ultima riga estratta. Se l'ultima estrazione non ha aggiunto alcun nuovo sollecito la data ultima estrazione non viene modificata.

- \*\*NOTIFICA\*\*

 :  : VOC Id="10004" Txt="NOTIFICA"

- \*\*Cosa si intende per solleciti \*\*

 :  : VOC Id="10005" Txt="Cosa si intende per solleciti "Da notificare" e "Solleciti Aperti"?"
 Per solleciti da notificare, si intendono quei solleciti che sono stati estratti, ma che non sono mai stati oggetto di un elaborazione di stampa o invio mail al corrispondente cliente. I solleciti aperti sono invece tutti quei solleciti estratti che non sono stati ancora saldati (i solleciti da notificare sono quindi un sottoinsieme dei solleciti aperti). NOTA BENE :  quando viene prodotta la comunicazione al cliente vengono sempre inclusi tutti i solleciti aperti.



- \*\*Sai cos'è e come controllare lo scaduto di un cliente?\*\*

 :  : VOC Id="SKIS0010" Txt="Sai cos'è e come controllare lo scaduto di un cliente?" Als="comm"
E' l'ammontare degli importi dovuti e non pagati, si può controllare dallo scadenzario clienti.
- \*\*Sai cos'è un sollecito di pagamento?\*\*

 :  : VOC Id="SKIS0020" Txt="Sai cos'è un sollecito di pagamento?" Als="comm"
E' un intervento che si mette in pratica per provare a recuperare quanto scaduto e non pagato dal cliente. Si attua solitamente con comunicazione scritta, spesso con varie forme anche in base al numero di tentativi già effettuati.
- \*\*Sai come configurare una o più lettere di sollecito?\*\*

 :  : VOC Id="SKIS0030" Txt="Sai come configurare una o più lettere di sollecito?"
Nella tabella C5X si codificano i vari livelli di sollecito, ai quali si abbina una lettera dedicata (raggiungibile col comando T G69 da riga comandi o dalla gestione lettere del menu di contabilità).
- \*\*Sai come configurare una o più lettere di sollecito in lingua estera?\*\*

 :  : VOC Id="SKIS0040" Txt="Sai come configurare una o più lettere di sollecito in lingua estera?"
Nell'anagrafica del cliente da sollecitare va gestito il codice lingua, che poi viene riportato in testa alla lettera in questione.
- \*\*Sai come controllare lo scaduto di tutti i clienti ad una certa data?\*\*

 :  : VOC Id="SKIS0050" Txt="Sai come controllare lo scaduto di tutti i clienti ad una certa data?" Als="comm"
Utilizzando lo scadenzario residuo dalla lista clienti, con un filtro sulla data scadenza finale.
- \*\*Sai come si configura una sequenza di solleciti di pagamento con periodici\*\*

 :  : VOC Id="SKIS0060" Txt="Sai come si configura una sequenza di solleciti di pagamento con periodicità precisa?"
Oltre alla codifica dei tipi di sollecito codificabile nella tabella C5X, sull'elemento della tabella si impostano i giorni di passaggio al livello successivo.
- \*\*Sai come estrarre il solleciti di pagamento ed in che file vengono memoriz\*\*

 :  : VOC Id="SKIS0070" Txt="Sai come estrarre il solleciti di pagamento ed in che file vengono memorizzati?"
Utilizzando la funzione di estrazione solleciti, che scrive il risultato dell'analisi nel file C5SOLL0F.
- \*\*E' possibile non sollecitare un cliente anche se ha degli scaduti?\*\*

 :  : VOC Id="SKIS0080" Txt="E' possibile non sollecitare un cliente anche se ha degli scaduti?"
Nell'anagrafica del cliente c'è un campo che ne definisce l'insollecitabilità a priori.
- \*\*Sai come stampare una lettera di sollecito?\*\*

 :  : VOC Id="SKIS0090" Txt="Sai come stampare una lettera di sollecito?"
Nel dettaglio movimenti da sollecitare con l'opzione interattiva per ottenere una singola lettera.
- \*\*Sai come stampare tutte le lettere di sollecito?\*\*

 :  : VOC Id="SKIS0100" Txt="Sai come stampare tutte le lettere di sollecito?"
Con l'apposita funzione batch nella gestione solleciti.
- \*\*Sai come si 'chiude' un sollecito?\*\*

 :  : VOC Id="SKIS0110" Txt="Sai come si 'chiude' un sollecito?"
Si chiude automaticamente quando il cliente paga una scadenza, al successivo giro di estrazione il programma lo capisce e flegga il sollecito come chiuso. E' possibile farlo anche manualmente in modifica sullo stato del singolo sollecito.
- \*\*Sai come addebitare delle spese di incasso su un sollecito?\*\*

 :  : VOC Id="SKIS0120" Txt="Sai come addebitare delle spese di incasso su un sollecito?"
Nella tabella C53 utilizzando il campo 'Spese amministrative sollecito'.
- \*\*Sai come annullare completamente un'estrazione di massa?\*\*

 :  : VOC Id="SKIS0130" Txt="Sai come annullare completamente un'estrazione di massa?"
Mediante l'apposita funzione da menu solleciti.
