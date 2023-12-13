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
from Onour_Directory.Onour_Content import Alan_Turing_1, Alan_Turing_2, Alan_Turing_3, Alan_Turing_4, Alan_Turing_5,\
    Alan_Turing_6, Alan_Turing_7, Alan_Turing_8, Alan_Turing_9, Alan_Turing_10, Alan_Turing_11, Alan_Turing_13,\
    Alan_Turing_12, Alan_Turing_19, Alan_Turing_14, Alan_Turing_15, Alan_Turing_16, Alan_Turing_17, Alan_Turing_18, \
    Onour_Source_1, Onour_Source_2, Onour_Source_3

class GraphContent:

    def __init__(self, graph: Graph):
        self.create_demo_nodes(graph)

    @staticmethod
    def create_demo_nodes(graph):


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

        central_node = Node("Die bekanntesten Informatiker:innen und Ihre Beiträge zum Fachgebiet",
                            "Thema des Graphen")
        graph.add_new_node_to_graph(central_node)
