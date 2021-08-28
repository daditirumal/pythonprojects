"""Generate funny names by randomly combining names from 2 seperate lists."""
import sys
import random

def main():
    """choose names at random from 2 tuples of names and print to screen."""
    print("welcome to the psych 'Sidekick name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ('Baby oil', 'Bad News', 'Big Burps', 'Bill',
             'Beenie-Weenie', "Bob 'Stinkbug")
    last = ('Appleyard','Bigmeat', 'Bloominshine',
            'Clovenhoof', 'Clutterbuck', 'Cocktoasten')

    while True:
        firstname = random.choice(first)
        lastname = random.choice(last)

        print("\n\n")
        #Trick IDLE by using "fatal error" setting to print namw in red.
        print("{} {}".format(firstname, lastname), file=sys.stderr)
        print("\n\n")
        try_again = input("\n\nTry again? (press Enter else n to quit)\n")
        if try_again.lower == "n":
            break

    input ("\n press Enter to exit")


if __name__ == "__main__":
    main()
    """calling main function
    """
