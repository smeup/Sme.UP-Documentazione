### **Sai qual è l'archivio principale dei viaggi?**

L'archivio è il V5TRIP0F.
### **Sai quali sono le tabelle principali da Implementare?**

Le tabelle sono : 
V5T Tipo Viaggio
V55 Parametri Accantonamento e spedizione
GMO Tipo documento movimentazione
GMZ Tipo riga movimentazione
### **Sai come si imposta un Flusso di spedizione da viaggio?**

Il Flusso per emettere i documenti di spedizione (Bolle) da un viaggio prevede i seguenti passi : 
1. creazione testata viaggio (pgm V5AT11D, funzione NEWDOC, metodo CORD);
2. creazone righe da viaggio (pgm V5AT11E, funzione CORD, metodo U);
3. gestione testata Bolla (pgm V5DO15X, funzione DE, metodo 02);
4. stampa Bolla / Fattura (pgm V5BOFA)
5. collegamento magazzino (pgm V5DO15X, funzione CO).
### **Sai qual è la classe di autorizzazione per la gestione dei viaggi?**

La classe di autorizzazione è la V5TR01.
