from trueskill import Rating, rate_1vs1
import networkx as nx
import random
from datetime import datetime
from measures import measure_pairs_agreement
import argparse
def compute_trueskill(pairs, players):
    if not players:
        for u, v in pairs:
            if u not in players:
                players[u] = Rating()
            if v not in players:
                players[v] = Rating()
    random.shuffle(pairs)
    for u, v in pairs:
        players[v], players[u] = rate_1vs1(players[v], players[u])
    return players
def get_players_score(players, n_sigma):
    relative_score = {}
    for k, v in players.items():
        relative_score[k] = players[k].mu - n_sigma * players[k].sigma
    return relative_score
def trueskill_ratings(pairs, iter_times=15, n_sigma=3, threshold=0.85):
    start_time = datetime.now()
    players = {}
    for i in range(iter_times):
        players = compute_trueskill(pairs, players)
        relative_scores = get_players_score(players, n_sigma=n_sigma)
        accu = measure_pairs_agreement(pairs, relative_scores)
        if accu >= threshold:
            return relative_scores
    end_time = datetime.now()
    time_used = end_time - start_time
    print("Time used in computing Trueskill: %0.4f s, iteration time is: %i" % (time_used.seconds, (i + 1)))
    return relative_scores
def graphbased_trueskill(g, iter_times=15, n_sigma=3, threshold=0.95):
    from s_c_c import scc_nodes_edges
    relative_scores = trueskill_ratings(list(g.edges()), iter_times=iter_times, n_sigma=n_sigma, threshold=threshold)
    scc_nodes, scc_edges, nonscc_nodes, nonscc_edges = scc_nodes_edges(g)
    print("---- Strongly Connected Components ----")
    scc_accu = measure_pairs_agreement(scc_edges, relative_scores)
    print("---- Non-Strongly Connected Components ----")
    nonscc_accu = measure_pairs_agreement(nonscc_edges, relative_scores)
    print("SCC Accuracy: %0.4f, Non-SCC Accuracy: %0.4f" % (scc_accu, nonscc_accu))
    return relative_scores
def main(edges_file_name="/home/sunjiank/Dropbox/Data/cit-Patents/cit-Patents.txt"):
    g = nx.read_edgelist(edges_file_name, create_using=nx.DiGraph(), nodetype=int)
    graphbased_trueskill(g)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--graph", type=str, default="", help="Graph edges list file")
    args = parser.parse_args()
    edges_file_name = args.graph
    main(edges_file_name)