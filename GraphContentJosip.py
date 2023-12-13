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
from Teating_Grounds.Teating_Grounds import Bill_Intro, Kindheit_Fruh, Kindheit_Spaet, Vor_Microsoft, Harvard,\
    Microsoft_Anfang, IBM_DOS, Microsoft_Windows, Microsoft_Andere, Monopol, Ehe, Bill_Image,\
    Kontroverse_Klein, Kontroverse_Epstein, Kontroverse_Pandemie, Kontroverse_Klima, Religion, Vermoegen, Fazit, \
    Ehre, Facts, Quellen

class GraphContent:

    def __init__(self, graph: Graph):
        self.create_demo_nodes(graph)

    def create_demo_nodes(self, graph):
        """
        Diese Methode dient Ihnen also Demonstration für den Aufbau eines Graphen.
        TODO: Löschen oder kommentieren Sie diese Methode aus wenn Sie Ihren eigenen Graphen erstellen.
        """

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

