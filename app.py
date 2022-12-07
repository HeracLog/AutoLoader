from pytube import YouTube


#Takes text file input and divides it to array elements
Links = open("Links.txt", "r")
LinksContent = Links.read()
LinksArray  = LinksContent.split(",")

#Loops through array elements to download them
def downloadVideos():

    for n in LinksArray:
        print("Downloading video: ")
        YouTube(n).streams.filter(res="360p").first().download()


#Calls function to start the program
downloadVideos()