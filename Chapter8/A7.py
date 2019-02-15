
def make_album(artist_name, album_title, num_of_tracks=""):
    temp_dict = {}
    temp_dict['artist_name'] = artist_name
    temp_dict['album_title'] = album_title
    if num_of_tracks:
        temp_dict['num_of_tracks'] = num_of_tracks
    return temp_dict

done = False
while not done:
    artist_name_input = input("Enter the name of the artst: ")
    album_name_input = input("Enter the name of the album: ")
    confirmation = input("Would you like to enter the number of tracks? Y/N ")
    if confirmation.upper() == 'Y':
        valid_input = False
        while not valid_input:
            num_of_tracks_input = input("Enter the number of tracks: ")
            try:
                num_of_tracks_input = int(num_of_tracks_input)
            except:
                print("ERROR: Improper syntax. Try Again.")
                continue
            valid_input = True
        print(make_album(artist_name_input, album_name_input, num_of_tracks_input))
    else:
        print(make_album(artist_name_input, album_name_input))
    confirmation = input("Would you like to create another album? Y/N ")
    if confirmation.upper() == 'N':
        done = True

