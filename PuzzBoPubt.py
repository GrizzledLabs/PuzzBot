#!/usr/bin/python3
# bot.py

import os, discord, random, time, wordladderlist
from word_ladder_solver import get_shortest_route
from fanshim import FanShim

fanshim = FanShim()

def episodepicker():
  """ Picks the episode, intro, and packages them together and returns message """
  episodelist = ['ep.78 James Bond\'s Cousins', \
  'ep.77 ON MY GIRLFRIENDS BIRTHDAY???', \
  'ep.76 How Far Up The Egg Do The Pants Go?', \
  'ep.75 The Night Before Puzzmis w/ J.P. Riddles', \
  'ep.74 Booty Butt', \
  'ep.73 Sharkest Heart', \
  'ep.72 Skull & Boneheads', \
  'ep.71 Kid Friendly Episode (really!)', \
  'ep.70 Hundie Dollie Giveaway Returns! AKA Rap for Daddy!', \
  'ep.69 Dirty Sexy Riddles', \
  'ep.68 The Birds, the Bees, the Nicholas Cages', \
  'ep.67 Bleh Riddle Riddle 2!', \
  'ep.66 On the Ground, In Disguise', \
  'ep.65 Watson Can You Hear Me?', \
  'ep.64 The Purple Episode', \
  'ep.63 A Pun in the Pool', \
  'ep.62 Hey Riddle City Part 2!', \
  'ep.61 Fun at songs', 'ep.60 Floor Soup!', \
  'ep.59 That Sucks! That Rules!', \
  'ep.58 Flirty Chef!', \
  'ep.57 The Question is the Answer! with the teachers lounge', \
  'ep.56 Hey Riddle City! A Pod Noir, Part 1', \
  'ep.55 Just Plain Comedy!', \
  'BONUS - Hey Relationship Relationship!', \
  'ep.54 A Star is Wars! with Jeffrey Cranor', \
  "ep.53 It's Been... ONE YEAR!", \
  'ep.52 Body Magic!', \
  'ep.51 JANETMORPH! with Janet Varney!', \
  'ep.50 Fifty Riddles GUARANTEED!', \
  'ep.49 Carrot Bottom!', \
  'ep.48 Boat Detective with Hayes Davenport!', \
  'ep.47 Pyramid-Life Crisis!' \
  'ep.46 It Came From the Basement!', \
  'ep.45 Lucky Songbird, with Jon Gabrus', \
  "ep.44 Adal's $100 Give Away!", \
  "ep.43 He's Mimble!", \
  'ep.42 Post Potatoes!', \
  'ep.41 Dr. Funny Comedy', \
  'AMA Special!', \
  'ep.40 All Sherlock!', \
  'ep.39 Horse Court with TJ Jagodowski!', \
  'ep.38 The Great Butterbeer Showdown!', \
  'ep.37 Raccoon Penis Bone!', \
  'ep.36 Dear Diary...', \
  'ep.35 JUST Trains & Automobiles', \
  'ep.34 The More You Know!', \
  'ep.33 The One With The Most!', \
  'Patreon Episode 1!', \
  'ep.32 LOST Boyz!', \
  'ep.31 Take a Riddle Bit Off the Top!', \
  'ep.30 Love Arrow Arrow! (AKA Hey Kissy Kissy!)', \
  "ep.29 Dungeon's & Dragons & Riddles with Becca Barish!", \
  'ep.28 Thank you, Snake!', \
  'ep.27 Kiss Kiss, Riddle Riddle', \
  'ep.26 Rip Van Puzzles', \
  'ep.25 Puzzles and Wizzys', \
  "ep.24 New Year's Re:SOLUTIONS! With Zach Reino & Jess McKenna", \
  'ep.23 A Year End Riddle-view', \
  'ep.22 Sleigh Riddle Riddle', \
  'ep.21 Jester Tester with Brooke Breit!',
  'ep.20 School Runnings', \
  'ep.19 A Puzzle a Day Keeps the Riddle Away', \
  'ep.18 Hey Gobble Gobble!', \
  'ep.17 The Episode That Sounds a Riddle Bit Different', \
  'ep.16 Riddle Nation', \
  'ep.15 Bleh Riddle Riddle! a.k.a. RiddleWeen!', \
  'ep.14 A Riddle a Day Saves Nine', \
  'ep.13 Throw another Riddle on the Barbie', \
  'ep.12 Three Men and A Riddle Lady with Justin McElroy', \
  'ep.11 Night of the Living DEAD STOP', \
  'ep.10 Judge, Jury, and Riddlecutioner', \
  'ep.9 Quiz Bop', \
  'ep.8 My Riddle Pony with Arnie Niekamp', \
  'ep.7 Riddle Miss Sunshine', \
  'ep.6 Sheep Impact!', \
  "ep.5 Greased Lightnin' Round", \
  'ep.4 Guilty Beyond a Reasonable Mrs. Doubtfire',
  "ep.3 Everyone's Dead!", \
  'ep.2 My Puzzle Lies Over the Ocean', \
  'ep.1 Stuck in the Riddle with You',]

  intros = ['Erin was adorable in', \
  'PuzzBot suggests', \
  "PuzzBot wants to see a scene. You are", \
  'JPC was mildly appropriate in', \
  "Based on your browsing history, you would like", \
  "Adal dedicated this one to PuzzBot", \
  'Initiating recommendation protocol...', \
  'PuzzBot enjoys', \
  'This one made PuzzBot feel emotion for the first time', \
  'PuzzBot is currently listening to', \
  'PuzzBot serving up a hot plate of', \
  'Phoebe P. Peabody Beebee told PuzzBot she loves', \
  'RiddieKitty told PuzzBot he loves', \
  "JP Riddles said his favorite was popcorn farts, but PuzzBot thinks he meant", \
  'Santa Baby, play', \
  "Smashmouth won't return PuzzBot's calls.", \
  "PuzzBot's favorite episode is"]

  introrandom = random.choice(intros)
  episoderandom = random.choice(episodelist)
  episodesuggestion = ('*bzzzt*... {0} {1}'.format(introrandom, episoderandom))
  return episodesuggestion

