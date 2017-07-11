
vertices = [(0,radius,0),(0,radius+body_width,0),(0,radius+body_width,body_height),(0,radius,body_height),(0,radius,0)]

edges = []
for i in range(4):
  edge = Part.makeLine(vertices[i],vertices[i+1])
  edges.append(edge)

wire = Part.Wire(edges)
surface = Part.Face(wire)




https://github.com/tpaviot/pythonocc-core/blob/master/examples/core_topology_revolved_shape.py
