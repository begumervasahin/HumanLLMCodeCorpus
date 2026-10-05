from trueskill import Rating, rate_1vs1
import networkx as nx
import random
from measures import measure_pairs_agreement
import argparse
def initialize_players(pairs, players):
    if not players:
        for u, v in pairs:
            if u not in players:
                players[u] = Rating()
            if v not in players:
                players[v] = Rating()
def update_player_ratings(pairs, players):
    random.shuffle(pairs)
    for u, v in pairs:
        players[v], players[u] = rate_1vs1(players[v], players[u])
def calculate_relative_scores(players, n_sigma):
    relative_scores = {}
    for k, v in players.items():
        relative_scores[k] = players[k].mu - n_sigma * players[k].sigma
    return relative_scores
def trueskill_ratings(pairs, iter_times=15, n_sigma=3, threshold=0.85):
    players = {}
    for i in range(iter_times):
        initialize_players(pairs, players)
        update_player_ratings(pairs, players)
        relative_scores = calculate_relative_scores(players, n_sigma=n_sigma)
        accu = measure_pairs_agreement(pairs, relative_scores)
        if accu >= threshold:
            return relative_scores
    return relative_scores
def split_edges(g):
    edges = list(g.edges())
    scc_nodes, scc_edges, nonscc_nodes, nonscc_edges = scc_nodes_edges(g)
    return edges, scc_edges, nonscc_edges
def print_results(scc_accu, nonscc_accu):
    print("----scc-------")
    print("----non-scc---")
    print("scc accu: %0.4f, nonscc accu: %0.4f" % (scc_accu, nonscc_accu))
def main(edges_file_name="/home/sunjiank/Dropbox/Data/cit-Patents/cit-Patents.txt"):
    g = nx.read_edgelist(edges_file_name, create_using=nx.DiGraph(), nodetype=int)
    edges, scc_edges, nonscc_edges = split_edges(g)
    relative_scores = trueskill_ratings(edges)
    scc_accu = measure_pairs_agreement(scc_edges, relative_scores)
    nonscc_accu = measure_pairs_agreement(nonscc_edges, relative_scores)
    print_results(scc_accu, nonscc_accu)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--graph", type=str, default="", help="graph edges list file")
    args = parser.parse_args()
    edges_file_name = args.graph
    main(edges_file_name)