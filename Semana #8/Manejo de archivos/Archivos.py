def sort_songs(input_file, output_file):
    try:

        with open(input_file, "r", encoding="utf-8") as file:
            songs = [song.strip() for song in file if song.strip()]

        songs.sort(key=str.lower)

        with open(output_file, "w", encoding="utf-8") as file:
            for song in songs:
                file.write(song + "\n")


        print(f" Canciones ordenadas guardadas en '{output_file}'")

    except FileNotFoundError:
        print(f" No se encontró el archivo '{input_file}'.")
    except Exception as e:
        print(f" Ocurrió un error: {e}")


sort_songs(
    r"C:\Users\Usuario\Desktop\Python\Archivos Python\My_songs.txt",
    r"C:\Users\Usuario\Desktop\Python\Archivos Python\Sort_songs.txt"
)
