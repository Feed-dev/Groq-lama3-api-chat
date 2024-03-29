import os
from dotenv import load_dotenv
from groq import Groq

text = """
Secret of the Emerald Tablet  
Dr. Gottlieb Latz 
Chapter 1: The Origin of the Emerald Tablet 
The Ancient Science of Alchemy 
Alchemy is the study of the Arcanum and how one can obtain it. The Arcanum, also known as the Elixir, 
Powder, or Stone, is the fundamental secret of nature. It is said to have the ability to perfect anything, to 
change baser metals into gold, to cure disease, to make man whole. The search for the Arcanum began 
in the darkest reaches of antiquity. Early alchemists called it Soma (the Body) in ancient Vedic texts and 
concealed its properties in a colorful variety of archetypal Gods. The Chinese called sought for it in the 
form of a Pill of Immortality. Later Indian alchemists referred to it as Rasayana. It was traced back to the 
first day of creation by Jewish alchemists. Greek philosophers saw it everywhere in nature, hidden in the 
composition of all matter. But it was the Egyptians who made finding it a science. 
The ideas of alchemy were incorporated into all levels of Egyptian culture. It was their practical science as 
well as their religion. An Egyptian sage known as Hermes Trismegistus is said to have written thousands 
of books on alchemy and other topics. Although some of his works were kept in secret by priests, many of 
his manuscripts were lost when the great world library at Alexandria was burned by Muslims and 
Christians. Only about forty of his alleged works have survived. Nevertheless, he is said to authored the 
most important and revered document of alchemy, the Tabula Smaragdina or Emerald Tablet.  
The Emerald Tablet 
The Emerald Tablet is such an important document that the entire history of alchemy can be divided into 
the period before the discovery of the tablet and the period after. Alchemical thought centered on the 
interpretation of the tablet for over 2,000 years. This mysterious communication speaks directly to our 
inner understanding, and the readers throughout the ages have felt compelled to search for the deeper 
meaning of its precepts. The alchemists believed that the secrets of their art were buried in its enigmatic 
lines. 
The origin of the Emerald Tablet has been traced as far back as the biblical Genesis, but most scholars 
attribute it to Hermes Trismegistus, whose name means "Thrice Greatest Hermes" or "Ruler of the Three 
Worlds." In all probability, such a person really existed, but it is now impossible to separate the actual 
person from the legends that identify him with Thoth, the Egyptian god of learning and magic, the inventor 
of all numbers and science, and later the god of the Greeks, Hermes, who became the Roman god 
Mercury.  
Albertus Magnus wrote that Alexander the Great discovered the tablet at the tomb of Hermes in Egypt. 
Wilhelm Kriegsmann has related a legend that Sarah, wife of Abraham, stumbled upon the tablet in a 
cave near Hebron and pried it loose from the stiff fingers of a mummified corpse. Other sources allege 
that Hermes was the son of Adam. He supposedly discovered the tablet in a cave while traveling in 
Ceylon. Some say it was discovered in an underground room of the pyramid of Cheops. Most stories 
describe the tablet as a green-colored stone with raised, bas-relief lettering in an alphabet that resembled 
Phoenician characters.  
After extensive and painstaking research into the history of the Emerald Tablet, I discovered that a 
revised Greek translation of the original text was issued around 300 BC. This translation was performed 
by three groups of Alexandrian alchemists, who were attempting to use the mysterious tablet to unify 
conflicting Jewish, Greek, and Egyptian versions of alchemy. The mixing of cultures in Alexandria caused 
a shattering clash of dogmas that shook alchemy to its roots. But because these ideas were treated with 
such secrecy among the ruling classes, the masses (and history) took little note of the potentially 
catastrophic nature of the conflict. Even today, it is hard for us to imagine the shattering impact this crisis 
of interpretation had on the world. Alchemy was considered a gift direct from God and was the hidden 
foundation upon which the world's religions and sciences were built. The truths of alchemy were a 
nation's highest secrets and were revealed only to a small group of worthy priests and philosophers.  
The enlightened tone of the Emerald Tablet so effectively defused this explosive situation, that it must 
have been divinely inspired. In fact, the translation of the tablet actually preserved the esoteric basis of 
Western Civilization. Although the rise of Christianity suppressed the Hermetic doctrines, they were 
passed on to later generations through a variety of occult groups and secret disciplines. 
The Three Titles of the Emerald Tablet 

The Emerald Tablet calls itself the "philosophy of the whole universe," and this is perhaps its most fitting 
title. However, it was never the nature of alchemists to freely divulge the importance of their work, nor to 
offer the uninitiated such an obvious and tantalizing prize. The original version was probably named 
Tabula Smaragdina, because it was precisely what the Latin implies: a green-colored stone tablet. The 
first Greek translation and first revision probably went by that same name. 
The second revision has been called the Tabula Hermetica. More fitting perhaps would be Tabula 
Aegyptia, owing to its origins. Most appropriate would be Tabula Khemica, a term which reflects the 
ancient name of Egypt (kheme = black soil of the Nile) and the roots of our own science of chemistry. The 
modern name of alchemy stems from the Arabic Al-Khemi, meaning "from Egypt" or "the Egyptian 
science."  
The third revision came to be known as the Tabula de Operatione Solis. This was a metaphysical 
interpretation that received wide acceptance and became the driving force behind alchemy through the 
sixteenth century. In the present work, the author will refer to the Emerald Tablet generally as the Tabula.  
The Age of the Emerald Tablet 
Unfortunately, the original Emerald Tablet has not survived or has been hidden away for safekeeping. As 
I noted, a few legends trace it as far back as Genesis, while other evidence suggests that it was written 
about 3000 BC, when the Phoenicians settled on the Syrian coast. The only complete modern text is a 
very early Latin translation, which exists in three versions. These three Latin versions correspond to the 
three Greek language revisions of a still older translation of the original Emerald Tablet. All three revisions 
were written in Alexandria, where Greek was the common tongue. Since neither the original translation 
nor the original document has survived, we have only the three revisions with which to work. 
The history of Alexandria is usually divided into two periods. The first, from 332 BC to 30 BC, is the time 
of the Ptolemies and the great library. The city was founded by Alexander the Great as a center of Greek 
culture in Egypt. The harbor town quickly inherited the trade of the ancient Phoenician city of Tyre and 
even passed Carthage in size. The second period runs from 30 BC to 638 AD. The city became a part of 
the Roman Empire during the early part of this period, and then after 300 AD, it became a center of 
Christian learning. It was finally conquered by the Arabs around 640 AD. 
For our purposes, it is convenient to divide the two Alexandrian Periods into three subdivisions, which 
correspond to the three revisions of the Emerald Tablet. The First Revision was written sometime 
between 300 BC and 270 BC, because it is based on ideas of the First Alexandrian School, which 
flourished at that time. The Egyptian and Hellenic cultures were involved in a fruitful merging, and this 
version reflects their worldview. This first version is centered on the three states of matter of Liquid, Solid, 
and Air. Fire was considered the agent of change between those states.  
The Second Revision was probably written around 270 BC, because the Alexandrian Empirical School 
came into power at that time. Among other things, the Empiricists accepted Fire as a fourth state matter. 
By this time the city had also become a center of Semitic scholarship and a Greek version of the Old 
Testament was being translated there. Specific changes were made in the Second Revision of the Tabula 
that reflected the empirical Greek and Jewish biblical interpretations. 
The Third Revision was probably conceived sometime in the period from 50 BC to 1 AD. This 
metaphysical evaluation suggested that non-physical processes were involved in the transformation of 
the states of matter and of the base metals into gold. It was this interpretation that allowed the rise of 
swindlers, puffers, and fakes, who called themselves alchemists. But it was also with this third 
interpretation that the ideas of alchemy finally took a form that could be understood by all men, regardless 
of culture or religion. 
It should be mentioned that a fourth interpretation originated in Alexandria around 300 AD. It stemmed 
from the Neoplatonic School, which attempted to combine Greek philosophy with Arab mysticism and 
combine them with the moral doctrines of Judaism and Christianity. This rendering did not require another 
revision of the Tabula, but it was the first of many dozens of personal, philosophical, and even prophetic 
interpretations of the original three revisions. 
With the Arab conquest of Egypt in the seventh century, Alexandrian alchemy was passed through 
Arabian sources -- most notably the alchemist Geber (Jabir Hayyan). Eventually, knowledge of the art 
spread to Morocco, and by the eighth century alchemy had taken a strong hold in Spain. The three 
revisions of the Emerald Tablet found their way to Europe along this same path. For the next thousand 
years, alchemy was to flourish in the fertile soil of European thinkers.
"""

load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

client = Groq(
    api_key=os.getenv('GROQ_API_KEY'),
)

stream = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a research assistant, help me explain the secret of the emerald tablet in short."
        },
        {
            "role": "user",
            "content": f"{text}",
        }
    ],
    model="mixtral-8x7b-32768",
    max_tokens=1024,
    temperature=0.5,
    top_p=1,
    stop=None,
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
