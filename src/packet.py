from sim import Sim

class Packet(object):
    def __init__(self,source_address=1,source_port=0,
                 destination_address=1,destination_port=0,
                 ident=0,protocol="None",body="",length=0):
        # standard packet fields
        self.source_address = source_address
        self.source_port = source_port
        self.destination_address = destination_address
        self.destination_port = destination_port
        self.ident = ident
        self.protocol = protocol
        self.body = body
        self.length = length
        if self.body:
            length = len(self.body)
        # measurements
        self.created = Sim.scheduler.current_time()
        self.enter_queue = 0
        self.queueing_delay = 0
