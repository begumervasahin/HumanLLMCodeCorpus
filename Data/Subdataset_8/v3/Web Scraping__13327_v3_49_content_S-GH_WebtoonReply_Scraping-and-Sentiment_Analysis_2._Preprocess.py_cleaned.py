import pandas as pd
def main():
    star_info_path = 'path/to/weebtoon_star_info.csv'
    reply_info_path = 'path/to/weebtoon_reply_info.csv'
    star_info_df = pd.read_csv(star_info_path)
    reply_info_df = pd.read_csv(reply_info_path)
    reply_info_df.drop(columns=['Unnamed: 0'], inplace=True)
    comments_list = [[] for _ in range(10)]
    low_rated_webtoons = process_webtoons(star_info_df, reply_info_df, 1000, 9.99)
    save_to_csv(low_rated_webtoons, "./lowstar_reply.csv")
    high_rated_webtoons = process_webtoons(star_info_df, reply_info_df, 1000, 9.99)
    save_to_csv(high_rated_webtoons, "./highstar_reply.csv")
def process_webtoons(star_info_df, reply_info_df, num_webtoons, star_threshold):
    sorted_star_info = star_info_df.sort_values(by='star_point', axis=0)
    selected_webtoons = sorted_star_info[:num_webtoons].drop_duplicates(["titleId", "nom"], keep='first')
    titleIds = list(selected_webtoons['titleId'])
    noms = list(selected_webtoons['nom'])
    comments_list = [[] for _ in range(10)]
    for i in range(len(titleIds)):
        filtered_reply_df = reply_info_df[reply_info_df['titleId'].isin([f'{titleIds[i]}'])]
        relevant_replies = filtered_reply_df[filtered_reply_df['nom'].isin([f'{noms[i]}'])]
        for j in range(1, 11):
            try:
                comments_list[j - 1].append(str(relevant_replies[f'comment{j}'].values[0]))
            except:
                comments_list[j - 1].append('')
                pass
    for i in range(10):
        selected_webtoons[f'comment{i+1}'] = comments_list[i]
    empty_comment_rows = selected_webtoons[selected_webtoons['comment1']==''].index
    selected_webtoons = selected_webtoons.drop(empty_comment_rows)
    selected_webtoons = selected_webtoons[:500 - len(selected_webtoons)]
    return selected_webtoons
def save_to_csv(dataframe, filename):
    dataframe.to_csv(filename, encoding="utf_8_sig", mode='w', index=False)
if __name__ == "__main__":
    main()