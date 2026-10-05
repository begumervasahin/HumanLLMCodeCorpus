from flask import Flask, request, render_template
import re
import math
app = Flask("__name__")
universal_set_of_unique_words = []
@app.route("/")
def load_page():
    return render_template('index.html', query="")
@app.route("/", methods=['POST'])
def cosine_similarity():
    try:
        global universal_set_of_unique_words
        input_query = request.form['query']
        lowercase_query = input_query.lower()
        query_word_list = re.sub("[^\w]", " ", lowercase_query).split()
        for word in query_word_list:
            if word not in universal_set_of_unique_words:
                universal_set_of_unique_words.append(word)
        with open("database1.txt", "r") as file:
            database_text = file.read().lower()
            database_word_list = re.sub("[^\w]", " ", database_text).split()
            for word in database_word_list:
                if word not in universal_set_of_unique_words:
                    universal_set_of_unique_words.append(word)
        query_tf = []
        database_tf = []
        for word in universal_set_of_unique_words:
            query_tf_counter = query_word_list.count(word)
            query_tf.append(query_tf_counter)
            database_tf_counter = database_word_list.count(word)
            database_tf.append(database_tf_counter)
        dot_product = sum(query_tf[i] * database_tf[i] for i in range(len(query_tf)))
        query_vector_magnitude = math.sqrt(sum(tf ** 2 for tf in query_tf))
        database_vector_magnitude = math.sqrt(sum(tf ** 2 for tf in database_tf)))
        match_percentage = (dot_product / (query_vector_magnitude * database_vector_magnitude)) * 100
        output = f"Input query text matches {match_percentage:.02f}% with database."
        return render_template('index.html', query=input_query, output=output)
    except Exception as e:
        output = "Please Enter Valid Data"
        return render_template('index.html', query=input_query, output=output)
if __name__ == "__main__":
    app.run()