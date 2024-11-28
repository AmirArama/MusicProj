titles = [] 
pages = []
sub_pages = []
images = []
imagesSize = []


title = "Pythagorean Tuning (c. 570–495 BCE)"
page = """
Aside from the right-angle formula, Pythagoras is also credited with uncovering 
the mathematical basis of musical intervals. According to legend, 
he experimented with strings and found that harmonious tones are
produced when their lengths are in simple ratios, 
such as 2:1 for an octave or 3:2 for a perfect fifth and 4:3 for a perfect fourth.
For this reason Pythagoras is considered the father of music and harmony
"""
page2 = """
Pythagorean Tuning was derived from the natural harmonic series, 
specifically starting with the note C and stacking perfect fifths on top of it. 
Pythagoras and his followers likely discovered the beauty of these simple ratios
and used them to form scales.
"""
image = "static/images/pythagoras.webp"
imageSize = 25

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)

title = "Why we are not using Pythagorean Tuning today?"
page = """
Tuning of Other Intervals: The major third (5:4), a key interval for harmony, 
is not as perfectly tuned in Pythagorean tuning. In fact, it's slightly sharp (around 81/80), 
meaning that chords involving thirds (like major triads) don't sound as pure. 
This leads to a certain "roughness" or "beating" in some chords,
which can be perceived as unpleasant.

"""
page2 = """  
Limited Key Modulation: Pythagorean tuning works well for music in a single key,
but as you move to other keys (like G major, D major, etc.),
the tuning becomes increasingly "out of tune," especially for intervals beyond the perfect fifth.
This makes modulation to distant keys problematic and impractical.
"""
image = "static/images/pythagoras.webp"
imageSize = 25

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)

title = "Just Intonation"
page = """
Just intonation, a tuning system based on pure intervals derived 
from whole-number frequency ratios, has roots tracing back to ancient civilizations. 
While no single individual can be credited as its sole originator, 
several key figures have significantly contributed to its development:
"""
page2 = """  
Pythagoras (c. 570-495 BCE): 
His work laid the groundwork for understanding harmonic ratios, 
which are fundamental to just intonation.
Claudius Ptolemy (c. 100–170 CE): 
A Greco-Roman mathematician and astronomer, Ptolemy expanded upon earlier 
theories by describing a 5-limit diatonic scale in his treatise "Harmonics." 
This scale, known as "Ptolemy's intense diatonic," utilized just intervals and 
influenced subsequent tuning systems. 
Harry Partch (1901-1974): A 20th-century American composer and theorist, 
Partch developed an extensive system of just intonation, 
creating custom instruments to perform his compositions. 
His work emphasized the use of pure intervals and expanded the possibilities 
of just intonation in contemporary music.
"""
image = ""
imageSize = 25

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)

title = "Just Intonation"
page = """
Just intonation is a system based on the natural harmonic series, 
where intervals are derived from simple integer ratios. 
For example, the major third is tuned to the ratio 5:4, 
and the perfect fifth to 3:2. In just intonation, 
all the intervals align with the harmonic overtones produced 
by a vibrating string or column of air. 
This system favors the purity of intervals, leading to more consonant-sounding chords.
"""
page2 = """
Advantages: Perfect Intervals: Just intonation produces pure thirds,
sixths, and other intervals based on small, simple ratios 
(e.g., 5:4 for the major third, 3:2 for the perfect fifth). 
This results in a highly consonant, pleasing sound, 
especially when played in a single key or tonal center.
"""
image = ""
imageSize = 25

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)

title = "Just Intonation today?"
page = """
Problems: Key Dependence: Just intonation is key-specific. 
The intervals are tuned for a particular tonic note, so they will sound perfect in that key, 
but if you shift to another key, the tuning will no longer be pure. 
For example, in the key of C, the note G will sound perfect as a perfect fifth (3:2), 
but in the key of D, the same interval will sound 
slightly off because the tuning system is based on the harmonic series of D, not C. 
This restricts the ability to modulate freely between keys.  
"""
page2 = """
No Chromaticism: Just intonation struggles with chromatic notes 
(e.g., sharps and flats) because each new note would require recalibrating all the other intervals. 
In essence, you can't have both a perfectly tuned C major chord and a perfectly tuned F# major chord
in the same system.
"""
image = ""
imageSize = 25

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)

