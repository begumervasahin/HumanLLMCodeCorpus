import nltk
import json
def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
def preprocess_activities(data):
    return [activity['object']['content'].lower().split() for activity in data if activity['object']['content'] != '']
def calculate_tf_idf(activities, query_terms):
    tc = nltk.TextCollection(activities)
    relevant_activities = []
    for i, activity in enumerate(activities):
        score = sum(tc.tf_idf(term.lower(), activity) for term in query_terms)
        if score > 0:
            relevant_activities.append({
                'score': score,
                'title': data[i]['title'],
                'url': data[i]['url']
            })
    return sorted(relevant_activities, key=lambda a: a['score'], reverse=True)
def print_relevant_activities(relevant_activities):
    for ra in relevant_activities:
        print('Title:', ra['title'])
        print('URL:', ra['url'])
        print('Score:', ra['score'])
        print()
def main():
    file_path = '[change to your googleplus_posts.json location]'
    data = load_data(file_path)
    QUERY_TERMS = ['mobile']
    activities = preprocess_activities(data)
    relevant_activities = calculate_tf_idf(activities, QUERY_TERMS)
    print_relevant_activities(relevant_activities)
if __name__ == '__main__':
    main()