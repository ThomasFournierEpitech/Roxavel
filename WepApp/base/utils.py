import os

def parseListSummonerName(str):
    myfilter = [" à rejoin la partie.", " joined the room"]
    splited = str.split(os.linesep)
    cleaned = list(filter(lambda x : x != '', splited)) # fastest
    count = 0
    for string in cleaned:
        tmp = string
        for sep in myfilter:
            tmp = tmp.split(sep)[0]
        cleaned[count] = "".join(tmp)
        count += 1
    return cleaned
