- \*\*Come posso passare dai costi sul COSAR a quelli sul D5COSO?\*\*

 :  : VOC Id="10001" Txt="Come posso passare dai costi sul COSAR a quelli sul D5COSO?"
 Prima di tutto bisogna ricordare che i costi sul COSAR (SM) possono coesistere con quelli sul D5COSO (S2) (vedi FAQ seguente).
 Per avviare il modulo D0 bisogna impostare sulla tabella B£1 il campo 'Costi std' a S2 (si può utilizzare anche il comando UP VER
 per accedere alla B£1).
 Il menù da utilizzare non sarà più il CS00, ma il D000 e quindi anche le funzioni di lancio calcolo costi e di manutenzione saranno diverse.
 La nuova /COPY per i costi è la £G55, che sostituisce la £G17.

- \*\*Posso mantenere i costi sia sul COSAR sia sul D5COSO?\*\*

 :  : VOC Id="10002" Txt="Posso mantenere i costi sia sul COSAR sia sul D5COSO?"
 Sì. Una volta passati alla gestione dei costi versione S2, l'interfaccia costi capisce se un costo è presente sul COSAR
 o sul D5COSO a seconda della presenza o meno del tema nella tabella del tipo costo, quindi è il tipo costo che specifica dove reperire
 il costo.

- \*\*La £G17 non viene più utilizzata?\*\*

 :  : VOC Id="10003" Txt="La £G17 non viene più utilizzata?"
 La /COPY £G17 che recupera i costi di un articolo viene ancora utilizzata nel caso in cui nel tipo costo richiesto non sia stato specificato
 che il tipo costo è di tipo 'CS' (viene chiamata automaticamente dalla £G55)

- \*\*Posso usare la £G55 anche con i costi sul COSAR?\*\*

 :  : VOC Id="10004" Txt="Posso usare la £G55 anche con i costi sul COSAR?"
 Sì. Se in B£1 i costi standard sono impostati su SM viene chiamato il programma B£G55G_SM che richiama la £G17 (interfaccia costi
 che legge dal COSAR) e allo stesso modo se nella B£1 è indicato S2, ma nella tabella TCO ho indicato che il costo è di tipo CS.
