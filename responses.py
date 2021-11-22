from googletrans import Translator
trans = Translator()

ttt = 0
nim = 0
rpg = 0
end = 0



def sample_responses(input_text):
    global trans
    global ttt
    global rpg
    global nim
    global end
    user_message = str(input_text).lower()

###########################################################################
#help   
    if user_message.lower() == ("help"):
        return """
        Hello! I am Kenny's bot 
        Please type the commands below to view corresponding functions:
        =====
            >translate |  >games   |  >study  |    

        """
    if user_message.lower() == (">games"):
        return """
        =====
        Type the following commands to play different games:
        ======
        !ttt | tic tac toe
        !banana | a nim game about banana
        ======
        You can force-end a game anytime by responding "!end"

        """ 
    if user_message.lower() == ("!end"):
        nim, ttt, rpg = 0,0,0
###########################################################################
#STUDY
    if user_message.lower() == (">study"):
        return """
        Please type what subjects do you want to study:
        available subjects:
        ================================
        |  maths  |  cantonese  |  english  |  computer science  |
        """
    if user_message.lower() == ("english"):
        return """
        Please type one category!!!
        ================================
        |  reading  |  writing  |  listening  |  speaking  |"""
    if user_message.lower() == ("reading"):
        return """

        7 ways to IMPROVE ENGLISH READING skills and comprehension | Learning English Technique Lesson
        https://www.youtube.com/watch?v=sWZ9LNXZSvA

        Improve Your Reading Skills / READING Tips
        https://www.youtube.com/watch?v=myjdpOrnX4k
        """
    if user_message.lower() == ("writing"):
        return """
        7 Ways to Improve English Writing Skills | IELTS | EXAM | ESSAY | ACADEMIC
        https://www.youtube.com/watch?v=ZP_axfR9NKM

        How to Improve Your Vocabulary in Writing
        https://www.youtube.com/watch?v=DwQFll2LrFg

        15 Stunningly Beautiful English Words YOU Should Use More Often!
        https://www.youtube.com/watch?v=OTnJrYyn8ac
        """
    if user_message.lower() == ("listening"):

        return """
        32 Minutes of English Listening Practice for Beginners
        https://www.youtube.com/watch?v=bEB8-SWMYhI

        Improve Vocabulary ★ Learn English While Sleeping ★ Listening English Practice Level 3 ✔
        https://www.youtube.com/watch?v=OazE2vXzLf4

        English Conversation; Learn while you Sleep with 5000 words
        https://www.youtube.com/watch?v=3ha-kqV0P38&t=497s"""
    if user_message.lower() == ("speaking"):
        return """
        2 Hours of English Conversation Practice - Improve Speaking Skills
        https://www.youtube.com/watch?v=NNamZZsggM4&t=3632s

        Advanced speaking practice: English Imitation Lesson
        https://www.youtube.com/watch?v=FfhZFRvmaVY

        English Speaking 01 **Highly recommend!!!**
        https://www.youtube.com/watch?v=ZmUm29fc6nI"""


    if user_message.lower() == ("cantonese"):
            return """
            https://www.youtube.com/watch?v=w10my9tG9uY
            https://www.youtube.com/watch?v=jpVxzWuJUh8
            https://www.youtube.com/watch?v=Uo5lJlBnzAg
            https://www.youtube.com/watch?v=Q8JwKRCsXKs
            
            """
    if user_message.lower() == ("maths"):
        return """
        which area?
        | geometry  | category theory | differential | linear algebra |
        """
    if user_message.lower() == ("geometry"):
        return """
        these are some useful links, hope they can help!!!

        𝗻𝗲𝘄 𝗹𝗲𝗮𝗿𝗻𝗲𝗿𝘀

        (by:  The Organic Chemistry Tutor  ):
        Introduction to geometry 
        https://www.youtube.com/watch?v=302eJ3TzJQU
        Triangles - Basic Introduction, Geometry
        https://www.youtube.com/watch?v=q7vI2oXL0gQ
        Area of a Rectangle, Triangle, Circle & Sector, Trapezoid, Square, Parallelogram, Rhombus, Geometry
        https://www.youtube.com/watch?v=JnLDmw3bbuw

        (by:  mathantics  ):
        Math Antics - Polygons
        https://www.youtube.com/watch?v=IaoZhhx_I9s&list=PLUPEBWbAHUsxuIbsAS--B6cobarm2bty2&index=4
        Math Antics - Quadrilaterals
        https://www.youtube.com/watch?v=yiREqzDsMP8&list=PLUPEBWbAHUsxuIbsAS--B6cobarm2bty2&index=6

        𝘀𝗼𝗺𝗲 𝗱𝗶𝗳𝗳𝗶𝗰𝘂𝗹𝘁 𝗾𝘂𝗲𝘀𝘁𝗶𝗼𝗻𝘀:

        (by:  MindYourDecisions  )
        https://www.youtube.com/watch?v=HQc-54hQ8kw
        https://www.youtube.com/watch?v=GbQQcrwYHt0
        https://www.youtube.com/watch?v=8GnyjbUj-eE&t=235s
        """
    if user_message.lower() == ("category theory"):
        return """
        By  Bartosz Milewski:
        https://youtube.com/playlist?list=PLbgaMIhjbmEnaH_LTkxLI7FMa2HsnawM_
        """
    if user_message.lower() == ("differential"):
        return """
        by The Organic Chemistry Tutror:
        https://www.youtube.com/watch?v=C5RI5eLzVfo
        
        by blackpenredpen:
        https://www.youtube.com/watch?v=2ooWs_8hzxQ"""
    if user_message.lower() == ("linear algebra"):
        return """
        by FreeCodeCamp:
        https://www.youtube.com/watch?v=JnTa9XtvmfI"""
    if user_message.lower() == ("computer science"):
        return """
        Please choose one category:
        |  intro  |  programming  |  computer components  |  ai  |"""
    if user_message.lower() == ("intro"):
        return """
        Please check the videos for a brief intro to computer science!!!
        Map of Computer Science:
        https://www.youtube.com/watch?v=SzJ46YA_RaA&t=244s

        Introduction to Programming and Computer Science - Full Course:
        https://www.youtube.com/watch?v=zOjov-2OZ0E"""
    if user_message.lower() == ("programming"):
        return """
        Please choose one language to learn!!!
        | python | javascript | html-css | c | c++ | c# | java | php |
        """
    if user_message.lower() == ("python"):
        return """
        Learn Python - Full Course for Beginners [Tutorial]:
        https://www.youtube.com/watch?v=rfscVS0vtbw&t=4501s"""
    if user_message.lower() == ("javascript"):
        return """
        Learn JavaScript - Full Course for Beginners
        https://www.youtube.com/watch?v=PkZNo7MFNFg&t=2684s"""
    if user_message.lower() == ("html-css"):
        return """
        HTML & CSS Full Course 🌎 (𝙁𝙧𝙚𝙚)
        https://www.youtube.com/watch?v=cyuzt1Dp8X8"""
    if user_message.lower() == ("c"):
        return """
        C Programming Tutorial for Beginners
        https://www.youtube.com/watch?v=KJgsSFOSQv0&t=100s"""
    if user_message.lower() == ("c++"):
        return """
        C++ Tutorial for Beginners - Full Course
        https://www.youtube.com/watch?v=vLnPwxZdW4Y&t=4389s"""
    if user_message.lower() == ("c#"):
        return """
        C# Tutorial - Full Course for Beginners
        https://www.youtube.com/watch?v=GhQdlIFylQ8&t=78s"""
    if user_message.lower() == ("java"):
        return """
        Java Tutorial for Beginners [2020]
        https://www.youtube.com/watch?v=eIrMbAQSU34&t=5759s"""
    if user_message.lower() == ("php"):
        return """
        PHP Programming Language Tutorial - Full Course
        https://www.youtube.com/watch?v=OK_JCtrrv-c"""
    if user_message.lower() == ("computer components"):
        return """
        What does what in your computer? Computer parts Explained
        https://www.youtube.com/watch?v=ExxFxD4OSZ0"""
    if user_message.lower() == ("ai"):
        return """
        What is Artificial Intelligence? In 5 minutes.
        https://www.youtube.com/watch?v=2ePf9rue1Ao&t=107s
        
        Artificial Intelligence In 5 Minutes | What Is Artificial Intelligence? | AI Explained | Simplilearn
        https://www.youtube.com/watch?v=ad79nYk2keg
        
        Healed through A.I. | The Age of A.I.
        https://www.youtube.com/watch?v=V5aZjsWM2wo"""