title = "Just Intonation Intervals"
page = """
"""
page2 = """
"""
image = "static/images/just_table.png"
imageSize = 75

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Equal Temperament (c. 16th-18th Century)"

page = """
Equal temperament divides the octave into 12 equal steps (semitones), 
meaning each semitone has the same frequency ratio (the 12th root of 2, or about 1.05946). 
This tuning system allows for perfectly equal spacing between all notes, 
making it ideal for playing in all keys without needing to retune the instrument.
"""
page2 = """
Advantages: Flexibility Across Keys: 
Equal temperament allows musicians to modulate freely between keys and play in every key 
without worrying about interval purity. 
This was especially important during the rise of Baroque and Classical music, 
where key changes (modulations) and chromaticism became more central to musical expression.
"""
image = ""
imageSize = 25

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)

title = "Equal Temperament strength"
page = """  
Uniformity: Equal temperament works equally well for all intervals, 
which means that no single interval is perfectly pure. 
This can be seen as a compromise that allows for a more consistent, 
uniform tuning system across all keys and instruments.
"""
page2 = """  
Chromaticism and Harmony: Equal temperament also makes it easier to explore complex 
harmonic and chromatic relationships. 
It supports the full chromatic scale (12 notes per octave), 
which became important in later Western classical music.
"""
image = ""
imageSize = 25

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)

title = "Equal Temperament Problems"
page = """
Compromise on Interval Purity: The key trade-off of equal temperament 
is that the intervals, while evenly spaced, are not perfectly aligned 
with the natural harmonic series. For example:
The perfect fifth (3:2) in equal temperament is slightly flattened (by about 1/6th of a semitone), 
and the major third (5:4) is similarly slightly sharp (by about 1/4 of a semitone). 
These small adjustments make the intervals sound slightly less "pure" 
compared to just intonation or Pythagorean tuning.
"""
page2 = """  
Loss of Harmonic "Color": 
Because every key and interval is altered by the same amount in equal temperament, 
the harmonic "color" of different keys and chords becomes more uniform. 
Some of the subtleties and emotional resonances of specific keys or modes 
(as found in earlier music) are lost.
"""
image = ""
imageSize = 25

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)

title = "Equal Temperamets Intervals"
page = """
"""
page2 = """
"""
image = "static/images/equal_table.png"
imageSize = 75

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)

title = "The shift in Tuning - to Just"
page = """
Pythagorean to Just Intonation: 
The shift to just intonation came as music became more harmonically complex. 
As Western music evolved, especially during the Renaissance and early Baroque periods, 
composers and musicians began to focus on more sophisticated harmony, including thirds and sixths. 
The Pythagorean system’s issues with third intervals led to the development of just intonation, 
which offered purer intervals.
"""
page2 = """
"""
image = ""
imageSize = 25

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)

title = "The shift in Tuning - to Equal Temperament"

page = """
Just Intonation to Equal Temperament: The transition to equal temperament was motivated 
by the growing demand for modulatory freedom in Baroque and Classical music. 
Composers and performers wanted to move freely between distant keys 
(e.g., from C major to A flat major) without retuning or encountering "out-of-tune" intervals. 
The rise of keyboard instruments like the harpsichord and piano, 
which required fixed tuning, also made equal temperament more practical. 
Musicians began to accept the slight "imperfections" in tuning because the 
flexibility it offered was far more valuable.
"""
page2 ="""
"""
image = ""
imageSize = 25

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)

