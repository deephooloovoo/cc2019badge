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
SHEET_H =6.5
STRIPL =SHEET_H
TAPEW = .98


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
def drawstrip(ctx,t,col):
    #ctx.rectangle(0,0,MARGINX,MARGINY)
    d,txt = t
    ctx.set_source_rgb(0,0,0)
    #ctx.set_source_rgb(0,0,0)
    #ctx.fill()
    #for s in range(1):
    s = col
    print(s)
        
    ctx.rectangle((s%8) * TAPEW+MARGINX, 0+MARGINY, TAPEW,SHEET_H)
    ctx.set_source_rgb(0,0,0)
    #ctx.set_source_rgb(0,0,0)
    ctx.fill()
    ctx.rectangle((s%8) * TAPEW+MARGINX, 0+MARGINY, TAPEW,SHEET_H)
    ctx.set_source_rgb(1,1,1)
    ctx.set_line_width(.005)
    ctx.stroke()
    for n in range(len(d)):
        drawbyte(ctx,d,n,s%8)
    ctx.set_source_rgb(0,0,0)
    ctx.move_to(TAPEW*(s%8+.5)-.1+MARGINX,STRIPL+MARGINY+.1)
    ctx.set_font_size(.10)
    ctx.save()
    ctx.rotate(3.14/2)
    ctx.show_text("{:02d}     ".format(s)+txt)
    ctx.restore()
        
def drawbyte(ctx,d, n, strip):
    #print(n,strip)
    py = SPACING*n+OVERLAP +MARGINY
    #-(STRIPL - OVERLAP) * strip + MARGINY
    for a in range(8):
        px = HOLE0X + SPACING*(a +(a>=3)) + strip*TAPEW + MARGINX
        if (ord(d[n])>>a)&1:
            if(onsheet(px,py)):
                drawhole(ctx,px,py,DHOLER)
    px = HOLE0X + SPACING*(3)+strip*TAPEW + MARGINX
    if(onsheet(px,py)):
        drawhole(ctx,px,py,FHOLER)
def maketape(d,fn):
    surf = cairo.PDFSurface(fn,72*8.5,72*11)
    # PS worked better on the laserjet 5 that was used at the con, but PDF works better on my home printer
    # surf = cairo.PSSurface(fn,72*8.5,72*11)
    ctx = cairo.Context(surf)
    ctx.scale(72,72) # work in inches, because that's how tape specs are
    ctx.select_font_face("mono")
    for q in range(len(d)):
        if (q and (q%8) == 0):
            ctx.show_page()
        drawstrip(ctx,d[q],q)
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
            a = "\x00" * 2 + l.strip() + "\x00" * 2
            f = "".join(fixparity(b) for b in a)
            o.append((f,l.strip()))
           

        maketape(o,ofn)
if __name__ == '__main__':
    main()
