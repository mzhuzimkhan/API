import requests
headers = {
    "X-RapidAPI-Key": "6820df4fa1msh8d0d92b4378c66ep1f564ajsn3449bd715661",
    "X-RapidAPI-Host": "instagram188.p.rapidapi.com"
}

"""
link to the Instagram API: https://rapidapi.com/ahmetarpaci/api/instagram188/pricing
The key from free subsciption, need to change to Pro or Ultra subscription
"""

class Instagram():
    def get_user(self, user_name):
        url = f"https://instagram188.p.rapidapi.com/userinfo/{user_name}"
        response = requests.request("GET", url, headers=headers).json()
        is_succes = response['success']
        if is_succes == False:
            return response['data']
        if is_succes == True:
            response = response['data']
            user_posts = []
            user_media = response['edge_owner_to_timeline_media']['edges']
            limit = 10
            for shortcode in user_media:
                if limit == 0:
                    break
                user_posts.append({'shortcode':shortcode['node']['shortcode']})
                limit-=1
            user_info = {
                'biography': response['biography'],
                'url': response['external_url'],
                'followers': response['edge_followed_by']['count'],
                'follows' : response['edge_follow']['count'],
                'full_name' : response['full_name'],
                'id' : response['id'],
                'category' : response['category_enum'],
                'profile_picture': response['profile_pic_url_hd'],
                'username' : response['username'],
                'videos_count' : response['edge_felix_video_timeline']['count'],
                'media_count' : response['edge_owner_to_timeline_media']['count'],
                'is_private' : response['is_private'],
                'user_posts' : user_posts
            }
            return user_info

    def get_posts(self, shortcode):
        url = f"https://instagram188.p.rapidapi.com/postinfo/{shortcode}"
        response = requests.request("GET", url, headers=headers).json()
        is_succes = response['success']
        if is_succes == False:
            return response['data']
        if is_succes == True:
            response = response['data']
            if 'location' in response:
                user_location = {
                    'name' : response['location']['name'],
                    'address' : response['location']['address'],
                    'latitude' : response['location']['lat'],
                    'longitude' : response['location']['lng']
                }
            else: 
                user_location = {}
            
            if 'usertags' in response:
                user_tags = []
                for i in response['usertags']['in']:
                    user_tags.append({'username' : i['user']['username']})
            else:
                user_tags = []
            user_content = []
            if response['product_type'] == 'carousel_container':
                for i in response['carousel_media']:
                    user_content.append({'content':i['image_versions2']['candidates'][0]['url']})
            if response['product_type'] == 'feed':
                user_content.append({'content' : response['image_versions2']['candidates'][0]['url']})
            if response['product_type'] == 'igtv':
                user_content.append({'content' : response['video_versions'][0]['url']})
            post_info = {
                'username' : response['user']['username'],
                'post_type' : response['product_type'],
                'text' : response['caption']['text'],
                'date' : response['taken_at'],
                'like_count' : response['like_count'],
                'comment_count' : response['comment_count'],
                'location' : user_location,
                'tagged_users' : user_tags,
                'content' : user_content
            }
            return post_info
    
    def get_comments(self, shortcode):
        url = f"https://instagram188.p.rapidapi.com/postcomment/{shortcode}/%7Bend_cursor%7D"
        response = requests.request("GET", url, headers=headers).json()
        is_succes = response['success']
        if is_succes == False:
            return response['data']
        if is_succes == True:
            response = response['data']
            comments = response['comments']
            post_comments = []
            for comment in comments:
                comment_replies = []
                if comment['child_comment_count'] > 0:
                    replies = comment['preview_child_comments']
                    for rep in replies:
                        reply ={
                            'username': rep['user']['username'],
                            'text' : rep['text'],
                            'date' : rep['created_at'],
                            'like_count' : rep['comment_like_count']
                        }
                        comment_replies.append(reply)
                else:
                    comment_replies = []
                comment_info = {
                    'username': comment['user']['username'],
                    'text': comment['text'],
                    'date' : comment['created_at'],
                    'like_count': comment['comment_like_count'],
                    'replies_count' : comment['child_comment_count'],
                    'replies' : comment_replies
                }
                post_comments.append(comment_info)
            return post_comments

