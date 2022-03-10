 #!/usr/bin/python
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(remote_controller):
    "Create a network."
    net = Mininet_wifi()

    info("*** Adding servers\n")

    server1 = net.addHost("server1", ip="10.0.1.10", mac="00:00:00:00:01:0a")
    server2 = net.addHost("server2", ip="10.0.1.11", mac="00:00:00:00:02:0a")

    info("*** Adding Switches (core)\n")

    switchDC1 = net.addSwitch("switchDC1")
    switchAG1 = net.addSwitch("switchAG1")

    switch1 = net.addSwitch("switch1")
    switch2 = net.addSwitch("switch2")
    switch3 = net.addSwitch("switch3")
    switch4 = net.addSwitch("switch4")
    switch5 = net.addSwitch("switch5")

    switch1.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switch1.name)
    )
    switch2.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switch2.name)
    )
    switch3.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switch3.name)
    )
    switch4.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switch4.name)
    )
    switch5.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switch5.name)
    )
    switchDC1.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switchDC1.name)
    )
    switchAG1.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switchAG1.name)
    )
    
    info("* Adding Stations\n")

    sta01B1 = net.addStation(
        "sta01B1",
        ip="10.0.1.21",
        mac="00:00:00:00:01:21",
        position="35,230,0",
    )

    sta02B1 = net.addStation(
        "sta02B1",
        ip="10.0.1.22",
        mac="00:00:00:00:01:22",
        position="35,160,0",
    )
    
    sta03B1 = net.addStation(
        "sta03B1",
        ip="10.0.1.23",
        mac="00:00:00:00:01:23",
        position="35,80,0",
    )

    sta04B1 = net.addStation(
        "sta04B1",
        ip="10.0.1.24",
        mac="00:00:00:00:01:24",
        position="35,10,0",
    )

    sta01B2 = net.addStation(
        "sta01B2",
        ip="10.0.1.25",
        mac="00:00:00:00:01:25",
        position="125,230,0",
    )

    sta02B2 = net.addStation(
        "sta02B2",
        ip="10.0.1.26",
        mac="00:00:00:00:02:22",
        position="125,160,0",
    )
    
    sta03B2 = net.addStation(
        "sta03B2",
        ip="10.0.1.27",
        mac="00:00:00:00:02:23",
        position="125,80,0",
    )

    sta04B2 = net.addStation(
        "sta04B1",
        ip="10.0.2.24",
        mac="00:00:00:00:02:24",
        position="125,10,0",
    )

    sta01B3 = net.addStation(
        "sta01B3",
        ip="10.0.3.21",
        mac="00:00:00:00:03:21",
        position="225,230,0",
    )

    sta02B3 = net.addStation(
        "sta02B3",
        ip="10.0.3.22",
        mac="00:00:00:00:03:22",
        position="225,160,0",
    )
    
    sta03B3 = net.addStation(
        "sta03B3",
        ip="10.0.3.23",
        mac="00:00:00:00:03:23",
        position="225,80,0",
    )

    sta04B3 = net.addStation(
        "sta04B3",
        ip="10.0.3.24",
        mac="00:00:00:00:03:24",
        position="225,10,0",
    )

    sta01B4 = net.addStation(
        "sta01B4",
        ip="10.0.4.21",
        mac="00:00:00:00:04:21",
        position="315,230,0",
    )

    sta02B4 = net.addStation(
        "sta02B4",
        ip="10.0.4.22",
        mac="00:00:00:00:04:22",
        position="315,160,0",
    )
    
    sta03B4 = net.addStation(
        "sta03B4",
        ip="10.0.4.23",
        mac="00:00:00:00:04:23",
        position="315,80,0",
    )

    sta04B4 = net.addStation(
        "sta04B4",
        ip="10.0.4.24",
        mac="00:00:00:00:04:24",
        position="315,10,0",
    )

    sta01B5 = net.addStation(
        "sta01B5",
        ip="10.0.5.21",
        mac="00:00:00:00:05:21",
        position="405,230,0",
    )

    sta02B5 = net.addStation(
        "sta02B5",
        ip="10.0.5.22",
        mac="00:00:00:00:05:22",
        position="405,160,0",
    )
    
    sta03B5 = net.addStation(
        "sta03B5",
        ip="10.0.5.23",
        mac="00:00:00:00:05:23",
        position="405,80,0",
    )

    sta04B5 = net.addStation(
        "sta04B5",
        ip="10.0.5.24",
        mac="00:00:00:00:05:24",
        position="405,10,0",
    )
    
    info("*** Adicionando AccessPoints\n")

    ap01B1 = net.addAccessPoint(
        "ap01B1",
        failMode="standalone",
        mac="00:00:00:00:00:10",
        ssid="BLOCO1-ap01B1",
        mode="g",
        channel="1",
        position="10,190,0",
    )
    ap02B1 = net.addAccessPoint(
        "ap02B1",
        failMode="standalone",
        mac="00:00:00:00:00:11",
        ssid="BLOCO1-ap02B1",
        mode="g",
        channel="6",
        position="100,50,0",
    )

    ap01B2 = net.addAccessPoint(
        "ap01B2",
        failMode="standalone",
        mac="00:00:00:00:00:12",
        ssid="BLOCO2-ap01B2",
        mode="g",
        channel="2",
        position="100,190,0",
    )
    ap02B2 = net.addAccessPoint(
        "ap02B2",
        failMode="standalone",
        mac="00:00:00:00:00:13",
        ssid="BLOCO2-ap02B2",
        mode="g",
        channel="7",
        position="100,50,0",
    )
    ap01B3 = net.addAccessPoint(
        "ap01B3",
        failMode="standalone",
        mac="00:00:00:00:00:14",
        ssid="BLOCO3-ap01B3",
        mode="g",
        channel="3",
        position="190,190,0",
    )
    ap02B3 = net.addAccessPoint(
        "ap02B3",
        failMode="standalone",
        mac="00:00:00:00:00:15",
        ssid="BLOCO3-ap02B3",
        mode="g",
        channel="8",
        position="190,50,0",
    )
    ap01B4 = net.addAccessPoint(
        "ap01B4",
        failMode="standalone",
        mac="00:00:00:00:00:16",
        ssid="BLOCO4-ap01B4",
        mode="g",
        channel="4",
        position="280,190,0",
    )
    ap02B4 = net.addAccessPoint(
        "ap02B4",
        failMode="standalone",
        mac="00:00:00:00:00:17",
        ssid="BLOCO4-ap02B4",
        mode="g",
        channel="9",
        position="280,50,0",
    )
    ap01B5 = net.addAccessPoint(
        "ap01B5",
        failMode="standalone",
        mac="00:00:00:00:00:18",
        ssid="BLOCO5-ap01B5",
        mode="g",
        channel="5",
        position="370,190,0",
    )
    ap02B5 = net.addAccessPoint(
        "ap02B5",
        failMode="standalone",
        mac="00:00:00:00:00:19",
        ssid="BLOCO5-ap02B5",
        mode="g",
        channel="10",
        position="370,50,0",
    )

    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4)

    info("*** Configuring WiFi Nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")

    info("**** Creating links DC\n")

    net.addLink(server1, switchDC1, bw=1000)
    net.addLink(server2, switchDC1, bw=1000)

    info("**** Creating links DC-AG\n")

    net.addLink(switchAG1, switchDC1, bw=1000)

    info("**** Creating links AG-BLOCOS\n")

    net.addLink(switch1, switchAG1, bw=1000)
    net.addLink(switch2, switchAG1, bw=1000)
    net.addLink(switch3, switchAG1, bw=1000)
    net.addLink(switch4, switchAG1, bw=1000)
    net.addLink(switch5, switchAG1, bw=1000)

    info("**** Creating links Switches-AccessPoint\n")

    net.addLink(ap01B1, switch1, bw=100)
    net.addLink(ap02B1, switch1, bw=100)

    net.addLink(ap01B2, switch2, bw=100)
    net.addLink(ap02B2, switch2, bw=100)

    net.addLink(ap01B4, switch3, bw=100)
    net.addLink(ap02B4, switch3, bw=100)

    net.addLink(ap01B4, switch4, bw=100)
    net.addLink(ap02B4, switch4, bw=100)

    net.addLink(ap01B5, switch5, bw=100)
    net.addLink(ap02B5, switch5, bw=100)

    info("**** Creating links AccessPoint-Stations\n")
    
    info("**** Creating on Bloco1\n")

    net.addLink(sta01B1, ap01B1)
    net.addLink(sta02B1, ap01B1)
    net.addLink(sta03B1, ap02B1)
    net.addLink(sta04B1, ap02B1)

    info("**** Creating on Bloco2\n")

    net.addLink(sta01B2, ap01B2)
    net.addLink(sta02B2, ap01B2)
    net.addLink(sta03B2, ap02B2)
    net.addLink(sta04B2, ap02B2)

    info("**** Creating on Bloco3\n")

    net.addLink(sta01B3, ap01B3)
    net.addLink(sta02B3, ap01B3)
    net.addLink(sta03B3, ap02B3)
    net.addLink(sta04B3, ap02B3)

    info("**** Creating on Bloco4\n")

    net.addLink(sta01B4, ap01B4)
    net.addLink(sta02B4, ap01B4)
    net.addLink(sta03B4, ap02B4)
    net.addLink(sta04B4, ap02B4)

    info("**** Creating on Bloco5\n")

    net.addLink(sta01B5, ap01B5)
    net.addLink(sta02B5, ap01B5)
    net.addLink(sta03B5, ap02B5)
    net.addLink(sta04B5, ap02B5)

    info("*** Starting network\n")
    net.plotGraph(max_x=500, max_y=500)
    net.start()
    net.staticArp()

    info("*** Applying switches configurations\n")

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    remote_controller = False
    topology(remote_controller)
