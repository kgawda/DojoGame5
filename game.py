# -*- coding: utf-8 -*-
import networkx as nx


graph = nx.DiGraph()


class Location(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


graph.add_node(1, info=Location(u'Dom', u'Jesteś w domu, budzisz się z ciężkim kacem.'))
graph.add_node(2, info=Location(u'Przed dom', u'Jesteś przed swoją marną chatką. Widzisz, że droga ma tylko jeden kierunek - sklep monopolowy'))
graph.add_node(3, info=Location(u'Sklep monopolowy', u'Sklep monopolowy "Flaszka". Za ladą stoi pani Halinka. Masz ochotę na wino.'))
graph.add_node(4, info=Location(u'Łąka Mariana', u'Łąka pod wsią. Słyszysz tupok kopyt. Napada Cię agresywny koń chuligan i rozbija Ci wino. Tracisz przytomność. Budzisz się w środku nocy, z kopytem odciśniętym na czole. Masz tylko jeden cel - zemsta'))
graph.add_node(5, info=Location(u'Żabie Doły', u'Idąc w stronę Żabich Dołów zauważasz srebrny spodek. Stojący nieopodal zielony ludzik przepuści Cię tylko, jeżeli dasz mu laskę krakowskiej.'))
graph.add_node(6, info=Location(u'Krowia Górka', u'We wsi grasuje stado szatańskich kóz, które niszczą wszystko, co napotkają na drodze. Staw im opór lub uciekaj!'))
graph.add_node(7, info=Location(u'Koniec wszechświata', u'Wyszedłeś poza granice wszechświata'))


graph.add_edge(1, 2)
graph.add_edge(2, 1)
graph.add_edge(3, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 4)
graph.add_edge(6, 4)
graph.add_edge(6, 7)


def end(arg):
    print(arg)


def display(graph, id):
    info = graph.node[id]['info']

    print ""
    print u"-" * 30
    print u"Jesteś w     : %s" % info.name
    print u"Opis         : %s" % info.description

    neighbors = graph.neighbors(id)
    if not neighbors:
        return end(u"     This the end! :D")

    print u"Możesz isć do: "
    for nid in graph.neighbors(id):
        print u"    %s | %s" % (nid, graph.node[nid]['info'].name)

    print ""
    print "Where would you like to go?"
    inp = raw_input(">>> ")
    inp = int(inp)

    if inp in graph:
        display(graph, inp)


if __name__ == '__main__':
    display(graph, 1)
