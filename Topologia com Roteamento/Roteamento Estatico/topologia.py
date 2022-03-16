#!/usr/bin/python
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(remote_controller):
    "Create a network."
    net = Mininet_wifi()

    info("*** Adding stations/hosts\n")
    # Criando Redes

    # REDE A
    h1_redeA = net.addHost("h1RedeA", ip="192.0.2.5/24")
    h2_redeA = net.addHost("h2RedeA", ip="192.0.2.10/24")

    # REDE B
    h1_redeB = net.addHost("h1RedeB", ip="203.0.113.5/24")
    h2_redeB = net.addHost("h2RedeB", ip="203.0.113.10/24")

    # REDE C
    h1_redeC = net.addHost("h1RedeC", ip="198.51.100.5/24")
    h2_redeC = net.addHost("h2RedeC", ip="198.51.100.10/24")

    # REDE D ( Estacoes )
    sta01 = net.addStation(
        "sta01", 
        ip="192.168.10.5/24",
        mac="00:00:00:00:02:21"
        )
    
    sta02 = net.addStation(
        "sta02", 
        ip="192.168.10.10/24",
        mac="00:00:00:00:02:22"
        )

    # Accesspoint
    ap01 = net.addAccessPoint(
        "ap1",
        failMode="standalone",
        mac="00:00:00:00:00:10",
        ssid="AP1",
        mode="g",
        channel="1"
    )

    info("*** Adding Switches (core)\n")

    # Switches

    switchA = net.addSwitch("switchA0")
    switchB = net.addSwitch("switchB0")
    switchC = net.addSwitch("switchC0")

    info("*** Adding routers\n")
    
    # Routers

    roteador1 = net.addHost("roteador1", ip="192.0.2.1/24")
    roteador2 = net.addHost("roteador2", ip="10.10.100.254/24")
    roteador3 = net.addHost("roteador3", ip="10.10.102.254/24")
    roteador4 = net.addHost("roteador4", ip="10.10.101.254/24")
    roteador5 = net.addHost("roteador5", ip="10.10.105.254/24")
    roteador6 = net.addHost("roteador6", ip="10.10.201.254/24")
    roteador7 = net.addHost("roteador7", ip="10.10.203.254/24")
    roteador8 = net.addHost("roteador8", ip="10.10.200.254/24")
    roteador9 = net.addHost("roteador9", ip="198.51.100.1/24")
    roteador10 = net.addHost("roteador10", ip="203.0.113.1/24")
    roteador11 = net.addHost("roteador11", ip="10.10.204.254/24")

    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4)

    info("*** Configuring WiFi Nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")

    # Criando Links

    net.addLink(h1_redeA, switchA, bw=1000)
    net.addLink(h2_redeA, switchA, bw=1000)
    net.addLink(switchA, roteador1, bw=1000)

    net.addLink(h1_redeB, switchB, bw=1000)
    net.addLink(h2_redeB, switchB, bw=1000)
    net.addLink(switchB, roteador10, bw=1000)

    net.addLink(h1_redeC, switchC, bw=1000)
    net.addLink(h2_redeC, switchC, bw=1000)
    net.addLink(switchC, roteador9, bw=1000)

    net.addLink(sta01, ap01)
    net.addLink(sta02, ap01)
    net.addLink(roteador9, ap01, bw=1000)

    # roteadores

    # Roteador1
    net.addLink(roteador1, roteador2, bw=1000)
    net.addLink(roteador1, roteador3, bw=1000)

    # Roteador2
    net.addLink(roteador2, roteador4, bw=1000)

    # Roteador3
    net.addLink(roteador3, roteador4, bw=1000)

    # Roteador4
    net.addLink(roteador4, roteador5, bw=1000)

    # Roteador5
    net.addLink(roteador5, roteador8, bw=1000)
    net.addLink(roteador5, roteador6, bw=1000)

    # Roteador6
    net.addLink(roteador6, roteador10, bw=1000)
    net.addLink(roteador6, roteador7, bw=1000)

    # Roteador7
    net.addLink(roteador7, roteador11, bw=1000)
    net.addLink(roteador7, roteador8, bw=1000)

    # Roteador8
    net.addLink(roteador8, roteador11, bw=1000)
    net.addLink(roteador8, roteador9, bw=1000)

    # Roteador10
    net.addLink(roteador10, roteador11, bw=1000)

    net.start()
    net.staticArp()

    switchA.cmd("ovs-ofctl add-flow {} \"actions=output:NORMAL\"".format(switchA.name))
    switchB.cmd("ovs-ofctl add-flow {} \"actions=output:NORMAL\"".format(switchB.name))
    switchC.cmd("ovs-ofctl add-flow {} \"actions=output:NORMAL\"".format(switchC.name))

    # Criando Interfaces

    # Roteador 1
    roteador1.cmd("ifconfig roteador1-eth1 10.10.100.1/24")
    roteador1.cmd("ifconfig roteador1-eth2 10.10.102.1/24")

    # Roteador 2
    roteador2.cmd("ifconfig roteador2-eth1 10.10.101.1/24")

    # Roteador 3
    roteador3.cmd("ifconfig roteador3-eth1 10.10.103.1/24")

    # Roteador 4
    roteador4.cmd("ifconfig roteador4-eth1 10.10.103.254/24")
    roteador4.cmd("ifconfig roteador4-eth2 10.10.105.1/24")

    # Roteador 5
    roteador5.cmd("ifconfig roteador5-eth1 10.10.200.1/24")
    roteador5.cmd("ifconfig roteador5-eth2 10.10.201.1/24")

    # Roteador 6
    roteador6.cmd("ifconfig roteador6-eth1 10.10.202.1/24")
    roteador6.cmd("ifconfig roteador6-eth2 10.10.203.1/24")

    # Roteador 7
    roteador7.cmd("ifconfig roteador7-eth1 10.10.204.1/24")
    roteador7.cmd("ifconfig roteador7-eth2 10.10.207.1/24")

    # Roteador 8
    roteador8.cmd("ifconfig roteador8-eth1 10.10.207.254/24")
    roteador8.cmd("ifconfig roteador8-eth2 10.10.206.1/24")
    roteador8.cmd("ifconfig roteador8-eth3 10.10.208.1/24")

    # Roteador 9
    roteador9.cmd("ifconfig roteador9-eth1 192.168.10.1/24")
    roteador9.cmd("ifconfig roteador9-eth2 10.10.208.254/24")

    # Roteador 10
    roteador10.cmd("ifconfig roteador10-eth1 10.10.202.254/24")
    roteador10.cmd("ifconfig roteador10-eth2 10.10.205.1/24")

    # Roteador 11
    roteador11.cmd("ifconfig roteador11-eth1 10.10.205.254/24")
    roteador11.cmd("ifconfig roteador11-eth2 10.10.206.254/24")
    
    

    # Criando Rotas
    # Hosts

    h1_redeA.cmd("ip route add default via 192.0.2.1")
    h2_redeA.cmd("ip route add default via 192.0.2.1")

    h1_redeB.cmd("ip route add default via 203.0.113.1")
    h2_redeB.cmd("ip route add default via 203.0.113.1")

    h1_redeC.cmd("ip route add default via 198.51.100.1")
    h2_redeC.cmd("ip route add default via 198.51.100.1")

    sta01.cmd("ip route add default via 192.168.10.1")
    sta02.cmd("ip route add default via 192.168.10.1")

    # Roteador 1
    roteador1.cmd("ip route add to 10.10.101.0/24 via 10.10.100.254")
    roteador1.cmd("ip route add to 10.10.103.0/24 via 10.10.102.254")
    roteador1.cmd("ip route add default via 10.10.102.254")

    # Roteador 2
    roteador2.cmd("ip route add to 192.0.2.0/24 via 10.10.100.1")
    roteador2.cmd("ip route add to 10.10.102.0/24 via 10.10.100.1")
    roteador2.cmd("ip route add default via 10.10.101.254")

    # Roteador 3
    roteador3.cmd("ip route add to 192.0.2.0/24 via 10.10.102.1")
    roteador3.cmd("ip route add to 10.10.101.0/24 via 10.10.102.1")
    roteador3.cmd("ip route add default via 10.10.103.254")

    # Roteador 4
    roteador4.cmd("ip route add to 192.0.2.0/24 via 10.10.103.1")
    roteador4.cmd("ip route add to 10.10.100.0/24 via 10.10.101.1")
    roteador4.cmd("ip route add to 10.10.101.0/24 via 10.10.103.1")
    roteador4.cmd("ip route add default via 10.10.105.254")

    # Roteador 5
    roteador5.cmd("ip route add to 198.51.100.0/24 via 10.10.200.254")
    roteador5.cmd("ip route add to 192.168.10.0/24 via 10.10.200.254")
    roteador5.cmd("ip route add to 203.0.113.0/24 via 10.10.201.254")
    roteador5.cmd("ip route add to 10.10.202.0/24 via 10.10.201.254")
    roteador5.cmd("ip route add to 10.10.203.0/24 via 10.10.201.254")
    roteador5.cmd("ip route add to 10.10.204.0/24 via 10.10.200.254")
    roteador5.cmd("ip route add to 10.10.205.0/24 via 10.10.200.254")
    roteador5.cmd("ip route add to 10.10.206.0/24 via 10.10.200.254")
    roteador5.cmd("ip route add to 10.10.207.0/24 via 10.10.200.254")
    roteador5.cmd("ip route add to 10.10.208.0/24 via 10.10.200.254")
    roteador5.cmd("ip route add default via 10.10.105.1")


    # Roteador 6
    roteador6.cmd("ip route add to 203.0.113.0/24 via 10.10.202.254")
    roteador6.cmd("ip route add to 198.51.100.0/24 via 10.10.201.1")
    roteador6.cmd("ip route add to 192.168.10.0/24 via 10.10.201.1")
    roteador6.cmd("ip route add to 10.10.204.0/24 via 10.10.203.254")
    roteador6.cmd("ip route add to 10.10.205.0/24 via 10.10.202.254")
    roteador6.cmd("ip route add to 10.10.206.0/24 via 10.10.201.1")
    roteador6.cmd("ip route add to 10.10.207.0/24 via 10.10.203.254")
    roteador6.cmd("ip route add to 10.10.208.0/24 via 10.10.201.1")
    roteador6.cmd("ip route add to 10.10.200.0/24 via 10.10.201.1")
    roteador6.cmd("ip route add default via 10.10.201.1")

    # Roteador 7
    roteador7.cmd("ip route add to 203.0.113.0/24 via 10.10.203.1")
    roteador7.cmd("ip route add to 198.51.100.0/24 via 10.10.207.254")
    roteador7.cmd("ip route add to 192.168.10.0/24 via 10.10.207.254")
    roteador7.cmd("ip route add to 10.10.200.0/24 via 10.10.207.254")
    roteador7.cmd("ip route add to 10.10.201.0/24 via 10.10.203.1")
    roteador7.cmd("ip route add to 10.10.202.0/24 via 10.10.203.1")
    roteador7.cmd("ip route add to 10.10.205.0/24 via 10.10.204.254")
    roteador7.cmd("ip route add to 10.10.206.0/24 via 10.10.204.254")
    roteador7.cmd("ip route add to 10.10.208.0/24 via 10.10.207.254")
    roteador7.cmd("ip route add default via 10.10.203.1")

    #Roteador 8
    roteador8.cmd("ip route add to 203.0.113.0/24 via 10.10.206.254")
    roteador8.cmd("ip route add to 198.51.100.0/24 via 10.10.208.254")
    roteador8.cmd("ip route add to 192.168.10.0/24 via 10.10.208.254")
    roteador8.cmd("ip route add to 192.0.2.0/24 via 10.10.200.1")
    roteador8.cmd("ip route add to 10.10.201.0/24 via 10.10.200.1")
    roteador8.cmd("ip route add to 10.10.202.0/24 via 10.10.207.1")
    roteador8.cmd("ip route add to 10.10.203.0/24 via 10.10.207.1")
    roteador8.cmd("ip route add to 10.10.204.0/24 via 10.10.206.254")
    roteador8.cmd("ip route add to 10.10.205.0/24 via 10.10.206.254")
    roteador8.cmd("ip route add default via 10.10.200.1")

    # Roteador 9
    roteador9.cmd("ip route add default via 10.10.208.1")

    # Roteador 10
    roteador10.cmd("ip route add to 198.51.100.0/24 via 10.10.205.254")
    roteador10.cmd("ip route add to 192.168.10.0/24 via 10.10.205.254")
    roteador10.cmd("ip route add to 192.0.2.0/24 via 10.10.202.1")
    roteador10.cmd("ip route add default via 10.10.202.1")

    # Roteador 11
    roteador11.cmd("ip route add default via 10.10.204.1")

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    remote_controller = False
    topology(remote_controller)