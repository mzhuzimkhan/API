from fastapi import FastAPI
from fastapi import APIRouter
import parser.twitter as twitter
import parser.instagram as instagram
import parser.youtube as youtube
import parser.vk as vk

app = FastAPI()
router = APIRouter()

"""
Twitter
"""
@router.get("/twitter_user", tags = ["Twitter"])
def get_user(username: str):
    
    result = twitter.Twitter().get_user(username)      
    return result

@router.get("/twitter_tweets", tags = ["Twitter"])
def get_tweets(username: str, limit : int):

    result = twitter.Twitter().get_tweets(username, limit)      
    return result

@router.get("/tweet_replies", tags = ["Twitter"])
def get_tweet_replies(tweet_id: str):

    result = twitter.Twitter().get_tweet_replies(tweet_id)
    return result


"""
Instagram
"""
@router.get("/instagram_user", tags = ["Instagram"])
def get_user(nickname: str):
    
    result = instagram.Instagram().get_user(nickname)      
    return result

@router.get("/instagram_posts", tags = ["Instagram"])
def get_posts(shortcode: str):

    result = instagram.Instagram().get_posts(shortcode)      
    return result

@router.get("/instagram_comments", tags = ["Instagram"])
def get_user(shortcode: str):

    result = instagram.Instagram().get_comments(shortcode)
    return result


"""
Youtube
"""
@router.get("/youtube_channel", tags = ["YouTube"])
def get_channel(channel_id: str, limit: int):
    
    result = youtube.Youtube().get_channel(channel_id, limit)      
    return result

@router.get("/youtube_video", tags = ["YouTube"])
def get_video(video_id: str,):

    result = youtube.Youtube().get_video(video_id)      
    return result

@router.get("/youtube_comments", tags = ["YouTube"])
def get_comments(video_id: str, limit : int):

    result = youtube.Youtube().get_comments(video_id, limit)
    return result


"""
Vkontakte
"""
@router.get("/vkontakte_posts", tags = ["Vkontakte"])
def get_posts(group_or_user_name: str, post_counts : int):
    
    result = vk.Vkontakte().vk_posts(group_or_user_name, post_counts)      
    return result

@router.get("/vkontakte_comments", tags = ["Vkontakte"])
def get_comments(owner_id: str, post_id: str, comments_counts: int):

    result = vk.Vkontakte().vk_comments(owner_id, post_id, comments_counts)      
    return result

@router.get("/vkontakte_user", tags = ["Vkontakte"])
def get_user(user_id: str):

    result = vk.Vkontakte().vk_users(user_id)
    return result
app.include_router(router)