title = "Circle Of Fifths - Just Intonation Vs. Equal Temperament"
page = """
Circle of Fifths in Just Intonation:
In just tuning, the circle of fifths behaves differently. 
Instead of using the 7-semitone equal-tempered fifth, 
just tuning uses the pure perfect fifth with a ratio of 3:2. 
This is a consonant interval and closely aligns with harmonic overtone series, 
but as you stack these pure fifths, you encounter a problem called Pythagorean comma.
When you stack 12 pure fifths (each a 3:2 ratio), the result doesn't exactly match 7 octaves (which is a 2:1 ratio). 
This discrepancy creates a small difference in pitch—called the Pythagorean comma—which 
needs to be "closed" if you want to fit into the 12-tone octave structure.
The Pythagorean comma means that if you keep stacking pure fifths in just intonation, 
eventually the intervals between the notes will not align perfectly with the starting note 
when you complete the circle of fifths. 
This results in a slightly out-of-tune relationship between the final note and the first note 
(the tonic) when you return to the starting point of the circle. 
As a result, the tonic will be slightly sharper than the original note, which causes a noticeable 
discrepancy in tuning.
"""
page2 = """
In this image, green denotes the Just stacking as one can see there is a constant drift from the Equal Temperament (in blue) aside from the Pythagorean comma issue.  
"""
image = "static/images/circle_plot_transparent.png"
imageSize = 75

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)






title = "Overtones and harmonics"
page = """
Before delving into Pythagorean music theory, it's essential to understand the harmonic content of a real instrument's tone, such as that of a guitar. When a guitar string is plucked, it doesn't vibrate solely at its fundamental frequency; instead, it produces a series of overtones or harmonics. These harmonics are integer multiples of the fundamental frequency and contribute to the instrument's unique timbre. For instance, the first harmonic is the fundamental frequency, the second harmonic is twice that frequency, the third is three times, and so on. The specific combination and relative intensities of these harmonics define the characteristic sound of the guitar
"""
page2 = """
"""
image = ""
imageSize = 25

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Overtones and harmonics"
page = """
In acoustics, the term "overtone" refers to any resonant frequency above the fundamental frequency of a sound. 
When these overtones are integer multiples of the fundamental frequency, 
they are specifically termed "harmonics." Both overtones and harmonics 
are also known as "resonances." 
"""
page = page + """
When a string instrument plays A4 (440 Hz), it produces a complex waveform composed 
of the fundamental frequency and a series of harmonics or overtones. 
These harmonics are integer multiples of the fundamental frequency
and contribute to the instrument's unique sound.
"""

page = page + """
In theory, a musical note produced by an instrument generates an infinite series of harmonics, 
each being an integer multiple of the fundamental frequency.
"""
page2 = """
"""
image = ""
imageSize = 25

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Individual Harmonic Tones Of The A Note "
page = """
440 Hz (Fundamental), 880 Hz (Octave), 1320 Hz (Octave + Perfect Fifth), 1760 Hz (Two Octaves), 
2200 Hz (Two Octaves + Major Third), 2640 Hz (Two Octaves + Perfect Fifth), 3080 Hz (Two Octaves + Minor Seventh), 3520 Hz (Three Octaves).
"""
page2 = """
"""
image = "static/images/harmonics.png"
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Timbre"
page = """
Timbre, also known as tone color or tone quality, is the attribute of sound that allows listeners to distinguish between different sources producing the same pitch and loudness, such as differentiating a piano from a violin playing the same note.
"""
page2 = """
"""
image = "static/images/frequency_spectrum.png"
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Timbre"
page = """
The unique timbre of an instrument, characterized by its specific combination of overtone frequencies and amplitudes, plays a crucial role in source separation algorithms. This distinct harmonic content arises from factors such as the instrument's shape, materials, and method of sound production. By analyzing these timbral features, algorithms can effectively distinguish and isolate individual instruments within a complex audio mix. 
"""
page2 = """
"""
image = "static/images/frequency_spectrum.png"
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Timbre"
page = """
If a musical tone contains multiple harmonics at various octaves above the fundamental frequency,
why doesn't our ear perceive these higher octaves as separate pitches?
The answer lies in how our auditory system processes sound. 
The fundamental frequency is the loudest and most dominant component, 
defining the pitch we perceive. While harmonics contribute to the tone’s timbre, 
they are integrated by our brain as part of the same sound rather than as separate pitches. 
This psychoacoustic phenomenon ensures that we hear the tone as A4, 
with the harmonics enriching its tonal quality rather than competing with the fundamental 
frequency for perceived pitch.
In other words, the presence of harmonics shapes the timbre, 
or tonal color, of the sound but not its perceived pitch. 
To delve deeper into this, consider exploring topics such as 
psychoacoustics and tone masking. These concepts are also utilized in audio compression, 
where overtones are removed from the original sound without significantly 
compromising the overall experience and enjoyment—like removing a subtle 
shade of color without altering the overall shape.
Another related subject is sound entropy vs ear entropy. 
I will elaborate more on psychoacoustics and sound entropy on a later page.  
""" 
page2 = """
"""
image = ""
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title =""
page = """
A chord, much like a word, derives its meaning from its context. Just as a word gains significance within the flow of a sentence, a chord contributes to the overall message of a piece of music. To fully understand what the music conveys, one must listen to how its parts interact and build upon each other, creating a cohesive and expressive narrative.
"""
page2 = """
"""
image = ""
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


