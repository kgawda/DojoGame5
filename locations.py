# -*- coding: utf-8 -*-

class Location(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


graph.add_node(1, info=Location(u'Dom', u'Jesteś w domu, budzisz się z ciężkim kacem.'))
graph.add_node(2, info=Location(u'Przed domem', u'Jesteś przed swoją marną chatką. Widzisz, że droga ma tylko jeden kierunek - sklep monopolowy'))
graph.add_node(3, info=Location(u'Sklep monopolowy', u'Sklep monopolowy "Flaszka". Za ladą stoi pani Halinka. Masz ochotę na wino.'))
graph.add_node(4, info=Location(u'Łąka Mariana', u'Łąka pod wsią. Słyszysz tupok kopyt. Napada Cię agresywny koń chuligan i rozbija Ci wino.'))
graph.add_node(5, info=Location(u'Żabie Doły', u'Idąc w stronę Żabich Dołów zauważasz srebrny spodek. Stojący nieopodal zielony ludzik przepuści Cię tylko, jeżeli dasz mu laskę krakowskiej.'))
graph.add_node(6, info=Location(u'Krowia Górka', u'We wsi grasuje stado szatański kóz, które niszczą wszystko, co napotkają na drodze. Staw im opór lub uciekaj!'))

graph.add_edge(1,2)
graph.add_edge(2,1)
graph.add_edge(3,2)
graph.add_edge(2,3)
graph.add_edge(3,4)
graph.add_edge(4,5)
graph.add_edge(4,6)
graph.add_edge(5,4)
graph.add_edge(6,4)

