Here are the scripts I used during Cyphercon 2019 for badge hacking.

scantape.py takes a scanned image of a tape and reads the holes. It might work
with non-scanned tapes, but idk

makejob.py takes a user/badge id and outputs job strings for the badge

mktape.py takes job strings and turns them into a pdf, which when printed on
transparencies, can be read on the badge like paper tape.

I had to print it three times on the laserjet 5c used at the con to make it
dark enough. The laserjet 4050 at home has alignment/registration issues, so 
I couldn't test all of the example tapes.

example use:
makejob.py hlv > hlv.tap
mktape.py hlv.tap hlv.pdf
