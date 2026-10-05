import copy
def toposort( fanin_copy ) :
  topo_list = []
  while ( len(topo_list) < len( fanin_copy ) ) :
    curr_src = find_Node_Whose_All_Fanin_Nodes_Are_Processed( fanin_copy, topo_list )
    topo_list.append( curr_src )
    for v in range( len( fanin_copy ) ) :
      if ( curr_src in fanin_copy[v] ) :
        fanin_copy[v].remove( curr_src )
  return topo_list
def find_Node_Whose_All_Fanin_Nodes_Are_Processed( fanin_copy, topo_list ) :
  for v in range( len( fanin_copy ) ) :
    if ( len( fanin_copy[ v ] ) == 0 ) and ( v not in topo_list ) :
      return v
  return None
def aat_dynprog ( fanin, dly ) :
  aat = [ 0 for l in fanin ]
  toposort_list = toposort ( copy.deepcopy( fanin ) )
  for v in toposort_list :
    tmp = dly[ v ]
    for u in fanin[ v ] :
      if ( tmp < aat[u] + dly[v] ) :
        tmp = aat[u] + dly[v]
    aat[v] = tmp
  return aat
fanin = [[3, 2, 1], [], [8, 5, 4, 3], [7, 6], [8, 6, 5], [7, 6], [9, 8], [9], [9], []]
N = len(fanin)
dly = [ 10 for l in fanin ]
print "aat values are ", aat_dynprog( fanin, dly )