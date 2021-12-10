# burginfo

Gets some information about a Freifunk mesh and writes it into a JSON file.


`vpn_only_nodes` contains a list of nodeids that belong to supernodes which are not reachable via local meshes.
Even if a node in the obseerved mesh wrongly claims a supernode was his local mesh-neighbour, this override takes care of it.
The field is completely optional.
