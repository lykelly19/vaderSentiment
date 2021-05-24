import sys
import pandas as pd
from nrclex import NRCLex

fear = []
anger = []
anticipation = []
trust = []
surprise = []
sadness = []
disgust = []
joy = []

df = pd.read_csv(sys.argv[1])
sentences = df['tweet_text'].to_list()

for sentence in sentences:
    text_object = NRCLex(sentence)

    try:
        fear.append(text_object.raw_emotion_scores['fear'])
    except:
        fear.append(0)

    try:
        anger.append(text_object.raw_emotion_scores['anger'])
    except:
        anger.append(0)

    try:
        anticipation.append(text_object.raw_emotion_scores['anticipation'])
    except:
        anticipation.append(0)

    try:
        trust.append(text_object.raw_emotion_scores['trust'])
    except:
        trust.append(0)

    try:
        surprise.append(text_object.raw_emotion_scores['surprise'])
    except:
        surprise.append(0)

    try:
        sadness.append(text_object.raw_emotion_scores['sadness'])
    except:
        sadness.append(0)

    try:
        disgust.append(text_object.raw_emotion_scores['disgust'])
    except:
        disgust.append(0)

    try:
        joy.append(text_object.raw_emotion_scores['joy'])
    except:
        joy.append(0)

    print(text_object.affect_dict)


df['fear'] = fear
df['anger'] = anger
df['anticipation'] = anticipation
df['trust'] = trust
df['surprise'] = surprise
df['sadness'] = sadness
df['disgust'] = disgust
df['joy'] = joy

df.to_csv(sys.argv[2])
