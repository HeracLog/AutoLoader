from pytube import YouTube


#Takes text file input and divides it to array elements
Links = open("Links.txt", "r")
LinksContent = Links.read()
LinksArray  = LinksContent.split(",")

#Loops through array elements to download them
def downloadVideos():
    num = 1
    for n in LinksArray:
        print(f"Downloading video {num}: ")
        YouTube(n).streams.filter(res="360p").first().download()
        num += 1


#Calls function to start the program
downloadVideos()