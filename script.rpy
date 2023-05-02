# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define J = Character("Jaimie")
define C = Character("Captain")
define N = Character("???")
define M = Character ("Morven")
define G = Character ("Gregor")
define CG = Character ("Craig")
image Craig = im.Scale("craig.png" , 650, 890)
image Craigfa = im.Scale("craigfakelaugh.png" , 650, 890)
image Craigdi = im.Scale("craigdissaporving.png" , 650, 890)
image Craigsh = im.Scale("craigshocked.png" , 650, 890)

image Jaime =im.Scale ("Jaimie.png" , 650, 900, yalign = 1.0)
image Jaimie = im.Scale ("JaimieB.png" , 650, 900, yalign = 1.0)

image Jaimech = im.Scale ("Jaimiechuckle.png" , 650, 900, yalign = 1.0)
image Jaimeth = im.Scale ("Jaimiethinking.png" , 650, 900, yalign = 1.0)
image Jaimesh = im.Scale ("Jaimieshocked.png" , 650, 900, yalign = 1.0)
image Jaimefr = im.Scale ("Jaimieangry.png" , 650, 900, yalign = 1.0)
image Jaimela = im.Scale ("Jaimielaugh.png" , 650, 900, yalign = 1.0)
image Jaimede = im.Scale ("Jaimiedefeated.png" , 650, 900, yalign = 1.0)
image JaimeBde = im.Scale ("JaimieBdefeated.png" , 650, 900, yalign = 1.0)
image JaimeBch = im.Scale ("JaimieBchuckle.png" , 650, 900, yalign = 1.0)
image JaimeBla = im.Scale ("JaimieBlaugh.png" , 650, 900, yalign = 1.0)

image Morven = im.Scale ("morven.png" , 650, 900, yalign = 1.0)
image Morvencon =im.Scale ("morvenconfused.png" , 650, 900, yalign = 1.0)
image Morvenfru = im.Scale ("morvenfrustrated.png" , 650, 900, yalign = 1.0)

image Gregor = "gregor.png"

image Ferry = im.Scale("Ferry_Background.png" , 1920,1280)

image Captain =im.Scale ("Captain.png", 600, 880)
image Captainco =im.Scale ("captainconfused.png", 600, 880)
image Captainde =im.Scale ("captaindefeated.png", 600, 880)
image Captainfr =im.Scale ("captainfrustrated.png", 600, 880)

image CG1 = im.Scale("CG1.png" , 1920,1280)
image memory1 =im.Scale("memory 1.png" , 1920,1280)
image Blank =im.Scale ("blank.jpg", 1920,1280)

image Park = im.Scale ("park.png", 1920,1280)
image Butchers =im.Scale ("insidebutchers.png", 1920,1280)
image dock =im.Scale ("dockoutside.png", 1920,1280)
image key =im.Scale ("key.png" , 100,100)
image book =im.Scale ("book.png" , 100,100)
image toycar =im.Scale ("toycar.png" , 100,100)
image credit = im.Scale("credits.png" , 1920,1280)
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/theme.wav" volume 0.5
    scene CG1

    voice "audio/Jaimeopening.wav"
    J "Isle of the mind, what secrets do you hold for me? " 
    

    J "3 days ago I received a letter in the post." 
    
    J "3 days ago  I was sitting in my relatively warm office." 

    J "3 missing in 1 month." 

    scene Ferry
    play music "audio/ferrymusic.wav" volume 0.5
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Jaime with dissolve

    # These display lines of dialogue.

    voice "audio/Captainopen.wav"
    N "Shit! Where the fuck is it?"

    show Jaime at left  with dissolve



    show Captain at right with dissolve

    J "Is everything ok? "
    

    C "OH! Jesus!!"

    C "…Yes, sure it’s great, I’m great, super-duper, totally fine."
    hide Captain with dissolve
    show Captainde at right with dissolve
    C "I….I have lost my keys."

    J "Oh…."

    J "Wait"
    hide Jaime with dissolve
    show Jaimesh at left with dissolve
    J "WHAT!"

    J "Aren’t yo – I mean. Shouldn’t you be- Like- steering the boat?! "
    hide Captainde with dissolve
    show Captain at right with dissolve
    C "Dinnae get yer knickers in a twist."

    C "Ma wee boy Douglas is steering"
    hide Jaimesh with dissolve
    show Jaime at left with dissolve
    J "*“wee boy”…I have to say this isn’t filling me with confidence.*"

    C "Of course, this happens when I take the kids away for a weekend, you know give the wifey a break."

    C "She’s goanna be fuming. I can just hear her now."

    C "“You dobber, honestly Fergus. Bleeding idiot, how are you goanna lock up now, or get in the house ‘cause I’m telling you right now I ain’t letting you in.”"

    C " Ma was right when she said you would bring me nothing but disappointment and pain”"

    show Jaimech at left with dissolve
    J "I can give you a hand if you would like."
    
    
    menu:
       
        "Where did you see them last?":
            jump where

        "What do they look like?":
            jump look

    label where: 
    
        C "I don’t know, I took them out of my bag, went around the deck, and chatted with a couple of people."

        C "I swear one second, they were in my hand the next, gone, evaporated, poof."

        J "Curious"

        jump marry

