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

from Josip_Directory.Teating_Grounds import *
from Onour_Directory.Onour_Content import *
from Dennis_Directory.GraphDennisKliewer import *
from Lukas_Directory.GraphContentLinus import *
from Oliver_Directory.GraphContentOliver import *
class GraphContent:

    def __init__(self, graph: Graph):
        self.create_demo_nodes(graph)
        self.create_demo_nodes2(graph)
        self.create_demo_nodes4(graph)
        self.create_dennis_nodes(graph)
        self.create_lukas_nodes(graph)
        self.create_central_node(graph)


    @staticmethod
    def create_demo_nodes(graph):
        steve_jobs.connect(apple)
        steve_jobs.connect(quellen)
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
        
    @staticmethod
    def create_demo_nodes2(graph):


        Alan_Turing_1.connect(Alan_Turing_2)
        Alan_Turing_1.connect(Alan_Turing_3)
        Alan_Turing_1.connect(Alan_Turing_4)
        Alan_Turing_4.connect(Alan_Turing_5)
        Alan_Turing_1.connect(Alan_Turing_6)
        Alan_Turing_6.connect(Alan_Turing_11)
        Alan_Turing_1.connect(Alan_Turing_7)
        Alan_Turing_1.connect(Alan_Turing_8)
        Alan_Turing_1.connect(Alan_Turing_9)
        Alan_Turing_1.connect(Alan_Turing_10)
        Alan_Turing_10.connect(Alan_Turing_18)
        Alan_Turing_1.connect(Alan_Turing_12)
        Alan_Turing_1.connect(Alan_Turing_13)
        Alan_Turing_13.connect(Alan_Turing_14)
        Alan_Turing_13.connect(Alan_Turing_15)
        Alan_Turing_13.connect(Alan_Turing_16)
        Alan_Turing_13.connect(Alan_Turing_17)
        Alan_Turing_1.connect(Alan_Turing_19)
        Onour_Source_1.connect(Alan_Turing_1)
        Onour_Source_1.connect(Alan_Turing_6)
        Onour_Source_1.connect(Alan_Turing_4)
        Onour_Source_1.connect(Alan_Turing_10)
        Onour_Source_1.connect(Alan_Turing_3)
        Onour_Source_2.connect(Alan_Turing_4)
        Onour_Source_2.connect(Alan_Turing_2)
        Onour_Source_2.connect(Alan_Turing_7)
        Onour_Source_3.connect(Alan_Turing_9)
        Onour_Source_3.connect(Alan_Turing_14)
        Onour_Source_3.connect(Alan_Turing_15)

        graph.add_new_node_to_graph(Alan_Turing_1)
        graph.add_new_node_to_graph(Alan_Turing_2)
        graph.add_new_node_to_graph(Alan_Turing_3)
        graph.add_new_node_to_graph(Alan_Turing_4)
        graph.add_new_node_to_graph(Alan_Turing_5)
        graph.add_new_node_to_graph(Alan_Turing_6)
        graph.add_new_node_to_graph(Alan_Turing_7)
        graph.add_new_node_to_graph(Alan_Turing_8)
        graph.add_new_node_to_graph(Alan_Turing_9)
        graph.add_new_node_to_graph(Alan_Turing_10)
        graph.add_new_node_to_graph(Alan_Turing_11)
        graph.add_new_node_to_graph(Alan_Turing_12)
        graph.add_new_node_to_graph(Alan_Turing_13)
        graph.add_new_node_to_graph(Alan_Turing_14)
        graph.add_new_node_to_graph(Alan_Turing_15)
        graph.add_new_node_to_graph(Alan_Turing_16)
        graph.add_new_node_to_graph(Alan_Turing_17)
        graph.add_new_node_to_graph(Alan_Turing_18)
        graph.add_new_node_to_graph(Alan_Turing_19)
        graph.add_new_node_to_graph(Onour_Source_1)
        graph.add_new_node_to_graph(Onour_Source_2)
        graph.add_new_node_to_graph(Onour_Source_3)

    @staticmethod
    def create_central_node(graph):
        master_node = Node("!!!!BYTE BANDITS TITELKNOTEN!!!",
                           "Die bekanntesten Informatiker:innen und Ihre Beiträge zum Fachgebiet")
        master_node.connect(Alan_Turing_1)
        master_node.connect(Bill_Intro)
        master_node.connect(Larry_page)
        master_node.connect(Sergey_brin)
        master_node.connect(steve_jobs)
        master_node.connect(steve_wozniak)
        master_node.connect(header_linus_node)
        graph.add_new_node_to_graph(master_node)

    def create_demo_nodes4(self, graph):


        graph.add_new_node_to_graph(Bill_Intro)
        graph.add_new_node_to_graph(Kindheit_Fruh)
        graph.add_new_node_to_graph(Kindheit_Spaet)
        graph.add_new_node_to_graph(Vor_Microsoft)
        graph.add_new_node_to_graph(Harvard)
        graph.add_new_node_to_graph(Microsoft_Anfang)
        graph.add_new_node_to_graph(IBM_DOS)
        graph.add_new_node_to_graph(Microsoft_Windows)
        graph.add_new_node_to_graph(Microsoft_Andere)
        graph.add_new_node_to_graph(Monopol)
        graph.add_new_node_to_graph(Ehe)
        graph.add_new_node_to_graph(Bill_Image)
        graph.add_new_node_to_graph(Kontroverse_Klein)
        graph.add_new_node_to_graph(Kontroverse_Epstein)
        graph.add_new_node_to_graph(Kontroverse_Pandemie)
        graph.add_new_node_to_graph(Kontroverse_Klima)
        graph.add_new_node_to_graph(Religion)
        graph.add_new_node_to_graph(Vermoegen)
        graph.add_new_node_to_graph(Fazit)
        graph.add_new_node_to_graph(Ehre)
        graph.add_new_node_to_graph(Facts)
        graph.add_new_node_to_graph(Quellen)

    def create_dennis_nodes(self, graph):
        Larry_page.connect(Michigan_state_university)
        Michigan_state_university.connect(Stanford_university)
        Stanford_university.connect(Google_llc)

        Sergey_brin.connect(University_of_maryland)
        University_of_maryland.connect(Stanford_university)
        Stanford_university.connect(Google_llc)
        Sundar_pichai.connect(Google_llc)

        Google_llc.connect(Google_glass)
        Google_llc.connect(Android)

        Larry_page.connect(Marconi_preis)
        Larry_page.connect(Tr100_preis)
        Larry_page.connect(Amer_acad)

        Sergey_brin.connect(Marconi_preis)
        Sergey_brin.connect(Nsf_grfp)
        Sergey_brin.connect(Amer_acad)

        Sergey_brin.connect(Brin_wojcicki_foundation)
        Anne_wojcicki.connect(Brin_wojcicki_foundation)

        Sergey_brin.connect(Sergey_brin_family_foundation)
        Anne_wojcicki.connect(Wojcicki_foundation)

        Anne_wojcicki.connect(Twentythree_and_me)
        Linda_avey.connect(Twentythree_and_me)
        Paul_cusenza.connect(Twentythree_and_me)
        Google_llc.connect(Alphabet_inc)
        Quellen_Dennis.connect(Larry_page)
        Quellen_Dennis.connect(Sergey_brin)
        Quellen_Dennis.connect(Anne_wojcicki)
        Quellen_Dennis.connect(Linda_avey)
        Quellen_Dennis.connect(Paul_cusenza)
        Quellen_Dennis.connect(Sundar_pichai)

        graph.add_new_node_to_graph(Larry_page)
        graph.add_new_node_to_graph(Linda_avey)
        graph.add_new_node_to_graph(Sergey_brin)
        graph.add_new_node_to_graph(Sergey_brin_family_foundation)
        graph.add_new_node_to_graph(Marconi_preis)
        graph.add_new_node_to_graph(Tr100_preis)
        graph.add_new_node_to_graph(Google_llc)
        graph.add_new_node_to_graph(Google_glass)
        graph.add_new_node_to_graph(Alphabet_inc)
        graph.add_new_node_to_graph(Android)
        graph.add_new_node_to_graph(Anne_wojcicki)
        graph.add_new_node_to_graph(Sundar_pichai)
        graph.add_new_node_to_graph(Paul_cusenza)
        graph.add_new_node_to_graph(Twentythree_and_me)
        graph.add_new_node_to_graph(Brin_wojcicki_foundation)
        graph.add_new_node_to_graph(Wojcicki_foundation)
        graph.add_new_node_to_graph(University_of_maryland)
        graph.add_new_node_to_graph(Stanford_university)
        graph.add_new_node_to_graph(Quellen_Dennis)
        graph.add_new_node_to_graph(Nsf_grfp)
        graph.add_new_node_to_graph(Amer_acad)
        graph.add_new_node_to_graph(Michigan_state_university)

    def create_lukas_nodes(self, graph):
        """
                Hinzufügen zum Graphen
                """

        graph.add_new_node_to_graph(header_linus_node)
        graph.add_new_node_to_graph(topic_node)
        graph.add_new_node_to_graph(topic1_node)
        graph.add_new_node_to_graph(topic2_node)
        graph.add_new_node_to_graph(topic3_node)
        graph.add_new_node_to_graph(topic3v1_node)
        graph.add_new_node_to_graph(topic3v2_node)
        graph.add_new_node_to_graph(topic3v3_node)
        graph.add_new_node_to_graph(topic4_node)
        graph.add_new_node_to_graph(topic5_node)
        graph.add_new_node_to_graph(topic5v1_node)
        graph.add_new_node_to_graph(topic5v2_node)
        graph.add_new_node_to_graph(topic5v3_node)
        graph.add_new_node_to_graph(topic6_node)
        graph.add_new_node_to_graph(topic7_node)
        graph.add_new_node_to_graph(topic8_node)
        graph.add_new_node_to_graph(topic9_node)
        graph.add_new_node_to_graph(topic10_node)
        graph.add_new_node_to_graph(topic11_node)
        graph.add_new_node_to_graph(topic12_node)
        graph.add_new_node_to_graph(topic13_node)
        graph.add_new_node_to_graph(topic14_node)
        graph.add_new_node_to_graph(topic15_node)
        graph.add_new_node_to_graph(sources_node)

        """
        Verbindungen der Knoten
        """
        header_linus_node.connect(topic_node)
        header_linus_node.connect(topic1_node)
        header_linus_node.connect(topic2_node)
        header_linus_node.connect(topic3_node)
        topic3_node.connect(topic3v1_node)
        topic3_node.connect(topic3v2_node)
        topic3_node.connect(topic3v3_node)
        header_linus_node.connect(topic4_node)
        header_linus_node.connect(topic5_node)
        topic5_node.connect(topic5v1_node)
        topic5_node.connect(topic5v2_node)
        topic5_node.connect(topic5v3_node)
        header_linus_node.connect(topic6_node)
        header_linus_node.connect(topic7_node)
        header_linus_node.connect(topic8_node)
        header_linus_node.connect(topic9_node)
        topic9_node.connect(topic11_node)
        header_linus_node.connect(topic10_node)
        header_linus_node.connect(topic12_node)
        header_linus_node.connect(topic13_node)
        header_linus_node.connect(topic14_node)
        header_linus_node.connect(topic15_node)
        header_linus_node.connect(sources_node)