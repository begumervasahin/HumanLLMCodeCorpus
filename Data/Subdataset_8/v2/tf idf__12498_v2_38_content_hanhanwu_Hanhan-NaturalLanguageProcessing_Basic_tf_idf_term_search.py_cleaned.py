import nltk
import json
def main():
    file_path = '[change to your googleplus_posts.json location]'
    with open(file_path, 'r') as file:
        data = json.load(file)
    QUERY_TERMS = ['mobile']
    activities = [activity['object']['content'].lower().split() for activity in data if activity['object']['content'] != '']
    tc = nltk.TextCollection(activities)
    relevant_activities = []
    for i in range(len(activities)):
        score = 0
        for term in QUERY_TERMS:
            score += tc.tf_idf(term.lower(), activities[i])
        if score > 0:
            relevant_activities.append({
                'score': score,
                'title': data[i]['title'],
                'url': data[i]['url']
            })
    relevant_activities = sorted(relevant_activities, key=lambda a: a['score'], reverse=True)
    for ra in relevant_activities:
        print('Title:', ra['title'])
        print('URL:', ra['url'])
        print('Score:', ra['score'])
        print()
if __name__ == '__main__':
    main()