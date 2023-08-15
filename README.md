# wordle-solver
 The main goal of this project was to find an efficient way to solve Wordle puzles using python


Example:

**_1. Starts by asking you to enter your word_**

```
Some good starter words are: adieu, audio, or canoe

Enter your word: **audio**
```
**_2. Asks you to enter what the feedback from the game was_**


```
g - green, y - yellow, w - wrong/grey

Feedback: wwgyw
```
**_3. Gives a list of every possible word that could be the solution and keeps going until the game is over_**

```
biddy, bided, bider, bides, bidet, bidri, cided, cider, 

cides, diddy, didst, eider, fides, fidge, giddy, hided, 

hider, hides, indew, index, indri, kiddy, kidel, kidge, 

middy, midge, midgy, midst, nided, nides, rider, rides, 

ridge, ridgy, sided, sider, sides, sidey, sidhe, sidle, 

tiddy, tided, tides, widdy, widen, wider, wides, width, 

Enter your word: midst

Feedback: wygww

indew, index, indri, Enter your word: index

g - green, y - yellow, w - wrong/grey

Feedback: ggggg

Well done!
```

**_This led to us getting to the correct word - index_**



