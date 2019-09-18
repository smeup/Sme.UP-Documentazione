- **Cosa è il componente GEO?**

 :  : VOC Id="10001" Txt="Cosa è il componente GEO?"

 E' il componente che permette di visualizzare dei marcatori su una mappa di google

- **Che sintassi viene usata?**

 :  : VOC Id="10002" Txt="Che sintassi viene usata?"

 :  : G.SEZ Pos(1)
 :  : G.SUB.GEO Tit="Mappa di google"

 :  : G.SET.GEO Zoom="7" Latitude="45,91294" Longitude="9,46472" LatCol="GEOLAT" LngCol="GEOLNG"
TitCol="GEOTIT"

 :  : D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;WETEST_GEO) 2(;;GEO_001)


Gli attributi Latitudine e Longitudine servono a centrare la mappa.
Non sono obbligatori perché il componente cerca di centrare automaticamente la mappa.

LatCol è la colonna contente la latitudine del marcatore
LngCol è la colonna contente la longitudine del marcatore

