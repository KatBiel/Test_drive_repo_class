from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager!")

        while True:
            print("\nWhat would you like to do?")
            print("  1 - List all albums")
            print("  2 - List all artists")
            print("  q - Quit")

            user_choice = input("Enter your choice: ")

            if user_choice == '1':
                self.list_all_albums()
            elif user_choice == '2':
                self.list_all_artists()
            elif user_choice.lower() == 'q':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def list_all_albums(self):
        album_repository = AlbumRepository(self._connection)
        albums = album_repository.all()

        print("\nHere is the list of albums:")
        for album in albums:
            print(f" * {album.id} - {album.title}")

    def list_all_artists(self):
        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()

        print("\nHere is the list of artists:")
        for artist in artists:
            print(f" * {artist.id}: {artist.name} ({artist.genre})")

if __name__ == '__main__':
    app = Application()
    app.run()