title: "Uhříněves i Vršovice. Podívejte se, kde se v Praze staví"
perex: "Zatímco v Praze 7 se od roku 2012 postavilo jen 11 nových domů, v Praze 10 jich vyrostlo přes čtyři stovky. Převažují mezi nimi rodinné domy."
published: "22. května 2018"
coverimg: "https://interaktivni.rozhlas.cz/brexit/media/cover.jpg"
coverimg_note: "Foto <a href='#'>ČTK</a>"
styles: []
libraries: [jquery, highcharts, datatables] #jquery, d3, d3v5, d3csv, highcharts, datatables
options: [noheader, nopic] #wide, noheader (, nopic)
---

Výstavbu v Praze řeší aktuálně projednávaný [Metropolitní plán](http://plan.iprpraha.cz/cs/metropolitni-plan). Podle plánů jeho projektanta, Institutu plánování a rozvoje (IPR), má „zastavit nekontrolované rozpínání zástavby do polí stanovením jasné hranice mezi městem a krajinou“. Praha se podle IPR nemá rozšiřovat, ale zahušťovat, například zastavováním takzvaných brownfieldů - „městské džungle“.

Jak se v hlavním městě stavělo v posledních letech, ukazuje následující mapa. Červeně jsou na ní vyznačeny domy postavené po roce 2012, modře ty starší. Je z ní patrné zastavovaní periferií a k Praze přidružených obcí.

<wide>
<iframe src="https://dev.datarozhlas.cz/nove-domy-map/" width="100%" style="height: 80vh;" frameborder=0></iframe>
</wide>
<div id="posunko"><i>Zdrojem dat je registr <a href="https://www.cuzk.cz/ruian/RUIAN.aspx">RÚIAN</a>. Mapa nemusí být stoprocentně přesná: u některých budov v registru chybí jejich obrysy, takže do mapy nemohly být zakresleny; na druhou stranou mohou být jako nové zakreslené i různé nástavby na stavávající nemovitosti.</i></div>

Výstavba od roku 2012 setrvale zrychluje. Loni se na území Prahy postavilo 1148 nemovitostí. V hlavním městě se však [čeká na výstavbu desítek tisíc bytů](https://www.irozhlas.cz/ekonomika/praha-byty-vystavba-povoleni_1712171713_mos).

<div id="graf"></div>

Vůbec nejmíň se staví na Praze 7, nejvíc na Praze 10. 

<table id="tabulka2" class="display" style="width:100%">
<thead>
<tr><th>Městská část</th><th>Počet nemovitostí</th></tr>
</thead>
<tbody>
<tr><td>Praha 10</td><td>429</th></tr>
<tr><td>Praha 14</td><td>291</th></tr>
<tr><td>Praha 22</td><td>290</th></tr>
<tr><td>Praha 6</td><td>289</th></tr>
<tr><td>Praha 20</td><td>251</th></tr>
<tr><td>Praha 12</td><td>248</th></tr>
<tr><td>Praha 15</td><td>217</th></tr>
<tr><td>Praha 5</td><td>204</th></tr>
<tr><td>Praha 13</td><td>194</th></tr>
<tr><td>Praha 21</td><td>192</th></tr>
<tr><td>Praha 4</td><td>183</th></tr>
<tr><td>Praha 8</td><td>176</th></tr>
<tr><td>Praha-Libuš</td><td>145</th></tr>
<tr><td>Praha-Slivenec</td><td>143</th></tr>
<tr><td>Praha-Kunratice</td><td>139</th></tr>
<tr><td>Praha-Řeporyje</td><td>136</th></tr>
<tr><td>Praha-Klánovice</td><td>135</th></tr>
<tr><td>Praha-Čakovice</td><td>116</th></tr>
<tr><td>Praha-Vinoř</td><td>107</th></tr>
<tr><td>Praha 18</td><td>104</th></tr>
<tr><td>Praha-Dolní Počernice</td><td>100</th></tr>
<tr><td>Praha 9</td><td>100</th></tr>
<tr><td>Praha-Kolovraty</td><td>92</th></tr>
<tr><td>Praha 16</td><td>86</th></tr>
<tr><td>Praha-Dolní Chabry</td><td>86</th></tr> 
<tr><td>Praha-Dolní Měcholupy</td><td>78</th></tr>
<tr><td>Praha-Dubeč</td><td>73</th></tr>
<tr><td>Praha 11</td><td>72</th></tr>
<tr><td>Praha-Ďáblice</td><td>70</th></tr>
<tr><td>Praha-Březiněves</td><td>65</th></tr>
<tr><td>Praha-Újezd</td><td>64</th></tr>
<tr><td>Praha-Benice</td><td>58</th></tr>
<tr><td>Praha-Suchdol</td><td>57</th></tr>
<tr><td>Praha-Koloděje</td><td>54</th></tr>
<tr><td>Praha 19</td><td>53</th></tr>
<tr><td>Praha-Zličín</td><td>50</th></tr>
<tr><td>Praha-Šeberov</td><td>48</th></tr>
<tr><td>Praha-Velká Chuchle</td><td>48</th></tr>
<tr><td>Praha-Křeslice</td><td>46</th></tr>
<tr><td>Praha-Lipence</td><td>45</th></tr>
<tr><td>Praha-Štěrboholy</td><td>44</th></tr>
<tr><td>Praha-Nebušice</td><td>44</th></tr>
<tr><td>Praha 2</td><td>40</th></tr>
<tr><td>Praha-Královice</td><td>40</th></tr>
<tr><td>Praha-Lysolaje</td><td>37</th></tr>
<tr><td>Praha-Běchovice</td><td>32</th></tr>
<tr><td>Praha 3</td><td>32</th></tr>
<tr><td>Praha-Petrovice</td><td>31</th></tr>
<tr><td>Praha-Zbraslav</td><td>31</th></tr>
<tr><td>Praha-Troja</td><td>20</th></tr>
<tr><td>Praha 17</td><td>19</th></tr>
<tr><td>Praha-Satalice</td><td>19</th></tr>
<tr><td>Praha-Přední Kopanina</td><td>15</th></tr>
<tr><td>Praha-Lochkov</td><td>13</th></tr>
<tr><td>Praha 1</td><td>13</th></tr>
<tr><td>Praha 7</td><td>11</th></tr>
<tr><td>Praha-Nedvězí</td><td>8</th></tr>
</tbody>
</table>
<br>

Nejvíc se staví rodinných domů.

<table id="tabulka" class="display" style="width:100%">
<thead>
<tr><th>Typ nemovitosti</th><th>Počet</th></tr>
</thead>
<tbody>
<tr><td>rodinný dům</td><td>3759</td></tr>
<tr><td>bytový dům</td><td>711</td></tr>
<tr><td>garáž</td><td>478</td></tr>
<tr><td>jiná stavba</td><td>212</td></tr>
<tr><td>víceúčelová stavba</td><td>114</td></tr>
<tr><td>stavba pro administrativu</td><td>97</td></tr>
<tr><td>stavba občanského vybavení</td><td>92</td></tr>
<tr><td>objekt k bydlení</td><td>79</td></tr>
<tr><td>stavba pro obchod</td><td>59</td></tr>
<tr><td>stavba pro rodinnou rekreaci</td><td>50</td></tr>
<tr><td>stavba pro výrobu a skladování</td><td>49</td></tr>
<tr><td>stavba technického vybavení</td><td>35</td></tr>
<tr><td>objekt občanské vybavenosti</td><td>19</td></tr>
<tr><td>stavba ubytovacího zařízení</td><td>15</td></tr>
<tr><td>stavba pro dopravu</td><td>7</td></tr>
<tr><td>zemědělská stavba</td><td>3</td></tr>
<tr><td>průmyslový objekt</td><td>2</td></tr>
<tr><td>skleník</td><td>2</td></tr>
</tbody>
</table>

Obecně se taky na levém břehu Vltavy staví míň než na pravém 1670 x 4113. Podle xx je to dáno metropolitním plánem: citace z repky.
