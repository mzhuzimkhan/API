import requests
headers = {
    "X-RapidAPI-Key": "6820df4fa1msh8d0d92b4378c66ep1f564ajsn3449bd715661",
    "X-RapidAPI-Host": "twitter154.p.rapidapi.com"
}

"""
link to the Twitter api: https://rapidapi.com/omarmhaimdat/api/twitter154/pricing
The key from free subsciption, need to change to pro subscription
"""

class Twitter():
    def get_user(self, username):
        url = "https://twitter154.p.rapidapi.com/user/details"
        querystring = {"username":username}
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        user_info = {
            'id': response['user_id'],
            'username' : response['username'],
            'name' : response['name'],
            'description' : response['description'],
            'creation_date' : response['creation_date'],
            'timestamp' : response['timestamp'],
            'number_of_tweets' : response['number_of_tweets'],
            'follower_count' : response['follower_count'],
            'following_count' :response['following_count'],
            'is_private' : response['is_private'],
            'profile_picture' : response['profile_pic_url'],
            'location' : response['location'],
            'url' : response['external_url']
        }
        return user_info
    
    def get_tweets(self, username, limit):
        url = "https://twitter154.p.rapidapi.com/user/tweets"
        limit+=1
        querystring = {"username":username,"limit":limit}
        responses = requests.request("GET", url, headers=headers, params=querystring).json()['results']
        users_tweet = []
        for response in responses:
            contents = []
            media = response['media_url']
            if media != None:
                for med in media:
                    contents.append(med)
            user_tweet = {
                'id' : response['tweet_id'],
                'text' : response['text'],
                'creation_date' : response['creation_date'],
                'timestamp' : response['timestamp'],
                'like_count' : response['favorite_count'],
                'comment_count' : response['reply_count'],
                'retweet_count': response['retweet_count'],
                'retweets_with_responses' : response['quote_count'],
                'video_view_count' : response['video_view_count'],
                'contents' : contents,
            }
            users_tweet.append(user_tweet)
        return users_tweet
    
    def get_tweet_replies(self, tweet_id):
        url = "https://twitter154.p.rapidapi.com/tweet/replies"
        querystring = {"tweet_id":tweet_id}
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        replies = response['replies']
        replies_info = []
        for reply in replies:
            reply_info ={
                'id' : reply['tweet_id'],
                'creation_date' : reply['creation_date'],
                'text' : reply['text'],
                'username': reply['user']['username'],
                'likes_count' :reply['favorite_count'],
                'comment_count' : reply['reply_count'],
                'retweet_count' :reply['retweet_count'],
                'retweet_with_responses' : reply['quote_count']
            }
            replies_info.append(reply_info)
        return replies_info
    