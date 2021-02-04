
"""
Empty Graph Template to implement :D

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

# This is our Markov Chain representation
import random

# Define the graph in terms of vertices


class Vertex(object):
    def __init__(self, value):  # value will be the word
        self.value = value
        self.adjacent = {}  # nodes that have and edge from this vertex
        self.neighbors = []
        self.neighbors_weights = []

    def add_edge_to(self, vertex, weight=0):
        # this is adding and edge to the vertex we input with weight
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        # this is incrementing the weight of the edge
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        pass

    # initializes probability map
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        # randomly select next word based on weights
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]


# Now that we have our vertex representation, we put this together in a graph
class Graph(object):
    def __init__(self):
        self.vertices = {}  # maps string to Vertex

    def get_vertex_values(self):
        # what are the values of all the vertices?
        # in other words, return all posible words
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        # what if the value is not in the graph?
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]  # get the Vertex object

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
