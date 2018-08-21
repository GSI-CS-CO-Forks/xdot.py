
from decimal import Decimal

def extractGsiDmType(attrs):
  ret = ''
  for key, value in attrs.items():
    if key == "type":
      ret = value.decode("utf-8")
  return ret    


def getGsiDmElement(attrs):
  typeDict = {
    #Nodes
    "tmsg"       :  GsiDmTmsg,
    "noop"       :  GsiDmNop,
    "flow"       :  GsiDmFlow,
    "flush"      :  GsiDmFlush,
    "wait"       :  GsiDmWait,
    "block"      :  GsiDmBlock,
    "blockfixed" :  GsiDmBlock,
    "blockalign" :  GsiDmBlock,
    "qinfo"      :  GsiDmMeta,
    "listdst"    :  GsiDmMeta,
    "qbuf"       :  GsiDmMeta,
    "meta"       :  GsiDmMeta,
    #Edges
    "defdst"     : GsiDmEdge,
    "altdst"     : GsiDmEdge,
    "listdst"    : GsiDmEdge,
    "baddefdst"  : GsiDmEdge,
    "target"     : GsiDmEdge,
    "flowdst"    : GsiDmEdge,
    "dynid"      : GsiDmEdge,
    "dynpar0"    : GsiDmEdge,
    "dynpar1"    : GsiDmEdge,
    "dyntef"     : GsiDmEdge,
    "dynres"     : GsiDmEdge,
    "meta"       : GsiDmEdge,
    "dynflowdst" : GsiDmEdge,
    "resflowdst" : GsiDmEdge,
    "domflowdst" : GsiDmEdge,
  }



  eType = extractGsiDmType(attrs)
  try:
    elem = typeDict[eType](attrs)
  except KeyError:
     elem = None 
  return elem

class viewAttrs():
  def __init__(self, index, tag, raw, desc, value):
    self.index  = index
    self.tag    = tag
    self.raw    = raw
    self.desc   = desc
    self.value  = value

class GsiDmEdge():
    def __init__(self, attrs):
      self.attrs = attrs
      self.d = {}
      self.d['type']     = ''

      self.prettyTypeDict = {
        "defdst"     : "Default Destination",
        "altdst"     : "Default Destination",
        "listdst"    : "Destination List",
        "baddefdst"  : "Bad Default Destination",
        "target"     : "Command Target",
        "flowdst"    : "Flow Command Destination",
        "dynid"      : "Get ID field",
        "dynpar0"    : "Get Par0 Field",
        "dynpar1"    : "Get Par1 Field",
        "dyntef"     : "Get TEF Field",
        "dynres"     : "Get reserved Field",
        "meta"       : "Meta Connection",
        "dynflowdst" : "Dynamic Flow Destination (carpeDM internal)",
        "resflowdst" : "Resident Flow Destination (carpeDM internal)",
        "domflowdst" : "Dominant Flow Destination (carpeDM internal)",
      }

      self.prettyD = {
        'type'      : 'Edge Type',
      }

      self.indexD = {  
        'type'      : '00',
      }

      self.assign()

    def nsTime2scientific(self, nsTime):
      pass



    def assign(self):
      for key, value in self.attrs.items():
        if key in self.d:
          self.d[key] = value.decode("utf-8")

    def convertTime(self):
      pass      

    def listAll(self):
      ret = []
      for key in self.d:
        ret.append(viewAttrs(index=self.indexD[key], tag=key, raw=self.d[key], desc=self.prettyD[key], value=self.d[key]))
      return ret 

