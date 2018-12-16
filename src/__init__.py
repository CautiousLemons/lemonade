import json

from mininet.net import Containernet
from mininet.node import Controller, OVSSwitch
from mininet.log import info, setLogLevel
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import info, setLogLevel
setLogLevel('info')

data = ""
with open("sample.json") as f:
    data = json.load(f)

# init the network
net = Containernet(controller=Controller)

nodeDic = {}
net.addController('c0')

# add nodes
jsonKey = list(data.keys())

if 'routers' in jsonKey:
    routers = data['routers']
    for r in routers:
        keys = list(r.keys())
        sId = ""
        sName = ""
        if 'id' in keys:
            sId = r['id']
        if 'name' in keys:
            sName = r['name']

        rT = net.addController(sId)
        nodeDic[sId] = rT

if 'containers' in jsonKey:
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
        if 'devices' in keys:
            cDevices = c['devices']
        if cVolumes == "":
            d = net.addDocker(cName, ip=cIp, dimage=cImage)
        else:
            d = net.addDocker(cName, ip=cIp, dimage=cImage, volumes=cVolumes, devices=cDevices)
        nodeDic[cId] = d



if 'switches' in jsonKey:
    switches = data['switches']
    for s in switches:
        keys = list(s.keys())
        sId=""
        sName= ""
        if 'id' in keys:
            sId = s['id']
        if 'name' in keys:
            sName = s['name']

        sT = net.addSwitch(sName, cls=OVSSwitch)
        nodeDic[sId] = sT


if 'links' in jsonKey:
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
                        lT = net.addLink(nodeDic[lFrom], nodeDic[lTo],
                                         delay=lDelay, bw=lBandwidth, loss=lLoss, cls=TCLink)
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
