import Draft

v1 = Base.Vector(0,radius,0)
v2 = Base.Vector(0,radius+body_width,0)
v3 = Base.Vector(0,radius+body_width,body_height)
v4 = Base.Vector(0,radius,body_height)
wire = Draft.makeWire([v1,v2,v3,v4],closed=True)
surface = Part.Face(wire)

decoy = Draft.makeWire([v1,v2,v3,v4],closed=True)
wire = decoy.Shape
surface = Part.Face(wire)

edge1 = Part.Line(v1,v2)


https://github.com/tpaviot/pythonocc-core/blob/master/examples/core_topology_revolved_shape.py
