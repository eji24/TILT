import random
import re

NICHE_CATEGORIES = {
    "Model": ["model", "runway", "editorial", "signed", "fashion", "posing"],
    "Photographer": ["photographer", "photo", "lens", "film", "visuals", "captures", "studio", "shot by"],
    "Stylist": ["stylist", "wardrobe", "fashion stylist"],
    "Creative Director": ["creative director", "art director", "visionary"],
    "Brand / Business": ["brand", "founder", "ceo", "entrepreneur", "store", "label", "shop"],
    "Artist": ["artist", "painter", "illustrator", "gallery", "sketch", "canvas"],
    "Music / DJ": ["dj", "music", "producer", "beats", "vinyl", "mix"],
    "Fan / Public": ["fan", "supporter", "lover of", "admire", "follower"],
    "Party Promoter": ["party", "event", "promoter", "club"],
    "Athlete / Coach": ["coach", "athlete", "sports", "trainer", "fitness"],
    "Tech / Startup": ["tech", "startup", "founder", "developer", "coder", "engineer"]
}

DEFAULT_HASHTAGS = {
    "Model": ["#model", "#runway", "#editorial", "#style", "#fashion"],
    "Photographer": ["#photography", "#film", "#behindthescenes", "#captures"],
    "Stylist": ["#styling", "#fashionstylist", "#wardrobe"],
    "Creative Director": ["#creative", "#director", "#vision"],
    "Brand / Business": ["#brand", "#entrepreneur", "#founder"],
    "Artist": ["#artist", "#painting", "#illustration", "#gallery"],
    "Music / DJ": ["#music", "#djlife", "#producer", "#beats"],
    "Fan / Public": ["#fan", "#love", "#support"],
    "Party Promoter": ["#party", "#club", "#events"],
    "Athlete / Coach": ["#fitness", "#sports", "#coach"],
    "Tech / Startup": ["#tech", "#startup", "#innovation"],
    "Uncategorized": ["#creative", "#inspiration", "#explore"]
}

def is_only_emoji(text):
    return bool(re.fullmatch(r"[^\w]+", text.strip()))

def categorize_bio(bio, username, bio_url=None):
    target = (bio or "").strip()
    if not isinstance(target, str):
        target = str(target)
    target = target.lower()

    for category, keywords in NICHE_CATEGORIES.items():
        for kw in keywords:
            if kw in target:
                return category

    if bio_url:
        bio_url = bio_url.lower()
        if "cargo.site" in bio_url or "portfolio" in bio_url or "studio" in bio_url:
            return "Photographer"
        if "shop" in bio_url:
            return "Brand / Business"

    if "photography" in username.lower() or "studio" in username.lower():
        return "Photographer"

    if is_only_emoji(target):
        return "TooMinimal"

    return "Uncategorized"

def generate_persona_card(username, bio, bio_url=None):
    niche = categorize_bio(bio, username, bio_url)
    description_map = {
        "Model": "A style-forward individual immersed in the world of modeling and fashion.",
        "Photographer": "A creative eye capturing life’s best moments through the lens.",
        "Stylist": "A wardrobe curator and expert in fashion aesthetics.",
        "Creative Director": "A visionary leader driving creative projects to life.",
        "Brand / Business": "An entrepreneurial spirit growing brands and communities.",
        "Artist": "A dedicated creator making visual or fine art.",
        "Music / DJ": "A sound enthusiast mixing beats and sharing music.",
        "Fan / Public": "An admirer and supporter of the creative scene.",
        "Party Promoter": "An energizer behind nightlife and event vibes.",
        "Athlete / Coach": "A performer pushing physical limits and leading teams.",
        "Tech / Startup": "A builder innovating in tech and digital spaces.",
        "TooMinimal": "This profile is too minimal for the free tool.",
        "Uncategorized": "A unique creative with diverse interests."
    }

    hashtags = DEFAULT_HASHTAGS.get(niche, ["#creative"])
    reels = [
        "Introduce yourself",
        "Behind the scenes",
        "Favorite tools of your trade",
        "A day in your life",
        "Share your journey"
    ]
    follower_types = {
        "Creatives": 30,
        "Fans": 25,
        "Brands": 15,
        "Agencies": 10,
        "Event Planners": 5,
        "Collaborators": 5,
        "Local Community": 5,
        "Other": 5
    }
    return {
        "username": username,
        "bio": bio,
        "niche_category": niche,
        "description": description_map.get(niche, "A unique creative."),
        "hashtags": hashtags,
        "reels": reels,
        "followers": follower_types
    }
