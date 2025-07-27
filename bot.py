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

    dispatcher.add_handler(CommandHandler('start', handlers.start))
    dispatcher.add_handler(CommandHandler('list_playlists', handlers.list_playlists))

    dispatcher.add_handler(MessageHandler(Filters.audio, handlers.handle_audio))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handlers.add_audio_to_playlist))

    dispatcher.add_handler(CallbackQueryHandler(
        handlers.send_songs,
        pattern='^(On the Street Playlist|Home Playlist|Study Playlist|Party Playlist|Favorites)$'
    ))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