label look:
    show Jaime at left  with dissolve
    hide Captain with dissolve 
    show Captainco at right with dissolve
    voice "audio/Captainconfused.wav"  
    C "...ther... they're keys, mate."
    C "You know, metal, with one jagged edge."
    C "You lose them on a night out."
    hide Captainco with dissolve
    show Captain at right with dissolve
    C "It's got a pissing fish keyring on it."
    hide Jaime with dissolve
    show Jaimede at left with dissolve
    J "*sigh*"
    
    jump marry

label marry:
    menu:
        "Touch bag":
            jump Ferry





label Ferry:
    scene Ferry
    show Jaime at left  with dissolve
    show Captain at right with dissolve
    J "Your keys captain"

    C "Yah beauty."
    C "Thank you...umm"

    J "Jamie Hawthorn"

    C "Hawthorn"
    C "Welcome to Eilean nah inntinn!"    
    stop music
    pause 4
    # Define a label for the nightmare scene
# Define scene for blank screen


# Play the music and display the scene with Jaime's dialogue
label dock:
    
    play music "audio/dockmusic.wav" volume 0.5
    scene dock

    show Jaime with dissolve
    J "I had never ventured this far north before, let alone crossed the open ocean."
    J "My legs and stomach were both grateful for the sturdy granite beneath my feet"
    J "The air is crisp untouched by the pollution of the city"
    J "Breathin in that cool crisp air. I allow my mind to wander"

    show Jaime at left with dissolve 
    show Craig at right with dissolve
    voice "audio/CGgreet.wav"
    CG "Greetings!"
   
    CG "Hi."
    CG "Hello Over here!"
    

    J "Hello..."

    CG "PI Hawthorn, I thought I recognised you."
    CG "Craig Gabharson, mayoral candidate"
    CG "But please call me Craig."

    J "Mr Gab- I mean craig"
    J "It's a pleasure to meet you,"
    J "sorry to be here under such circumstances. "

    CG "Yes, it's a horrid thing."
    CG "And please the pleasures all mine"
    CG "I assume you received details about the case. "

    J "I have a few questions,"
    J "If I may?"
    pause 2
    show Jaimeth at left with dissolve
    J "Could you give me a timeline of the missing. "

    CG "Well at the start of the month we had one of our eldest disappear. "
    CG "Then a week or 2 ago, Victor seemed to get up and leave. "
    CG "Then our most recent Gayle went missing a couple days ago. no luck no far."
    hide Jaimeth with dissolve
    show Jaime at left with dissolve 
    J "Has there been a history of missing people on the island?"

    CG "Oh well there's a few ghost stories about people going missing since the early settlers."
    CG "I suppose to keep the children from wandering off. "
    CG "My grandfather would tell me stories of the demons dancing with the devil upon the hills."
    hide Craig with dissolve
    show Morven at right with dissolve
    voice "audio/MorvenF.wav"
    M "That didn't keep you from wandering off, did it?"
    hide Morven with dissolve
    show Craigsh at right with dissolve

    CG "Auch, "
    CG "Hawthorn, this is our very own village hero, Morven Gabharson. "
    CG "Morven, this is Inspector Jamie Hawthorn. "
    hide Craigsh with dissolve
    show Morven at right with dissolve

    M "Inspector, I cannot express how grateful the whole island is."
    M "As you can imagine it’s just been a total shock. "
    M "And the Police round here well… let’s say they could find a shite in a..."
    hide Morven with dissolve
    show Craigdi at right with dissolve

    CG "*scoff"
    CG "Charming as always Morven"
    hide Craigdi with dissolve
    show Morven at right with dissolve

    J "Sorry, but um you went missing yourself Craig."    

    M "Auch aye!"
    M "Had the whole town looking for him for 3 days. When he was a boy." 

    J "What Happened"

    M "I found him down by the beach, those ghost stories didn't stop him. "
    hide Morven with dissolve
    show Craigfa at right with dissolve
    voice "audio/Craigfakelaugh.wav"
    CG "*flat chuckle* "
    CG "Well what was a young man to do to pass the time?"
    CG "That's a story for another time. "
    CG "Anyway Morven truly knows all the nooks and crannies of the island and she'll be your aid in the investigation."
    hide Craigfa with dissolve
    show Craig at right with dissolve
    show Jaimesh at left with dissolve    
    J "Oh..."
    J "Ummmm...."
    J "That’s so kind, sir, but really its not nes-"
    hide Jaimesh with dissolve
    show Jaime at left with dissolve
    CG "Nonsense!"
    CG "And there’s really no need to thank me!"  
    CG "Now I must be aff. "
    CG "Good luck."
    voice "audio/CGbye.wav"
    hide Craig with dissolve
    show Morven at right with dissolve

    M "Shall we Inspector?"
    stop music


