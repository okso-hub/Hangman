# Hangman

This program creates the game *Hangman* in the terminal. To launch it, direct to the directory where the `main.py` file is stored and enter the following command:

```
python3 main.py
```

Now you will be asked to enter the word which should be guessed. Let's take *pineapple* as an example.

```
Enter the word which should be guessed: pineapple
```

Now the screen clears and you enter the mode where you guess the characters of the word.

```
 []
_________ length: 9
Enter character: 
```

Each wrong character will be stored inside of the list you see in the first line. After six wrong guesses, you lose:

```
You were wrong! ['q', 'w', 'r', 't', 'z']
_________ length: 9
Enter character: u
You guessed 6 times which is too much!
```

Each right character will be added to the hidden phrase. If you guessed everything without exceeding 6 misses, you win:

```
You were right! []
pineappl_ length: 9
Enter character: e
The solution is pineapple!
You won the game!
```
