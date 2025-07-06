import instaloader

def get_public_bio(username):
    """
    Gets the public bio of any Instagram user without login (if account is public).
    Returns: tuple (bio, external_url) if available
    """
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        return profile.biography, profile.external_url
    except Exception as e:
        print(f"Error fetching bio for {username}: {e}")
        return "", ""
