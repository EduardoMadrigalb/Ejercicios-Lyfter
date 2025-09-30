import csv

def write_file(file_path, data, headers, dialect= "excel"):

    with open (file_path, "w", encoding="utf-8", newline= "") as file:
          writer = csv.DictWriter(file, fieldnames= headers, dialect= "excel-tab")
          writer.writeheader()
          writer.writerows(data)
		
video_games_list = []

n = int(input("How many Videogames do you wish to enter?"))

for i in range(n):
	print(f"\nVideo Game{i+1}")
	name= input("Name: ")
	genre= input("Genre: ")
	developer= input("Developer: ")
	ersb_rating= input("ERSB Rating: ")

	video_games_list.append({
		"Name":name,
		"Genre": genre,
		"Developer": developer,
		"ERSB Rating": ersb_rating,
	})


write_file("video_games.tsv", video_games_list, video_games_list[0].keys())

print(f"\n{n} video_games have been saved in the 'video_games.csv' file.")