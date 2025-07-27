import json
from telegram import User


def add_user(user: User):
    try:
        with open('database/data.json', 'r+', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {"users": []}

            for existing_user in data['users']:
                if existing_user['telegram_id'] == user.id:
                    return False

            data['users'].append({
                'telegram_id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'playlist': [
                    {'name': 'On the Street Playlist', 'songs': []},
                    {'name': 'Home Playlist', 'songs': []},
                    {'name': 'Study Playlist', 'songs': []},
                    {'name': 'Party Playlist', 'songs': []},
                    {'name': 'Favorites', 'songs': []},
                ]
            })
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True
    except FileNotFoundError:
        # Agar fayl mavjud bo'lmasa, yaratish
        with open('database/data.json', 'w', encoding='utf-8') as file:
            data = {
                "users": [{
                    'telegram_id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'playlist': [
                        {'name': 'On the Street Playlist', 'songs': []},
                        {'name': 'Home Playlist', 'songs': []},
                        {'name': 'Study Playlist', 'songs': []},
                        {'name': 'Party Playlist', 'songs': []},
                        {'name': 'Favorites', 'songs': []},
                    ]
                }]
            }
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True


def get_users(user: User):
    try:
        with open('database/data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        for existing_user in data['users']:
            if existing_user['telegram_id'] == user.id:
                return existing_user
        return None
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def add_audio_to_playlist(user: User, playlist_name: str, audio_file_id: str):
    try:
        with open('database/data.json', 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for existing_user in data['users']:
                if existing_user['telegram_id'] == user.id:
                    for playlist in existing_user['playlist']:
                        if playlist['name'] == playlist_name:
                            playlist['songs'].append({'file_id': audio_file_id})
                            file.seek(0)
                            file.truncate()
                            json.dump(data, file, indent=4, ensure_ascii=False)
                            return True
            return False
    except (FileNotFoundError, json.JSONDecodeError):
        return False
