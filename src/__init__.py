import json

from mininet.net import Containernet
from mininet.node import Controller
from mininet.log import info, setLogLevel
from mininet.link import TCLink
from mininet.cli import CLI


data = ""
with open("../sample.json") as f:
    data = json.load(f)

# init the network
net = Containernet(controller=Controller)
net.addController('c0')

nodeDic = {}

# add nodes
containers = data['containers']
for c in containers:
    keys = list(c.keys())
    cImage = ""
    cId =""
    cIp=""
    cVolumes=""
    if 'dimage' in keys:
        cImage = c['dimage']
    if 'id' in keys:
        cId = c['id']
    if 'ip' in keys:
        cIp = c['ip']
    if 'name' in keys:
        cName = c['name']
    if 'volumes' in keys:
        cVolumes = c['volumes']
    if cVolumes == "":
        d = net.addDocker(cName, ip=cId, dimage=cImage)
    else:
        d = net.addDocker(cName, ip=cId, dimage=cImage, volumes=cVolumes)
    nodeDic[cId] = d



switches = data['switches']
for s in switches:
    keys = list(s.keys())
    sId=""
    sName= ""
    if 'id' in keys:
        sId = s['id']
    if 'name' in keys:
        sName = s['name']

    sT = net.addSwitch(sName)
    nodeDic[sId] = sT

links = data['links']
for l in links:
    keys = list(l.keys())
    lBandwidth=""
    lDelay=""
    lLoss=""
    lFrom=""
    lTo=""
    if 'bandwidth' in keys:
        lBandwidth = l['bandwidth']
    if 'delay' in keys:
        lDelay = l['delay']
    if 'loss' in keys:
        lLoss = l['loss']
    if 'from' in keys:
        lFrom = l['from']
    if 'to' in keys:
        lTo = l['to']
    if (lBandwidth == "") & (lLoss == "") & (lDelay == ""):
        lT = net.addLink(nodeDic[lFrom], nodeDic[lTo])
    else:
        if lBandwidth != "":
            if lDelay != "":
                if lLoss != "":
                    lT = net.addLink(nodeDic[lFrom], nodeDic[lTo], delay=lDelay, bw=lBandwidth, loss=lLoss, cls=TCLink)
                else:
                    lT = net.addLink(nodeDic[lFrom], nodeDic[lTo], delay=lDelay, bw=lBandwidth, cls=TCLink)

            else:
                if lLoss != "":
                    lT = net.addLink(nodeDic[lFrom], nodeDic[lTo], bw=lBandwidth, loss=lLoss, cls=TCLink)
                else:
                    lT = net.addLink(nodeDic[lFrom], nodeDic[lTo], bw=lBandwidth, cls=TCLink)
        else:
            if lDelay != "":
                if lLoss != "":
                    lT = net.addLink(nodeDic[lFrom], nodeDic[lTo], delay=lDelay, loss=lLoss, cls=TCLink)
                else:
                    lT = net.addLink(nodeDic[lFrom], nodeDic[lTo], delay=lDelay, cls=TCLink)

            else:
                if lLoss != "":
                    lT = net.addLink(nodeDic[lFrom], nodeDic[lTo], loss=lLoss, cls=TCLink)
                else:
                    lT = net.addLink(nodeDic[lFrom], nodeDic[lTo])

info('*** Starting network\n')
net.start()

CLI(net)
info("stop")
net.stop()
