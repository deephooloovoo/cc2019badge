#!/usr/bin/python

from __future__ import print_function
from PIL import Image
import numpy as np
import sys
threshold = 128
DPI = 300
SPACING = .1
PSPACING = int(SPACING * DPI)
FEEDX = 95 #int(.392* PSPACING)
READERY = 221
READERLEN = 1700+READERY #DPI * 11

class Tapereader:
    def __init__(self, im):
        self.im = im
        self.threshhold = 0
    def thresh(self,v):
        return v>self.threshold
    def pxthresh(self,x,y):
        p = self.im.getpixel((x, y))
        return self.thresh(p)
    def findfeed(self):
        fs = [0] * self.im.size[1]
        for y in range(self.im.size[1]):
            fs[y] = self.im.getpixel((FEEDX, y))
        self.threshold = sum(fs)/len(fs) #hope that's good enough
        for y in range(len(fs)):
            fs[y] = self.thresh(fs[y]) +0
        fs=fs
        y = READERY
        x = FEEDX
        feed=[]
        while not self.pxthresh(x,y):
            #TODO: remove this, and tape things to the scanner
            y+=1
            y+=int(.046/2*DPI)
        #assert self.pxthresh(x,y)
        while y < READERLEN:
            #print(feed,x,y)
            hys = y
            hye = y
            while (self.pxthresh(x,hys)): hys-=1
            while (self.pxthresh(x,hye)): hye+=1
            hy = (hys+hye)//2
            hxs = FEEDX
            hxe = FEEDX
            
            while (self.pxthresh(hxs,hy)): hxs-=1
            while (self.pxthresh(hxe,hy)): hxe+=1
            #while (self.thresh(self.im.getpixel((hxe,hy)))): hxe+=1
            hx = (hxs+hxe)//2
            hs = (hxe-hxs)
            feed.append((hx,hy,hs))
            x = hx
            y = hy + PSPACING
            #print(hys,hye,hxs,hxe)
            #print(hs)
            assert (hs > 10)
            assert (hs < 17)
        self.feed = feed
            
        #print(self.feed)
    def readpunches(self):
        tape = []
        for x,y,s in self.feed:
            b = 0
            for a in range(8):
                if a < 3:
                    hx = x - int(SPACING * DPI * (3-a))
                else:
                    hx = x + int(SPACING * DPI * (a-2))
                b|=(self.pxthresh(hx,y)+0)<<a
            print("{:02x}".format(b))
            
            
        
        
def main():
    if len(sys.argv) != 2:
        print("usage: tape.py image")
        exit(0)
    fn = sys.argv[1]
    im = Image.open(fn)
    #print(im.format,im.size,im.mode)
    tr = Tapereader(im)
    tr.findfeed()
    tr.readpunches()

if __name__ == "__main__":
    main()
