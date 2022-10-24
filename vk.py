import requests
token = 'vk1.a.IA-0n-vJJ-CutXMOMAvFKtiVMkwnfhTdNvAljjHpYt4brmmB5C6q5_GO8PMOunn2nUgxpV83S8d_Cm-z0mSY4HUjCLdlpDg-DlV3p89knQkjzeCfCJ9oWM5iq8Maqawj-MswWuhLlwDuVzdpAR_V3-BpXE5IyAPe7TOs6L-r4DaektXiA-hAcKi2cF0UoMCJ'

"""
It works with self vk API so there is no need to any subscription
"""
class Vkontakte():
    def vk_posts(self, group_name, count):
        url_post = f"https://api.vk.com/method/wall.get?domain={group_name}&count={count}&access_token={token}&v=5.131"
        req_post = requests.get(url_post).json()
        if 'error' in req_post:
            return req_post['error']['error_msg']
        req_post_response = req_post['response']
        posts = req_post_response['items']
        results = []
        for post in posts:
            post_text = post['text'] if 'text' in post else ''
            post_date = post['date'] if 'date' in post else ''
            post_id = post['id'] if 'id' in post else ''
            post_owner_id = post['owner_id'] if 'owner_id' in post else ''
            post_likes = post['likes']['count'] if 'likes' in post else ''
            post_reposts = post['reposts']['count'] if 'reposts' in post else ''
            post_views = post['views']['count'] if 'views' in post else ''
            post_photos = []
            if 'attachments' in post:
                photos = len(post['attachments'])
                photos -= 1
                if 'photo' in post['attachments'][photos]:
                    while photos >= 0:
                        sizes = len(post['attachments'][photos]['photo']['sizes'])
                        post_photos.append(post['attachments'][photos]['photo']['sizes'][sizes-1]['url'])
                        photos -= 1
            res = {
                'text' : post_text,
                'date' : post_date,
                'id' : post_id,
                'owner_id' : post_owner_id,
                'likes' : post_likes,
                'reposts' : post_reposts,
                'views' : post_views,
                'photos' : post_photos
            }
            results.append(res)
        return results

    def vk_comments(self, owner_id, post_id, count):
        url_comments = f"https://api.vk.com/method/wall.getComments?owner_id={owner_id}&post_id={post_id}&count={count}&need_likes=1&extended=1&access_token={token}&thread_items_count=5&v=5.131"
        req_comments = requests.get(url_comments).json()
        if 'error' in req_comments:
            return req_comments['error']['error_msg']
        req_comments_response = req_comments['response']
        comments = req_comments_response['items']
        results = []
        for comment in comments:
            comment_text = comment['text'] if 'text' in comment else ''
            comment_id = comment['id'] if 'id' in comment else ''
            comment_date = comment['date'] if 'date' in comment else ''
            comment_likes = comment['likes']['count'] if 'likes' in comment else ''
            comment_post_id = comment['post_id'] if 'post_id' in comment else ''
            comment_owner_id = comment['owner_id'] if 'owner_id' in comment else ''
            comment_replies = []
            if 'thread' in comment:
                if 'items' in comment['thread']:
                    replies_number = len(comment['thread']['items'])
                    replies_number -=1
                    while replies_number > 0:
                        replies_res ={
                            'id' : comment['thread']['items'][replies_number]['id'],
                            'text' : comment['thread']['items'][replies_number]['text']
                        }
                        replies_number-=1
                        comment_replies.append(replies_res)
            res = {
                'text' : comment_text,
                'id' : comment_id,
                'date' : comment_date,
                'likes' : comment_likes,
                'post_id' : comment_post_id,
                'owner_id' : comment_owner_id,
                'replies' : comment_replies
            }
            results.append(res)
        return results

    def vk_users(self, user_id):
        url_users = f"https://api.vk.com/method/users.get?user_ids={user_id}&fields=bdate,activities,books,connections,counters,education,followers_count,interests,last_seen,movies,music,nickname,personal,quotes,relatives,relation,schools,sex,site,status,usniversities,about,contacts,city,country&access_token={token}&v=5.131"
        req_users = requests.get(url_users).json()
        if 'error' in req_users:
            return req_users['error']['error_msg']
        user = req_users['response'][0]
        return user
