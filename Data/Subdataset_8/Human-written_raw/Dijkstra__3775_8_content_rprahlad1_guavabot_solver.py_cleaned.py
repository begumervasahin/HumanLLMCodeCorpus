import networkx as nx
import random
import operator
import numpy as np
def update_weight(client, s_weight, s_loss):
    epsilon = 0.2
    return s_weight*((1-epsilon)**(s_loss))
def findbots(client, mst):
    all_students = list(range(1, client.students + 1))
    non_home = list(range(1, client.home)) + list(range(client.home + 1, client.v + 1))
    losses = {}
    student_weights = {}
    paths = {}
    student_response = {}
    scores = {}
    bots_found = 0
    dont_remote = []
    for student in all_students:
        student_weights[student] = 1
        losses[student] = 0
    for i in non_home:
        student_response[i] = client.scout(i, all_students)
        scores[i] = sum(student_response[i].values())
    bots_remoted_home = 0
    while bots_found < client.bots:
        if scores:
            sorted = max(scores.items(), key=operator.itemgetter(1))
            max_vertex = sorted[0]
        else:
            break
        path = nx.dijkstra_path(mst, max_vertex, client.home)
        scores.pop(max_vertex)
        if path[0] not in dont_remote:
            num = client.remote(path[0], path[1])
            if num and path[1] == client.home:
                bots_remoted_home += num
            if num:
                paths[max_vertex] = path[1:]
                dont_remote.append(path[1])
            bots_found += num
            dont_remote.append(path[0])
        responses = student_response[max_vertex]
        for stud in responses.keys():
            if responses[stud] != num:
                losses[stud] += 1
                new_weight = update_weight(client, student_weights[stud], losses[stud])
                student_weights[stud] = new_weight if new_weight > 0.5 else 0
                if losses[stud] >= client.v/2:
                    student_weights[stud] = 1
        for s in student_weights.keys():
            total = sum(student_weights.values())
            student_weights[s] = student_weights[s]/total if total != 0 else 0
        for v in scores.keys():
            resp = student_response[v]
            for stud in resp.keys():
                if resp[stud] == num and num != 0:
                    weight = student_weights[stud]
                    scores[v] += weight if resp[stud] else 0
    return paths, bots_remoted_home
def solve(client):
    client.end()
    client.start()
    mst = nx.minimum_spanning_tree(client.G)
    paths, bots_home = findbots(client, client.graph)
    print("REMOTING HOME")
    remoted_on = []
    path_lengths = {}
    for p in paths.keys():
        path_lengths[p] = len(paths[p])
    while bots_home < client.bots:
        max_length = max(path_lengths.items(), key=operator.itemgetter(1))[1]
        if max_length == 1:
            break
        for bot in paths.keys():
            if path_lengths[bot] == max_length:
                botpath = paths[bot]
                if botpath[0] not in remoted_on:
                    num = client.remote(botpath[0], botpath[1])
                    remoted_on.append(botpath[0])
                    paths[bot] = paths[bot][1:]
                    path_lengths[bot] -= 1
                    if num == 0:
                        break
                    if botpath[1] == client.home:
                        bots_home += num
    print(bots_home)
    client.end()