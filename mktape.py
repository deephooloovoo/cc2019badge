#!/usr/bin/python2
import cairo
import sys
import math
DHOLER = .072/2
FHOLER = .046/2
HOLE0X = .392 - .3
MARGINX=.25
MARGINY=.25
SPACING= .1
OVERLAP= 1
SHEET_W =8
SHEET_H =10.5
STRIPL =SHEET_H


def onsheet(px,py):
    if px >= 0 and py >= 0 and px<SHEET_W and py<SHEET_H:
        return True
    return True
    return False
def drawhole(ctx,x,y,r):
    #ctx.move_to(x,y)
    ctx.new_sub_path()
    ctx.set_source_rgb(1,1,1)
    print x,y,r
    ctx.arc(x,y,r,0.0,2*math.pi)
    ctx.close_path()
    ctx.fill()
def drawstrip(ctx,d,col):
    #ctx.rectangle(0,0,MARGINX,MARGINY)
    ctx.set_source_rgb(0,0,0)
    #ctx.set_source_rgb(0,0,0)
    #ctx.fill()
    #for s in range(1):
    s = col
    print(s)
    if 1:
        
        ctx.rectangle(s * 1.0+MARGINX, 0+MARGINY, 1.0,SHEET_H)
        ctx.set_source_rgb(0,0,0)
        #ctx.set_source_rgb(0,0,0)
        ctx.fill()
        ctx.rectangle(s * 1.0+MARGINX, 0+MARGINY, 1.0,SHEET_H)
        ctx.set_source_rgb(1,1,1)
        ctx.set_line_width(.005)
        ctx.stroke()
        for n in range(len(d)):
            drawbyte(ctx,d,n,s)
        
def drawbyte(ctx,d, n, strip):
    #print(n,strip)
    py = SPACING*n+OVERLAP +MARGINY
    #-(STRIPL - OVERLAP) * strip + MARGINY
    for a in range(8):
        px = HOLE0X + SPACING*(a +(a>=3)) + strip + MARGINX
        if (ord(d[n])>>a)&1:
            if(onsheet(px,py)):
                drawhole(ctx,px,py,DHOLER)
    px = HOLE0X + SPACING*(3)+strip + MARGINX
    if(onsheet(px,py)):
        drawhole(ctx,px,py,FHOLER)
def maketape(d,fn):
    surf = cairo.PDFSurface(fn,72*8.5,72*11)
    # PS worked better on the laserjet 5 that was used at the con, but PDF works better on my home printer
    # surf = cairo.PSSurface(fn,72*8.5,72*11)
    ctx = cairo.Context(surf)
    ctx.scale(72,72) # work in inches, because that's how tape specs are
    for q in range(len(d)):
        a = "\x00" * 5 + d[q].strip() + "\x0d\x0a" + "\x00" * 5
        drawstrip(ctx,a,q)
def parity(a):
    p=0
    for b in range(7):
        if (a>>b)&1:
            p+=1
    return (p & 1)<<7
def fixparity(a):
    c = ord(a)
    p = parity(c)
    return chr((c & 0x7f) | p)
def main():
    fn = sys.argv[1]
    ofn = sys.argv[2]
    with open(fn,"rb") as f:
        d = f.readlines()
        o = []
        for l in d:
            f = "".join(fixparity(a) for a in l)
            o.append(f)
           

        maketape(o,ofn)
if __name__ == '__main__':
    main()
