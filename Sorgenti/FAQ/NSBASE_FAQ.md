- **Sai come si installano smens e smedg su AS400?**

 :  : VOC Id="SKIAA010" Txt="Sai come si installano smens e smedg su AS400?"
Tramite l'utilità Sme.UP UT3, quindi tramite UP UT3 da riga comando AS400
- **Sai come si installano differenti release di smens e/o smedg sullo stesso **

 :  : VOC Id="SKIAA020" Txt="Sai come si installano differenti release di smens e/o smedg sullo stesso AS400?"
Gestendo il parametro "Path specifico £G53" nella tabella JA1
- **Sai dove si trova il file di configurazione di smens?**

 :  : VOC Id="SKIAA030" Txt="Sai dove si trova il file di configurazione di smens?"
Nella cartella smens relativa all'installazione
- **Sai come si chiama il file di configurazione di smens?**

 :  : VOC Id="SKIAA040" Txt="Sai come si chiama il file di configurazione di smens?"
Configurazione.cfg
- **Sai come impostare il server di posta per l'invio delle mail tramite /copy**

 :  : VOC Id="SKIAA050" Txt="Sai come impostare il server di posta per l'invio delle mail tramite /copy G53?"
Attraverso il parametro MailServer del file di configurazione
- **Sai che è possibile gestire differenti file di configurazione di smens da **

 :  : VOC Id="SKIAA060" Txt="Sai che è possibile gestire differenti file di configurazione di smens da utilizzare a scelta?"
E' possibile tramite il parametro £G53CF della /copy £G53 si può passare, per la singola chiamata, uno specifico file di configurazione che verrà utilizzato per quella singola chiamata
- **Sai che nella generazione PDF è possibile utilizzare dei font personalizza**

 :  : VOC Id="SKIAA070" Txt="Sai che nella generazione PDF è possibile utilizzare dei font personalizzati?"
Posizionandoli nella cartella Fonts presente, o da creare, nella cartella smedg. Chiamandoli con prefisso P*_ possono poi essere riferiti con la lettere che verrà messa al posto del * alla stregua dei font standard
- **Sai come si attivano i log di smens e smedg?**

 :  : VOC Id="SKIAA080" Txt="Sai come si attivano i log di smens e smedg?"
Attraverso i bottoni appositi presenti nella scheda del modulo NSBASE o creando direttamente su AS400 la cartella logs nella cartella Smeup, posizionandovi un file di nome logsmedg.yes per attivare i log di smedg ed un file logsmens.yes per i log smens. Il file saranno distinti per utente
- **Sai come interrogare i file di log di smens e smedg?**

 :  : VOC Id="SKIAA090" Txt="Sai come interrogare i file di log di smens e smedg?"
Attraverso la voce di menù specifica della scheda NSBASE o direttamente aprendoli come file di testo
- **Sai che relazione esiste fra /copy £G53, smens e smedg?**

 :  : VOC Id="SKIAA100" Txt="Sai che relazione esiste fra /copy £G53, smens e smedg?"
La /copy £G53 è il programma RPG che fornisce diverse funzionalità di eterogenea finalità, fra queste funzionalità ne esisteno qualcuno che utilizzano delle classi java. Queste classi java sono conosciute come smens e smedg
- **Sai come attivo il file di trace della /copy £G53?**

 :  : VOC Id="SKIAA110" Txt="Sai come attivo il file di trace della /copy £G53?"
Attraverso i bottoni appositi presenti nella scheda del modulo NSBASE o creando direttamente su AS400 la cartella trace nella cartella Smeup, posizionandovi un file di nome traceG53.yes per attivare i log di smedg e smens. Il file è unico per utente per entrambe le funzionalità ed è in formato CSV
- **Sai come interrogare i file di trace della /copy £G53?**

 :  : VOC Id="SKIAA120" Txt="Sai come interrogare i file di trace della /copy £G53?"
Attraverso la voce di menù specifica della scheda NSBASE o direttamente aprendoli come file CSV
- **Sai come inviare una mail con la G53?**

 :  : VOC Id="SKIAA130" Txt="Sai come inviare una mail con la G53?"
Tramite la funzione MAILTO
- **Sai che differenza esiste fra MAILTO e MAILTO/AS400 della /copy G53?**

 :  : VOC Id="SKIAA140" Txt="Sai che differenza esiste fra MAILTO e MAILTO/AS400 della /copy G53?"
La prima invia la mail tramite un server smens che dev'essere attivo su una macchina Windows, mentre il secondo invia la mail direttamente tramite lo smens presente sull'AS400.
- **Sai come inviare ad una lista di destinatari una mail tramite /copy G53?**

 :  : VOC Id="SKIAA150" Txt="Sai come inviare ad una lista di destinatari una mail tramite /copy G53?"
Creando un file sull'IFS dell'AS400 contenente l'elenco degli indirizzi (uno per riga) e poi inserendo nel campo B£G53EM della /copy G53 il percorso IFS del suddetto file
- **Sai come inviare una mail in formato HTML tramite /copy G53?**

 :  : VOC Id="SKIAA160" Txt="Sai come inviare una mail in formato HTML tramite /copy G53?"
Creando un file su IFS contenente il codice HTML del corpo della mail e poi inserendo nel campo B£G53TX il percorso IFS del suddetto file preceduto del tag -TEXT-
- **Sai come inviare una mail con allegati multipli tramite /copy G53?**

 :  : VOC Id="SKIAA170" Txt="Sai come inviare una mail con allegati multipli tramite /copy G53?"
Creando un file sull'IFS dell'AS400 contenente l'elenco dei percorsi dei file da allegare (uno per riga) e poi inserendo nel campo B£G53AT della /copy G53 il percorso IFS del suddetto file preceduto dal tag -TEXT-
- **Sai come inviare una mail con destinatari in Copia Conoscenza?**

 :  : VOC Id="SKIAA180" Txt="Sai come inviare una mail con destinatari in Copia Conoscenza?"
Utilizzando il campo B£G53CC. Per gli indirizzi multipli vale il discorso sui destinatari multipli descritto in AA150
