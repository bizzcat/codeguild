votes = {
    "chocolate": 1,
    "vanilla": 1,
    "strawberry": 1,
}


def save_vote(flavor):
    votes[flavor] += 1

def get_total_votes():
    return (votes["chocolate"] + votes["vanilla"] + votes["strawberry"])

def convert_to_percentages():
    vote_percentages = {}

    chocolate_average = str( ( votes["chocolate"] / get_total_votes() ) * 100 ) + "%  " + "  ( " + str(votes["chocolate"]) + " )"
    vote_percentages["chocolate"] = chocolate_average

    vanilla_average = str( ( votes["vanilla"] / get_total_votes() ) * 100 ) + "%  " + "  ( " + str(votes["vanilla"]) + " )"
    vote_percentages["vanilla"] = vanilla_average

    strawberry_average = str( ( votes["strawberry"] / get_total_votes() ) * 100 ) + "%  " + "  ( " + str(votes["strawberry"]) + " )"
    vote_percentages["strawberry"] = strawberry_average

    return vote_percentages


















#
