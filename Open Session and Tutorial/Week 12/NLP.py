import spacy
import matplotlib.pyplot as plt

from textblob import TextBlob
from wordcloud import WordCloud
from collections import defaultdict

nlp = spacy.load('en_core_web_lg')

sentences = [
    "I love this product. It works great and has made my life so much easier!",
    "This is the worst movie I have ever seen. Completely disappointed.",
    "What a fantastic experience! Truly memorable and enjoyable.",
    "I'm so sad this vacation is over, it was terrible from start to finish.",
    "The customer service was amazing and very helpful.",
    "The food was bland and I'm unhappy with the service.",
    "Absolutely a joy to use. I'm very satisfied with the performance."
]

positive_words = defaultdict(int)
negative_words = defaultdict(int)

for sentence in sentences:

    doc = nlp(sentence)
    tokens = [token.lemma_.lower().strip() for token in doc if not token.is_stop and token.is_alpha]
    for token in tokens:
        blob = TextBlob(str(token))

        polarity = blob.sentiment.polarity

        if polarity > 0:
            positive_words[token.lower()] += 1
        elif polarity < 0:
            negative_words[token.lower()] += 1

pos_wordcloud = WordCloud(width=400, height=200, background_color ='white').generate_from_frequencies(positive_words)
neg_wordcloud = WordCloud(width=400, height=200, background_color ='white').generate_from_frequencies(negative_words)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(pos_wordcloud, interpolation='bilinear')
ax[0].set_title('Positive Words')
ax[0].axis('off')

ax[1].imshow(neg_wordcloud, interpolation='bilinear')
ax[1].set_title('Negative Words')
ax[1].axis('off')

plt.show()