page = """
I want to make the subject of tonal harmony simple and approachable, so anyone can understand how it shapes music across all genres today.
But please note: Tonal harmony is a vast and intricate subject, offering endless opportunities for deep exploration and understanding of how music conveys emotion and meaning.
"""
page2 = """
"""
image = ""
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Tonal Harmony"
page = """
Tonal harmony is a system of musical organization that revolves around the concept of a tonic, which serves as the central and most stable note or chord in a key. It is the foundation of Western music from the Baroque period (1600–1750) through the Romantic era (19th century), and it remains influential in modern genres such as pop, jazz, and film scores.
"""
page2 = """
"""
image = ""
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "The Tonic as the Center"
page = """
The tonic is the "home" or "resting point" of the harmony. It is typically represented by the first scale degree (I chord in Roman numeral notation).
"""
page2 = """
"""
image = ""
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Tonal Harmony"
page = """
All other chords and notes are heard in relation to the tonic, creating a sense of hierarchy and resolution.
"""
page2 = """
"""
image = ""
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Tonal Harmony"
page = """
Tonal harmony is built on diatonic scales (e.g., major, minor, and modes), each consisting of seven notes that form the basis for chords and harmonic structures.
If a piece of music is described as tonal, it follows specific guiding rules that establish a tonal center (the tonic) and a hierarchy of pitches and harmonies. These rules are rooted in the principles of tonal harmony, which organize music around a key and govern how chords and melodies interact.
"""
page2 = """
"""
image = ""

imageSize = 100
titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Functional Harmony basics (Tonal Harmony)"
page = """
Before diving into diatonic harmonization, let's first focus on the individual diatonic pitches. For now, we’ll concentrate solely on the regular diatonic scale, excluding the chromatic scale. The diatonic scale is characterized by a specific interval formula: WWHWWWH (whole step, whole step, half step, whole step, whole step, whole step, half step). This pattern begins from the tonic and concludes on the next tonic, an octave above.
"""
page2 = """
"""
image = ""
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Functional Harmony basics (Tonal Harmony)"
page = """
If we take this formula (WWHWWWH), we see that it formalizes the following intervals: Tonic, Major 2nd, Major 3rd, Perfect 4th, Perfect 5th, Major 6th, Major 7th, and Tonic (octave). Excluded from this pattern are: minor 2nd, minor 3rd, diminished 5th, minor 6th, and minor 7th.
The seven notes in this diatonic pattern are not all equal in function; they have distinct roles and purposes in relation to the tonic, with the half steps playing a particularly significant role in shaping the scale's character.
"""
image = ""
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Chord Progressions"
page = """
"""
page2 = """
"""
image = ""
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Cadences"
page = """
"""
page2 = """
"""
image = ""
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)


title = "Voice Leading"
page = """
"""
page2 = """
"""
image = ""
imageSize = 100

titles.append(title)
pages.append(page)
images.append(image)
imagesSize.append(imageSize)
sub_pages.append(page2)



tenssions_carousel_data = []
for i in range(len(titles)):
    dt = {
        "title": titles[i],
        "content":pages[i],
        "page_number": i+1
    }

    if images[i] != "":
        dt["image"] = images[i]
        dt["image_size"] = imagesSize[i]
    
    if sub_pages[i] != "":
        dt["content2"] = sub_pages[i]
    tenssions_carousel_data.append(dt)



