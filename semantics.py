import spacy

# Interesting notes about the similarities between the words monkey, banana and apple.
# Cat and monkey seem to be similar because they are both animals.
# Apple and banana have a similarity of around 0.584.. because they are both fruits.

nlp_sm = spacy.load('en_core_web_sm')
nlp_md = spacy.load('en_core_web_md')

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"
]

print('Sentence to compare:\n' + sentence_to_compare)

print("\n-----MD Test-----\n")

# Similarity test with en_core_web_sm
model_sentence = nlp_sm(sentence_to_compare)

for sentence in sentences:
    similarity = nlp_sm(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

print("\n\n-----MD Test-----\n")

# Similarity test with en_core_web_md
model_sentence = nlp_md(sentence_to_compare)

for sentence in sentences:
    similarity = nlp_md(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)