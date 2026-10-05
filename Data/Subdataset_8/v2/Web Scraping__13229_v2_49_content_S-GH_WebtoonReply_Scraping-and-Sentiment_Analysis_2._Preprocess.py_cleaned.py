import pandas as pd
def main():
    star_info_path = 'path/to/weebtoon_star_info.csv'
    reply_info_path = 'path/to/weebtoon_reply_info.csv'
    star_info_df = pd.read_csv(star_info_path)
    reply_info_df = pd.read_csv(reply_info_path)
    del reply_info_df['Unnamed: 0']
    comments_list = [[] for _ in range(10)]
    sorted_star_info = star_info_df.sort_values(by='star_point', axis=0)
    low_rated_webtoons = sorted_star_info[:1000].drop_duplicates(["titleId", "nom"], keep='first')
    low_titleIds = list(low_rated_webtoons['titleId'])
    low_noms = list(low_rated_webtoons['nom'])
    for i in range(len(low_titleIds)):
        filtered_reply_df = reply_info_df[reply_info_df['titleId'].isin([f'{low_titleIds[i]}'])]
        relevant_replies = filtered_reply_df[filtered_reply_df['nom'].isin([f'{low_noms[i]}'])]
        for j in range(1, 11):
            try:
                comments_list[j - 1].append(str(relevant_replies[f'comment{j}'].values[0]))
            except:
                comments_list[j - 1].append('')
                pass
    for i in range(10):
        low_rated_webtoons[f'comment{i+1}'] = comments_list[i]
    empty_comment_rows = low_rated_webtoons[low_rated_webtoons['comment1']==''].index
    low_rated_webtoons = low_rated_webtoons.drop(empty_comment_rows)
    low_rated_webtoons = low_rated_webtoons[:500 - len(low_rated_webtoons)]
    low_rated_webtoons.to_csv("./lowstar_reply.csv", encoding="utf_8_sig", mode='w', index=False)
    high_rated_webtoons = star_info_df[star_info_df['star_point'].isin([9.99])].sample(n=1000).drop_duplicates(["titleId", "nom"], keep='first')
    comments_list = [[] for _ in range(10)]
    high_titleIds = list(high_rated_webtoons['titleId'])
    high_noms = list(high_rated_webtoons['nom'])
    for i in range(len(high_titleIds)):
        filtered_reply_df = reply_info_df[reply_info_df['titleId'].isin([f'{high_titleIds[i]}'])]
        relevant_replies = filtered_reply_df[filtered_reply_df['nom'].isin([f'{high_noms[i]}'])]
        for j in range(1, 11):
            try:
                comments_list[j - 1].append(str(relevant_replies[f'comment{j}'].values[0]))
            except:
                comments_list[j - 1].append('')
                pass
    for i in range(10):
        high_rated_webtoons[f'comment{i+1}'] = comments_list[i]
    empty_comment_rows = high_rated_webtoons[high_rated_webtoons['comment1']==''].index
    high_rated_webtoons = high_rated_webtoons.drop(empty_comment_rows)
    high_rated_webtoons = high_rated_webtoons[:500 - len(high_rated_webtoons)]
    high_rated_webtoons.to_csv("./highstar_reply.csv", encoding="utf_8_sig", mode='w', index=False)
if __name__ == "__main__":
    main()