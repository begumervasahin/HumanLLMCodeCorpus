import nltk
import json
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
def extract_activities(data):
    return [activity['object']['content'].lower().split() for activity in data if activity['object']['content'] != '']
def calculate_activity_scores(activities, query_terms, text_collection):
    relevant_activities = []
    for activity_index, activity_content in enumerate(activities):
        score = sum(text_collection.tf_idf(term.lower(), activity_content) for term in query_terms)
        if score > 0:
            relevant_activities.append({
                'score': score,
                'title': data[activity_index]['title'],
                'url': data[activity_index]['url']
            })
    return relevant_activities
def print_relevant_activities(relevant_activities):
    for activity in relevant_activities:
        print('Title:', activity['title'])
        print('URL:', activity['url'])
        print('Score:', activity['score'])
        print()
def main():
    json_file_path = '[change to your googleplus_posts.json location]'
    data = load_json(json_file_path)
    query_terms = ['mobile']
    activities = extract_activities(data)
    text_collection = nltk.TextCollection(activities)
    relevant_activities = calculate_activity_scores(activities, query_terms, text_collection)
    relevant_activities.sort(key=lambda activity: activity['score'], reverse=True)
    print_relevant_activities(relevant_activities)
if __name__ == '__main__':
    main()