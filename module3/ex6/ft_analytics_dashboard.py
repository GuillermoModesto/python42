def main():
    unique_achievements = {
        "first_kill", "level_10", "boss_slayer", "explorer",
        "collector", "speed_runner", "sharpshooter",
        "survivor", "strategist", "champion",
        "veteran", "elite"
    }
    players = {
        "alice": {
            "score": 2300,
            "is_active": True,
            "achievements": 5,
            "region": "north"
        },
        "bob": {
            "score": 1800,
            "is_active": True,
            "achievements": 3,
            "region": "east"
        },
        "charlie": {
            "score": 2150,
            "is_active": True,
            "achievements": 7,
            "region": "central"
        },
        "diana": {
            "score": 2050,
            "is_active": False,
            "achievements": 4,
            "region": "north"
        },
        "eve": {
            "score": 950,
            "is_active": False,
            "achievements": 2,
            "region": "west"
        },
        "frank": {
            "score": 2750,
            "is_active": False,
            "achievements": 8,
            "region": "south"
        },
        "grace": {
            "score": 1600,
            "is_active": True,
            "achievements": 6,
            "region": "east"
        },
        "henry": {
            "score": 1200,
            "is_active": False,
            "achievements": 1,
            "region": "north"
        },
        "ivy": {
            "score": 3100,
            "is_active": True,
            "achievements": 9,
            "region": "central"
        },
        "jack": {   
            "score": 1990,
            "is_active": False,
            "achievements": 3,
            "region": "west"
        }
    }
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    highscores = [
        player for player, data
        in players.items()
        if data["score"] >= 2000
        ]
    print(f"High scorers (>2000): {highscores}")
    d_highscores = [
        data["score"] * 2 for data
        in players.values()
        if data["score"] >= 2000
        ]
    print(f"Scores doubled: {d_highscores}")
    active = [
        player for player, data
        in players.items()
        if data["is_active"]
    ]
    print(f"Active players: {active}")
    print("\n=== Dict Comprehension Examples ===")
    p_scores = {
        player: data["score"] for player, data
        in players.items()
        if "score" in data
    }
    print(f"Player scores: {p_scores}")
    score_c = {
        "high": 0,
        "medium": 0,
        "low": 0
    }
    for data in players.values():
        if (data["score"] >= 2000):
            score_c["high"] += 1
        elif (data["score"] >= 1000):
            score_c["medium"] += 1
        else:
            score_c["low"] += 1
    print(f"Score categories: {score_c}")
    active_reg = {
        
    }


if __name__ == "__main__":
    main()
