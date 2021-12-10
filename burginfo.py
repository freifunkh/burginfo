#!/usr/bin/env python3

import datetime
import json
import nodesTk
import socket
import urllib

api_version = 1

if __name__ == "__main__":
    with open("config.json", "r") as f:
        config = json.load(f)

    result = dict()

    try:
        net = nodesTk.generate_from_urls(config["nodes_json"], config["graph_json"])
    except (TypeError, socket.gaierror, urllib.error.URLError):
        net = None

    if net:
        try:
            net.vpn_only_nodes = set(config["vpn_only_nodes"])
        except KeyError:
            pass
        routers = set()
        for mac in config["known_hosts"]:
            routers |= net.get_mesh_of_node(mac)

        result["version"] = api_version
        result["updated"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        result["nodes"] = len(routers)
        result["clients"] = 0
        for mac in routers:
            result["clients"] += net.get_node(mac).client_count

        with open(config["output"], "w") as f:
            json.dump(result, f)
