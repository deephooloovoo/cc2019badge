#!/usr/bin/python
import sys
HEAD="0102"
END="0319"
bodies = [
    #"ADD1EACCE55EDA5C11",
    "5afe11fe512e501ace".upper(),
    "C0DED15C105ED10CA1",
    "A11CEDD05EDB0BC01D"
    ]
        
def openuser(userfn):
    lines=[]
    with open(userfn) as f:
        l = f.readlines()
        for a in l:
            lines.append(a.strip())
    if len(lines[0])<13:
        lines[2] += (13-len(lines[2]))*" "
        
    return (lines[0], lines[1], lines[2])
        

def makeflag(uid,bn,auid, body ):
    assert len(body) == 18
    return "0102"+uid+bn+auid+body+"0319"
        


def main():
    lines =[]
    uf = sys.argv[1]
    u,bid,a = openuser(uf)
    for b in bodies:
        f = makeflag(u,bid,a,b)
        print(f)
    
if __name__=="__main__":
    main()
