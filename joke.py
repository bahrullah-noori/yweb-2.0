import random

def github_jokes():
    jokes = [
        "Why did the programmer quit GitHub? Because they couldn't handle the merge conflicts!",
        "Why did the repo bring a ladder to GitHub? To reach the top branch!",
        "Why do developers love GitHub? It's where all the *pull* happens!",
        "I tried to fork a repository yesterday... but it said, 'No spoons allowed!'",
        "Why was the GitHub issue so talkative? Because it had so many comments!",
        "Why did the file cross the road? To get committed on the other side!",
        "GitHub is like a gym membership. Everyone has it, but only a few actually *push* themselves!"
    ]

    # Select a random joke
    joke = random.choice(jokes)
    return joke

# Run the program
if __name__ == "__main__":
    print("Welcome to the GitHub Joke Generator!")
    print("Here's a joke for you:")
    print(github_jokes())

Welcome to the GitHub Joke Generator!
Here's a joke for you:
Why do developers love GitHub? It's where all the *pull* happens!