###########################################################################
#translate
    if user_message.lower() == (">translate"):
        return """
        you can translate any language to English using this bot!!! (supported by gogletrans==4.0.0-rc1)
        to translate a sentence, please follow this format:
        ===================================================
        -translate ("your sentence here")
        https://im7.ezgif.com/tmp/ezgif-7-0c0d8bc0cd4a.gif
        
        """
    if "-translate" in user_message.lower():
            if "-translate" == user_message.split()[0]:
                return (" ".join(user_message.split()[1:]) + " -> " +trans.translate(" ".join(user_message.split()[1:])).text)
###########################################################################
#ttt
    if user_message.lower() == ("!ttt"):
        ttt = 1
        return """
        Let's start the game!!!
        =======================
        please place your mark first:
        |1|2|3|
        |4|5|6|
        |7|8|9|
        """
    if ttt == 1:
        if user_message == ("1"):
            ttt += 9
            return """
            valid marks: 2,3,4,6,7,8,9
            |x| | | 
            | |o| |
            | | | |
            """
        elif user_message == ("2"):
            ttt =20
            return """
            valid marks: 2,3,4,6,7,8,9
            | |x| | 
            | |o| |
            | | | |
            
            Please place your mark
            """
        elif user_message == ("3"):
            ttt =30
            return """
            valid marks: 2,3,4,6,7,8,9
            | | |x| 
            | |o| |
            | | | |

            Please place your mark
            """
        elif user_message == ("4"):
            ttt =40
            return """
            valid marks: 2,3,4,6,7,8,9
            | | | | 
            |x|o| |
            | | | |

            Please place your mark
            """
        elif user_message == ("5"):
            ttt =50
            return """
            valid marks: 2,3,4,6,7,8,9
            |o| | | 
            | |x| |
            | | | |

            Please place your mark
            """
        elif user_message == ("6"):
            ttt =60
            return """
            valid marks: 2,3,4,6,7,8,9
            | | | | 
            | |o|x|
            | | | |

            Please place your mark
            """
        elif user_message == ("7"):
            ttt =70
            return """
            valid marks: 2,3,4,6,7,8,9
            | | | | 
            | |o| |
            |x| | |

            Please place your mark
            """
        elif user_message == ("8"):
            ttt =80
            return """
            valid marks: 2,3,4,6,7,8,9
            | | | | 
            | |o| |
            | |x| |

            Please place your mark
            """
        elif user_message == ("9"):
            ttt = 90
            return """
            valid marks: 2,3,4,6,7,8,9
            | | | | 
            | |o| |
            | | |x|

            Please place your mark
            """
    if ttt == 10:
        if user_message == ("1"):
            return """
            please do not place your mark in repeating positions!!
            """
        elif user_message == ("2"):
            ttt = 12
            return """
            valid marks: 4,6,7,8,9
            |o|o|x| 
            | |x| |
            | | | |

            Please place your mark
            """
        elif user_message == ("3"):
            ttt = 13
            return """
            valid marks: 4,6,7,8,9
            |o|x|o| 
            | |x| |
            | | | |

            Please place your mark
            """
        elif user_message == ("4"):
            ttt = 14
            return """
            valid marks: 2,3,6,8,9
            |o| | | 
            |o|x| |
            |x| | |

            Please place your mark
            """
        elif user_message == ("5"):
            return """
            you can't replace my mark hehe
            """
        elif user_message == ("6"):
            ttt = 16
            return """
            valid marks: 3,4,7,8,9
            |o|x| | 
            | |x|o|
            | | | |

            Please place your mark
            """
        elif user_message == ("7"):
            ttt = 17
            return """
            valid marks: 2,3,6,8,9
            |o| | | 
            |x|x| |
            |o| | |

            Please place your mark
            """
        elif user_message == ("8"):
            ttt = 18
            return """
            valid marks: 2,3,6,7,9
            |o| | | 
            |x|x| |
            | |o| |

            Please place your mark
            """
        elif user_message == ("9"):
            ttt = 19
            return """
            valid marks: 3,4,6,7,8
            |o|x| | 
            | |x| |
            | | |o|

            Please place your mark
            """   
    if ttt == 12:

        if user_message == ("1") or user_message == ("2") or user_message == ("3"):
            return "there is already a mark there!!! Please place somewhere else!"
        if user_message == ("5"):
            return "you can't cheat in front of a bot!!!"
        if user_message == ("4"):
            ttt = 0
            return """
            -
            |o|o|x| 
            |o|x| |
            |x| |o|

            I won!!!
            """   

        if user_message == ("6"):
            ttt = 0
            return """
            -
            |o|o|x| 
            | |x|o|
            |x| | |

            I won !!!
            """

        if user_message == ("8"):
            ttt = 0
            return """
            -
            |o|o|x| 
            | |x| |
            | |o| |

            I won!!!
            """
        if user_message == ("9"):
            return """
            -
            |o|o|x| 
            | |x| |
            |x| |o|

            I won!!!

            """
        if user_message == ("7"):
            ttt = 127
            return """
            valid marks: 6, 8, 9
            |o|o|x| 
            |x|x| |
            |o| | |

            """
    if ttt == 127:
        if user_message == ("1") or user_message == ("2") or user_message == ("3") or user_message == ("4") or user_message == ("5") or user_message == ("7"):
            return "invalid mark, please try again!"
        if user_message == ("6"):
            ttt = 0
            return """
            -
            |o|o|x| 
            |x|x|o|
            |o|x| |

            it's a tie!!!
            """
        if user_message == ("8"):
            ttt = 0
            return """
            -
            |o|o|x| 
            |x|x|x|
            |o|o| |

            I won!!!
            """
        if user_message == ("9"):
            ttt = 0
            return """
            -
            |o|o|x| 
            |x|x|x|
            |o| |o|

            I won!!!
            """

    if ttt == 13:
        if user_message == ("1") or user_message == ("2") or user_message == ("3") or user_message == ("5") :
            return """
            please do not place your mark in used positions!!
            """
        elif user_message == ("4"):
            ttt = 0
            return """
            -
            |o|x|o| 
            |o|x| |
            | |x| |

            I won!!!
            """
        elif user_message == ("6"):
            ttt = 0
            return """
            -
            |o|x|o| 
            | |x|o|
            | |x| |

            I won!!!
            """
        elif user_message == ("7"):
            ttt = 0
            return """
            -
            |o|x|o| 
            | |x| |
            |o|x| |

            I won!!!
            """
        elif user_message == ("8"):
            ttt = 138
            return """
            valid marks: 6,7,9
            |o|x|o| 
            |x|x| |
            | |o| |

            Please place your mark
            """
        elif user_message == ("9"):
            ttt = 13
            return """
            -
            |o|x|o| 
            | |x| |
            | |x|o|

            I won!!!
            """
    if ttt == 138:
        if user_message == ("1") or user_message == ("2") or user_message == ("3") or user_message == ("4") or user_message == ("5") or user_message == ("8"):
            return "invalid mark, please try again!"
        if user_message == ("6"):
            ttt = 0
            return """
            -
            |o|x|o| 
            |x|x|o|
            | |o|x|

            It is a tie!!!
            """
        elif user_message == ("7"):
            ttt = 0
            return """
            -
            |o|x|o| 
            |x|x|x|
            |o|o| |

            I won!!!
            """
        elif user_message == ("9"):
            ttt = 0
            return """
            -
            |o|x|o| 
            |x|x|x|
            | |o|o|

            I won!!!
            """

    if ttt == 14:
        if user_message == ("1") or user_message == ("4") or user_message == ("5") or user_message == ("7") :
            return """
            please do not place your mark in used positions!!
            """
        elif user_message == ("2"):
            ttt = 0
            return """
            -
            |o|o|x| 
            |o|x| |
            |x| | |

            I won!!!
            """            
        elif user_message == ("3"):
            ttt = 143
            return """
            valid marks: 6,8,9
            |o|x|o| 
            |o|x| |
            |x| | |

            Please place your mark
            """    
        elif user_message == ("6"):
            ttt = 0
            return """
            -
            |o| |x| 
            |o|x|o|
            |x| | |

            I won!!!
            """    
        elif user_message == ("8"):
            ttt = 0
            return """
            -
            |o| |x| 
            |o|x| |
            |x|o| |

            I won!!!
            """    
        elif user_message == ("9"):
            ttt = 0
            return """
            -
            |o| |x| 
            |o|x| |
            |x| |o|

            I won!!!
            """   
    if ttt == 143:
        if user_message == ("1") or user_message == ("2") or user_message == ("3") or user_message == ("4") or user_message == ("5") or user_message == ("7") :
            return """
            please do not place your mark in used positions!!"""
        if user_message == ("6"):
            ttt = 0
            return """
            -
            |o|x|o| 
            |o|x|o|
            |x|x| |

            I won!!!
            """  
        if user_message == ("8"):
            ttt = 0
            return """
            -
            |o|x|o| 
            |o|x|x|
            |x|o| |

            It is a tie!!!
            """   
        if user_message == ("9"):
            ttt = 0
            return """
            -
            |o|x|o| 
            |o|x|x|
            |x| |o|

            It is a tie!!!
            """                                                                                             
                                   
