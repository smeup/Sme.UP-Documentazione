- \*\*Frase\*\*

 :  : VOC Id="00001" Txt="Frase"
È un elemento di testo da tradurre.
L'originale in italiano, estratto da Sme.UP, si trova nel file A£TROR0F.
- [A£TROR0F Traduzioni&-x3a; frasi origine (italiano](Sorgenti/OJ/FILE/A£TROR0F)
Le traduzioni nelle diverse lingue si trovano nel file A£TRDE0F.
- [A£TROR0F Traduzioni&-x3a; destinazione (traduzioni](Sorgenti/OJ/FILE/A£TRDE0F)

- \*\*Contesto\*\*

 :  : VOC Id="00002" Txt="Contesto"
È il posto all'interno di Sme.UP in cui viene utilizzata una frase.
Il contesto è costituito da : 
 \* Un oggetto di Sme.UP (es. OJ\*PGM/programma, OJ\*DSPF/video, MBSCP_SCH/script...);
 \* Un eventuale dettaglio aggiuntivo (es. nei programmi il nome della schiera in cui la frase è contenuta.
La stessa frase in diversi contesti può avere diverse traduzioni in una lingua.
Quindi, ad esempio : 
 \* La stessa frase nello stesso programma in due schiere diverse può avere due traduzioni diverse.
 \* La stessa frase nello stesso programma nella stessa schiera può avere una sola traduzione, perchè il massimo livello di dettaglio è la schiera.

- \*\*Ambito\*\*

 :  : VOC Id="00003" Txt="Ambito"
È un codice che identifica la "responsabilità" di una frase, se standard o a carico del cliente.
Sono previste due tipologie di ambiti : 
 \* 00 :  standard.
 \* >=10 :  personale.
Ambito consentito :  ambito utilizzabile in un determinato ambiente.
Ambito modificabile :  ambito che può essere modificato (estratto, tradotto) su una determinata macchina.
Per maggiori dettagli fare riferimento alla documentazione del modulo A£LING.

- \*\*Estrazione\*\*

 :  : VOC Id="00004" Txt="Estrazione"
Operazione che consiste nello scandire gli oggetti di Sme.UP al fine di individuare le frasi in italiano da scrivere nel file A£TROR0F. Sono le frasi che andranno tradotte.

- \*\*Preparazione\*\*

 :  : VOC Id="00005" Txt="Preparazione"
Operazione che consiste nel copiare le frasi italiane dal file A£TROR0F al file A£TRDE0F per una determinata lingua. Questo predispone l'archivio A£TRDE0F per la traduzione in quella lingua.

- \*\*Personalizzazione\*\*

 :  : VOC Id="00006" Txt="Personalizzazione"
Operazione che consiste nel copiare alcuni record nel file A£TRDE0F da un ambito 00 ad un ambito >=10, al fine di personalizzarne la traduzione. Questo può essere fatto solo per una determinata lingua.

- \*\*Generazione\*\*

 :  : VOC Id="00007" Txt="Generazione"
Operazione che consiste nel generare versioni in una determinata lingua degli oggetti che  non sono tradotti dinamicamente :  DSPF, MSGF, PRTF. Questo crea i nuovi sorgenti e li compila direttamente.

