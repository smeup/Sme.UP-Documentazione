- \*\*Cosa è il componente OPN?\*\*

 :  : VOC Id="10001" Txt="Cosa è il componente OPN?"
 E' il componente che permette di aprire file o cartelle, utilizzando il gestore predefinito in windows.

- \*\*Che sintassi viene usata?\*\*

 :  : VOC Id="10002" Txt="Che sintassi viene usata?"
 _R_F(OPN;PATH;) 1(J1;PATHFILE; percorso del file)  oppure _R_F(OPN;PATH;) 1(J1;PATHDIR; percorso di cartella) 

- \*\*E' possibile scaricare una risorsa 'file' web?\*\*

 :  : VOC Id="10003" Txt="E' possibile scaricare una risorsa 'file' web?"
Si, tramite sintassi: F(OPN;PATH;) 1(J1;URL;http://www.server.com/nomefile.xxx)

- \*\*Come si può aprire il client di posta tramite OPN?\*\*

 :  : VOC Id="10004" Txt="Come si può aprire il client di posta tramite OPN?"
Mediante sintassi :  F(OPN;PATH;) 1(J1;URL;mailto : <indirizzo mail>)

- \*\*Come si può aprire modulo 'telefono' su smartphone tramite OPN?\*\*

 :  : VOC Id="10005" Txt="Come si può aprire modulo 'telefono' su smartphone tramite OPN?"
Mediante sintassi :  F(OPN;PATH;) 1(J1;URL;tel : <numero di telefono>)
