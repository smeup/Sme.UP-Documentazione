- \*\*Sai a cosa servono i parametri di pianificazione?\*\*

 :  : VOC Id="SKIB0010" Txt="Sai a cosa servono i parametri di pianificazione?"
Ad indicare quale politica, con che vincoli sui lotti e con che leadtimes deve essere pianificato un articolo
- \*\*Sai dove si impostano le politiche di pianificazione?\*\*

 :  : VOC Id="SKIB0020" Txt="Sai dove si impostano le politiche di pianificazione?"
Si impostano nella tabella M5A
- \*\*Sai a cosa servono i periodi di raggruppamento?\*\*

 :  : VOC Id="SKIB0030" Txt="Sai a cosa servono i periodi di raggruppamento?"
Servono a cumulare i fabbisogni che debbon essere coperti con un solo riordino
- \*\*Sai come si impostano le risalite dei parametri di pianificazione?\*\*

 :  : VOC Id="SKIB0040" Txt="Sai come si impostano le risalite dei parametri di pianificazione?"
Dalla gestione parametri, mettendo ! nel campo "livello" si accede alla struttura di definizione e di risalita dei parametri di pianificazione

- \*\*Sai come si fa a fare una risalita a pettine, ossia che sostituisce parte \*\*

 :  : VOC Id="SKIB0050" Txt="Sai come si fa a fare una risalita a pettine, ossia che sostituisce parte dei parametri e non tutti?"
Si imposta nella tabella M51 il carattere "S" nel campo "tipo risalita" . Leggere help di tabella
- \*\*Sai come si impostano le risalite in un ambiente multiplant completo?\*\*

 :  : VOC Id="SKIB0060" Txt="Sai come si impostano le risalite in un ambiente multiplant completo?"
Si impostano con 6 livelli di risalita, i primi tre come per l'ambiente singolo plant, il 4,5 e 6, sono la risalita orizzontale del magazzino al campo "stringa" \*\*.
- \*\*Sai come si impostano i i leadtimes per il trasferimento tra plant?\*\*

 :  : VOC Id="SKIB0070" Txt="Sai come si impostano i i leadtimes per il trasferimento tra plant?"
I leadtimes per i trasferimenti tra plants si impostano nella tabella M5J
- \*\*Sai quali sono i campi che possono essere usati come ulteriore oggetto di \*\*

 :  : VOC Id="SKIB0080" Txt="Sai quali sono i campi che possono essere usati come ulteriore oggetto di rottura dei parametri di pianificazione?"
Sono la commessa (CM), la configurazione (CF), il fornitore (CNFOR) e l'esponente di modifica (EM)
- \*\*Sai come si fa a dire che tutti gli articoli di un fornitore hanno 20 gior\*\*

 :  : VOC Id="SKIB0090" Txt="Sai come si fa a dire che tutti gli articoli di un fornitore hanno 20 giorni di leadtime?"
Si imposta il leadtime sull'ultimo livello di risalita, per il fornitore specifico.
- \*\*Sai qual è la gerarchia di risalita dei parametri quando esiste un ulterio\*\*

 :  : VOC Id="SKIB0100" Txt="Sai qual è la gerarchia di risalita dei parametri quando esiste un ulteriore codice di rottura?"
E' la seguente  :  prima vengono risaliti i parametri con l'oggetto di rottura specificato, poi vengono risaliti i parametri per articolo. Quindi, se in qualche risalita si trova l'oggetto di rottura specificato, quello comanda !
- \*\*Sai qual è la politica di pianificazione per un articolo che non trova nei\*\*

 :  : VOC Id="SKIB0110" Txt="Sai qual è la politica di pianificazione per un articolo che non trova nei parametri nessuna indicazione?"
Quella che si trova sulla tabella M51 :  quella di produzione se l'articolo ha tipo parte 1 o 2. Quella di acquisto per gli altri tipi parte.
- \*\*Sai come si fa a deviare la lettura dei parametri su un'altro file?\*\*

 :  : VOC Id="SKIB0120" Txt="Sai come si fa a deviare la lettura dei parametri su un'altro file?"
Bisogna scrivere il pgm M5M5A0_xx, dove XX indica l'ambiente su cui si vuole deviare la lettura dei parametri di pianificazione, e poi impostare nella tabella B£1 , nel campo "parametri di pianificazione" il valore xx
- \*\*Sai come si fa a produrre il 70 % del fabbisogno e comprare il 30 % del re\*\*

 :  : VOC Id="SKIB0130" Txt="Sai come si fa a produrre il 70 % del fabbisogno e comprare il 30 % del resto?"
Nei parametri di pianificazione si impostano le due politiche, una di acquisto ed una di produzione e si specificano le percentuali
- \*\*In una pianificazione multiplant completa, sai come si fa a produrre in un\*\*

 :  : VOC Id="SKIB0140" Txt="In una pianificazione multiplant completa, sai come si fa a produrre in un plant un articolo che non è di sua competenza?"
Si imposta in uno dei livelli inferiori , 1, 2 o 3, per il plant specifico la politica di produzione, senza compilare la colonna con la politica di trasferimento