# BOOT NOTIFICATION
fanshim.set_light(200, 0, 0) # rgb 255
time.sleep(0.5)
fanshim.set_light(255, 0, 255) # rgb 255
time.sleep(1)
fanshim.set_light(200, 0, 0) # rgb 255
time.sleep(0.5)
fanshim.set_light(0, 0, 0)

# IDENTIFIERS
myid = 'MY ID REMOVED'
token = 'TOKEN REMOVED'
client = discord.Client()

# CONNECT MESSAGE
@client.event
async def on_ready():
    print('{0} has connected to Discord!'.format(client.user))

# ROLE SETTER - Sets new discorders to the Patrons role
@client.event
async def on_member_join(member):
    fanshim.set_light(255, 255, 255) # rgb 255
    print('test')
    role = discord.utils.get(member.guild.roles, name='Patrons')
    await member.add_roles(role)
    time.sleep(0.5)
    fanshim.set_light(0, 0, 0) # rgb 255

# MESSAGE MONITOR AND RESPONDER
@client.event
async def on_message(message):
  # PUZZBOT - episode picker and 69 420 jokes
    if '🤖' in message.content.lower() or 'puzzbot' in message.content.lower():
        if message.author != client.user:
            fanshim.set_light(255, 0, 255) # rgb 255
            time.sleep(0.5)
            await message.channel.send(episodepicker())
    if '69' in message.content:
        chance = random.randint(1,5)
        if chance == 5:
          fanshim.set_light(255, 0, 255) # rgb 255
          time.sleep(1)
          await message.channel.send('Nice...')
    if '420' in message.content:
        chance = random.randint(1,5)
        if chance == 5:
            fanshim.set_light(255, 0, 255) # rgb 255
            time.sleep(1)
            await message.channel.send('Blaze it')

    # CHARACTERS - they have a 1/3 chance of running to avoid spamming.
    if 'phoebe' in message.content.lower():
        chance = random.randint(1,3)
        if chance == 3:
            fanshim.set_light(255, 0, 255) # rgb 255
            time.sleep(0.5)
            await message.channel.send(':woman_raising_hand: Pheobe B. Peabody Beebee')
    if 'riddie kitty' in message.content.lower():
        chance = random.randint(1,3)
        if chance == 3:
            fanshim.set_light(255, 0, 255) # rgb 255
            time.sleep(0.5)
            await message.channel.send(':smiley_cat: :closed_umbrella: :briefcase:')
    if 'canoe dog' in message.content.lower():
        chance = random.randint(1,3)
        if chance == 3:
            fanshim.set_light(255, 0, 255) # rgb 255
            time.sleep(0.5)
            await message.channel.send(':canoe: :dog: :knife:')
    if 'jp riddles' in message.content.lower():
        chance = random.randint(1,3)
        if chance == 3:
            fanshim.set_light(255, 0, 255) # rgb 255
            time.sleep(0.5)
            await message.channel.send(':older_man: :fork_and_knife:  :right_facing_fist: :chipmunk: :man_frowning: :woman_facepalming:')
    if 'twins' in message.content.lower():
        chance = random.randint(1,3)
        if chance == 3:
            fanshim.set_light(255, 0, 255) # rgb 255
            time.sleep(0.5)
            await message.channel.send(':couple: TWWWIIIIIIIINNNS')

    # SONG JOKES
    if message.content.lower() == 'some':
        fanshim.set_light(255, 0, 255) # rgb 255
        time.sleep(0.5)
        await message.channel.send('...BODY ONCE TOLD ME!')
    if message.content.lower() == 'it\'s been':
        fanshim.set_light(255, 0, 255) # rgb 255
        time.sleep(0.5)
        await message.channel.send('ONE WEEK SINCE YOU LOOKED AT ME')
        time.sleep(3)
        await message.channel.send('COCKED YOUR HEAD TO THE SIDE AND SAID I\'M ANGRY')

  # TED - Accuses user of always "doing this!"
    if 'ted kennedy killed that girl' in message.content.lower():
        if message.author != client.user:
            fanshim.set_light(255, 0, 255) # rgb 255
            time.sleep(0.5)
            text = str(message.author).upper()
            dspot = text.find('#')
            username = text[:dspot]
            await message.channel.send(f'{username}, YOU ALWAYS DO THIS!')

  # GAMES - Word ladders and dice rolling
    if 'solve word ladder' in message.content.lower():
        if message.author != client.user:
            word1, word2 = message.content.lower().split()[-2:]
            if len(word1) == len(word2) == 4:
                if word1 not in wordladderlist.words:
                    response = f'Word "{word1}" does not compute'
                elif word2 not in wordladderlist.words:
                    response = f'Word "{word2}" does not compute'
                else:
                    response = "PuzzBot has solved this!\n||"
                    response += join(' ').get_shortest_route(word1, word2)
                    response += "||"
            else:
                response = 'Words must be 4 letters long!'
            fanshim.set_light(255, 0, 255) # rgb 255
            await message.channel.send(response)
    elif 'word ladder' in message.content.lower():
        if message.author != client.user:
            fanshim.set_light(255, 0, 255) # rgb 255
            word1 = random.choice(wordladderlist.words)
            word2 = random.choice(wordladderlist.words)
            await message.channel.send(f'Change **{word1.upper()}** into **{word2.upper()}** by changing one letter at a time.')
    if 'roll me' in message.content.lower():
        fanshim.set_light(255, 0, 255) # rgb 255c
        time.sleep(0.5)
        text = message.content.lower()
        text = text.split()
        if text[0] == 'roll' and text[1] == 'me':
            try:
                dspot = text[2].find('d')
                dienum = text[2][0:dspot]
                diesides = text[2][dspot+1:]
                numcheck1 = dienum.isdigit()
                numcheck2 = diesides.isdigit()
                if numcheck1 == False or numcheck2 == False:
                    refusal = message.content.lower().replace("roll me", '').upper()
                    await message.channel.send(f'SURELY YOU CANNOT EXPECT PUZZBOT TO ROLL **{refusal}**.')
                elif int(dienum) > 5000:
                    time.sleep(0.5)
                    await message.channel.send(f'PUZZBOT REFUSES TO ROLL {dienum} DICE')
                else:
                    roll = 0
                    for i in range(int(dienum)):
                        roll += random.randint(1, int(diesides))
                    await message.channel.send(f'PUZZBOT ROLLED **{roll}**')
            except Exception as e:
                await message.channel.send(f'PUZZBOT WON\'T FALL FOR THAT. NOT AGAIN...')

  # UTILITIES - message purging
    if 'purge' in message.content[0:5]:
        if message.guild.id != 631209898461626406:
            fanshim.set_light(255, 0, 255) # rgb 255
            print(message.author)
            if str(message.author) in ('HeyThatsTim#8784', 'messgirl#4970', 'Adal#2145','jpsofly#6646', 'Erinkeif#2977', 'Aidan#2567', 'Lazar#8675', 'alunardragon#6969', 'capnsoapy#4719', 'Slackferno#3769', 'lizard#2286'):
                try:
                    amt = message.content[5:]
                    amt = int(amt)
                    await message.channel.send(f'Deleting {amt} messages...')
                    amt2 = amt + 2
                    print(f'{amt2} messages to be deleted instead of {amt}')
                    time.sleep(2)
                    await message.channel.purge(limit=amt2)
                except Exception as e:
                    await message.channel.send(f'@HeyThatsTim ERROR: {e}')
                    print(e)
    if 'bothelp' in message.content.lower():
        await message.channel.send(f'CHECK YOUR MESSAGES FOR MY COMMAND LIST')
        await message.author.send("COMMAND LIST\n\n🤖 **or PuzzBot**\nPuzzBot will send you a recommendation.\n\n**Name various characters**\nThis is currently set to a 33% to respond to avoid spamming the chat. Puzzie will describe the character.\n\n**Some/It's Been**\nPuzzBot will finish the lyrics.\n\n**Word Ladder**\nPuzzBot will give you two four letters words. Play the game by changing one word into the other by old chaning one letter at a time. Ex. TOOL to MALL, TOOL TOLL TALL MALL. Please use this in the wordladders channel.\n\n**Solve Word Ladder <word1> <word2>\n Puzzbot will solve your word ladder (only 4-letter words)\n\n**Roll Me...**\nHave PuzzBot roll for you. Ex. roll me 4d6.\n\n**Ted Kennedy Killed That Girl**\nPuzzBot will yell at you.\n\n**Purge**\nOnly mods and developer can use this command.\nEx. \"purge5\" will delete the last 5 messages in a channel.")

    # LED OFF
    fanshim.set_light(0, 0, 0) # rgb 255

client.run(token)
