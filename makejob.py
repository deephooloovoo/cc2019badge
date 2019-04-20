#!/usr/bin/python
import sys
HEAD="0102"
END="0319"
        
def openuser(userfn):
    lines=[]
    with open(userfn) as f:
        l = f.readlines()
        for a in l:
            lines.append(a.strip())
    if len(lines[0])<13:
        lines[0] += (13-len(lines[0]))*" "
        
    return (lines[0], lines[1])

def openbody(userfn):
    lines=[]
    with open(userfn) as f:
        l = f.readlines()
        for a in l:
            sline = a.strip().split(" ")
            gid = int(sline[1],16)
            gid = "{:02x}".format(gid)
            
            lines.append((sline[0],gid))
    return lines
        

def makeflag(uid,bn,gid, body ):
    assert len(body) == 18
    return "0102"+gid+bn+uid+body+"0319"
        


def main():
    lines =[]
    uf = sys.argv[1]
    bf = sys.argv[2]
    u,bid = openuser(uf)
    bodies = openbody(bf)
    for b,gid in bodies:
        f = makeflag(u,bid,gid,b)
        print(f)
    
if __name__=="__main__":
    main()
