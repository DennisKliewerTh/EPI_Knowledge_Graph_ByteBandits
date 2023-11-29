from GraphModel.Graph import Graph
from GraphModel.Node import Node


class GraphContentLinus:

    def __init__(self, graph: Graph):
        self.create_demo_nodes(graph)

    @staticmethod
    def create_demo_nodes(graph):

        """
        Inhalt der einzelnen Knoten
        """

        header_linus_node = Node("Linus Torvald ist das Gesicht hinter Linux. Er ist dafür verantwortlich das "
                                 "es heute Linux gibt. "
                                 "Esprofitieren viele Programmierer von seiner Arbeit. Das beste Beispiel dafür ist "
                                 "git, welches Linus auch selber entwickelt hatte. Dies ist eine Versionsverwaltung "
                                 "die es Programmierern zusammen an"
                                 "verschiedenen Stellen im Code gleichzeitig zu arbeiten.\n"
                                 "Dieser Knotenteil des Wissensgraph „Die bekanntesten Informatiker:innen und Ihre "
                                 "Beiträge zum"
                                 "Fachgebiet“ behandelt alle wichtigen Informationen zu Linus Torvald. Dies beinhaltet "
                                 "seine Kindheit und sein Bildungsweg. Des weiteren sind Informationen zu Git und"
                                 "Linux und anderen"
                                 "Projekten zu finden, mit denen sich Linus auseinander gesetzt hat. Unter "
                                 "anderen werden auch die Hürden genannt, die es bei der Entwicklung von Linux gab. "
                                 "Es gibt Informationen zum Namenstreit vom „Linux“ und welche Rolle Linux in der "
                                 "Industrie und der allgemeinen Technologie spielt.", "Linus Torvald")

        topic_node = Node("Linus Torvalds wurde am 28.12.1969 in Helsinki geboren. Sein voller Name lautet "
                          "Linus Benedict"
                          "Torvalds. Seine Eltern heißen Anna Torvalds uns Nils Torvalds."
                          " Beide waren damals Studenten an"
                          "der Universität Helsinki und haben an der Studentenbewegung der 1960er Jahre teilgenommen.\n"
                          "Im weiteren Verlauf wurde die Mutter Torvalds Übersetzerin bei der "
                          "finnischen Nachrichtenagentur"
                          "STT. Der Vater, Nils Torvalds wurde nach der Karriere als Fernseh- und Rundfunkjournalist"
                          "Mitglied des Europaparlaments.Die Familie Torvalds gehört dabei zur schwedischsprachigen"
                          "Minderheit der Finnen.\n"
                          "Linus Torvalds hat eine Schwester, die 16 Monate nach ihm geboren wurde und trägt den Namen"
                          "Sara. Die Eltern von Linus trennten sich als Linus 7 Jahre alt war. Linus "
                          "bekam noch einen Bruder"
                          "väterlicherseits. Dieser heißt Leo Torvalds und wurde zwei Jahre nach der "
                          "Trennung von Nils und"
                          "Anna Torvalds geboren.\n"
                          "Linus wurde nach dem berühmten Chemiker Linus Carl Pauling benannt. Der Nachname wurde"
                          "durch den Namen des Großvater Väterlicherseits geschaffen. Dieser hieß Ole "
                          "Torvald Elis Saxberg"
                          "Karanko.\n"
                          "Während der Schulzeit wuchs Linus im Helsinkier Stadtteil Punavouri. Laut dem "
                          "Worten von Linus"
                          "selbst, bezeichnet er sich als „Freek“, „Nerd“ und „Geek“.\n"
                          "Linus hatte pflegte wenig Interesse an Sport. Er widmete sich eher den Modellbau,"
                          "und widmete seine Zeit den Büchern der Genres Horror und Science-Fiction."
                          "(Quelle2)",
                          "Kindheit und Jugend von Linus Torvald")

        """
        Hinzufügen zum Graphen
        """

        graph.add_new_node_to_graph(header_linus_node)
        graph.add_new_node_to_graph(topic_node)

        """
        Verbindungen der Knoten
        """
        header_linus_node.connect(topic_node)
