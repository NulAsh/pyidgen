import zlib
import random

maxmalefam = 6497311
maxfemfam = 6911258
maxmalename = 8632824
maxfemname = 8496163
maxmaleotc = 8561810
maxfemotc = 8492512
adr2 = (
(0x000000, 0x0340C),
(0x00340C, 0x21055),
(0x024461, 0x09048),
(0x02D4A9, 0x01C80),
(0x02F129, 0x06D65),
(0x035E8E, 0x00251),
(0x0360DF, 0x042D9),
(0x03A3B8, 0x00904),
(0x03ACBC, 0x033AC),
(0x03E068, 0x06B28),
(0x044B90, 0x06AC7),
(0x04B657, 0x0589E),
(0x050EF5, 0x05C03),
(0x056AF8, 0x0767A),
(0x05E172, 0x0313C),
(0x0612AE, 0x12DD9),
(0x074087, 0x02FF1),
(0x077078, 0x0F444),
(0x0864BC, 0x04429),
(0x08A8E5, 0x049EA),
(0x08F2CF, 0x09ED8),
(0x0991A7, 0x12B73),
(0x0ABD1A, 0x1EF50),
(0x0CAC6A, 0x15439),
(0x0E00A3, 0x0DC4F),
(0x0EDCF2, 0x0F984),
(0x0FD676, 0x0873F),
(0x105DB5, 0x06F2C),
(0x10CCE1, 0x06A1B),
(0x1136FC, 0x09299),
(0x11C995, 0x0AC72),
(0x127607, 0x0FCDB),
(0x1372E2, 0x0CDBB),
(0x14409D, 0x14A4A),
(0x158AE7, 0x10D43),
(0x16982A, 0x1A4A3),
(0x183CCD, 0x0E843),
(0x192510, 0x11E64),
(0x1A4374, 0x078A9),
(0x1ABC1D, 0x06687),
(0x1B22A4, 0x01D28),
(0x1B3FCC, 0x1795F),
(0x1CB92B, 0x15E66),
(0x1E1791, 0x0A20E),
(0x1EB99F, 0x024CB),
(0x1EDE6A, 0x08C8B),
(0x1F6AF5, 0x093D9),
(0x1FFECE, 0x08344),
(0x208212, 0x01947),
(0x209B59, 0x2601D),
(0x22FB76, 0x024A9),
(0x23201F, 0x1EF58),
(0x250F77, 0x0C52A),
(0x25D4A1, 0x100E8),
(0x26D589, 0x11403),
(0x27E98C, 0x1111D),
(0x28FAA9, 0x07CDD),
(0x297786, 0x0BEE3),
(0x2A3669, 0x150D2),
(0x2B873B, 0x0EF67),
(0x2C76A2, 0x27207),
(0x2EE8A9, 0x0A1E6),
(0x2F8A8F, 0x0BA08),
(0x304497, 0x16AE7),
(0x31AF7E, 0x04559),
(0x31F4D7, 0x188EC),
(0x337DC3, 0x079DA),
(0x33F79D, 0x0B506),
(0x34ACA3, 0x18494),
(0x363137, 0x08178),
(0x36B2AF, 0x0E435),
(0x3796E4, 0x0BAD6),
(0x3851BA, 0x0A541),
(0x38F6FB, 0x1A940),
(0x3AA03B, 0x0A6C7),
(0x3B4702, 0x0F4FF),
(0x3C3C01, 0x10216),
(0x3D3E17, 0x0AAC9),
(0x3DE8E0, 0x020A7),
(0x3E0987, 0x001B0),
(0x3E0B37, 0x01ECD),
(0x3E2A04, 0x00650),
(0x3E3054, 0x003B1),
(0x3E3405, 0x00495),
(0x3E389A, 0x01A4D),
(0x3E52E7, 0x0438C),
(0x3E9673, 0x0100E),
(0x3EA681, 0x0013C),
(0x3EA7BD, 0x024DB),
(0x3ECC98, 0x0028C))

sr = random.SystemRandom()
sex = sr.randrange(2)
if sex:
    d = zlib.decompress(open('malefam.bin','rb').read()).split(b'\x0a')
    fid = sr.randrange(maxmalefam)
else:
    d = zlib.decompress(open('femfam.bin','rb').read()).split(b'\x0a')
    fid = sr.randrange(maxfemfam)
id_sum = 0
for line in d:
    id_sum += int(line[:line.find(b';')])
    if id_sum>fid:
        s = line.decode('cp866')
        break
Fam = s[s.find(';')+1:].title()
if sex:
    d = zlib.decompress(open('malename.bin','rb').read()).split(b'\x0a')
    fid = sr.randrange(maxmalename)
else:
    d = zlib.decompress(open('femname.bin','rb').read()).split(b'\x0a')
    fid = sr.randrange(maxfemname)
id_sum = 0
for line in d:
    id_sum += int(line[:line.find(b';')])
    if id_sum>fid:
        s = line.decode('cp866')
        break
Name = s[s.find(';')+1:].title()
if sex:
    d = zlib.decompress(open('maleotc.bin','rb').read()).split(b'\x0a')
    fid = sr.randrange(maxmaleotc)
else:
    d = zlib.decompress(open('femotc.bin','rb').read()).split(b'\x0a')
    fid = sr.randrange(maxfemotc)
id_sum = 0
for line in d:
    id_sum += int(line[:line.find(b';')])
    if id_sum>fid:
        s = line.decode('cp866')
        break
Otc = s[s.find(';')+1:].title()
print(Fam, Name, Otc)
d = zlib.decompress(open('adr1.bin','rb').read()).split(b'\x0a')
fid = sr.randrange(142369610)
id_sum = 0
i = 0
for line in d:
    id_sum += int(line[:line.find(b';')])
    if id_sum>fid:
        s = line.decode('cp866')
        break
    else:
        i += 1
FullAdr = s[s.find(';')+1:]
f = open('adr2.bin','rb')
f.seek(adr2[i][0])
d = zlib.decompress(f.read(adr2[i][1])).split(b'\x0a')
f.close()
i = 0
while True:
    numread = int(d[i])
    i += 1
    sl = []
    sumi = 0
    for j in range(numread):
        s = d[i]
        sumi += int(s[:s.find(b';')])
        sl.append(s)
        i += 1
    iid = sr.randrange(sumi)
    sumi = 0
    for line in sl:
        sumi += int(line[:line.find(b';')])
        if sumi>iid:
            s = line.split(b';')
            break
    FullAdr += ' -> '+s[3].decode('cp866')
    if s[1]:
        Index = s[1].decode('cp866')
    if not s[2]:
        break
    while d[i] != s[2]:
        i += 1
    i += 1
print(Index)
print(FullAdr)
