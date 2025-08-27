shows = ["  ihsanul haq: from Deolai",
         "anwar", "  azAn",  "rayyan   "]

def main():
    cleaned_shows = []
    for show in shows:
        cleaned_shows.append(show.strip().title())
    print(', '.join(cleaned_shows))

main()