class GsiDmNode():
    def __init__(self, attrs):
      self.attrs = attrs
      self.d = {}
      
      self.d['type']     = ''
      self.d['node_id']  = ''      
      self.d['cpu']      = ''
      self.d['thread']   = ''  
      self.d['flags']    = ''  
      self.d['patentry'] = 'false'    
      self.d['patexit']  = 'false'    
      self.d['pattern']  = ''    
      self.d['bpentry']  = 'false'    
      self.d['bpexit']   = 'false'  
      self.d['beamproc'] = ''    


      self.prettyTypeDict = {

        'tmsg'       :  'Timing Message',
        'noop'       :  'Noop Command',
        'flow'       :  'Flow Command',
        'flush'      :  'Flush Command',
        'wait'       :  'Wait Command',
        'block'      :  'Block',
        'blockfixed' :  'Block',
        'blockalign' :  'Block (aligns to time grid)',
        'qinfo'      :  'Queue Information',
        'listdst'    :  'Destination List',
        'qbuf'       :  'Queue Buffer',
        'meta'       :  'Meta Information',
      }

      self.prettyD = {
        'type'      : 'Node Type',
        'node_id'   : 'Name',
        'cpu'       : 'CPU',
        'thread'    : 'Thread',
        'flags'     : 'Flags',
        'patentry'  : 'Pattern entry',
        'patexit'   : 'Pattern exit',
        'pattern'   : 'Pattern Name',
        'bpentry'   : 'Beamprocess entry',
        'bpexit'    : 'Beamprocess exit',
        'beamproc'  : 'Beamprocess Name',
        'tperiod'   : 'Time Block Period',
        'qil'       : 'Has high prio Queue',
        'qhi'       : 'Has medium prio Queue',
        'qlo'       : 'Has low prio Queue',
        'toffs'     : 'Time Offset',
        'id'        : 'ID',
        'fid'       : ' +- Format',
        'gid'       : ' +- Group',
        'evtno'     : ' +- Evt No',
        'sid'       : ' +- Sequence',
        'bpid'      : ' +- Beamprocess',
        'beamin'    : ' +- Beam in',
        'reqnobeam' : ' +- Request no beam',
        'vacc'      : ' +- Virt. Accelerator',
        'res'       : 'Reserved',
        'par'       : 'Parameter',
        'tef'       : 'Time Extension Field',
        'tvalid'    : 'Valid Time',
        'vabs'      : 'Valid Time is abs.',
        'prio'      : 'Priority',
        'qty'       : 'Quantity',
        'permanent' : 'Flow is permanent',
        'twait'     : 'Wait Time',
      }

      self.indexD = {  
        'type'      : '00',
        'node_id'   : '01',
        'cpu'       : '02',
        'thread'    : '03',
        'flags'     : '04',
        'patentry'  : '05',
        'patexit'   : '06',
        'pattern'   : '07',
        'bpentry'   : '08',
        'bpexit'    : '09',
        'beamproc'  : '10',
        'tperiod'   : '11',
        'qil'       : '12',
        'qhi'       : '13',
        'qlo'       : '14',
        'toffs'     : '15',
        'id'        : '16',
        'fid'       : '17',
        'gid'       : '18',
        'evtno'     : '19',
        'sid'       : '20',
        'bpid'      : '21',
        'beamin'    : '22',
        'reqnobeam' : '23',
        'vacc'      : '24',
        'res'       : '25',
        'par'       : '26',
        'tef'       : '27',
        'tvalid'    : '28',
        'vabs'      : '29',
        'prio'      : '30',
        'qty'       : '31',
        'permanent' : '32',
        'twait'     : '33',
      }

    def nsTime2scientific(self, nsTime):
      ret = '{0:.10e} s'.format(Decimal(float(nsTime) / 1e+9))
      return ret




    def assign(self):
      for key, value in self.attrs.items():
        if key in self.d:
          self.d[key] = value.decode("utf-8")

    def convertTime(self):
      pass      

    def listAll(self):
      ret = []
      for key in self.d:
        ret.append(viewAttrs(index=self.indexD[key], tag=key, raw=self.d[key], desc=self.prettyD[key], value=self.d[key]))
      return ret



class GsiDmBlock(GsiDmNode):
  def __init__(self, attrs):
    super(GsiDmBlock, self).__init__(attrs)

    self.d['tperiod']  = ''
    self.d['qil']      = 'false'
    self.d['qhi']      = 'false'
    self.d['qlo']      = 'false'

    self.assign()
    self.convertTime()

  def convertTime(self):
    self.d['tperiod'] = self.nsTime2scientific(self.d['tperiod']) 
  

class GsiDmEvent(GsiDmNode):
  def __init__(self, attrs):
    super(GsiDmEvent, self).__init__(attrs)

    self.d['toffs'] = ''


    self.assign()
    self.convertTime()

  def convertTime(self):
    self.d['toffs'] =  self.nsTime2scientific(self.d['toffs']) 


class GsiDmTmsg(GsiDmEvent):
  def __init__(self, attrs):
    super(GsiDmTmsg, self).__init__(attrs)

    self.d['id']         = ''
    self.d['fid']        = ''      
    self.d['gid']        = ''
    self.d['evtno']      = ''
    self.d['sid']        = ''
    self.d['bpid']       = ''
    self.d['beamin']     = ''
    self.d['reqnobeam']  = ''
    self.d['vacc']       = ''
    self.d['res']        = ''
    self.d['par']        = ''
    self.d['tef']        = ''


    self.assign()
    self.convertTime()


class GsiDmCmd(GsiDmEvent):
  def __init__(self, attrs):
    super(GsiDmCmd, self).__init__(attrs)

    self.d['tvalid']     = ''
    self.d['vabs']       = 'false'
    self.d['prio']       = ''
    self.d['qty']        = ''
    


    self.assign()
    self.convertTime()

  def convertTime(self):
    super(GsiDmCmd, self).convertTime()
    self.d['tvalid'] =  self.nsTime2scientific(self.tvalid)   

class GsiDmNop(GsiDmCmd):
  def __init__(self, attrs):
    super(GsiDmNop, self).__init__(attrs)
    self.assign()
    self.convertTime()


  

class GsiDmFlow(GsiDmCmd):
  def __init__(self, attrs):
    super(GsiDmFlow, self).__init__(attrs)
    self.d['permanent']  = 'false'

    self.assign()
    self.convertTime()

class GsiDmFlush(GsiDmCmd):
  def __init__(self, attrs):
    super(GsiDmFlush, self).__init__(attrs)
    self.assign()
    self.convertTime()


  

class GsiDmWait(GsiDmCmd):  
  def __init__(self, attrs):
    super(GsiDmWait, self).__init__(attrs)
    self.d['twait']      = ''

    self.assign()
    self.convertTime()

  def convertTime(self):
    super(GsiDmCmd, self).convertTime()
    self.d['twait'] =  self.nsTime2scientific(self.d['twait'])  

class GsiDmMeta(GsiDmNode):
  def __init__(self, attrs):
    super(GsiDmNode, self).__init__(attrs)
    self.assign()

