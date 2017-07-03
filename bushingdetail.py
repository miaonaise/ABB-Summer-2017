import math
import FreeCAD
import Part
from FreeCAD import Base,Placement,Rotation


BH = 30 # bush height/total length
BHL = 4 # head length
BTL = 6 # tap length
BCL = BH-BHL-BTL # core length
BOR = 3 # outer radius
BCR = 2.7 # core radius

BIRSm = 3.5 # radius of small CI
BIHSm = 0.5 # height of small CI
BIRLg = 4 # radius of large CI
BIHLg = float(BIRLg*BIHSm)/BIRSm # height of large CI (proportional)
BIS = 0.5 # seperation between CIs

BIHPack = BIHSm+BIHLg+2*BIS #pack length
BIno = int(BCL//BIHPack) # number of packs fitted into core length
BIrem = BCL % BIHPack # remainder length


Btap = Part.makeCylinder(BOR,BTL)
Bcore = Part.makeCylinder(BCR,BCL,Base.Vector(0,0,BTL))
Bhead = Part.makeCylinder(BOR,BHL,Base.Vector(0,0,BTL+BCL))
BushingSHP = Btap.fuse(Bcore).fuse(Bhead)

BIinit = BTL+float(BIrem)/2+BIS # initial height for first cone
for i in range(0,BIno):
	Bconez = BIinit + i*BIHPack	
	BconeLg = Part.makeCone(BIRLg,BCR,BIHLg,Base.Vector(0,0,Bconez))
	BconeSm = Part.makeCone(BIRSm,BCR,BIHSm,Base.Vector(0,0,Bconez+BIHLg+BIS))
	BushingSHP = BushingSHP.fuse(BconeLg).fuse(BconeSm)

BA = 25
BIn = 3
TW = 32
TH = 20
BSIN = math.sin(math.radians(BA)) ; BCOS = math.cos(math.radians(BA))


leftBushSHP = BushingSHP
leftBushSHP.rotate(Base.Vector(0,0,0),Base.Vector(1,0,0),BA)
leftBushSHP.translate(Base.Vector(BIn+BOR,float(TW)/2-10-BOR*BCOS,TH-BOR*BSIN))


rightCyl = Part.makeCylinder(BR,BH,Base.Vector(BIn+BR,float(TW)/2+10+BR*BCOS,TH-BR*BSIN),Base.Vector(0,BSIN,BCOS))
rightBushSHP = rightCyl.cut(tankSHP)
doc.addObject("Part::Feature","rightBush")
doc.rightBush.Shape = rightBushSHP

midBushSHP = BushingSHP
midBushSHP.translate(Base.Vector(BIn+BOR,float(TW)/2,TH))
doc.addObject("Part::Feature","midBush")
doc.midBush.Shape = midBushSHP

leftBushSHP = midBushSHP
leftBushSHP.rotate(Base.Vector(0,0,0),Base.Vector(1,0,0),BA)
leftBushSHP.translate(Base.Vector(BIn+BOR,float(TW)/2-BS-BOR*BCOS,TH-BOR*BSIN))
doc.addObject("Part::Feature","leftBush")
doc.leftBush.Shape = leftBushSHP



Part.show(leftBushSHP)
