import requests

headers = {
    "X-RapidAPI-Key": "6820df4fa1msh8d0d92b4378c66ep1f564ajsn3449bd715661",
    "X-RapidAPI-Host": "youtube138.p.rapidapi.com"
}

"""
link to the YouTube API: https://rapidapi.com/Glavier/api/youtube138/pricing
The key from free subsciption, need to change to Pro or Ultra subscription
"""

class Youtube():
    def get_channel(self, channel_id, limit):
        url = "https://youtube138.p.rapidapi.com/channel/details/"
        url_for_videos = "https://youtube138.p.rapidapi.com/channel/videos/"
        querystring = {"id":channel_id,"hl":"en","gl":"US"}
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        video_response = requests.request("GET", url_for_videos, headers=headers, params=querystring).json()['contents']
        channel_videos = []
        for video in video_response:
            if limit == 0:
                break
            vid = {
                'video_name': video['video']['title'],
                'video_id': video['video']['videoId']
            }
            channel_videos.append(vid)
            limit -=1

        channel_info = {
            'channel_id': response['channelId'],
            'name': response['title'],
            'created_date': response['joinedDate'],
            'description': response['description'],
            'subscribers' : response['stats']['subscribers'],
            'views': response['stats']['views'],
            'keywords' : response['keywords'],
            'photo' : response['avatar'][2]['url'],
            'videos' : channel_videos
        }
        print(len(channel_videos))
        return channel_info

    def get_video(self, video_id):
        url = "https://youtube138.p.rapidapi.com/video/details/"
        querystring = {"id":video_id,"hl":"en","gl":"US"}
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        video_detail = {
            'video_id' : response['videoId'],
            'title' : response['title'],
            'published_date' : response['publishedDate'],
            'description' : response['description'],
            'category' : response['category'],
            'views' : response['stats']['views'],
            'likes' : response['stats']['likes'],
            'comments' :response['stats']['comments'],
            'length' : response['lengthSeconds'],
            'keywords' : response['keywords']
        }
        return video_detail

    def get_comments(self, video_id, limit):
        url = "https://youtube138.p.rapidapi.com/video/comments/"
        querystring = {"id":video_id,"hl":"en","gl":"US"}
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        comments = response['comments']
        comments_info = []
        for comment in comments:
            if limit == 0:
                break
            com = {
                'author_name' : comment['author']['title'],
                'author_id' : comment['author']['channelId'],
                'text' : comment['content'],
                'likes': comment['stats']['votes'],
                'replies': comment['stats']['replies'],
                'published_time' : comment['publishedTimeText'],
            }
            comments_info.append(com)
            limit-=1
        return comments_info
        