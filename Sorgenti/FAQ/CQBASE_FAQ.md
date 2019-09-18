- \*\*Cosa avviare e perchè?\*\*

 :  : VOC Id="10001" Txt="Cosa avviare e perchè?"
 I moduli del Q9000 si possono avviare singolarmente anche in tempi differenti a seconda delle esigenze.
 Alcuni moduli non prevedono agganci/interfaccie con il resto del sistema informativo; in caso di primo approccio con il cliente non
 Sme.UP l'avvio di uno di questi moduli potrebbe essere propedeutico alla conoscenza degli standard, tabelle, note, autorizzazioni, ecc. : 
 \* STRUMENTI DI MISURA
 \* GESTIONE DOCUMENTAZIONE
 \* GESTIONE PERSONALE
 \* MANUTENZIONE IMPIANTI

- \*\*E' possibile avviare solo alcuni moduli dell'applicazione Q9000?\*\*

 :  : VOC Id="10002" Txt="E' possibile avviare solo alcuni moduli dell'applicazione Q9000?"
 I moduli del Q9000 si possono avviare singolarmente, anche se sono previsti alcuni link tra i vari moduli dell'applicazione.
 Il modulo DOCU Gestione Documenti è in relazione con tutti gli altri; in caso non lo si voglia utilizzare è necessario codificare
 un documento fittizio '\*\*' (oppure modificare B£CQ70).
 Il modulo ACMC Gestione Strumenti di Misura è in relazione con CCOL-Cicli di Collaudio, RILI-Rilievi e Misure (anche in questo caso
 è necessario codificare una Categoria strumenti fittizia \*\*. oppure modificare il programma interfaccia B£IFST_SM).
 Il modulo VEND Vendor Rating consente la valutazione Fornitori e si basa sui dati raccolti in accettazione materiali (modulo LOTT)
 per la parte relativa alla Qualità delle Consegne (Lotti Scarto, accettati, deroga, ecc.).
 La mancata attivazione del suddetto modulo ovviamente non permette il calcolo automatico del Vendor Rating.

- \*\*Non trova elementi in tabella?\*\*

 :  : VOC Id="10003" Txt="Non trova elementi in tabella?"
 E' possibile che elementi di tabella non vengano trovati nel relativo sottosettore.
 E' necessario verificare gli eventuali sottosettori esistenti e controllare la metodologia di risalita
 definita nalla definizione di tale tabella con sottosettore 'bianco' secondo la documentazione 'Definizione tabelle'.

- \*\*Il tipo lotto non si fasa?\*\*

 :  : VOC Id="10004" Txt="Il tipo lotto non si fasa?"
 Il tipo lotto che viene riportato nella non conformità è quello che viene riportato nel tipo lotto che non è quello usato nelle V5D che
 è di 3 caratteri contro i 2 del precedente.

- \*\*Dove viene gestita la politica di accorpamento dei lotti?\*\*

 :  : VOC Id="10005" Txt="Dove viene gestita la politica di accorpamento dei lotti?"
 La politica di accorpamento dei lotti è molto importante e viene gestita attraverso la tabella CQ1.
 In questa è presente il campo **Raggr. Articoli Acq.** che gestisce la politica.
 Per ulteriori informazioni vedi help tabella.





