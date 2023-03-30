def final_series(results):
    scores = [0, 0]
    for game in results:
        scores[0] += game[0] > game[1]
        scores[1] += game[1] > game[0]
        if scores[0] == 4 or scores[1] == 4:
            break
    if scores[0] > scores[1]:
        return "Team A won with a score of {}-{}".format(scores[0], scores[1])
    else:
        return "Team B won with a score of {}-{}".format(scores[1], scores[0])
