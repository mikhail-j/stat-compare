#!/usr/bin/python
#coding=utf-8
#Qijia (Michael) Jin
#Python Pokemon Project

import cgi
form = cgi.FieldStorage()
print "Content-type: text/html; charset=utf-8\n\n"
b0 = open("data.txt","r")
b1 = b0.read()
b0.close()
b0 = b1.split("\n")
b1 = None
i = 0
ln = len(b0)
while (i < ln):
    b0[i] = b0[i].split(",")
    i += 1
b1 = b0.pop(0)[1:9]
item0 = form.getvalue('stats')
item1 = form.getvalue('stats1')
def acrn(it):
    if (it == None):
        print "null"
        return
    else:
        i = int(it)
        return b0[i - 1][1:(len(b0[i]) - 1)]

def btdh(br,bx):#base stats
    s = '<tr><th colspan="2" class="default">' + br[0] + " Base Stats</th></tr>"
    i = 1
    ln = len(br)
    while (i < ln):
        if (i % 2 == 0):
            s += '<tr><th class="stat">' + str(bx[i]) + '</td><td>' + str(br[i]) + "</td></tr>"
        else:
            s += '<tr><th class="stata">' + str(bx[i]) + '</td><td class="alt">' + str(br[i]) + "</td></tr>"
        i += 1
    return s

def mtdh(br,bx):#max stat table code
    s = '<tr><th colspan="2" class="default">' + br[0] + " Theoretical Maximum Stats</th></tr>"
    i = 1
    ln = len(br)
    while (i < ln):
        if (i % 2 == 0):
            s += '<tr><th class="stat">' + str(bx[i]) + '</td><td>' + str(br[i]) + "</td></tr>"
        else:
            s += '<tr><th class="stata">' + str(bx[i]) + '</td><td class="alt">' + str(br[i]) + "</td></tr>"
        i += 1
    return s

def maxstt(bx):#max stats
    b = bx[:]
    b[1] = int(b[1]) * 2 + 31 + (252/4) + 100 + 10
    i = 2
    ln = len(b)
    while (i < ln):
        b[i] = int((int(b[i]) * 2 + 31 + float(252/4) + 5) * 1.1)
        i += 1
    return b

def pic(it,n):#image sprite exception handler
    s = '<div class="sprites" style="display: inline-block;"><img src="../images/pkmn_ico/'
    if (it[0] == "Deoxys-(Attack_Forme)"):
        s += "386_a.gif"
    elif (it[0] == "Deoxys-(Defense_Forme)"):
        s += "386_d.gif"
    elif (it[0] == "Deoxys-(Speed_Forme)"):
        s += "386_s.gif"
    elif (it[0] == "Wormadam-(Sandy_Cloak)"):
        s += "413_s.gif"
    elif (it[0] == "Wormadam-(Trash_Cloak)"):
        s += "413_g.gif"
    elif (it[0] == "Rotom-(Heat_Rotom)"):
        s += "479_h.gif"
    elif (it[0] == "Rotom-(Wash_Rotom)"):
        s += "479_w.gif"
    elif (it[0] == "Rotom-(Frost_Rotom)"):
        s += "479_f.gif"
    elif (it[0] == "Rotom-(Fan_Rotom)"):
        s += "479_s.gif"
    elif (it[0] == "Rotom-(Mow_Rotom)"):
        s += "479_c.gif"
    elif (it[0] == "Giratina-(Origin_Forme)"):
        s += "487_o.gif"
    elif (it[0] == "Shaymin-(Sky_Forme)"):
        s += "492_s.gif"
    elif (it[0] == "Darmanitan-(Zen_Mode)"):
        s += "555-d.gif"
    elif (it[0] == "Tornadus-(Therian_Forme)"):
        s += "641-t.gif"
    elif (it[0] == "Thundurus-(Therian_Forme)"):
        s += "642-t.gif"
    elif (it[0] == "Landorus-(Therian_Forme)"):
        s += "645-t.gif"
    elif (it[0] == "Kyurem-(Black_Kyurem)"):
        s += "646-b.gif"
    elif (it[0] == "Kyurem-(White_Kyurem)"):
        s += "646-w.gif"
    elif (it[0] == "Meloetta-(Pirouette_Forme)"):
        s += "648_s.gif"
    else:
        s += str(b0[(int(n) - 1)][0]) + ".gif"
    s += '"></div>'
    return s