label Parkin:
    
    scene Park
    play music "audio/parkmusic.wav" volume 0.5
    show Jaime at left with dissolve
    show Morven at right with dissolve

    M "It’s truly a shame you had to visit under such circumstances."
    M "The island is beautiful and Craig has really been helping me modernise it."
    M "It wasn’t until I convinced him  that we stopped tying up the swings on a Sunday. "
    voice "audio/Thinking01.wav"
    J "*mmmhh*"
    J "Did you know the victims?"
    
    M "Auch, everyone knows everyone round here, can't sneeze without spreading it around the village."
    hide Jaime with dissolve
    show Jaimeth at left with dissolve
    voice "audio/Thinking01.wav"
    J "*note self wee villages love a gossip.*"
    hide Jaimeth with dissolve
    show Jaime at left with dissolve
    M "So do you prefer being referred to as Inspector or Jamie?"
    show Jaimefr at left with dissolve
    J "Inspector."

    M "….Nah"
    M "It's so formal, if you wanna be called that you’ll have to call me something cool."
    M "You know like, special agent, double O seven or -"
    hide Jaimefr 
    show Jaime at left with dissolve
    menu:
        
        "Miss Marple":
            jump Green
        "PC Plum":
            jump Grass
    label Green:
        voice "audio/MorvenFru.wav"
        hide Morven with dissolve
        show Morvenfru at right with dissolve
        M "Are you saying I look like an 80 year old woman?"
        show Jaimech at left with dissolve
        J "No gosh, sorry I-I didn't mean it like that-"
        hide Jaimech with dissolve
        show Jaime at left with dissolve
        hide Morvenfru with dissolve
        show Morven at right with dissolve
        jump cont
    
    
    label Grass:
        voice "audio/MorvenFru.wav"
        M "….Your not good at the whole compliment thing are you."
        M "Pc Plum"
        jump cont



    label cont:
    show Jaime at left with dissolve
    M "Let's just move on shall we."


    J "Could you tell me more about Gayle?"
    J "What was she like on the day of the disappearance? Was she irritated? "

    M "Wee Gayle no way wouldn't hurt a fly"
    M "She's a sweet wee hing, barely six years old."
    hide Jaime with dissolve
    show Jaimesh at left with dissolve
    J "Oh…."
    J "Well Please don’t feel as though you must stay,"
    J "I can work efficiently alone."

    M "Hey I don't think so!"
    M "You don't get to just brush me off like that"
    M "This is my village, my people."
    M "And I am of much better use here than I’m sitting in an office, organising the hall for the next car boot sale."
    M "So “Inspector”, are we gonna stand around all day or get to work? "
    hide Jaimesh with dissolve
    show Jaime at left with dissolve
