import json
from telegram import User


def add_user(user: User):
    with open('database/data.json', 'r+') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = {"users": []}
        
        # Check if user already exists
        for existing_user in data['users']:
            if existing_user['telegram_id'] == user.id:
                return  False

        # Add new user with default playlist
        data['users'].append({
            'telegram_id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'playlist': [
                {
                    'name': 'Workout Playlist',
                    'songs': []
                },
                {
                    'name': 'Chill Playlist',
                    'songs': []
                },
                {
                    'name': 'Study Playlist',
                    'songs': []
                },
                {
                    'name': 'Party Playlist',
                    'songs': []
                },
                {
                    'name': 'Favorites',
                    'songs': []
                }
            ]
        })
        file.seek(0)
        json.dump(data, file, indent=4)
    
    return True


def get_users(user: User):
    with open('database/data.json', 'r') as file:
        data = json.load(file)
    for existing_user in data['users']:
        if existing_user['telegram_id'] == user.id:
            return existing_user
    return None


def add_audio_to_playlist(user: User, playlist_name: str, audio_file_id: str):
    with open('database/data.json', 'r+') as file:
        data = json.load(file)
        for existing_user in data['users']:
            if existing_user['telegram_id'] == user.id:
                for playlist in existing_user['playlist']:
                    if playlist['name'] == playlist_name:
                        playlist['songs'].append({
                            'file_id': audio_file_id
                        })
                        file.seek(0)
                        json.dump(data, file, indent=4)
                        return True
    return False

