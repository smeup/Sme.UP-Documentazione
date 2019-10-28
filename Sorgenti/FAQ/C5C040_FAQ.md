### **Sai a cosa serve il controllo fatture passive?**

Ad effettuare la registrazione di una fattura di acquisto formandone la composizione partendo dalle bolle di acquisto, verificando la correttezza di quantità, prezzi, condizioni di pagamento, ecc.
### **Sai quali sono le tabelle che ne governano le funzioni di base?**

Generali
-  C56 Impost.base Contab.Docum.Pass.
-  C5Y Fonti Contab.docum.passivi
-  C6S Codici spese Controllo fatture

Non conformità
-  C6D Destinazione "NON conformità"
-  C6N Non conformità
### **Sai come attivare il controllo durante la registrazione contabile?**

Nella tabella C5D (registrazioni contabili) è presente un flag che abilita tale gestione.
### **Sai che riflessi ha il collegamento delle bolle ad una fattura verso i documenti?**

Sulle bolle vengono posti dei flag, i riferimenti della registrazione collegata, il protocollo assegnato alla registrazione. Vengono poi regitrati le quantità e i prezzi effettivi.
### **Sai se, una volta contabilizzata una fattura, è possibile eliminare il movimento e gli effetti del controllo?**

Purchè non siano stati stampati i registri IVA in definitivo, e la fattura non sia stata saldata parzialmente o totalmente, annullando il movimento contabile spariscono anche gli effetti sulle bolle collegate se nella tabella C51 viene impostato il flag 'Scollegamento documenti'.
### **Sai come interfacciare il controllo fatture con la gestione non conformità?**

Vista la complessità dell'argomento riferirsi alla documentazione dedicata all'argomento, raggiungibile nel documento di 'Controllo documenti/fatture'.
### **Sai come gestire il problema nel caso manchino bolle durante il controllo di una fattura?**

Effettuando la gestione bolle mancanti, previa impostazione dei parametri che la governano, richiamabile con F18.
### **Sai come inserire delle spese finanziarie eventualmente addebitate sulla fattura in controllo?**

Con la gestione spese aggiuntive, previa impostazione dei parametri che la governano, richiamabile con F18.
### **Sai come collegare singole righe di bolle su fatture diverse?**

Entrando in modifca della bolla e selezionando le singole righe, anzichè tutto il documento.
### **Sai a cosa servono le funzioni di differenza quantità e differenza prezzo?**

Servono a 'chiudere' il controllo su un documento qualora non si rilevino quantità e/o prezzi diversi da quelli previsti sulla bolla, e non si sia in presenza di bolle mancanti oppure di spese finanziarie aggiuntive.
### **Sai se è possibile modifiicare il collegamento già effettuato delle bolle ad una fattura?**

In modifica sulla registrazione, premendo il tasto F11 si accede al controllo dei documenti già collegati.
### **Sai se è possibile non effettuare il collegamento di bolle ad una fattura anche se presenti?**

Forzando la conferma con F6 senza effettuare nessuna selezione, se presenti bolle disponibili.
### **Sai se è possibile effettuare un pre-controllo delle bolle da contabilizzare?**

Abilitando la funzione di validazione bolle, da eseguire prima della contabilizzazione vera e propria.
### **E' possibile avere un elenco per fornitore delle bolle non ancora contabilizzate?**

Nelle interrogazioni fornitore o lista fornitori utilizzando la funzione Y con metodo L.
### **E' possibile controllare anche le note credito da ricevere durante la fase di controllo?**

Codificando un tipo fonte S11.
### **In caso di non conformità durante il controllo, sai se è possibile bloccare le scadenze della fattura?**

Viene proposto il blocco automatico, che si può però non effettuare tramite tasto funzione di sblocco.
### **Stampando i registri IVA in definitivo, sai se è poi possibile modificare la registrazione sulle parti relative al controllo?**

Si.
### **Sai come viene effettuata la risalita per reperire la contropartita contabile al termine del controllo?**

Si/No.
### **Sai come eliminare dal controllo eventuali bolle già fatturate ma non collegate a registrazioni?**

Nella registrazione contabile il valore residuo, non attribuito a documenti in attesa, viene associato  al conto presente nella Fonte £02 mancanti. Se si attiva questo campo il valore residuo viene  associato al conto di contropartita dell'ente (£17 dei dati di estensione dell'ente).
Nel caso non fosse presente rimane associato al conto mancanti.
