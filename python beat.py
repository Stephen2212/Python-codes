"""
This program will play a sound beat 
"""


import winsound

for x in range(3):
    winsound.PlaySound("BOOGEZ_B" , winsound.SND_FILENAME)
    winsound.PlaySound("BOOGEZ_B" , winsound.SND_FILENAME)
    winsound.PlaySound("BOOGEZ_B" , winsound.SND_FILENAME)
    winsound.PlaySound("GTR_DRUM" , winsound.SND_FILENAME)
    winsound.PlaySound("GTR_DRUM" , winsound.SND_FILENAME)
    winsound.PlaySound("CRISP_SN" , winsound.SND_FILENAME)
    
winsound.PlaySound("Clap396" , winsound.SND_FILENAME)
winsound.PlaySound("Clap396" , winsound.SND_FILENAME)


"""
Outcome: A sound beat will play
"""