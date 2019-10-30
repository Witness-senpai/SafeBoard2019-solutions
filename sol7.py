import collections, itertools

data = []

while True:
    try:
        s = input()
        if s != '':
            data = s.split(" ")
        else:
            break
    except:
        break

def get_loops(node_):
    network = {}
    for a,b in node_:
        network[a].add(b) if a in network else network.update({a:{b}})
        network[b].add(a) if b in network else network.update({b:{a}})
    chain = collections.OrderedDict()
    def __loop_iterator(node):
        if node not in chain:
            chain[node] = None
            next = network[node]
            while next:
                n = next.pop()
                network[n].remove(node)
                yield from __loop_iterator(n)
            chain.popitem()
        else: 
            yield tuple(itertools.chain(itertools.takewhile(lambda x: x is not node, reversed(chain)), (node,)))

    for n in network: 
        return tuple(__loop_iterator(n))

if (get_loops(data) is None):
    print("FALSE")
else:
    print("TRUE")