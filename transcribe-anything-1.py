from transcribe_anything.api import transcribe

def main():
    url=input("Enter the URL of the video you want to transcribe:")

    #transcribe a video on youtube
    transcribe(url_or_file=url, language="en")
   

    


if __name__ == "__main__":
    main()
