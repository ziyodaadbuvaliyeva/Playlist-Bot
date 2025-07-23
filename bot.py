from config import TOKEN
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)
import handlers


def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # command hanlers
    dispatcher.add_handler(CommandHandler('start', handlers.start))
    dispatcher.add_handler(CommandHandler('list_playlists', handlers.list_playlists))

    # message handler
    dispatcher.add_handler(MessageHandler(Filters.audio, handlers.handle_audio))
    dispatcher.add_handler(MessageHandler(Filters.text, handlers.add_audio_to_playlist))

    # inline button handler
    dispatcher.add_handler(CallbackQueryHandler(handlers.send_songs, pattern='^(Workout Playlist|Chill Playlist|Study Playlist|Party Playlist|Favorites)$'))
    # start bot
    updater.start_polling()
    updater.idle()

main()
