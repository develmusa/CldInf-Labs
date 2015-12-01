#!/usr/bin/python
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet

class SimpleHub(app_manager.RyuApp):
        OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

        def __init__(self, *args, **kwargs):
                super(SimpleHub,self).__init__(*args, **kwargs)

        @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
        def switch_features_handler(self, ev):
                datapath = ev.msg.datapath
                ofproto = datapath.ofproto
                parser = datapath.ofproto_parser
                match = parser.OFPMatch()
                actions = [parser.OFPActionOutput (ofproto.OFPP_CONTROLLER, ofproto.OFPCML_NO_BUFFER)]
                self.add_flow(datapath, 0, match, actions)

        def add_flow(self, datapath, priority, match, actions):
                ofproto = datapath.ofproto
                parser = datapath.ofproto_parser
                inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,actions)]
                mod = parser.OFPFlowMod(datapath=datapath,priority=priority,match=match,instructions=inst)
                datapath.send_msg(mod)

        @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
        def _packet_in_handler(self, ev):
                msg = ev.msg
                datapath = msg.datapath
                ofproto = datapath.ofproto
                parser = datapath.ofproto_parser
                in_port = msg.match['in_port']
                out_port = ofproto.OFPP_FLOOD
                actions = [parser.OFPActionOutput(out_port)]

                data = None
                if msg.buffer_id == ofproto.OFP_NO_BUFFER:
                        data = msg.data


                out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,in_port=in_port, actions=actions, data=data)
                datapath.send_msg(out)
                dpid = datapath.id
                self.logger.info(("packet in %s %s", dpid, in_port)
