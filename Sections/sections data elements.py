
"""
file sections data elements
pja 10-18-2019
"""
import ETCVRClass
db = ETCVRClass.ETCVR()
def partof(db,master,subp):
    T = master
    C = T+"."+subp
    R=db.genx()
    V=R
    db.writeTCVR(T,C,V,R)
#end partof

partof(db,'master','page1')
partof(db,'master.page1','p1')
partof(db,'master.page1','p2')
partof(db,'master.page1','p3')
# subpart(master,page1)
#alias(master.page1.p1,master.page1.banner)

db.dumpTCVR()
db.dumpTRCV()
m = db.search('master','master.page1','','')
print(m)
