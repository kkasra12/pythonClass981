def loop_size(node):
    visited_nodes={node:0}
    last_node=node
    while 1:
        new_node=last_node.next
        tmp=visited_nodes.get(new_node,-1)
        if tmp!=-1:
            return len(visited_nodes)-tmp
        visited_nodes.update({new_node:len(visited_nodes)})
        last_node=new_node
