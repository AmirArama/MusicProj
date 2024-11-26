page1 = """
As I began working on this page, my initial goal was to clarify music theory concepts for myself 
and organize them in a way that finally made sense. I realized that by developing this site's content,
 I could gain a deeper understanding of music theory while also sharing what I’ve learned. My aim here 
 is to make things as simple and straightforward as possible. I intend to explore modes,
   chord progressions, and the circle of fifths in a way that’s approachable and engaging.
     I will try to demystify these ideas and make music theory something we can truly understand and enjoy!"""

page2 = """
Modes are permutations of other scales. If we take the key of C as an example, 
starting from the C major scale, and begin with the first interval (scale degree one), 
we get the C major scale, also known as the C Ionian mode. 
By playing this same pattern but beginning on the second note, or the second scale degree, D, 
we create the Dorian mode. This means we’re still using the exact same notes from the C major scale, 
but the starting point has shifted, altering the sequence of intervals."""


page3 = """
Continuing this pattern, if we start on the third degree, E, 
we derive the Phrygian mode. Similarly, beginning on F (the fourth degree) 
produces the Lydian mode, starting on G (the fifth degree) gives us the Mixolydian mode, 
A (the sixth degree) forms the Aeolian mode, and B (the seventh degree) leads to the Locrian mode.
Each mode retains the notes of the C major scale but shifts the tonal center, creating a unique
sequence of whole steps and half steps."""

page3 = page3 + """
This approach of rearranging the same scale highlights how modes are interconnected
and emphasizes their mathematical structure. Understanding this allows us to
derive all seven modes from any key, revealing the deeper relationships within the scale system."""

page4 = "Mode diagrame"
page4Image = "\static\images\modes\modes_diagram_transparent.png"
page4imageSize = 50

page5 = "Mode diagrame shifted"
page5Image = "\static\images\modes\modes_diagram_shifted.png"
page5imageSize = 60

page6 = "Mode diagrame shifted"
page6Image = "\static\images\modes\modes_diagram_shifted_WH.png"
page6imageSize = 60

page7 = """
A Personal Reflection
It took me some time to fully grasp what modes are and how to harmonize them. But now that it has finally clicked for me, I feel confident in trying to simplify it for anyone reading this.
"""

page8 = """
In Western music, scales pick up sharps or flats based on the relationship between the intervals of the major scale and how they are imposed on different roots. For example, if we apply the formula of WWHWWWH (Whole-Whole-Half-Whole-Whole-Whole-Half) to the A as the root, while maintaining the order of the notes A-B-C-D-E-F-G, we immediately notice the introduction of three sharps (F#, C#, and G#) to preserve the pattern of the major scale. This principle forms the foundation of the Circle of Fifths, which organizes the addition of sharps as we move clockwise and flats as we move counterclockwise.
"""

page9 = """
Modes, however, follow an intriguing pattern. While they adhere to the same formula of whole and half steps as their parent major scale, they “undo” or “revert” the sharps or flats introduced by their relative major scale. For example, A Aeolian is built from the C major scale, so it reverts the three sharps introduced by the A major scale. These reversions are represented as three flats in the A Aeolian chord degrees. Another example is F Lydian: since F major introduces one flat and C major (its parent scale) removes it, F Lydian ends up with one sharp.
The number of sharps or flats in a mode is related to the parallel major scale of that mode!
"""

page10 = """
"As long as you know the sharps or flats of the parent major scale (from the Circle of Fifths), you can determine the sharps or flats in any mode by understanding its structure relative to the parent scale. Specifically, a mode will 'revert' or adjust the sharps or flats introduced by its parent scale to align with the interval pattern unique to that mode."
D Mixolydian - is actualy G major with F#. Its relative D major has F# and C# (in the 7th position) - So again we get a flat 7th by reverting this 7th
As long as you remember this you will always end up with the same degrees formula for each mode.
"""
page10Image = "\static\images\modes\modes_diagram_shifted_deg.png"
page10imageSize = 60

page11 = """
The formula-based approach: To systematically modify the chords of the parallel major scale 
to match the mode's structure. This involves adjusting the chord types (major, minor, diminished) 
based on the scale degrees altered by the mode. To constract G Dorian, simply take G Major i.e., G major, A minor, B minor, C major, D major, E minor, F# diminished.
Apply the formula of the Dorian mode: i, ii, ♭III, IV, v, vi°, ♭VII on it. First alter the chords of the major scale accordingly this will give: 
G minor, A minor, B major, C major, D minor, E diminisged, F# major. Now lower the 3rd anf the 7th degrees to finaly get the G dorian: 
G minor, A minor, Bb major, C major, D minor, E diminisged, F major.
"""