#mini game here
    M "Did you find anything, Inspector?"
    M "Inspector?"
    M "Jamie?"
    M "Hello?!"

    J "*Sharp intake of breath*"
    J "Sorry."
    J "Yes, I found these."

    M "Cigarette butts?"
    M "I hate to break it to you, but there's plenty of folk who partake in smoking."
    M "So unless your gonna swab some DNA or something."

    J "No need."
    J "I have our next lead."
    J "Where's the nearest butcher?"
    voice "audio/MorvenFru.wav"
    hide Morven with dissolve
    show Morvencon at right with dissolve

    M "Butchers?"
    M "How could you possibly think the butcher has anything to do with Gayle?"

    J "You're gonna have to trust me on that one"
    J "Call it Inspectors intuition."
            
label Butcher:
    scene Butchers
    play music "audio/butchermusic.wav" volume 0.5
    show Jaimie at left with dissolve
    show Morven at right with dissolve

    M "So what's the plan?"
    M "I could go in first, butter him up ya know. "
    voice "audio/JamieAS.wav"
    J "That won't be necessary."

    M "Hey don't diminish the powers of the town hero."
    M "Ok I have influence here."
    M "I was the one who saved the great charity bake sale, when those rogue seagulls got into the village hall, ok."
    M "That took a lot of persuading…"

    J "…I think I’ll be fine."

    M "Whoa whoa, hold your horses there. "
    M "You do know I'm here to help, don't yah."
    M "I have known these people for a lot longer than you."
    M "Gregor isn't just gonna speak to yah"
    hide Jaimie with dissolve
    show JaimeBde at left with dissolve
    J "I know what i'm doing!"
    hide JaimeBde with dissolve
    show Jaimie at left with dissolve
    M "Alright Taggart, calm down."
    M "Will you just trust me?"
    M "Just take it easy with him ok, he struggles to open up to people."
    M "So at least you have something in common. "
    hide Jaimie with dissolve
    hide Morven with dissolve
    show gregor with dissolve

    J "Good evening Mr.McNulty. I am going to ask you some questions about Gayle's dissapearance'"

    G "Year sure ,just let me close the shop"
    pause 2

    G "So What do you want to ask me about?"

    menu: 
        "Where were you the night of Gayle’s disappearance?":
            jump Op1
        "PC Why were you at the park the night of Gayle’s disappearance?":
            jump Op2
    label Op1:
        G "I closed the shop, then I probably had a smoke."
        G "I ‘on know the specifics, it wasni really an important night for me..."
        G "...until I found out obviously."
        J "Right, can you try and remember where you went for a smoke"
        G "I really ken why you’re assumin I went somewhere but I probably went tae the park."
    label Op2:
        G "Now how the fuck did ya ken that..."
        G "... sorry I souldni shout, just how on earth did ya  find that out"

    J "Were you aware that the park was the last known location of Gayle?"
    G "Don’t tell me, you actually think I had a hand in it"
    menu:
        "Not at all, just need to know if you saw anything there that night":
            jump Op3
        "You have to say, it’s quite the coincidence":
            jump Op4
    label Op4:
        G "Now you listen here, I wouldn’t touch a hair on Gayle’s head, get out my shop this is over"
        J "*I think i messed up gotta go back!"
        jump fail
    label fail:
        return    
    label Op3:
        G "Yeah, sorry, I dinnae think I saw any’in out o’ order, it was pretty dark"
        J "I see, there's no helping it."
        J "can you recollect a more exact time for when you were there it may shed some light on a time of disappearance for Gayle"
        G "Aye, must’ve been after 10:30, so about 10:50 tae 11:10"
        J "Thank you that’ll help" 
            


    J "Now there’s just a few more questions to ask."
    J "first, is there anyone you could imagine having kidnapped Gayle, It is very likely someone who lives on the island?"
    G "Nae one comes tae mind, we’re all real close on this island."
    G "I cannie imagine , anyone wanting to hurt little Gayle "

    menu:
        "Ok, lets change our focus, what about anywhere someone might be able to keep Gayle so she wouldn’t be found?":
            jump Op5
        "Ok, let’s change our focus, what about any way to smuggle Gayle of the Island so she wouldn’t be found?":
            jump Op6
    label Op5:
        G "Well, the only place that comes tae mind is the lighthouse."
        G "Though I cannie imagine Fergus bein the one who took 'er we go wayy back"
        J "Fergus?"
        G "A buddy ‘o mine, he’s the lighthouse keeper,"
        G "As I said, there's the only place I ken of that you’d be able to store a person, but Fergus would never"
    label Op6:
        G "You’d never get a whole person of the island by the main docks."
        G "The only other dock is by the lighthouse"
        G "Thought I cannie imagine Fergus bein the who took 'er we go wayy back"
        J "Fergus?"
        G "A buddy ‘o mine, he’s the lighthouse keeper."
        G "As I said, there's the only other dock on the Island the north sides got too many wonky currents to be usable."
        G "But Fergus would never"

    J "You seem to have a lot of faith in this Fergus guy."
    J "Are you certain he couldn't have done it?"
    G "Well he has been off fer a while,"
    G "It’s just..."
    G "... fuck it I shouldnae say this but he’s pissy because he had to give up his dream tae look after the lighthouse after his folks died."
    G "The because he had to give up his dream tae look after the lighthouse after his folks died."
    J "Noted, I’ll go have a chat with him tomorrow, good night Mr. McNulty"
    G "Oh..."
    G "...uhh"
    G "...Ok, see you later"
    hide gregor with dissolve
    show Jaimie at left with dissolve
    show Morven at right with dissolve
    
    M "Well I can certainly see why you were hired, not to be shabby at all."
    hide Jaimie with dissolve
    show JaimeBch at left with dissolve

    J "Not too bad yourself, thanks for the heads up."
    J "Sorry, for my curtness earlier on Morven."
    hide JaimeBch at left with dissolve
    show Jaimie at left with dissolve
    voice "audio/Morvengiggle.wav"
    M "Hey thats Miss Marple to you."

    hide Jaimie with dissolve
    show JaimeBla at left with dissolve
    J "I appreciate the help"
    J "I’ll see you tomorrow."
    M "Night Jamie."
