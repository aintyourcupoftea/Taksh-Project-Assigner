from flask import Flask, jsonify
import random
from flask_cors import CORS # Import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://www.khojcommunity.com"}})
    # Replace this with your actual JSON data or logic to fetch data

projects = [
    {
        "name": "Quick Draw Skribble",
        "description": "Challenge your Skribble skills with AI!",
        "svg": "https://scribble-io.co/upload/imgs/quick-draw.png",
        "link": "https://admitted-reason-dc3.notion.site/Quick-Draw-skribble-75a5d881a1d343f382f6e257b46bcc9c?pvs=4"
    },
    {
        "name": "Clean Windows",
        "description": "Clean your C: Drive and flaunt your freed space!",
        "svg": "https://pccleaningtools.com/wp-content/uploads/2014/10/ico-cleanup.png",
        "link": "https://admitted-reason-dc3.notion.site/Clean-Up-Windows-4e501feda2c14b5181b2f7830127df70?pvs=4"
    },
    {
        "name": "Deep Beat Composer",
        "description": "Beat up your music game with AI-generated lyrics!",
        "svg": "https://deepbeat.org/img/deepbeat_logo4.png",
        "link": "https://admitted-reason-dc3.notion.site/Deep-Beat-composer-d964385ef91a4c94884bc2994aee7401?pvs=4"
    },
    {
        "name": "Project Stick Bridge",
        "description": "Build a stick bridge and see how much weight it can hold!",
        "svg": "https://i.pinimg.com/236x/76/2a/d5/762ad56aeafc0d6946d37156754df821.jpg",
        "link": "https://admitted-reason-dc3.notion.site/Project-Stick-Bridge-5a4dbb965b65446f90aa71c86e9d218c?pvs=4"
    },
    {
        "name": "Rubber Band Car",
        "description": "Race to victory with your innovative rubber band-powered car!",
        "svg": "https://i.ytimg.com/vi/lTNlAlcUtIc/sddefault.jpg",
        "link": "https://admitted-reason-dc3.notion.site/Rubber-Band-Car-3dc4c80fc8994b2d8077a47d4f71812d?pvs=4"
    },
    {
        "name": "Excuse with AI",
        "description": "Master the art of excuses with AI’s help!",
        "svg": "https://media.theresanaiforthat.com/icons/sabori-work-gpt.png",
        "link": "https://admitted-reason-dc3.notion.site/Excuse-With-AI-0c69194d45894c4d94e7a685751bca1b?pvs=4"
    },
    {
        "name": "Auto Draw Graphic",
        "description": " Elevate your art with AI-generated sketches and symbols!",
        "svg": "https://logowik.com/content/uploads/images/autodraw7185.jpg",
        "link": "https://admitted-reason-dc3.notion.site/Auto-Draw-graphic-aa66e0a15e2c4db5a973ae508111930f?pvs=4"
    },
    {
        "name": "Book Music",
        "description": "Book Music",
        "svg": "https://v1.whalesyncusercontent.com/v1/054166ee54f426e9cd3e081e/d77d4c00c3593b07c4b411e3/3c1631f02353f28080165fa0/Muzify-ai-apps-directory_cover-1200x628.jpeg",
        "link": "https://admitted-reason-dc3.notion.site/Book-to-Music-c8c42309b4a842eead9ab69623c23838?pvs=74"
    },
    {
        "name": "Freddy Meter",
        "description": "Literary playlists: Music inspired by favorite authors.",
        "svg": "https://townsquare.media/site/366/files/2019/11/FreddieMeter_Social_Asset_UGC_Static.jpg?",
        "link": "https://admitted-reason-dc3.notion.site/Freddie-Mercury-paradise-7007740e0eb4463481e31b9c2036a65b"
    },
    {
        "name": "Markdown Basics",
        "description": "Format text easily with Markdown language",
        "svg": "https://www.markdownguide.org/assets/images/tool-icons/markdown-here.png",
        "link": "https://admitted-reason-dc3.notion.site/Markdown-Basics-9d8f2612fd604cdbaee318fdfd9f58d6?pvs=4"
    },
   {
        "name": "Read QR",
        "description": "Create and share your social media QR code",
        "svg": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMauoS2HZC_z02jEBWdhqFcE97_BPJGyXZe-ImvIk-J3WbLqW582Pk6Voy&s",
        "link": "https://admitted-reason-dc3.notion.site/Read-Me-QR-2f6fc62ab24e4b7f97d31796eccbea20?pvs=4"
    },
    {
        "name": "Webpage Read",
        "description": "Create a simple HTML webpage.",
        "svg": "data:image/jpeg;base64,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",
        "link": "https://admitted-reason-dc3.notion.site/Web-Page-Read-71f6d37c8586456880f30380ef9915bf?pvs=4"
    },
    {
        "name": "Radio Garden",
        "description": "Capture the vibe of wild beats.",
        "svg": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAC4ALgMBEQACEQEDEQH/xAAaAAACAgMAAAAAAAAAAAAAAAAGBwQFAgMI/8QANBAAAQMCBAQEBAQHAAAAAAAAAQIDBAURAAYSITFBYXEHEyJRMoGRwaGx4fAVIzNCYnKS/8QAGgEAAgMBAQAAAAAAAAAAAAAAAgMBBAUABv/EACwRAAICAQIDBwMFAAAAAAAAAAECAAMRITEEEmEiQVGBoeHwEzJxFIKRksH/2gAMAwEAAhEDEQA/AHVOmxqfDdlzXkMx2k6luLOwGJAzoJBIAyYq8xeJkqTGeXSULiRknSlSkjzXOu/wjtv15Y4IzWCsGLNmF5os5+Z61PfKHJ8hZKrgFaifre+Lq0VqdokuxGsN6BSs9sUtFTpFRS64CfMhKklSrA8kn0/jhLmptNuok/SYjQwwyX4ipqkgU2usohz0i2rWNKjcgi3I3GE2Ia9dxEji2qYLdsdM/wCHw/PoIwMDNCIDxyzW5UK8nL8ZwiFAIL4Sf6jxF9+iQbdyfYYs0rgcxirD3QXy6/T9TbDzl3VnSgKB035X9iTt88dxAcjKe8UmASW9pbu0RqDIWEoCA7fe5IB42HbFUcWzAZgcNbVxCc6eu/Q+e46TaqPIjLE2IS1KaCdLzaih0bek3vYpNrb+1sMS/TDbenXzgfqazxH0F+7B16jcfkaaeEGszSJ0+ouzZ0Zpp97dxUdJSlxXNdrmxPO1hfkMXK2Ur2DmNbOdY8fB3Nb2YaCuLPcC50ApQpd93GzfSo9dlA9r88VLECHA2jKMKvJ4TnisSlTqvNmOElUiQ47v/kon74tAYGJBOTMqY6mPPivufA0+hauwUCfyxJBZSB3gxHEIXqdBuQR/IjaDaJL649tZ0ly5GwGpRG/XUD8sYOcDM86Ln4ekcQSVGQMeOig/15T5HTG8jT1h6nrWhvdZAASncHXqt8rfjgkJDR9NZp4tFsOq656BcA/uOw3wIG5sdMQoYCruOICiOQG/LGlwn2lptpcLySNhJ3hJWHqTmKQ40fS5CWlSeR9aLff64daMqJYTOuIN5qp6qTmSp09xJSpiW4lP+hN0n/kg4JTkAzmGDKxPuDbBiBGXQKumRDS4ysNOq9K06Rsoe23D9MZN9HI2DtEW8DTxaBLhnHU+0wmVRqJcyHkoUoElI47nkMDXQ9n2ic9SjsDu89oI5jTIl1JT7aAttTY0FFiAnhv7ceeNKpRXWFPwzqiirgwv8FMvOTsx1Ey2lJaixdC7j+9S0kb9kKxFrdkYlqllcZUwt8Y8lJmSo2Zo0Zb6GCgVNhoet1lJF1ptzCbg9Le2ArfHZjGA3iwEjJpusQJ6dSb+XqKgCSjYHzAdgldiea9wQAA3FnjBys3RqlluNUo7kaNLbiC5cSQonii1/wCZudndwQPUi4Ok45kZ1IaRlM5k5+tZRlPB2RTZ6pPlaPMc3SlQFh6A4Lgm5O/TsCVWIvKpgHlO8kx2Ms1BCmaXTpsiQ5ZuI0tS1eY5wOoFVingehT3wq2x07PfIPK50B+fPmkdeSsvjL1FRHcKVSnT5khSeGo8h0HD6nnhYBxrH1oEGAJf4mHFtnHwhpNbfcm0h7+GTHDqWlKNTKz76dtJ7bdDhy3EaGAUBiurWWa9k1RbcmxLKcFiwSTfgD6kbccPDK8WQVlnQfDWu5ocM6RU4TLblit2ylr4AfDZI4dcCbQugEkV51MceUMmUzK0ZCY2uTJCdJlP2K7XvYWGw/e+KrHmbmhhANYSYiHP/9k=",
        "link": "https://admitted-reason-dc3.notion.site/Radio-Garden-Party-60533accd41a405189f2aa773ff7d723?pvs=4"
    },
    {
        "name": "Staggering Beauty",
        "description": "Shake your cursor and see surprises!",
        "svg": "data:image/jpeg;base64,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",
        "link": "https://admitted-reason-dc3.notion.site/Staggering-Beauty-925f1fcfb994492a8a9a06990c4aadbd?pvs=4"
    },
    {
        "name": "Pointer",
        "description": "Let your cursor reveal unexpected paths.",
        "svg": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4sjQPMsY5-wLzQK0CEmnFS3nFwLWkoe-4ts1b7_rJg2BIwUbjMYwBe3n7&s",
        "link": "https://admitted-reason-dc3.notion.site/Pointer-Pointing-e9ac5416552e4da386bfa498a5cf7a0c?pvs=4"
    },
    {
        "name": "Window Swap",
        "description": "Snap a screenshot of the window that leaves you saying, “What on earth?”",
        "svg": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAC4AUgMBIgACEQEDEQH/xAAcAAABBAMBAAAAAAAAAAAAAAAFAwQGBwACCAH/xAA+EAACAQMCAwMGCgoDAAAAAAABAgMABBEFIQYSMRNBUSJCYXGBkRQjM2NyoaKxwdEHMjRDUmKys8LwFRYk/8QAFgEBAQEAAAAAAAAAAAAAAAAAAQAC/8QAGREBAQEAAwAAAAAAAAAAAAAAABEBEiFB/9oADAMBAAIRAxEAPwCm4bqVZ41BTlBA+TXp68V0ZwDP2nCOkMcfsiDYY6DFc2L8tGfSKtLhfiW7s9I0+C3kAhhj5HQqDkhj7emKcZ1dCyjFVPxpOf8AtGornYMvf82DUwTW4rk2klrMTE7kHqM924qvOMLjm4o1EjcFk/tCkLL4CuyeFkaWQkK7qCxzgeFVj+g+9luOL7gzdn5GnSY5IlT95F/CBmpbwffJHwn2btgmV/wqvv0N3S2fEt1K2cf8fJ/Wh/Cg+OhTLSMku3WoZrnFkcOlzmJ2huXHLFjc+k+jao5ZcZzQaHcwTTvJfc3xDyAtkEjOT4jfHsprMTbifV49I06S6bkZgDyI78vMcdKpbXNau9VvDcXXZqwgZQqoMAbjvz4061HUbzVXU3dy8rLkAv3Z6gVHtQ+LmaMEkcib+t6qcwLljLSO3ixPhWUsJgBgjcVlZaNQcMhqU6AxZWhDKvltuT6TUV81aN2TkMQNvLPf7ajEysL/AOCl15/KQ5GD0oLql001/PKTzM2Mt4+QabrLyuN/NGPdWrxu4llB8kYHX0EfjVREg0LUhDpvZlsbk7nrUU4LujaanK4862Zfey0tC57ADPTcZoVob9ndk/NkfWKlEjurppJ5WbfLdCaaGUAKWO3ppF5PKc56mk0cl8Z9vWstToR7Qs/Vcdoe7cbUE1R/jpGHcEH3mjHNmUHA6vuD03oHqjZeX6YH2a1gIvCxdiOmTispRJwEUEDOKypGQ/UHronauA5ydzg/ZFDYgGGCSN+6i9hzBeWK9uox4L0++pHYY8wIz0xkU9gdmsrhRuRg5pBIbh+mozH6UamtmsLpgD8NQ58bZPyqgrSyEc8XZCCWS6bPZonQ/wC70H0SESzuWYhVj6jGfdUi7CSFFP8A5iwH63wZAfX0oRE8CSMEtIScecDj6iKU8lyhYYPWvICTMvXr40sizuSUtrIDO2TIf8qVFteNuFsV9UWfvoh5PA57UHHmtvjHU0H1E5J/mkY+7AovJY3p3MtoPVbJ+VDLy1k8+RTjuCBR9VUFM6ytuU+isqL/2Q==",
        "link": "https://admitted-reason-dc3.notion.site/Window-Swap-105b0b8e321143a798e127b1d26ecae7?pvs=4"
    },
    {
        "name": "Receiptify Bill",
        "description": "Shop last month's top music hits.",
        "svg": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7pU9ejuWEsL99FqTEjNIYb5avKq0UPFGghurKE6-nsfbheOo9Nv6rBkFM&s",
        "link": "https://admitted-reason-dc3.notion.site/Receiptify-Music-bill-b68f2bea140742ac9d4df8a2ea3ae243?pvs=4"
    },
    {
        "name": "93 Quest",
        "description": "Uncover hidden gems in Windows 93.",
        "svg": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQorNACBtbxq8A1494U2D4ta5EsyU1DLEl8MA&s",
        "link": "https://admitted-reason-dc3.notion.site/93-Achievement-Quest-618740d15efd4165bbe35e06edfb4a64?pvs=4"
    },
    {
        "name": "Greeting Quest",
        "description": "Create animated greeting cards with Scratch.",
        "svg": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAEIALgMBIgACEQEDEQH/xAAbAAEAAwEAAwAAAAAAAAAAAAAHAAUGBAECCP/EADoQAAEDAgQCBQkHBQEAAAAAAAECAwQAEQUGEiEHMRMyQVFhIjRScXOBkbGyFBUjQmLB8DVDY8LRFv/EABkBAAIDAQAAAAAAAAAAAAAAAAMEAAIFAf/EACcRAAICAQEGBwEAAAAAAAAAAAECABEDMQQhMkFhcRMiJFGh4fAS/9oADAMBAAIRAxEAPwDDDNWZEkhOYMW59s1w/M10tZvzGLJ+/wDEQT2rkqPzqlWwptpt8i7bilAKHYoc0nx3B9RFeY0xyNq0JbNzfyk3/nOtYIp5RUlgN0v05tzMjlmOTfxkX+dRzOmaWrKGYpB8A4lR+VV0Rcia1IKEMoTHb12SjrEEEDn+k/w1zHE3j/bZHqSe+/fVvCT2+IIZHJIHLrLc58zXb+vS9/BH/KUuDOYcWxuHiP3vNclqadGhbgF0iw22AoKSCohCQSVEAAC5Jpl4EtKYbxhpdtaHglVjyNhcUttCqENCMoTcKsKntw1uszY/2rD3zZ9gK0q25LQfyrFzY8jcg7GrGXlV5yIvEcAlNYrhyespCgh5i/IONk3B8RcGs+rYmt5w2wAYuoIaWht53UVOqF9KUnkPnTSqNSaHOLZ8xxp5RZO4d5SwoTuFNxw+SFypKUrS3vZOlQsfequZjKmMSpwhwov2hRBIWlaUp0jmSSRal7NuWI0NzLLENu+qelt5ZG7hI5n4GvfOuTmGI0mdE6MRSn8WMobbmxt4b8qsM2J6UGr0/dYl6nCWyEA1xfXaEslMDLiFNRJbWIYyRpVIYN2Iff0Z/O5+rkns33pB4Bi0bFR/lH0iiOayI8x5lJuG3Ckeq9LnATzbFfaj6RSu0LSG5qY2DEEQeV3+NJ/CGFJl4ZOkYY8lvEYMkKQF9VxC0dU+9J+PvBf6XrpJ4HyZSMVxaHBcZRIfjtOJ6ZJKbIcsrYb9VZ99qJkYqhIlGxrk8rRay4/KxeAl7GoaW5MeQejBQUkEJ2VY8jZRFUz33xmJ2XHnpRDwmO6SshBCnEpJ2BPPlueW3uq/nyH0vrkFrEG2cPVqLTKUKE0KQRsNz5JN7XBuOR2rhzdNdw/LuYpC5iVkQFLZjaUhTN0lO9tzdXb4UkuWmJUDfp07SNs39IFZiQNevefMzj3TuresR0iiux7Lm9MHALzbFfaj6RQ4kWAApi4Bea4r7UfSKa2ngMImsHT1j662nB+YImfYV72kNOs7dvk6v9KqXcm5lbcUleCygoHceSf3qzylgGPYVmfCpz+EyUNsykFainZKCbKOx7ia67KVIucANx1Xh6G1QVQ1LUuNJU5rkl1yyV31gb897AHZPYKyXFJuPhuRJwjl1yRJcba6d66nChTvSFOojdPWsOwGtR00JM1wQXnoiunEmQpDQ0yiQRpKlDwHK1rDsNYLiW2/OyphEPCcKfbV9pU+/Fa/ELR0qvqKbg3Kz20lj4xcK11BwkAbc6YeAXmuK+1H0ijL/wA9jYVqVg01Q7ugV+1KvA6DLgsYmmbFfjqU4CkPNlJIsOV6azsCh3waA3Few7hU0juHwqVKz4eTSn0R8K8aE+iPhUqVJJOjR6CfhUCEp5JA9QqVKkk//9k=",
        "link": "https://admitted-reason-dc3.notion.site/Greeting-Card-Quest-29036977e48641b8a4578587da605e46?pvs=4"
    },
    {
        "name": "Infinte Drum",
        "description": "Create music with bizarre object sounds.",
        "svg": "data:image/jpeg;base64,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",
        "link": "https://admitted-reason-dc3.notion.site/Infinite-Drum-Machine-90b7f8fbb01b4e0ab638db5b4f5da4ef?pvs=4"
    }
]


    
@app.route('/api/projects', methods=['GET'])
def get_projects():
    # Select 9 random projects
    selected_projects = random.sample(projects, 9)
    return jsonify(selected_projects)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))