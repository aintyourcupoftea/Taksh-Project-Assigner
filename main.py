from flask import Flask, jsonify
import random

app = Flask(__name__)
    # Replace this with your actual JSON data or logic to fetch data
projects = [
    {
        "name": "Project 1",
        "description": "Explore the Quick, Draw tool to unravel your inner Skribble player.",
        "svg": "https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/android.svg",
        "link": "https://admitted-reason-dc3.notion.site/Quick-Draw-skribble-75a5d881a1d343f382f6e257b46bcc9c?pvs=4"
    },
    {
        "name": "Project 2",
        "description": "Clean Windows",
        "svg": "link_to_project2_svg",
        "link": "https://admitted-reason-dc3.notion.site/Clean-Up-Windows-4e501feda2c14b5181b2f7830127df70?pvs=4"
    },
    {
        "name": "Project 3",
        "description": "Deep Beat",
        "svg": "link_to_project3_svg",
        "link": "https://admitted-reason-dc3.notion.site/Deep-Beat-composer-d964385ef91a4c94884bc2994aee7401?pvs=4"
    },
    {
        "name": "Project 4",
        "description": "Stick Bridge",
        "svg": "link_to_project1_svg",
        "link": "https://admitted-reason-dc3.notion.site/Project-Stick-Bridge-5a4dbb965b65446f90aa71c86e9d218c?pvs=4"
    },
    {
        "name": "Project 5",
        "description": "Rubber band Car",
        "svg": "link_to_project2_svg",
        "link": "https://admitted-reason-dc3.notion.site/Rubber-Band-Car-3dc4c80fc8994b2d8077a47d4f71812d?pvs=4"
    },
    {
        "name": "Project 6",
        "description": "Excuse AI",
        "svg": "link_to_project3_svg",
        "link": "https://admitted-reason-dc3.notion.site/Excuse-With-AI-0c69194d45894c4d94e7a685751bca1b?pvs=4"
    },
    {
        "name": "Project 7",
        "description": " Auto Draw",
        "svg": "link_to_project1_svg",
        "link": "https://admitted-reason-dc3.notion.site/Auto-Draw-graphic-aa66e0a15e2c4db5a973ae508111930f?pvs=4"
    },
    {
        "name": "Project 8",
        "description": "Book Music",
        "svg": "link_to_project2_svg",
        "link": "https://admitted-reason-dc3.notion.site/Book-to-Music-c8c42309b4a842eead9ab69623c23838?pvs=74"
    },
    {
        "name": "Project 9",
        "description": "Freddy Meter",
        "svg": "link_to_project3_svg",
        "link": "https://admitted-reason-dc3.notion.site/Book-to-Music-c8c42309b4a842eead9ab69623c23838?pvs=74"
    },
    {
        "name": "Project 10",
        "description": "Markdown Basics",
        "svg": "link_to_project1_svg",
        "link": "https://admitted-reason-dc3.notion.site/Markdown-Basics-9d8f2612fd604cdbaee318fdfd9f58d6?pvs=4"
    },
    {
        "name": "Project 11",
        "description": "Read QR",
        "svg": "link_to_project1_svg",
        "link": "https://admitted-reason-dc3.notion.site/Read-Me-QR-2f6fc62ab24e4b7f97d31796eccbea20?pvs=4"
    },
    {
        "name": "Project 12",
        "description": "Webpage Read",
        "svg": "link_to_project1_svg",
        "link": "https://admitted-reason-dc3.notion.site/Web-Page-Read-71f6d37c8586456880f30380ef9915bf?pvs=4"
    },
    {
        "name": "Project 13",
        "description": "Radio Garden",
        "svg": "link_to_project1_svg",
        "link": "https://admitted-reason-dc3.notion.site/Radio-Garden-Party-60533accd41a405189f2aa773ff7d723?pvs=4"
    },
    {
        "name": "Project 14",
        "description": "Staggering Beauty",
        "svg": "link_to_project1_svg",
        "link": "https://admitted-reason-dc3.notion.site/Staggering-Beauty-925f1fcfb994492a8a9a06990c4aadbd?pvs=4"
    },
    {
        "name": "Project 15",
        "description": "Pointer",
        "svg": "link_to_project1_svg",
        "link": "https://admitted-reason-dc3.notion.site/Pointer-Pointing-e9ac5416552e4da386bfa498a5cf7a0c?pvs=4"
    },
    {
        "name": "Project 16",
        "description": "Window Swap",
        "svg": "link_to_project1_svg",
        "link": "https://admitted-reason-dc3.notion.site/Window-Swap-105b0b8e321143a798e127b1d26ecae7?pvs=4"
    },
    {
        "name": "Project 17",
        "description": "Receiptify Bill",
        "svg": "link_to_project1_svg",
        "link": "https://admitted-reason-dc3.notion.site/Receiptify-Music-bill-b68f2bea140742ac9d4df8a2ea3ae243?pvs=4"
    },
    {
        "name": "Project 18",
        "description": "93 Quest",
        "svg": "link_to_project1_svg",
        "link": "https://admitted-reason-dc3.notion.site/93-Achievement-Quest-618740d15efd4165bbe35e06edfb4a64?pvs=4"
    },
    {
        "name": "Project 19",
        "description": "Greeting Quest",
        "svg": "link_to_project1_svg",
        "link": "https://admitted-reason-dc3.notion.site/Greeting-Card-Quest-29036977e48641b8a4578587da605e46?pvs=4"
    },
    {
        "name": "Project 20",
        "description": "Infinte Drum: ",
        "svg": "link_to_project1_svg",
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