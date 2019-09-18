- **Sai come generare il report di una vista di matrice?**

 :  : VOC Id="SKIBP010" Txt="Sai come generare il report di una vista di matrice?"
Tasto destro su tab della sezione e Visualizza come... PDF Matrice
- **Sai come generare il report di una matrice prodotta da un servizio?**

 :  : VOC Id="SKIBP020" Txt="Sai come generare il report di una matrice prodotta da un servizio?"
Richiama la funzione che genera l'XML della matrice con il componente REP anzichè EXB
- **Conosci la differenza fra le due domande precedenti?**

 :  : VOC Id="SKIBP030" Txt="Conosci la differenza fra le due domande precedenti?"
La prima utilizza le impostazioni visualizzate in quel momento, anche se modificate dall'utente. La seconda ripete da capo la chiamata e non considera eventuali setup utente caricati o modificati
- **Sai come cambiare i loghi di tutti i report prodotti?**

 :  : VOC Id="SKIBP040" Txt="Sai come cambiare i loghi di tutti i report prodotti?"
Modifica le variabili di Loocup LGO.001 e LGO.002. Di default queste variabili sono dirottate sull'immagine associata all' oggetto VO COD_SEL LGO.001
- **Sai come modificare il default delle impostazioni di setup del report?**

 :  : VOC Id="SKIBP050" Txt="Sai come modificare il default delle impostazioni di setup del report?"
Modificando l'oggetto J3 FRM.REP A01 nello script SCP_SCH/J3_SET_STD
- **Sai come si passa un setup di report da servizio?**

 :  : VOC Id="SKIBP060" Txt="Sai come si passa un setup di report da servizio?"
Inserendo nel XML restituito del servizio un nodo Setup/FRM con Type="REP"
- **Sai come visualizzare la toolbar che espone i bottoni per le funzioni Visu**

 :  : VOC Id="SKIBP070" Txt="Sai come visualizzare la toolbar che espone i bottoni per le funzioni Visualizza come...?"
Impostando ExtToolBar="Yes" sul  :  : G.SUB.MAT relativo alla matrice dati
- **Sai come impostare la copertina di un report?**

 :  : VOC Id="SKIBP080" Txt="Sai come impostare la copertina di un report?"
L'XML dei dati deve contenere una sezione Cover
- **Sai come usare la specifica  :  : S.FRM.REP per impostare il setup del report**

 :  : VOC Id="SKIBP090" Txt="Sai come usare la specifica  :  : S.FRM.REP per impostare il setup del report"
Bisogna "inscatolare" la sezione della matrice in una scheda o sottoscheda monosezione ed inserire la specifica  :  : S.FRM.REP fra  :  : I.SCH e  :  : G.SUB.MAT. Il setup verrà considerato eseguendo la funzione F(REP;\*SCO;) della scheda o sottoscheda in questione
- **Sai come generare un report con matrice Master e matrice Subreport**

 :  : VOC Id="SKIBP100" Txt="Sai come generare un report con matrice Master e matrice Subreport"
Va creata una scheda con una sezione matrice in cui viene aggiunta la riga  :  : G.SET.REP Type="Master"
ed una o più sezioni matrice in cui viene aggiunta la riga  :  : G.SET.REP Type="Subreport".
La matrice Master contiene un campo che serve come chiave per esplodere i subreport. Informazioni più dettagliate nella documentazione
