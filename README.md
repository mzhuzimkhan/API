
# Social networks API

The main purpose of this API is to collect data from Social Networks.

## How to work with API
This api get data from four Social Networks(Twitter, Instagram, 
YouTube, Vkontakte)

#### Twitter 
| Input | Output    | Router name           |
| :-------- | :------- | :------------------------- |
| `username`| Information about given profile | **/twitter_user**
| `username`| Tweets of given profile | **/twitter_tweets**
| `twitter_id`| Retweets of given tweet | **/tweet_replies**


#### Instagram

| Input | Output    | Router name           |
| :-------- | :------- | :------------------------- |
| `nickname`| Users information and its posts | **/instagram_user**
| `shortcode`| Information about given post | **/instagram_posts**
| `shortcode`| Comments of given post | **/instagram_comments**


#### Youtube

| Input | Output    | Router name           |
| :-------- | :------- | :------------------------- |
| `channel_id`| Channel information and its videos | **/youtube_channel**
| `video_id`| Information about given video | **/youtube_video**
| `video_id`| Comments of given video | **/youtube_comments**

#### Vkontakte

| Input | Output    | Router name           |
| :-------- | :------- | :------------------------- |
| group or user `username`| User or group posts | **/vkontakte_posts**
| `owner_id` and `post_id`| Comments of given post | **/vkontakte_comments**
| `username` or `user_id`| Information about given user | **/vkontakte_user**




### Getting Started

**Run locally**

```bash
  uvicorn parser.api:app 
```
**Run in Docker**
- Ensure you have docker and docker compose installed
- Place this API in Docker Containers
- Open the project in terminal
- Then:
```bash
   docker compose up --build -d
```