page12 = """
The modal circle of fifths is an incredibly intuitive tool that I use to visualize and understand musical concepts more easily. The inner ring represents the roots of the C major scale (or any mode derived from it). This enhanced version of the circle of fifths provides a comprehensive view of scales, modes, the number of flats or sharps, and the harmonization of each mode—all at a glance. Once you grasp how to interpret it, this tool becomes invaluable for navigating music theory in a clear and organized manner."""


page13 = """
Within a harmonized major scale (Ionian mode), the inner green ring represents the three major chords of the harmonized scale. At the center is the I degree (tonic), to the left is the IV degree (subdominant), and to the right is the V degree (dominant). Moving outward, the blue ring represents the three minor chords: at the center is the vi degree (Aeolian), to the left is the ii degree (Dorian), and to the right is the iii degree (Phrygian). Finally, the red ring represents the vii° diminished chord.

As discussed earlier, starting a scale from any of these positions forms the modes derived from the major root. The green ring holds Lydian, Ionian, and Mixolydian, in that order. The blue ring holds Dorian, Aeolian, and Phrygian, and the red ring contains the root for the Locrian mode. The way you shift the notes around the root chord in each colored space forms the harmonization of that mode.

This visualization clearly demonstrates that while the modes are built on the same set of chords, their arrangement and tonal focus differ. And yet, this tool offers even more insights beyond just the harmonization of modes..."""

page14 = """
Within each Ionian (center green), the structure of this enhanced Circle of Fifths allows you to determine the number of flats or sharps, just as with the classical Circle of Fifths. Moving clockwise, sharps are added, while moving counterclockwise, flats are introduced. By focusing on the highlighted colored section surrounding a root, you can easily count the number of flats or sharps and identify which degrees of the scale or harmonized scale contain them. This visualization makes it intuitive to track their placement across the modes and harmonized chords.
As one can see, C major (and its harmonized Ionian mode) has no sharps or flats. Moving to G major, we add one sharp, F, which becomes F# diminished. Progressing to D major, we add another sharp, C#, which forms the C# diminished chord. Meanwhile, F# shifts to the minor iii position as the circle rotates, maintaining the logical progression of sharps and their placement within the harmonized scale. Still more to come ..."""

page15 = """
One fascinating observation in this arrangement is that each root note of a specific key, highlighted in red, appears exactly three times. This symmetry reflects the structure of the chromatic scale in Western music, which consists of 12 notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B. Multiplying these 12 notes by 3 gives us the 36 elements that form this circle.

In terms of modes, we observe 3 major modes, 3 minor modes, and 1 diminished mode for each root note. By examining the three highlighted red notes for a given key, we can identify the Ionian mode that serves as the parent scale for each mode derived from that root.

Taking C as an example:

C appears as part of F Ionian because it sits to the right of F in the circle, making it the C Mixolydian mode of F major.
C is also to the left of G Ionian, meaning it serves as the C Lydian mode of G major.
Finally, C sits at the center of the C Ionian mode, forming the foundation of C major.
Similarly, for C minor:

C minor sits to the left of Bb Ionian, making it the C Dorian mode of Bb major.
It is to the right of Ab Ionian, identifying it as the C Phrygian mode of Ab major.
It aligns directly above Eb Ionian, where it functions as the C Aeolian mode of Eb major.
For C diminished, it aligns directly above Db Ionian, making it the C Locrian mode of Db major.

This elegant arrangement not only highlights the relationships between modes and their parent scales but also emphasizes the symmetry inherent in the Western chromatic system.
"""

page16 = """
In the Circle of Fifths (also known as the Circle of Fourths when moving counterclockwise), sharps are added to the 7th degree moving clockwise, and flats to the 4th degree moving counterclockwise, to preserve the WWHWWWH interval structure of the major scale. The 7th degree sharpens to maintain a whole step before the tonic, while the 4th degree flattens to maintain a half step between the 3rd and 4th degrees. This dual-directional nature highlights the symmetry and utility of the circle, allowing it to seamlessly represent relationships in both sharps and flats.
I am done explaining the Modal Circle of Fifths. Please use the dropdown menu to shift the highlighted space to explore a different key. Investigate the central modes of this key and how they relate to other modes as previously explained. For each mode, examine how it is harmonized and analyze the chord colors that emerge, shedding light on how each mode contributes to the unique character of the key. Happy exploring!
"""


