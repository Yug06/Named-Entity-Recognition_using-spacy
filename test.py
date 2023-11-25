# import spacy

# nlp = spacy.load("D:/chat/demo/en_core_web_lg-3.7.1/en_core_web_lg/en_core_web_lg-3.7.1/")

# # Example text for Named Entity Recognition (NER)
# text = "My Name is Mohit.I am from Delhi."

# # Process the text with spaCy NLP pipeline
# doc = nlp(text)

# # Extract named entities
# for ent in doc.ents:
#     print(f"Entity: {ent.text}, Label: {ent.label_}")


from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load("D:/chat/demo/en_core_web_lg-3.7.1/en_core_web_lg/en_core_web_lg-3.7.1/")

@app.route('/api/ner', methods=['POST'])
def extract_entities():
    data = request.get_json()
    text = data['text']
    doc = nlp(text)
    entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents if ent.label_ == "PERSON"]
    return jsonify(entities)

if __name__ == '__main__':
    app.run(debug=True)
