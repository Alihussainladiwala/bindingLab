print("Hello")
import hashlib
import time
from joblib import Parallel, delayed



#md5 = hashlib.md5()
#sha1 = hashlib.sha1()


def sha1(filename, hashN):
    h  = hashlib.sha1()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    
    if h.hexdigest() != hashN:
        print(False)

def checkSignatures():
    
    f = open("testdata/logs/sha1sum.txt", "r")
    
    arr = parseSigFile(f)
    
    results = Parallel(n_jobs=4)(delayed(sha1)("testdata/logs/"+name.strip(), hashN) for hashN, name in arr)
    
    
    
    
    
    
    #for hashN, name in arr:
        
        #with open(, 'rb') as f:
        #    while True:
        #        data = f.read(BUF_SIZE)
        #        if not data:
        #            break
                
        #        print("iter")   
                #md5.update(data)
        #        sha1.update(data)
        
                
        #print("MD5: {0}".format(md5.hexdigest()))
        #print(sha1.hexdigest(), hashN, name)
     #   if hashN == sha1("testdata/logs/"+name.strip()):
     #       pass
     #   else:
     #       print(False)            
        



def parseSigFile(f):
    
    
    lines = f.readlines()
    res = []
    for l in lines:
        arr = l.split(" ")
        
        res.append([arr[0], arr[-1]]) 
        
    return res   
    
    
ts = time.time()

checkSignatures()

et = time.time()

print(et - ts)
    
   
    
    
    
    

        
