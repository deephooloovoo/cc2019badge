Here are the scripts I used during Cyphercon 2019 for badge hacking.
Also included are some example tapes and input files

scantape.py takes a scanned image of a tape and reads the holes. It might work
with non-scanned tapes, but idk

makejob.py takes a user/badge id and outputs job strings for the badge
an example user id file is in hlv

mktape.py takes job strings and turns them into a pdf, which when printed on
transparencies, can be read on the badge like paper tape.

example use:
makejob.py hlv > hlv.tap
mktape.py hlv.tap hlv.pdf

I had to print it three times on the laserjet 5c used at the con to make it
dark enough. The laserjet 4050 at home has alignment/registration issues when
printing multiple sheets per job, but printing a single pdf 3 times onto a
transparency works correctly. I'm not really sure what the difference is.

so far the only special example tape is the party mode tapes, which make the
lights on the badge go crazy.