label nightmare:

    scene Blank
    play music "audio/dream.wav" volume 0.5
    # Display first menu option
    menu:
        "it happened again last night" : 
            jump menu_2

    # Jump here to display second menu option
    label menu_2:
        menu:
            "I Heard them":
                jump menu_3


    # Jump here to display third menu option
    label menu_3:
        menu:
            "Saw them":
                jump menu_4

    # Jump here to display fourth menu option
    label menu_4:
        menu:
            "I..I felt":
                jump menu_5

    # Jump here to display fifth menu option
    label menu_5:
        menu:
            "it...":
                jump menu_6

    # Jump here to display sixth menu option
    label menu_6:
        menu:
            "I couldn't move, I was running, but the world around me stayed stagnant":
                jump menu_7

    # Jump here to display seventh menu option
    label menu_7:
        menu:
            "I kept running and running and running":
                jump menu_8

    # Jump here to display eighth menu option
    label menu_8:
        menu:
            "knees buckling": 
                jump menu_9

    # Jump here to display ninth menu option
    label menu_9:
        menu:
            "lungs burning":
                jump menu_10

    # Jump here to display tenth menu option
    label menu_10:
        menu:
            "I tasted Iron":
                jump menu_11

    # Jump here to display eleventh menu option
    label menu_11:
        menu:
            "I was screeching":
                jump menu_12

    # Jump here to display twelfth menu option
    label menu_12:
        menu:
            "Screaming":
                jump menu_13

    # Jump here to display thirteenth menu option
    label menu_13:
        menu:
            "breaking":
                jump menu_14

    # Jump here to display fourteenth menu option
    label menu_14:
        menu:
            "but,my pleas fell silent":
                jump menu_15

    # Jump here to display fifteenth menu option
    label menu_15:
        menu:
            "reaching":
                jump menu_16

    # Jump here to display sixteenth menu option
    label menu_16:
        menu:
            "clawing":
                jump menu_17

    # Jump here to display seventeenth menu option
    label menu_17:
        menu:
            "clamouring":
                jump menu_18

    # Jump here to display eighteenth menu option
    label menu_18:
        menu:
            "Desperate":
                jump menu_19

    # Jump here to display nineteenth menu option
    label menu_19:
        menu:
            "your hand out of reach...":
                jump menu_20

    # Jump here to display twentieth menu option
    label menu_20:
        menu:
            "...always":
                jump menu_21

    # Jump here to display twenty-first menu option
    label menu_21:
        menu:
            "out of reach...":
                jump menu_22

    # Jump here to display twenty-second menu option
    label menu_22:
        menu:
            "I woke sweat drenching my clothes, my heart thundering. Out of breath":
                jump end_game
label end_game:
    scene credit
    play music "audio/theme.wav" volume 0.5
    show Jaime at right
    J "Thank You "