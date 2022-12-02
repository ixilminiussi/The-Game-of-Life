import type
import instance
import sys
import os
from jinja2 import Template

if len(sys.argv) < 2:
    raise AttributeError('Missing path to starting state file')
else:  
    if not os.path.isfile(sys.argv[1]):
        raise FileNotFoundError('Starting state file not present in the specified location')
    if len(sys.argv) < 3:
        outputFile = 'gol.xml'
    else: 
        outputFile = sys.argv[2]

appname = 'gol'

ping = type.MessageType(id='ping', cdata='gol/ping.c')
pong = type.MessageType(id='pong', cdata='gol/pong.c')
cell = type.DeviceType(id='cell', properties='gol/cell/properties.c', state='gol/cell/state.c', onInit='gol/cell/onInit.c', readyToSend='gol/cell/readyToSend.c', outputPin=[type.OutputPin('sender', 'ping', 'gol/cell/onSendPing.c')], supervisorOutPin=type.SupervisorOutPin('pong', 'gol/cell/onSendPong.c'), inputPin=[type.InputPin('receiver', 'ping', 'gol/cell/onReceive.c')])
supervisor = type.SupervisorType(id='id', code='gol/supervisor/code.c', state='gol/supervisor/state.c', onInit='gol/supervisor/onInit.c', onStop='gol/supervisor/onStop.c', supervisorInPin=[type.SupervisorInPin('', 'pong', 'gol/supervisor/onReceive.c')])
graphType = type.GraphType(id='gol_type', messageTypes=[ping, pong], properties='gol/properties.c', deviceTypes=[cell], supervisorType=supervisor)

graphInstance = instance.GraphInstance(id='gol_instance', graphTypeId='gol_type', P='{64,10,10}')

renderedGraphType = type.render(graphType=graphType)
renderedGraphInstance = instance.render(graphInstance=graphInstance, inputFile=sys.argv[1])

with open(outputFile, 'w') as f:
    f.write(
        type.fullRender(appname=appname, graphType=renderedGraphType, graphInstance=renderedGraphInstance)
    )