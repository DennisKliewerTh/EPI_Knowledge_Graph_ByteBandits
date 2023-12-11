"""
Copyright (C) 2023 TH Köln – University of Applied Sciences

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

from GraphModel.Graph import Graph
from GraphModel.Node import Node


class GraphContent:

    def __init__(self, graph: Graph):
        self.create_demo_nodes(graph)

    def create_demo_nodes(self, graph):


        steve_jobs = Node("Steve Paul Jobs war ein Unternehmer und begeisterter Elektroniker, er gründete"
                          " sowohl die Firma Apple, als auch viele weitere Marken wie zum Beispiele NeXT Computer.\n\n"
                          " Geboren wurde Steve Jobs am 24. Februar 1955 in San Francisco in Kalifornien in den USA."
                          " Er hatte Syrische und amerikanische Wurzel, doch er wurde sofort nach seiner Geburt von"
                          " seinen leiblichen Eltern zur Adoption freigeben. Adoptiert wurde Steve Jobs von seinen"
                          " neuen Eltern Paul und Carla Jobs. Bereits in seiner Kindheit war Jobs stark an der"
                          " Elektronik interessiert.\n\n Gestorben ist Steve Jobs am 5. Oktober im Jahr 2011 in Palo Alto,"
                          " Kalifornien, USA. Durch seine Krebserkrankung wurde er gerade mal 56 Jahre alt.\n\n Seine"
                          " adoptiv Eltern waren zwar keine Akademiker doch es war ihr Wunsch Steve die Möglichkeit"
                          " zu bieten Studieren zu gehen. Steve Jobs Studierte also später Kalligrafie, brach das"
                          " Studium aber nach den ersten 6 Monaten ab. Trotz dessen besuchte Jobs weiterhin"
                          " vereinzelte Vorlesungen, bis er nach ca. 1.5 Jahren das Studium endgültig abbrach.\n\n"
                          " Steve Jobs Eröffnete mit seinen damaligen Nachbarn Steve Wozniak und Ronald Wayne ein"
                          " Freund von Jobs, am 1. April 1976 Apple Computers in der Garage seiner Eltern. Diese"
                          " Firma leitete er auch bis 1985, doch aufgrund von internen Streitigkeiten verließ"
                          " er Apple für wenige Jahre und verfolgte andere Ziele.\n\n In dieser Zeit gründete er NeXT"
                          " im Jahr 1986, ein Computerunternehmen was jedoch nie einen großen Erfolg feierte."
                          " 1993 verkaufte Jobs die Firma an den Investor Canon.\n\n Parallel zur Gründung von NeXT"
                          " investierte Jobs auch noch in das Computertrickfilm-Studio Pixar, Wechsel"
                          " am 24. Januar 2006 an Disney verkauft wurde.\n\n  Im Jahre 1996 kaufte dann Apple"
                          " die Firma NeXT für ca. 402 Millionen US-Dollar, kurz darauf"
                          " kehrte Steve Jobs zurück zu Apple. Nach wenigen Monaten wurde dann auch der Damalige"
                          " Apple CEO Gil Amelio entlassen und Jobs wurde CEO von Apple.\n\n Bis zum 24. August 2011"
                          " blieb Steve Jobs der CEO von Apple. Doch er übergab diese Aufgabe an Tim Cook, da"
                          " Jobs aus gesundheitlichen Gründen nicht weiter Arbeiten konnte. Ab dem 24. August war"
                          " er trotzdem Vorsitzender des Verwaltungsrats und blieb dies auch bis"
                          " zu seinem Tod am 5. Oktober.\n","Steve Jobs", "Steve_Jobs.jpg")

        steve_wozniak = Node("Steve Wozniak oder auch „The Woz“ genannt war ein Elektriker und Unternehmer,"
                             " geboren wurde Steve Wozniak am 11. August 1950 im Silicon Vally, in Kalifornien, USA."
                             " Bekannt wurde Wozniak durch die Mitgründung der Firma Apple. Außerdem war Wozniak ein "
                             "Mitglied und später auch Präsident des Bekannten Homebrew Computer Clubs.\n\nWozniak hatte"
                             " polnische Vorfahren und sein Vater war Ingenieur bei Lockheed. Mit bereits 11 Jahren"
                             " baute Wozniak sein eigenes Radio und hatte eine Funker-Lizenz. Mit 13 Jahren baute"
                             " Wozniak seinen eigenen Taschenrechner und gewann damit auch Preise.\n\nSeinen ersten"
                             " Computer baute er mit 19 Jahren gemeinsam mit Bill Fernandez, es war der Cream"
                             " Soda Computer.\n\nSteve Wozniak studierte ab 1972 Elrktronik zuerst an"
                             " der Universität von Colorado, dann in DeAnza und zuletzt in Berkley. Nebenbei arbeitete"
                             " er bei der Firma Hewlett-Packard (HP) wo er auch maßgeblich an der Entwicklung des"
                             " HP 35 beteiligt war. Der HP 35 war der erste Weltweite wissenschaftliche "
                             "Taschenrechner.\n\n"
                             "Außerdem erfand Wozniak in seiner Freizeit die Blue Box, diese war ein Telefon, mit"
                             " welches man Kostenlos in der ganzen Welt telefonieren konnte. Jedoch war dieses"
                             " Verfahren illegal weshalb er es auch nicht weiter verfolgte.\n\nSpäter bat ihm sein"
                             " Freund und Nachbar Steve Jobs ihn bei ein Projekt zu helfen, Jobs sollte ein Spiel"
                             " Entwickeln und hatte dafür nur 3 Tage Zeit. Wozniak half ihn und entwickelte so das"
                             " Spiel Breakout für Atari, Jobs versprach Wozniak die Hälfte des Lohns, doch anstatt"
                             " ihn die 2500 $ zu zahlen, zahlte Jobs nur 350 $ und erzählte Wozniak, dass er"
                             " nur 700 $ von Atari erhielt.\n\nSpäter am 1. April 1976 Gründete Wozniak und Steve Jobs"
                             " gemeinsam mit Ronald Wayne die Marke Apple. Das erste Produkt also der Apple 1 wurde"
                             " zudem allein von Wozniak entwickelt, es war der erste Massen hergestellte Computer und"
                             " musste noch selber zusammen gebaut werden.\n\nAufgrund des Erfolges bat Steve Jobs Wozniak"
                             " einen weitern Computer zu entwickeln, diesmal war es der Apple 2, es war der"
                             " letzte bekannte Computer, der von einer Person entwickelt wurde.\n\nIm Jahre 1985 verließ"
                             " Wozniak Apple teilweise, aufgrund von Meinungsverschiedenheiten, doch er gilt immer"
                             " noch als Mitarbeiter bei Apple mit einen Festen Gehalt und einer Mitarbeiternummer."
                             " Im selben Jahr wurde er außerdem vom damaligen US-Präsident Ronald Reagan mit der"
                             " National Medal of Technology ausgezeichnet.\n\nAb diesen Zeitpunk konzentrierte sich"
                             " Wozniak auf sein neues Unternehmen CL 9, welches Universalfernbedienungen Entwickelte"
                             " und auf Unterrichten von Schülern.","Steve Wozniak", "Steve_Wozniak.jpg")

        apple = Node("Apple ist ein amerikanisches Unternehmen mit Hauptsitz in Cupertino in Kalifornien."
                     " Apple wurde von Steve Jobs, Steve Wozniak und Ronald Wayne in der Garage von Steve Jobs"
                     " Eltern gegründet, dies geschah am 1. April 1972. Apple ist bekannt für die Herstellung von"
                     " Computern, Smartphones, Tablets und noch vieler weiteren Unterhaltungselektronik.\n\nAktuell wird"
                     " die Firma von Tim Cook geleitet, er übernahm die Führung ab dem 24. August 2011, da an diesem"
                     " Datum der Gründer und CEO Steve Jobs starb.\n\nZu den bekanntesten Technologien gehört das iPhone,"
                     " der Macintosh, das MacBook und der iMac. Aber auch Kopfhörer und Uhren gehören zu den"
                     " bekanntesten Produkten. Apple verkauft zudem auch Musik, Filme und Software. Unter der"
                     " Software iTunes und die neue Software Apple Musik ermöglicht Apple die Neuzeit des"
                     " Musikstreaming. Tausende von Künstler können so ihre Musik vermarkten und somit"
                     " Geld einnehmen.\n\n Doch nicht nur die Musik Branche ist ein Erfolg auch mit"
                     " der Software App Store, ermöglicht es Apple Programmierer aus der ganzen Welt"
                     " ihre Apps, seien es Spiele oder Dienstleister zu vermarkten. Darüber hinaus zählt"
                     " der App Store zu den Zweitgrößten App Markt der Welt.\n\nIm Jahre 2007 entscheid sich dann"
                     " Apple ein Smartphone zu veröffentlichen, dieses Handy setzt in einigen Richtungen bis heute"
                     " den Standard und Revolutionierte die Smartphone-Welt.\n\nAktuell hat Apple einen Marktwert"
                     " von 2,95 Billionen USD stand 27.11.2023. Damit zählt Apple zu den Größten Unternehmen"
                     " der Welt, teilweise war es das Wertvollste Unternehmen der Welt.\n\n Bekanntheit erlangte Apple"
                     " durch die Entwicklung des Apple 1 und des Apple 2, beide Computer wurden vom Mitgründer"
                     " Steve Wozniak entwickelt. Sie waren die letzten Computer, die von einer Person"
                     " entwickelt wurden.\n\nWeitere bahnbrechende Entwicklungen waren zum Beispiel die Erfindung vom"
                     " Touchscreen für das Smartphone. Es wurde 2007 mit den iPhone 2G vorgestellt und wird bis"
                     " heute in den Smartphones verbaut.\n\n Mit rund 161000 Mitarbeitern weltweit gilt Apple"
                     " als einer der größten Arbeitgeber der Welt. Allein in Europa hat Apple ca. 22000"
                     " Mitarbeiter und durch verschiedene Zulieferer und durch den App Store kommt Apple"
                     " auf 1,76 Millionen Arbeitsplätze in Europa, die durch diese Marke geschaffen werden.\n\n Aber"
                     " auch in der Smartphone-Branche gehört Apple zu den Giganten, Apple gehört zu den 3 größten"
                     " Smartphone Herstellern der Welt und macht einen Marktanteil von 14,3 % stand Juni 2021 aus."
                     " Nur Samsung und Xiaomi haben mit 15,7 % und 17,1 % mehr Marktanteile.","Apple", "Apple_Logo.jpg.webp")

        software = Node("Bei Software handelt es sich anderes als bei Hardware um sogenannte in materielle Ware,"
                        " das heißt man kann die Ware nicht Physisch sehen oder Berühren.\n\nMan teilt Software in"
                        " mehreren Unterkategorien auf, da wäre zu einem die Middleware, die Systemsoftware, die"
                        " Anwendungssoftware, die Standardsoftware, die Individualsoftware, die Systemgebundene"
                        " Software und die Plattformunabhängige Software.\n\nBei der Middleware handelt es sich um"
                        " Programme die als Kommunikationsschnittstelle zwischen System und Anwendungssoftware"
                        " agiert.\n\nDie Systemsoftware ist die Verbindung zwischen Hardware und Software da, es sind"
                        " alle Abläufe, die für den Betrieb des Rechners notwendig sind.\n\nBei der Anwendungssoftware"
                        " handelt es sich um Programme, die den User sein Leben erleichtern sollen, bspw. dafür"
                        " wäre z.b. Textverarbeitungsprogramme wie Word aber auch Computerspiele.\n\nStandardsoftware "
                        "ist Software, die man für einen normalen Preis kaufen kann und nur begrenzt"
                        " individualisieren kann.\n\nIndividualsoftware ist eine Software, die speziell für den"
                        " Kunden programmiert wurde.\n\nSystemgebundene Software ist Software die beispielsweise"
                        " nur auf Windows Computer funktioniert, ein Beispiel wäre Safari, dieser geht nur auf Unix.\n\n"
                        "Plattformunabhängige Software ist das Gegenteil von Systemgebundene Software, sie"
                        " funktioniert auf allen Betriebssysteme.","Software")

        hardware = Node("Bei Hardware handelt es sich anders als bei Software um materielle Ware."
                        " Sie ist das Gegenstück zur Software aber genauso wichtig wie die Software, da"
                        " nur mit beiden Teilen ein Computer bedien fähig ist.\n\nEin Beispiel für Hardware"
                        " wäre zum Beispiel die CPU also der Prozessor des Computers, aber auch ein CD"
                        " Laufwerk zählt zur Hardware.\n\nMan unterscheidet Hardware in die folgenden zwei"
                        " Hardwaregruppen.Zuerst gibt es die Zentraleinheit, hierzu zählt man alles, was nötig"
                        " ist damit ein Computer funktioniert.\n Hierzu würde man dann die Verarbeitungsgeräte zählen,"
                        " da diese für die Hauptarbeit des Computers zuständig sind. Ein paar Beispiele für"
                        " diese Geräte wären zum Beispiel die CPU, der Arbeitsspeicher aber auch die Grafikkarte."
                        "Außerdem zählen auch die Speichergeräte zu der Zentraleinheit, da die Daten irgendwo"
                        " gespeichert und wieder abgerufen werden müssen. Hierzu zählt sowohl der USB-Stick als"
                        " auch die interne Festplatte.\nDie Zweite Gruppe wird auch Peripherie genannt, hiermit"
                        " sind alle gerate gemeint die an den Computer angeschlossen werden. Auch hier würde man"
                        " die Speicher Geräte dazu Zählen, da es auch externe Festplatten gibt, das heißt die"
                        " Festplatte wird per USB-Anschluss mit dem Computer verbunden.\nNatürlich gibt es aber"
                        " auch die Eingabe und Ausgabe Geräte. Die Eingabe Geräte sind die Geräte, mit der man"
                        " den Computer einen Befehl geben kann, dazu würde dann die Tastatur, die Maus aber auch"
                        " das Mikrofon zählen. Die Ausgabe gerate sind das Gegenstück dazu, hier werden unsere"
                        " Daten anhand eines zum Beispiel Monitors oder Drucker bildlich wiedergegeben.","Hardware")

        homebrew = Node("Der Homebrew Computer Club entstand am 5. März 1975 und wurde in einer Garage in "
                        "Kalifornien gegründet. Den Anstoß zur Gründung des Computer-Clubs gab der Damals neue "
                        "Atari 8800 Computer, diesen Computer konnten sich damals auch normale Bürger leisten.\n\n"
                        "Bei den treffen des Homebrew Computer Clubs treffen sich abends gegen 7 Uhr ca. 32 junge "
                        "Männer die alle das gleiche Hobby hatten, das Tüfteln mit der Technik. Da der Club schnell "
                        "an Begeisterung erlangte, wurde die Location immer größer, so war es nicht mehr die Garage, "
                        "sondern ein Hörsaal der SLAC.\n\nDie Teilnehmer Anzahl lag teilweise bei 240 Teilnehmern. Es "
                        "wurden Lochstreifen gemeinsam erstellt aber auch getauscht, um erlangte "
                        "Erfahrung weiterzugeben. Es wurde Software geteilt und verglichen, aber auch selbstgebaute "
                        "Hardware wurde den Mitgliedern gegenseitig vorgestellt.\n\nSo stellten Steve Jobs und Steve "
                        "Wozniak im Jahr 1976 erstmalig den Apple 1 Computer vor. Durch diese Erfindung erlangte "
                        "er Club ein großes Aufsehen.\n\nDoch zu den nennenswerten Mitgliedern gehörten nicht nur die "
                        "beiden Apple Gründer Steve Jobs und Steve Wozniak. Auch der Microsoft Gründer Bill Gates "
                        "war ein Mitglied des Homebrew Computer Clubs. Des Weiteren waren auch Lee Felsstein und Bob "
                        "Marsh Mitglieder des Clubs, beide trugen Maßgeblich zur heutigen Entwicklung des Computers"
                        " bei."
                        ,"Homebrew Computer Club")

        next = Node("NeXT Computer war eine Firma des Apple Gründer Steve Jobs. Er gründete die Firma"
                    " im Jahr 1985, da er aufgrund von Streitigkeiten Apple für wenige Jahre verlassen musste.\n\n"
                    "NeXT Computer war Steve Jobs zweite Möglichkeit Computer zu entwickeln und somit die Informatik"
                    " zu revolutionieren. Doch diese wurde durch eine Rechtsstreitigkeit zwischen Apple und"
                    " Steve Jobs erschwert. Durch diese Streitigkeit hatte NeXT die Auflage, Apple einen Einblick"
                    " in die Entwicklung des NeXT Computers zu liefern und auch keine Computer vor Juli 1987 zu"
                    " veröffentlichen.\n\nAnders als bei den Apple Computern hatte Steve Jobs die Höher gebildeten"
                    " Menschen als Zielgruppe, sie sollten also Akademiker sein.\n\nDas Betriebssystem des NeXT"
                    " Computer wird NeXTSTEP genannt und basiert auf Unix.\n\nDoch ein richtiger Erfolg war NeXT"
                    " Computer nie, man vermutet, dass gerade mal 50000 Rechner in der Zeit von 1985 bis 1989"
                    " Verkauft wurden. Vergleicht man diese Zahl mit den heutigen Apple die im Jahr 2022 über"
                    " 27,91 Millionen Mac Computer verkauft haben, so erkennt man den Misserfolg.\n\nZum Schluss"
                    " von NeXT Computer wurde die Firma 1996 für 402 Millionen US $ von Apple gekauft und"
                    " dient heutzutage als Basis der Betriebssysteme Mac, OS, X und iOS.", "Next")

        apple_m1 = Node ("Am 10. November 2020 stellte Apple in Cupertino, Kalifornien USA den ersten jemals"
                         "von Apple gebauten Prozessor speziell für die Mac Reihe vor.\n\nApple Silicon\nBei den M1 Chip"
                         " handelt es sich um ein SoC oder auch System on a Chip System. Ein SoC"
                         " vereint mehrere leistungsstarke Technologien auf einen Chip, so wurden früher jemals"
                         " ein Chip für zum Beispiel die CPU oder den In und Output benötigt. Durch den Apple M1"
                         " benötigt man nur noch einen einzigen Chip der alle Aufgabe umfasst.Der M1 ist der erste"
                         " Chip, der mit der 5 Nanometer Prozessor Technologie gebaut wurde. Der Chip umfasst"
                         " 16 Milliarden Transistoren, soviel gab es noch nie auf ein Chip. Vergleicht man"
                         " diese Daten mit den damals aktuellen Intel Core i7 so brauchte Intel eine große"
                         " von 14 Nanometer und hat gerade mal 10.3 Milliarden Transistoren.\n\nMit den Apple"
                         " M1 Chip, hat Apple einen neuen Bestwert für die Leistung pro Watt erreicht. Der M1"
                         " ist eine 8 Core Cup, die Aufteilung bei Apple sieht vor, dass 4 Kerne für hohe"
                         " Effizient stehen und die andren 4 Kerne für eine hohe Leistung sorgen. Durch"
                         " dieses Zusammen spiel der Kerne können leichte Aufgabe so schnell wie möglich"
                         " bearbeitet werden und das mit sowenig Strom Verbrauch wie nur möglich.\n\n Auch hat"
                         " Apple die Neutral Engine in den M1 verbaut. Dieser Chip ermöglicht es das"
                         " maschinelle Lernen und die KI (Künstliche Intelligenz) Algorithmen stark zu"
                         " optimieren. Dadurch kann zum Beispiel die Wärmedämmung bei ML (Maschinelles Lernen)"
                         " oder KI Berechnungen verbessert werden. Der Chip besteht aus 16 Kernen und schafft"
                         " es über 11 Billionen Berechnungen pro Sekunde zu lösen. Der Chip ist dabei keine"
                         " Neuheit von Apple, jedoch wurde er das erstmal in einen Mac verbaut.\n\nDer M1 hat"
                         " auch einen Integrierten Graphic Power Unit Chip oder auch GPU genannt. Auch dieser"
                         " Chip besteht aus 8 Kernen, diese können ca. 25000 Threads gleichzeitig erledigen.\n\n "
                         "Bis heute hat Apple zwei weitere CPU Generationen vorgestellt, der Apple M2 und der"
                         " Apple M3, außerdem gibt es die verschiedenen CPUs in verschiedenen Upgrades. Es gibt zu"
                         " einem die Pro-Variante, diese bietet nochmal mehr Leistung und dann gibt es noch die"
                         " Max oder Ultra Variante. Die Max und Ultra Variante ist dabei die leistungsstärkste"
                         " Variante und kostet dementsprechend auch mehr Geld.","Apple M1")


        apple_1_computer = Node ("Der Apple 1 war Apples erste Technologie und wurde im Jahr 1975 vom"
                                 " Mitgründer Steve Wozniak selber erfunden und gebaut. Der erste Prototyp wurde"
                                 " am 1976 beim Homebrew Computer Club vorgestellt.\n\nDas Design des Apple 1 war ein"
                                 " Holzkasten, der noch selber vom Kunden zusammen gebaut werden musste. "
                                 "Des Weiterem kam kein Ausgabegerät in Form eines Bildschirms dazu, das heißt"
                                 " man hatte noch weitere Kosten als die üblichen 666,66 $.\n\nEs war der Weltweit"
                                 " erste Personal Computer, jedoch brauchte man Elektronik oder Informatik"
                                 " Kenntnisse, da man den Computer noch selber zusammen bauen musste.\n\nDer Erfolg"
                                 " des Apple 1 lies nicht auf sich warten, so kaufte der damalige Computer"
                                 " Händler Byte Shop 50 der Apple 1 Computer. Aufgrund dessen mussten Steve Jobs"
                                 " und Steve Wozniak ihren ersten Mitarbeiter Daniel Kottke einstellen, dieser"
                                 " sollte die Computer zusammen bauen.\n\nDer Apple 1 konnte nur Basic Integer"
                                 " Berechnungen Rechen, dies schaffte er nur durch die Neuschöpfung des Basic"
                                 " Interpreten. Den gab es zwar schon für 8080er-Prozessoren, doch Wozniak"
                                 " wollte diesen auch für den 6502 Prozessor. Er erfuhr durch den "
                                 "Homebrew Computer Club, dass Bill Gates diesen für Atari schrieb und wollte"
                                 " das gleich für seinen Apple 1. So schrieb Wozniak den ganzen Code neu"
                                 " und schaffte es ihn auf eine 8Kb Kassette zu speichern.\n\nDoch der "
                                 "Apple 1 war nur ein Abschnitt für den Apple 2, da der Apple 2 der wahre"
                                 " Erfolg von Apple war.","Apple 1", "Apple_1.jpg")


        apple_2_computer = Node ("Kurz nach der Veröffentlichung des Apple 1 wurde auch schon der Apple 2 "
                                 "entwickelt, im April 1977 wurde erstmals der Apple 2 Veröffentlicht."
                                 "Kurz nach der Veröffentlichung des Apple 1 wurde auch schon der Apple 2 entwickelt,"
                                 " im April 1977 wurde erstmals der Apple 2 Veröffentlicht.\n\n "
                                 "Der Apple 2 war somit das zweite Produkt der Firma Apple und kam "
                                 "anders als der Apple 1 mit einem Monitor."
                                 " Zudem musste man den Computer nicht selber zusammen bauen, sondern er kam"
                                 " bereits voll funktionsfähig beim Kunden an.\n\n"
                                 "Das Besondere am Apple 2 war, dass er einer der ersten Mikrocomputer "
                                 "war die auch eine weite Verbreitung im Markt hatten. "
                                 "Er war also einer der ersten Rechner der kein Großrechner war und trotzdem von "
                                 "nur einer Person bedient werden konnte.\n\n"
                                 "Das Design des Apple 2 war diesmal nicht aus Holz, sondern aus Plastik gefertigt,"
                                 " außerdem kam der Apple 2 mit 8 freien Steckplätzen des 8 Bit Apple Bus Systems."
                                 " Er konnte also noch nach Kauf individuell erweitert werden.\n\n"
                                 "Im Markt kam der Apple 2 besonders gut an, da er ein Computer für jedermann war,"
                                 " man musste also anders als beim Apple 1 keine "
                                 "Erfahrungen mit Elektronik oder Informatik haben."
                                 " Dies spiegelte sich auch dann in den Verkaufszahlen, es gibt zwar keine offiziellen"
                                 " Verkaufszahlen doch Experten schätzen die Zahlen auf ca. 6 Millionen Computer.\n\n"
                                 "Ein weiterer Grund für den Erfolg waren die Kosten des Apple 2, die Verkaufssumme"
                                 " lag bei gerade mal 1298 $, somit war der Apple 2 um einiges Billiger als der"
                                 " Apple 1 und es konnten sich auch normale Arbeiter einen Apple 2 leisten.\n\n"
                                 "Beim Apple 2 wurde eine 8 Bit 6502 CPU verbaut die mit 1,020 MHz Taktfrequenz"
                                 " arbeitete, der RAM lag bei 4 KB und konnte Optional auf 64 KB aufgestockt werden.\n\n "
                                 "Bei späteren Modellen konnte dies sogar auf 16 MB aufgestockt werden.Auch bei der "
                                 "Grafik war der Apple 2 für seine Zeit revolutionär, durch einen Grafikgenerator,"
                                 " der noch zudem das refreshen des DRAM übernahm, konnte man Texte in „LoRes“"
                                 " Farbgrafik also eine Auflösung von 40 × 48 Pixeln in 15 Farben darstellen lassen."
                                 " Mit den erweiterten RAM war es sogar möglich eine HiRes Auflösung darstellen zu"
                                 " lassen, diese HiRes hatte 280 × 192 Pixel. Mit der HiRes konnte der Apple 2"
                                 " hochauflösende Grafik in sechs Farben darstellen.\n\nAuch das Speichermodul wurde"
                                 " beim Apple 2 revolutioniert, hierbei entwickelte Steve Wozniak eine neue Diskette "
                                 "mit der gleichen damals weitverbreitete Form 5¼ Zoll. Es gelang ihm die 80–90 KB"
                                 " Speicher große auf 110–140 KB zu steigern. Zudem konnten die neuen Disketten"
                                 " wesentlich effektiver Arbeiten. Betrieben wurde der Apple 2 mit dem Betriebssystem"
                                 " Apple Basic bzw. vor der Späten Version mit den Integer Basic Betriebssystem, es"
                                 " war aber auch möglich durch die Disketten Apple DOS/ ProDOS und auch Betriebssysteme"
                                 " andere Marken wie Diversi DOS.","Apple 2")

        iphone_2g = Node ("Am 9. Januar 20007 wurde erstmalig ein Smartphone des Unternehmens Apple vorgestellt,"
                          " das iPhone 2g war das erste Smartphone in der Apple Geschichte."
                          " In Deutschland war dieses Smartphone nur bei der Telekom erhältlich und das gemeinsam"
                          " mit ein Handy Vertrag. Die Kosten beliefen sich somit auch 399 € für die 8 GB Version.\n\n"
                          "Besonders am iPhone war das Display, hier verbaute Apple als erster Hersteller ein"
                          " Touchscreen in einem Smartphone. "
                          "Noch heute gilt das Touchscreen als Standard und wird immer noch verbaut."
                          " Revolutionär war das Touchscreen, da man zuvor ein Stift benötigt hat,"
                          " um es zu benutzen, außerdem wurde noch nie ein Touchscreen in ein Handy verbaut.\n\n"
                          "Das Design des iPhone war zudem in vielerlei Hinsicht revolutionär, "
                          "es war das Dünnste jemals gebaute Smartphone, es misst gerade mal 11,6 mm in der Dicke."
                          " Aber auch die Display große war kein Standard, das Display war mit 3.5 Zoll (88,9 cm)"
                          " eins der größten Displays, obwohl zu damaligen Zeit ein kleines Handy bevorzugt wurde."
                          " Außerdem wird im iPhone eine 2-Megapixel-Kamera"
                          " verbaut, doch diese lag der damaligen Zeit hinterher.\n\n"
                          "Betrieben wurde zudem das Smartphone mit den eigen entwickelten Betriebssystem iOS."
                          " Dieses Betriebssystem basiert auf Darwin, dieses Wiederrum basiert"
                          " auf der NeXTSTEP Betriebssystem, doch dieses System wurde in Unix entwickelt.\n\n"
                          "Das iPhone 2g wurde allein im Jahr 2007 1,39 Millionen mal verkauft.", "Iphone 2G")

        ipod = Node ("Am 23. Oktober 2001 stellte Apple der erste iPod vor, es war eine Art kleines"
                     " Smartphone mit den man nur Musik abspielen konnte. Doch durch die weitere Veröffentlichung"
                     " der iTunes Software wurde der iPod revolutionär.\n\nDas Design des iPods war aufgebaut wie ein "
                     "kleines Tasten Handy, es hatte eine Wiedergabe Taste, eine vor und rückwärts taste, eine Menü"
                     " taste und eine Bestätigungstaste. Zum Navigieren hatte man eine Mausrad ähnliche Fläche"
                     " die es erlaubte in der Menü-Zeile Hoch oder runter zu fahren. Der iPod wog gerade mal 185 g"
                     " und wurde aus hochwertigen Edelstahl gefertigt. Aufgrund der einfachen Bedienung wurde der"
                     " iPod auch ein Erfolg.\n\nBesonders am iPod war sowohl die unglaubliche Speicherkapazität von 5 GB"
                     " dadurch war es möglich ca. 1000 verschiedene Songs auf ein Gerät zu haben,"
                     " als auch der iTunes Store.\n\n Durch den iTunes Store war es möglich Online neue Musik"
                     " zukaufen und zu downloaden, für die damaligen Zeiten war das noch nicht möglich."
                     " Jedoch benötigte man dafür noch einen Mac Computer, da iTunes nur für Mac verfügbar war."
                     "Um die Musik dann auf den iPod zu laden war ein FireWire nötig, diese stellte die Verbindung"
                     " zwischen Mac und iPod her.Erste 1 Jahr später also im Jahre 2002 war es möglich "
                     "den iPod auch mit Windows Computer zu verbinden, jedoch gab es da noch kein iTunes für Windows."
                     " Dieses wurde wiederum erst 2003 veröffentlicht.\n\nMan musste sich Musik entweder als CD oder"
                     " illegal von Webseiten wie Napster downloaden, somit trug Apple also auch zum Kampf gegen die"
                     " Musikpiraterie dazu.\n\nZwar gab es noch viele weitere iPods, doch durch das iPhone verliert der "
                     "iPod seine Funktion, da man auch auf dem iPhone Musik hören konnte. Am 9. August wurde der iPod"
                     " eingestellt.","iPod")

        swift = Node ("Swift ist eine objektorientierte Programmiersprache von Apple, mit dieser man Apps"
                      " entwickeln kann. Erstmalig wurde die Sprache am 9. September 2014 vorgestellt, sie basiert "
                      "auf  Objektive-C, Rust, Haskall, Ruby und Python.\n\n Mit objektorientierter Programmiersprache"
                      " ist gemeint, dass der Code nicht auf Funktionen und Logik basiert, sondern auf Daten und "
                      "Objekten.\n\nDie Sprache hat dank ihrer kompakten Syntax eine leichte Bedienung, als Beispiel "
                      "muss man bei Swift kaum eine Typendeklaration vornehmen, da der Swift Compiler diesen oft "
                      "selber erkennt. Aber auch bei der Implementierung zeigt Swift Vorteile, in Objektive-C benötigt"
                      " man zwei Daten einmal den Header mit der Endung .h und die Implementierungsdatei mit"
                      " der Endung .m. Um also bei Änderungen die Datei aktuell zu halten, muss man sowohl die "
                      "Änderung in der Header als auch in der Implementierungsdatei vornehmen. In Swift gibt es"
                      " nur eine Klassendefinition in der Swift Datei, diese endet mit.Swift.\n\nFrüher wurde Objektive-C"
                      " zur Entwicklung von Apps genutzt, doch da Swift eine Art erweitertes Objektive-C ist wurde"
                      " diese Hauptsächlich genutzt. Das zeigen auch die Zahlen.","Swift")


        programmiersprachen = Node ("Eine Programmiersprache ist eine Künstlich erstellte Sprache, die dazu "
                                    "dient eine Kommunikation zwischen Mensch und Computer möglich zu machen.\n\n"
                                    "Da Computer mit numerischen Codes also mit binären Zahlen Operieren hat "
                                    "man Programmiersprachen entwickelt, um diese Kommunikation zu vereinfachen."
                                    " Im Grunde genommen kann man eine Programmiersprache mit "
                                    "unseren „normalen“ Sprache vergleichen. Sie wurde nämlich in Semantik "
                                    "und Syntax aufgeteilt. Die Semantik steht hierbei für die Bedeutung einzelner "
                                    "Zeichen, die Syntax beschreibt die Form der Sprache, sie beschreibt also die"
                                    " Menge an erlaubten Zeichenketten für Programme in dieser Sprache.\n\n"
                                    "Programmiersprachen werden in mehreren Kategorien aufgeteilt, da wäre die"
                                    " Maschinensprache, die Assemblersprache, die höheren Sprachen, die "
                                    "Anwendung orientierten Sprachen und die Dokumentbeschreibungssprachen.\n\n"
                                    "Die Maschinen Sprache kann anders als höre Sprachen direkt und ohne "
                                    "Compiler vom Prozessor gelesen werden und besteht aus Binären und digitalen Zahlen.\n\n"
                                    "Die Assemblersprache ist eine Sprache speziell für einen"
                                    " Prozessor, d.h man kann zum Beispiel keinen Assembler Code von Intel"
                                    " auf einen Assembler Code von AMD nutzen."
                                    " Der Code wird anders als bei der Maschinensprache in Zeichen geschrieben"
                                    " und anschließend durch den Assembler 1:1 „gemappt“, also in Binär übersetzt.\n\n"
                                    "Die höheren Sprachen sind Sprachen die durch Funktionen"
                                    " Programmieren, durch einen Compiler oder Interpreten werden"
                                    " diese Programme dann in Maschinensprache übersetzt.\n\n"
                                    "Außerdem werden die Sprachen noch in prozedural, funktional, logische"
                                    " und objektorientiert  Programmierung aufgeteilt. Diese Aufteilung nennt "
                                    "man auch Paradigma.\n\nMit einer Prozeduralen Sprache ist gemeint, dass die"
                                    " Sprache auf Prozeduren oder Funktionen besteht, ein Beispiel hierfür wäre"
                                    " die Sprache C. Mit der funktionalen Sprache ist gemeint, dass Programme"
                                    " hauptsächlich durch Anwendung von Funktionen erstellt wurde, hier zu wäre"
                                    " die Sprache Lisp ein Beispiel. Bei der logischen Programmierung werden"
                                    " anhand von mathematischen Formeln logische Programme entwickelt, eine"
                                    " Beispielsprache wäre Prolog. Zuletzt gibt es noch die objektorientierte"
                                    " Programmierung, hierbei basiert die Programmierung anhand von Daten und"
                                    " Objekte ein Beispiel ist Swift.","Programmiersprachen")


        itunes = Node ("Im Januar 2001 wurde iTunes erstmalig vorgestellt, es war eine neue Möglichkeit Musik zukaufen."
                       " Anders als bei physischen CD kaufte man bei iTunes nur eine Art von Lizenz die es"
                       " ermöglichte, die Musik Digital zu downloaden.\n\n Diese Art von Musik verkauf war für die"
                       " damalige Zeit eine Revolution, da man bisher nur Musik physisch kaufen konnte, oder sie"
                       " Illegal auf Webseiten wie Nepstar downloaden konnte. Da 2001 auch der erste iPod"
                       " erschien, konnte man die gekaufte Musik direkt auf sein iPod downloaden.\n\n Doch nicht"
                       " nur die Nutzer profitierten von der einfachen Software, auch Künstler hatten nun eine"
                       " weitere Möglichkeit ihre Musik zu verkaufen.\n\n Künstler konnten ihre Musik für 99 Cent"
                       " pro Lied verkaufen, zum Anfang hatte Apple gerade mal 200000 Kopien verfügbar. Bereits"
                       " nach einer Woche wurden jedoch schon 1 Millionen Songs verkauft.\n\n iTunes wurde jedoch"
                       " im Herbst 2019 abgeschaltet, da sich nun eine neue Möglichkeit Songs zu hören ergeben hat."
                       " Das Streaming, ist eine neue Möglichkeit Musik, ohne sie zu besitzen zu hören. Dabei werden"
                       " Datenpakete online auf das Endgerät gesendet. Man muss die Musik also nicht mal downloaden"
                       " und verbraucht auch so keinen Speicher.", "iTunes")

        apple_musik = Node ("Apple Musik ist ein Musikstreaming Dienst von Apple und erlaubt es Musik über "
                            "Onlinedaten zu empfangen, dabei muss man die Musik nicht auf das Endgerät Downloaden.\n\n"
                            " Am 8. Juni 2015 stellt Apple den neuen Musik Streamingdienst Apple Musik vor, dieser"
                            " Dienst sollte das bis dahin genutzte iTunes ablösen, da man mit Musik Verkäufen kaum"
                            " Geld einnahm.\n Ein Apple Musik Abo kostet aktuell für Studierende 5,99 € im Monat, für"
                            " Einzelpersonen 10,99 € und für eine Familie, die aus bis zu 6 Personen bestehen"
                            " darf 16,99 € im Monat.\n\n Es sollte ein Konkurrenz-Produkt zu Spotify und anderen"
                            " Streaming Diensten sein, nach stand 22. Februar 2023 hat Spotify mit rund"
                            " 188 Millionen Zahlenden Kunden immer noch die meisten zahlenden Nutzer, doch"
                            " Apple kann mit ihren ca. 88 Millionen Nutzer langsam mithalten.", "Apple Musik")

        app_store = Node ("AM 10. Julie 2008 wurde erstmalig der App Store von Apple vorgestellt, es war ein"
                          " digitaler Marktplatz für Apps und Software. Der App Store startet erstmalig mit"
                          " 500 Apps, heutzutage umfasst der App Store ca. 1,6 Millionen Apps und zählt damit"
                          " zu den Zweitgrößten App Markt der Welt.\n\n Durch den App Store haben sowohl große Entwickler"
                          " Studios als auch kleine Entwickler eine Möglichkeit ihre Apps und Software zu verkaufen."
                          " Dabei können sie mit mehreren Modellen Geld verdienen, zu einem kann die App am Anfang"
                          " Geld kosten, aber auch kostenlose Apps können durch sogenannte in"
                          " Game Käufe Geld verdienen.\n\n Hierbei können sich zum Beispiel digitale kosmetische"
                          " Items gekauft werden, durch den Verkauf dieser Produkte verdient dann sowohl Apple"
                          " als auch der Entwickler Geld. Aber auch ein Abo Model ist möglich"
                          " um Geld im App Store zu verdienen. Anders als die Konkurrenz, also der Play Store ist"
                          " der App Store nur den Apple Produkten.", "App Store")

        ios = Node ("iOS ist ein Betriebssystem das Spezielle von Apple "
                    "für die Hauseigenen Produkte entwickelt wurde. Erstmalig wurde OS am 9. Januar 2007"
                    " vorgestellt, dies geschah zusammen mit dem ersten Smartphone, den iPhone 2g.\n\n iOS ist nicht"
                    " nur auf dem iPhone verfügbar, sondern auch auf dem iPad und dem iPod. Anders als bei der"
                    " Konkurrenz wie Android verkauft Apple keine Lizenzen an andere Hersteller, somit ist das "
                    "Betriebssystem exklusiv für Apple Produkte.\n\n Das Betriebssystem iOS und auch andere von Apple "
                    "entwickelten Betriebssysteme basieren  dabei auf dem Unix Betriebssystem."
                    " Unix ist ein im Jahre 1969 entwickeltes Mehrbenutzersystem, dies erlaubt es "
                    "mehrere Nutzer auf einen Computer anzulegen."
                    " Unix basiert auf ein System des Unternehmens AT&T und wurde von Kenneth Lane Thomas entwickelt.","iOS")

        unix = Node ("Unix ist ein Mehr-Benutzer Betriebssystem, es wurde am 3. November"
                     " 1971 erstmalig veröffentlicht. Entwickelt wurde Unix im Jahre 1969 von Kenneth"
                     " Lane Thompson, ein amerikanischen Programmier. Er entwickelte das System im Auftrag "
                     "des Unternehmens Bell Labs, dies ist ein Tochter Unternehmen von AT&T.\n\nDurch Unix ist es möglich,"
                     " dass Mehrere Benutzer Konten auf einen Computer zugreifen können und somit ihre eigene "
                     "Arbeitsumgebung haben. Außerdem entstand durch Unix das Dateisystem und die Ordnerstruktur "
                     "auf den Computer.\n\nHeutzutage wird Unix nicht nur noch als eigenes Betriebssystem genutzt, "
                     "sondern es wird durch verschiedene Unternehmen erweitert und genutzt. So dient Unix nicht nur"
                     " als Basis von Linux sondern auch als Basis der Apple Betriebssysteme wie iOS, MacOS usw.", "Unix")

        quellen = Node ("Hardware:\n"
                        "https://www.sachsen.schule/~gdb/daten_verarbeiten/hw/Hardware.html"
                        "https://www.edv-lehrgang.de/hardware/\n\n"
                        "Homebrew:\n"
                        "https://blog.hnf.de/der-club-der-selbstgestrickten-computer/"
                        "https://www.heise.de/news/Mythos-des-Silicon-Valley-40-Jahre-Homebrew-"
                        "Computer-Club-2567331.html?hg=1&hgi=3&hgf=false\n\n"
                        "NeXT:\n"
                        "https://de.statista.com/statistik/daten/studie/203600/umfrage/absatz-von-apples-"
                        "mac-computern-weltweit/#:~:text=\n"
                        "https://digitalesleben.blog/2022/04/19/next-computer-die-zweite-karriere"
                        "-von-steve-jobs/#Zusammenfassung_und_Preise\n\n"
                        "Apple 1:\n"
                        "https://www.computerworld.ch/business/ios/apple-1-kostete-40-jahren-666"
                        "-dollar-heute-900-000-1335832.html\n"
                        "https://www.welt.de/wirtschaft/webwelt/gallery140218820/Das-sind-die-"
                        "Technik-Meilensteine-von-Apple.html\n\n"
                        "Apple M1:\n"
                        "https://www.intel.de/content/www/de/de/products/sku/199335/intel-core-i710700k-"
                        "processor-16m-cache-up-to-5-10-ghz/specifications.html\n"
                        "https://www.apple.com/de/newsroom/2020/11/apple-unleashes-m1/\n"
                        "https://iboysoft.com/de/wiki/was-ist-die-apple-neural-engine.html#what-is-apples-neural-engine\n\n"
                        "Apple 2:\n"
                        "https://www.hardware-aktuell.com/lexikon/Apple_II/\n"
                        "https://www.techtarget.com/iotagenda/definition/microcomputer\n"
                        "https://www.heise.de/hintergrund/Geschichte-von-Apple-Der-Apple-II-mehr-als-nur-Grundlage"
                        "-des-Erfolgs-4941086.html#:~:text=Wie schon den ersten Apple,Millionen von Apple"
                        " hergestellten Exemplaren.\n\n"
                        "iPhone 2g:\n"
                        "https://ap-verlag.de/infografik-alle-iphones-im-generationen-check/22868/#:~:text=\n"
                        "https://appleinsider.com/articles/18/06/29/the-story-of-the-original-iphone-that-"
                        "nobody-thought-was-possible\n"
                        "https://www.geschichte-von-apple.de/Gerate/iPhones/iPhone.php\n"
                        "https://www.eyefactive.com/whitepaper/geschichte-der-touchscreen-technologie#:~:text=2007 -"
                        " Apple: Der erste iPhone,Smartphone auf den Markt brachte.\n\n"
                        "iPod:\n"
                        "https://www.apple.com/de/newsroom/2022/05/the-music-lives-on/#:~:text=“&text=\n"
                        "https://www.mac-history.de/2018/06/14/die-geschichte-des-ipod/\n"
                        "https://www.turn-on.de/article/ipod-modelle-eine-chronologie-des-kult-"
                        "musikplayers-von-apple-537821#h2_summary_0\n"
                        "https://www.ifun.de/heute-vor-15-jahren-steve-jobs-stellt-den-ersten-ipod-vor-99121/\n"
                        "iTunes:\n"
                        "https://soundexperts.de/musik-streaming/#:~:text=Wie%20funktioniert%20"
                        "Musikstreaming%3F,etwa%20Smartphone%20und%20Tablet%20sein\n"
                        "https://blog.recordjet.com/itunes-wird-abgeschafft-wichtigste-antworten-fuer-musiker-und-user/\n"
                        "https://www.welt.de/newsticker/leute/stars/article115675941/Zehn-Jahre"
                        "-iTunes-Wie-Apple-die-Musikindustrie-revolutionierte.html\n"
                        "https://www.mactechnews.de/news/article/iTunes-Vom-kleinen-Musikplayer-zum-"
                        "Medienimperium-160034.html?page=4\n"
                        "Swift:\n"
                        "https://www.computerweekly.com/de/definition/Objektorientierte-Programmierung-OOP#:~:text=\n"
                        "https://www.ralfebert.de/ios-app-entwicklung/swift-ueberblick/#:~:text=\n"
                        "Programmierprachen:\n"
                        "https://ilu.th-koeln.de/goto.php?target=file_174004_download&client_id=thkilu\n"
                        "https://www.computerweekly.com/de/definition/Maschinensprache#:~:text=Maschinenlesbarer\n"
                        "https://linz.coderdojo.net/uebungsanleitungen/programmieren/sonstiges/assembler-hello"
                        "-world/#:~:text=In\n"
                        "App Store:\n"
                        "https://www.mactechnews.de/news/article/Vor-5-Jahren-Apple-Music-ist"
                        "-da-und-enttaeuscht-zunaechst-175183.html\n"
                        "https://www.apple.com/de/newsroom/2015/06/08Introducing"
                        "-Apple-Music-All-The-Ways-You-Love-Music-All-in-One-Place-/\n"
                        "iOS:\n"
                        "https://www.wertgarantie.de/lexikon/technik/ios\n"
                        "https://www.it-business.de/was-ist-ios-a-834fdeeb8083fc4c259982484101e352/\n"
                        "https://www.computerwissen.de/apple/ios/\n"
                        "Unix:\n"
                        "https://it-service.network/it-lexikon/unix#:~:text=\n"
                        "https://www.get-in-it.de/magazin/arbeitswelt/it-legenden/ken-thompson#:~:text=\n"
                        "https://it-service.network/it-lexikon/unix\n","Quellenerzeichniss")


        steve_jobs.connect(apple)
        steve_wozniak.connect(apple)
        steve_wozniak.connect(homebrew)
        steve_jobs.connect(homebrew)

        steve_jobs.connect(next)

        apple.connect(hardware)
        apple.connect(software)

        apple.connect(programmiersprachen)
        apple.connect(next)

        swift.connect(programmiersprachen)

        hardware.connect(ipod)
        hardware.connect(iphone_2g)
        hardware.connect(apple_m1)
        hardware.connect(apple_1_computer)
        hardware.connect(apple_2_computer)

        software.connect(ios)
        software.connect(apple_musik)
        software.connect(itunes)
        software.connect(app_store)

        ios.connect(unix)



        graph.add_new_node_to_graph(steve_jobs)
        graph.add_new_node_to_graph(steve_wozniak)
        graph.add_new_node_to_graph(apple)
        graph.add_new_node_to_graph(hardware)
        graph.add_new_node_to_graph(software)
        graph.add_new_node_to_graph(homebrew)
        graph.add_new_node_to_graph(next)
        graph.add_new_node_to_graph(apple_m1)
        graph.add_new_node_to_graph(apple_1_computer)
        graph.add_new_node_to_graph(apple_2_computer)
        graph.add_new_node_to_graph(iphone_2g)
        graph.add_new_node_to_graph(ipod)
        graph.add_new_node_to_graph(programmiersprachen)
        graph.add_new_node_to_graph(itunes)
        graph.add_new_node_to_graph(apple_musik)
        graph.add_new_node_to_graph(app_store)
        graph.add_new_node_to_graph(ios)
        graph.add_new_node_to_graph(unix)
        graph.add_new_node_to_graph(swift)
        graph.add_new_node_to_graph(quellen)