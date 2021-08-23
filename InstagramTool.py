import instaloader as insta

username = input("Username: ")
server = insta.Instaloader()
profile = insta.Profile.from_username(server.context, username)

print(f"Name: {profile.full_name}")
print(f"Bio: {profile.biography}")
print(f"Followers: {profile.followers}")
print(f"Following: {profile.followees}")
print(f"Posts: {profile.mediacount}")
print(f"Is private: {profile.is_private}")
print(f"Is buisness: {profile.is_business_account}")

if profile.is_private == False:
    posts = profile.get_posts()
    for post in posts:
        print(f"\n\nDate: {post.date}")
        print(f"Likes: {post.likes}")
        print(f"Description: {post.caption}")
        print(f"Comments: {post.comments}")
        print(f"Hashtags: {post.caption_hashtags}")
        print(f"Location: {post.location}")
        print(f"Image Url: {post.url}")
        input()
else:
    print("\nThis account is private. No posts found")
    input()
