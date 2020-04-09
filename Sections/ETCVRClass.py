# file ETCVRClass.py
""" embedded TCVR
pja 10-18-2019 added genx
pja 03-31-2018 added comments
PJA 10-30-2014
"""
class ETCVR:

    """ test

import ETCVRClass
db = ETCVRClass.ETCVR()
db.genx()
db.dumpTCVR()
db.writeTCVR('cust','fname','P','cid1')
db.writeTCVR('cust','cid','1','cid1')
# test that we overwrite record
db.writeTCVR('cust','fname','Paul','cid1') 

db.writeTCVR('cust','lname','Alagna','cid1')
db.writeTCVR('cust','em','Paul@g.com','cid1')
db.writeTCVR('cust','shoe','10.5','cid1')

db.writeTCVR('cust','cid','2','cid2')
db.writeTCVR('cust','fname','Carl','cid2')
db.writeTCVR('cust','lname','Mattocks','cid2')
db.writeTCVR('cust','em','CarlM@t.com','cid2')
db.dumpTCVR()
db.dumpTRCV()
    """
    def __init__(self):
        self.TCVR = {} # T-<C-<V-<R
        self.TRCV = {} # T-<R-<C=V
        # big data additions
        self.CV  = {}
        self.VC = {}
        import time
        self.T = time
    #END init
    def writeTCVR(self,T,C,V,R):
        """ assigns space into arrays """
        #TCVR
        # does [T] exist n-make one
        try:
            j = self.TCVR[T].__len__()
        except:
            self.TCVR[T] = {}
        finally:
            nop = -1
        #end try
        # does [T][C] exist n-make one
        try:
            j = self.TCVR[T][C].__len__()
        except:
            self.TCVR[T][C] = {}
        finally:
            nop = -1
        #end try
        # does [T][C][V] exist n-make one
        try:
            j = self.TCVR[T][C][V].__len__()
        except:
            self.TCVR[T][C][V] = {}
        finally:
            nop = -1
        #end try
        # does [T][C][V][R] exist n-make one
        try:
            j = self.TCVR[T][C][V][R].__len__()
        except:
            self.TCVR[T][C][V][R] = 'meta'
        finally:
            nop = -1
        #end try
        #TRCV
        # does [T] exist n-make one
        try:
            j = self.TRCV[T].__len__()
        except:
            self.TRCV[T] = {}
        finally:
            nop = -1
        #end try
        # does [T][R] exist n-make one
        try:
            j = self.TRCV[T][R].__len__()
        except:
            self.TRCV[T][R] = {}
        finally:
            nop = -1
        #end try
        # does [T][R][C] exist n-make one
        try:
            j = self.TRCV[T][R][C].__len__()
        except:
            self.TRCV[T][R][C] = V
        finally:
            nop = -1
        #end try
        # big data VC
        try:
            j = self.VC[V].__len__()
        except:
            self.VC[V] = {}
        finally:
            nop = -1
        # end try
        try:
            j = self.VC[V][C].__len__()
        except:
            self.VC[V][C] = 'meta' 
        finally:
            nop = -1
        # end try
    #end write
    def dumpTCVR(self):
        return(self.TCVR)
    #end dumpTCVR
    def dumpTRCV(self):
        return(self.TRCV)
    #end dumpTRCV
    def search(self,T,C,V,R):
        """ search by pattern """
        cc = 0
        if (T.__len__() != 0):
            cc = cc + 8
        #endif
        if (C.__len__() != 0):
            cc = cc + 4
        #endif
        if (V.__len__() != 0):
            cc = cc + 2
        #endif
        if (R.__len__() != 0):
            cc = cc + 1
        #endif
        # case list T C V R
        #           8 4 2 1
        print('cc='+cc.__str__())
        if (cc==0): # none - [T]
            ans = self.TCVR.keys()
        elif(cc==8): # T -> [C] == structure of T
            ans = self.TCVR[T].keys()
        elif(cc==12): # TC -> [V] == domain of C
            ans = self.TCVR[T][C].keys()
        elif(cc==9): # TR -> [C] == sub structure at R
            ans = self.TRCV[T][R].keys()
        elif(cc==13): #TCR -> V
            ans = self.TRCV[T][R][C]
        elif(cc==14): # TCV -> [R]  == rows of C=V
            ans = self.TCVR[T][C][V].keys()
        else:
            print('Error - returns blank')
            ans = ''
        #endif
        return(ans)
    #end 
    def genx(self):
        self.T.sleep(.1)
    	ans = "X" + self.T.time().__str__()
    	return(ans)
    #end genx
#end class
        
        
