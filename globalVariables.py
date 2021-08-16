import discord

intents = discord.Intents().default()
intents.members = True

client = discord.Client(intents= intents)

prefix = "eli"

unverifiedRole = {
    811369107181666343 : 811453152061685760,
    830752554148954123 : None,
    866160840037236736 : None
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
    811369107181666343 : 811386285876445184,
    866160840037236736 : 866160840037236739
}

numberEmoteList = [
            "<:gh_1:856557384071512065>",
            "<:gh_2:856557978383155200>",
            "<:gh_3:856557993030189096>",
            "<:gh_4:856558007352950795>",
            "<:gh_5:856558030836990002>",
            "<:gh_6:856558055138394169>",
            "<:gh_7:856558070069723146>",
            "<:gh_8:856558533814124544>",
            "<:gh_9:856558551547510794>",
            "<:gh_10:856558568986771466>"
        ]

joinChannel = {
    811369107181666343 : 811386285876445184,
    764385563289452545 : 764385563813871618,
    866160840037236736 : 866160840037236739
    }

botRole = {
   811369107181666343 : 811452026150977576,
   866160840037236736 : None
}

loadedInventories = {}

bumpChannel = {
    811369107181666343 : 812166022073024552
}