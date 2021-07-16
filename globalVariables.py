import discord

intents = discord.Intents().default()
intents.members = True

client = discord.Client(intents= intents)

prefix = "eli"

unverifiedRole = {
    811369107181666343 : 811453152061685760
}

verifyChannel = {
    811369107181666343 : 811492489230942259,
    830752554148954123 : None
}

ageRoleList = { 
    811369107181666343 : [
        811443057018142740,
        811451993645908068,
        811452000624967692,
        811452006971211797,
        811452013585891342,
        811452018387451914
    ]
}

pronounRoleList = { 
    811369107181666343 : [
        811443833832734750,
        811443883304419328,
        811443152857989120,
        811443911582548018
    ]
}

tooOldRole = { 
    811369107181666343 : 811452704617922590
}

verifiedRole = {
    811369107181666343 : 811442483115720706
}

logChannel = {
    811369107181666343 : 811498382211284992
}

roleChannel = {
    811369107181666343 : 811396496774922240
}

welcomeChannel = {
    811369107181666343 : 811386285876445184
}