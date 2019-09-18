- **Cosa è il componente **EDT**?**

 :  : VOC Id="10001" Txt="Cosa è il componente **EDT**?"
 E' il componente che permette di modificare il contenuto di membri di script su as400.

- **Come si può utilizzare all'interno di una scheda personalizzata?**

 :  : VOC Id="10002" Txt="Come si può utilizzare all'interno di una scheda personalizzata?"

Tramite la sintassi di componente :    :  : G.SEZ Pos(1)                      :  : G.SUB.EDT Tit="Mio Editor"        :  : D.FUN.STD F(EDT;\*EDTLET;LET) 1(MB;[file];[membro]) 2(OJ;\*LIB;[libreria])   
 oppure richiamato come fun da un altro componente (es. BTN)             
 F(EDT;\*EDTLET;LET) 1(MB;[file];[membro]) 2(OJ;\*LIB;[libreria])           
- **E' possibile inibire alcune funzionalità?**

 :  : VOC Id="10003" Txt="E' possibile inibire alcune funzionalità?"
 Si, agendo tramite configurazione del setup del componente tramite gli attributi :   -ReadOnly                                                                           -ShowOpen                                                                            -ShowSaveAs                                                                           -ShowInNewTab                                                                         -ShowExamine                                                                          -ShowRemoteHistory                                                                    -EnableToModifyFile                                                                   -EnableToModifyLibrary                                                                -EnableToModifyMember                                                                 Inoltre nella configurazione di Web.UP c'è un attributo che imposta il livello (USRLVL) che  compatibilemente a quello dell'utente Sme.UP abilita o meno la modifica dei membri.

- **E' presente un wizard che aiuti nella sinstassi?**

 :  : VOC Id="10004" Txt="E' presente un wizard che aiuti nella sinstassi?"
Sì, digitando CTRL+Barra spaziatrice viene mostrato un menu a tendina con gli attributi relativi al tag in cui ci si è posizionati col cursore.                                 Posizionandosi su una riga vuota, il comando di cui sopra mostrerà l'elenco dei tag.    Inoltre la bottoniera presenta la funzione 'Mostra attributi del tag' che permette di   visualizzare per ogni attributo del tag, i possibili valori.

- **E' possibile aprire contemporaneamente in modifica più di un membro?**

 :  : VOC Id="10005" Txt="E' possibile aprire contemporaneamente in modifica più di un membro?"
No, è possibile però aprirne 'n' in visualizzazione utilizzando la funzione da bottoniera di 'Esamina altro membro'