###########################################################################
#nim
    if user_message.lower() == ("!banana"):
        nim = 100
        return """
        Banana Roulette!!!
        ==================
        in the beginning of the game, there are 18 bananas, players can take 1 to 3 bananas turn by turn,
        🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
        ==================
        It's your turn now, how many 🍌 would you like to pick?
        Please give a number from 1 to 3
        """
    if nim == 100:
        if user_message == ("1"):
            nim = 1
            return """
            It's my turn, I will pick 1
            🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""

        elif user_message == ("2"):
            nim = 2
            return """
            It's my turn, I will pick 3
            🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("3"):
            nim = 3
            return """
            It's my turn, I will pick 2
            🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
    if nim == 1:
        if user_message == ("1"):
            nim = 3
            return """
            It's my turn, I will pick 2
            🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("2"):
            nim = 13
            return """
            It's my turn, I will pick 2
            🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("3"):
            nim = 14
            return """
            It's my turn, I will pick 3
            🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
    if nim == 2:
        if user_message == ("1"):
            nim = 4
            return """
            It's my turn, I will pick 3
            🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("2"):
            nim = 5
            return """
            It's my turn, I will pick 2
            🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("3"):
            nim = 6
            return """
            It's my turn, I will pick 1
            🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
    if nim == 3:
        if user_message == ("1"):
            nim = 4
            return """
            It's my turn, I will pick 3
            🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("2"):
            nim = 5
            return """
            It's my turn, I will pick 2
            🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("3"):
            nim = 6
            return """
            It's my turn, I will pick 1
            🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
    if nim == 4:
        if user_message == ("1"):
            nim = 7
            return """
            It's my turn, I will pick 3
            🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("2"):
            nim = 8
            return """
            It's my turn, I will pick 2
            🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("3"):
            nim = 9
            return """
            It's my turn, I will pick 1
            🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
    if nim == 5:
        if user_message == ("1"):
            nim = 7
            return """
            It's my turn, I will pick 3
            🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("2"):
            nim = 8
            return """
            It's my turn, I will pick 2
            🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("3"):
            nim = 9
            return """
            It's my turn, I will pick 1
            🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
    if nim == 6:
        if user_message == ("1"):
            nim = 7
            return """
            It's my turn, I will pick 3
            🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("2"):
            nim = 8
            return """
            It's my turn, I will pick 2
            🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("3"):
            nim = 9
            return """
            It's my turn, I will pick 1
            🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
    if nim == 7:
        if user_message == ("1"):
            nim = 0
            return """
            It's my turn, I will pick 3
            🍌
            I won"""
        elif user_message == ("2"):
            nim = 0
            return """
            It's my turn, I will pick 2
            🍌
            I won"""
        elif user_message == ("3"):
            nim = 12
            return """
            It's my turn, I will pick 1
            🍌
            I won"""
    if nim == 8:
        if user_message == ("1"):
            nim = 0
            return """
            It's my turn, I will pick 3
            🍌
            I won"""
        elif user_message == ("2"):
            nim = 0
            return """
            It's my turn, I will pick 2
            🍌
            I won"""
        elif user_message == ("3"):
            nim = 12
            return """
            It's my turn, I will pick 1
            🍌
            I won"""
    if nim == 9:
        if user_message == ("1"):
            nim = 0
            return """
            It's my turn, I will pick 3
            🍌
            I won"""
        elif user_message == ("2"):
            nim = 0
            return """
            It's my turn, I will pick 2
            🍌
            I won"""
        elif user_message == ("3"):
            nim = 12
            return """
            It's my turn, I will pick 1
            🍌
            I won"""
    if nim == 13:
        if user_message == ("1"):
            nim = 4
            return """
            It's my turn, I will pick 3
            🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("2"):
            nim = 5
            return """
            It's my turn, I will pick 2
            🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("3"):
            nim = 6
            return """
            It's my turn, I will pick 1
            🍌🍌🍌🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
    if nim == 14:
        if user_message == ("1"):
            nim = 15
            return """
            It's my turn, I will pick 3
            🍌🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("2"):
            nim = 7
            return """
            It's my turn, I will pick 3
            🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
        elif user_message == ("3"):
            nim = 8
            return """
            It's my turn, I will pick 2
            🍌🍌🍌🍌🍌
            how many 🍌 would you like to pick?
            Please give a number from 1 to 3"""
    if nim == 15:
        if user_message == ("1"):
            nim = 0
            return """
            🍌🍌
            You can only choose one,
            You won!!!"""
        elif user_message == ("2"):
            nim = 0
            return """
            It's my turn, I will pick 3
            🍌
            I won"""
        elif user_message == ("3"):
            nim = 0
            return """
            It's my turn, I will pick 2
            🍌
            I won"""
###########################################################################
