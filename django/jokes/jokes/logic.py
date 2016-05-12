joke_setups = []
joke_punchlines = []
jokes = []

def save_setup(setup):
    joke_setups.append(setup)

def save_punchline(punchline):
    joke_punchlines.append(punchline)

def save_joke(setup, punchline):
    jokes.append({"setup": setup, "punchline": punchline})

def get_all_jokes():
    return jokes