def analysis(bx, by):
    s = ""
    if (bx[1] > by[1]):
        s += bx[0] + " (" + str(bx[1]) + " HP) has better HP than " + by[0] + " (" + str(by[1]) + " HP). "
    elif (bx[1] == by[1]):
        s += bx[0] + " (" + str(bx[1]) + " HP) ties " + by[0] + " (" + str(by[1]) + " HP) in HP. "
    else:
        s += by[0] + " (" + str(by[1]) + " HP) has better HP than " + bx[0] + " (" + str(bx[1]) + " HP). "
    if (bx[2] > by[2]):
        s += bx[0] + " (" + str(bx[2]) + " Atk) has better attack than " + by[0] + " (" + str(by[2]) + " Atk). "
    elif (bx[2] == by[2]):
        s += bx[0] + " (" + str(bx[2]) + " Atk) ties " + by[0] + " (" + str(by[2]) + " HP) in attack stats. "
    else:
        s += by[0] + " (" + str(by[2]) + " Atk) has better attack than " + bx[0] + " (" + str(bx[2]) + " Atk). "
    if (bx[3] > by[3]):
        s += bx[0] + " (" + str(bx[3]) + " Def) has better defense than " + by[0] + " (" + str(by[3]) + " Def). "
    elif (bx[3] == by[3]):
        s += bx[0] + " (" + str(bx[3]) + " Def) ties " + by[0] + " (" + str(by[3]) + " Def) in defense stats. "
    else:
        s += by[0] + " (" + str(by[3]) + " Def) has better defense than " + bx[0] + " (" + str(bx[3]) + " Def). "
    if (bx[4] > by[4]):
        s += bx[0] + " (" + str(bx[4]) + " Sp.Atk) has better special attack than " + by[0] + " (" + str(by[4]) + " Sp.Atk). "
    elif (bx[4] == by[4]):
        s += bx[0] + " (" + str(bx[4]) + " Sp.Atk) ties " + by[0] + " (" + str(by[4]) + " Sp.Atk) in special attack stats. "
    else:
        s += by[0] + " (" + str(by[4]) + " Sp.Atk) has better special attack than " + bx[0] + " (" + str(bx[4]) + " Sp.Atk). "
    if (bx[1] > by[1]):
        s += bx[0] + " (" + str(bx[5]) + " Sp.Def) has better special defense than " + by[0] + " (" + str(by[5]) + " Sp.Def). "
    elif (bx[1] == by[1]):
        s += bx[0] + " (" + str(bx[5]) + " Sp.Def) ties " + by[0] + " (" + str(by[5]) + " Sp.Def) in special defense stats. "
    else:
        s += by[0] + " (" + str(by[5]) + " Sp.Def) has better special defense than " + bx[0] + " (" + str(bx[5]) + " Sp.Def). "
    if (bx[6] > by[6]):
        s += bx[0] + " (" + str(bx[6]) + " Spd) is faster than " + by[0] + " (" + str(by[6]) + " Spd). "
    elif (bx[6] == by[6]):
        s += bx[0] + " (" + str(bx[6]) + " Spd) ties " + by[0] + " (" + str(by[6]) + " Spd) in speed stats. "
    else:
        s += by[0] + " (" + str(by[6]) + " Spd) is faster than " + bx[0] + " (" + str(bx[6]) + " Spd). "
    return s

b2 = acrn(item0)
b3 = acrn(item1)
b4 = btdh(b2,b1)
b5 = btdh(b3,b1)
b6 = maxstt(b2)
b7 = maxstt(b3)
b8 = mtdh(b6,b1)
b9 = mtdh(b7,b1)
b10 = pic(b2, item0)
b10 += pic(b3, item1)
b11 = analysis(b6,b7)

print '<html><head><title>Pokémon Stats</title><link rel="stylesheet" type="text/css" href="../css/styles.css"></head>'
print "<body>"
print '<br><center>Base Stats<br><div>' + b10 + '</div><table id="pkmn0" style="display: inline-block;">'
print b4 + '</table><table id="pkmn1" style="display: inline-block;">' + b5
print '</table><br><hr>Theoretical Maximum Stats (with <i>beneficial nature</i>)<br><table id="pkmn0" style="display: inline-block;">'
print b8 + '</table><table id="pkmn1" style="display: inline-block;">' + b9
print '</table><br><hr>Analysis<p style="font-size: medium; width: 75%;">' + b11 + '</p></center></body></html>'