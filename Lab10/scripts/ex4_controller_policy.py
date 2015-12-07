#!/usr/bin/env python
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
         
class PolicyController(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    
    h1 = '00:00:00:00:00:01'
    h2 = '00:00:00:00:00:02'
    h3 = '00:00:00:00:00:03'
    h4 = '00:00:00:00:00:04'
    h5 = '00:00:00:00:00:05'
    h6 = '00:00:00:00:00:06'
    broadcast = 'ff:ff:ff:ff:ff:ff'
    
    group1 = ["00:00:00:00:00:02","00:00:00:00:00:03","00:00:00:00:00:04"]
    group2 = ["00:00:00:00:00:01","00:00:00:00:00:03","00:00:00:00:00:04"]
    group3 = ["00:00:00:00:00:01","00:00:00:00:00:02","00:00:00:00:00:04","00:00:00:00:00:05","00:00:00:00:00:06"]
    group4 = ["00:00:00:00:00:01","00:00:00:00:00:02","00:00:00:00:00:03","00:00:00:00:00:05","00:00:00:00:00:06"]
    group5 = ["00:00:00:00:00:03","00:00:00:00:00:04","00:00:00:00:00:06"]
    group6 = ["00:00:00:00:00:03","00:00:00:00:00:04","00:00:00:00:00:05"]

    print "----------------"

    print "Host 1", h1
    print "Host 2", h2
    print "Host 3", h3
    print "Host 4", h4
    print "Host 5", h5
    print "Host 6", h6

    print "Access Group Host1", group1
    print "Access Group Host2", group2
    print "Access Group Host3", group3
    print "Access Group Host4", group4
    print "Access Group Host5", group5
    print "Access Group Host6", group6    
    
    print "----------------"

    def __init__(self, *args, **kwargs):
        super(PolicyController, self).__init__(*args, **kwargs)
        self.mac_to_port = {}

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER, ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
        mod = parser.OFPFlowMod(datapath=datapath, priority=priority, match=match, instructions=inst)
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.match['in_port']

        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]

        dst = eth.dst
        src = eth.src

        dpid = datapath.id
        self.mac_to_port.setdefault(dpid,{})

        self.logger.info("packet in %s %s %s %s", dpid, src, dst, in_port)

        self.mac_to_port[dpid][src] = in_port

	print "-------------------"

	print "source address:", src
	print "destination address:", dst

	print "-------------------"

	actions = []
	out_port = ""

        if src == self.h1 and dst in self.group1[0:]:   
	    print "Fall 1: h1 ping to group1"
	    out_port = self.mac_to_port[dpid][dst]
            actions = [parser.OFPActionOutput(out_port)]
            match = parser.OFPMatch(in_port=in_port,eth_dst=dst)
            self.add_flow(datapath, 1, match, actions)
            self.logger.info("access allowed %s %s", src, dst)
        elif src == self.h2 and dst in self.group2[0:]:
            print "Fall 2: h2 ping to group2"
            out_port = self.mac_to_port[dpid][dst]
            actions = [parser.OFPActionOutput(out_port)]
            match = parser.OFPMatch(in_port=in_port,eth_dst=dst)
            self.add_flow(datapath, 1, match, actions)
            self.logger.info("access allowed %s %s", src, dst)
        elif src == self.h3 and dst in self.group3[0:]:
            print "Fall 3: h3 ping to group3"
            out_port = self.mac_to_port[dpid][dst]
            actions = [parser.OFPActionOutput(out_port)]
            match = parser.OFPMatch(in_port=in_port,eth_dst=dst)
            self.add_flow(datapath, 1, match, actions)
            self.logger.info("access allowed %s %s", src, dst)
        elif src == self.h4 and dst in self.group4[0:]:
            print "Fall 4: h4 ping to group4"
            out_port = self.mac_to_port[dpid][dst]
            actions = [parser.OFPActionOutput(out_port)]
            match = parser.OFPMatch(in_port=in_port,eth_dst=dst)
            self.add_flow(datapath, 1, match, actions)
            self.logger.info("access allowed %s %s", src, dst)
        elif src == self.h5 and dst in self.group5[0:]:
            print "Fall 5: h5 ping to group5"
            out_port = self.mac_to_port[dpid][dst]
            actions = [parser.OFPActionOutput(out_port)]
            match = parser.OFPMatch(in_port=in_port,eth_dst=dst)
            self.add_flow(datapath, 1, match, actions)
            self.logger.info("access allowed %s %s", src, dst)
        elif src == self.h6 and dst in self.group6[0:]:
            print "Fall 6: h6 ping to group6"
            out_port = self.mac_to_port[dpid][dst]
            actions = [parser.OFPActionOutput(out_port)]
            match = parser.OFPMatch(in_port=in_port,eth_dst=dst)
            self.add_flow(datapath, 1, match, actions)
            self.logger.info("access allowed %s %s", src, dst)        
	elif dst == self.broadcast:
	    print "Fall 7: destination is broadcast " 
            out_port = ofproto.OFPP_FLOOD
	    match = [parser.OFPMatch(in_port=in_port, eth_dst=dst)]
	    actions = [parser.OFPActionOutput(out_port)]
            self.logger.info("broadcast detect %s %s", src, dst)
        else:
	    print "Fall 8: no match" 
            self.logger.info("access denied %s %s", src, dst)

        data = None
        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data

        out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id, in_port=in_port, actions=actions, data=data)
        datapath.send_msg(out)
        dpid = datapath.id
