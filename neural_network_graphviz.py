# noinspection SpellCheckingInspection
from typing import List

graph_template = """
digraph G {{
    rankdir=LR
    splines=line
    nodesep=.05;
    
    node [label=""];
    
    {subgraph_clusters}
        
    {edges}
}}
"""

subgraph_cluster_template = """
    subgraph cluster_{num} {{
        color=white;
        node [style=solid,color={color}, shape=circle];
        {node_names};
        label = "{label}";
    }}
"""


def render_subgraph_cluster(n_layer: int, color: str, num_nodes: int, label: str) -> str:
    return subgraph_cluster_template.format(
        num=n_layer,
        color=color,
        node_names=' '.join([f'a{n_layer}_{x}' for x in range(num_nodes)]),
        label=label,
    )


def node_color(n_layer: int, num_layers: int) -> str:
    return 'seagreen' if n_layer == 0 else 'red2' if n_layer == num_layers - 1 else 'blue4'


def layer_label(n_layer: int, num_layers: int) -> str:
    return 'Input layer' if n_layer == 0 else 'Output layer' if n_layer == num_layers - 1 else f'Hidden layer {n_layer}'


def render_graph(layers: List[int]):
    edges = []
    for i, num_nodes in enumerate(layers):
        for source in range(num_nodes):
            if i == len(layers) -1:
                continue
            for dest in range(layers[i+1]):
                edges.append(f'a{i}_{source} -> a{i+1}_{dest}')

    subgraph_clusters = [
        render_subgraph_cluster(n_layer, node_color(n_layer, len(layers)), layers[n_layer], layer_label(n_layer, len(layers)))
        for n_layer in range(len(layers))
    ]
    return graph_template.format(
        subgraph_clusters='\n'.join(subgraph_clusters),
        edges='\n'.join(edges)
    )


if __name__ == '__main__':
    print(render_graph([3, 4, 1]))
