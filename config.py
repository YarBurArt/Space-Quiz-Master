import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
DB_URL = "mongodb://localhost:27017"

questions = {
    "quriosity_meaning": {
        "image": "https://fsmedia.imgix.net/af/04/5e/78/1e19/4018/a6b9"
                 "/4bd2a4f25d09/the-mars-opportunity-rover-in-this-"
                 "artist-rendering.png?rect=0%2C0%2C2038%2C1019"
                 "&auto=format%2Ccompress&dpr=2&w=650",
        "question": "the meaning of Opportunity's Mars rover mission?",
        "explanation": "here's an explanation\n https://science.nasa.gov/mission/mer-opportunity/"
    },
    "hubble_telescope_info": {
        "image": "https://science.nasa.gov/wp-content/uploads/2023/07/caldwell-69.jpg?w=2048&format=webp",
        "question": "What is the Hubble Space Telescope and what are its key discoveries?",
        "explanation": "The Hubble Space Telescope is a large, space-based observatory that"
            "has been in operation since 1990. It has made numerous groundbreaking discoveries, "
            "including observing distant galaxies, studying the evolution of stars,"
            " and providing insights into the expansion of the universe."
    },

    "international_space_station_info": {
        "image": "https://www.nasa.gov/wp-content/uploads/2021/08/44911459904-375bc02163-k-0.jpg?resize=768,512",
        "question": "What is the International Space Station and what kind of research is conducted there?",
        "explanation": "The International Space Station is a large, orbiting laboratory where"
            " astronauts from various countries conduct scientific experiments and research in fields"
            " such as biology, physics, astronomy, and Earth observation. It has been continuously inhabited "
            "since 2000 and serves as an important platform for advancing our understanding"
            " of space and its effects on living organisms."
    },

    "james_webb_telescope_info": {
        "image": "https://www.nasa.gov/wp-content/uploads/2023/02/International-Space-Station-in-2021.jpg?resize=1536,85",
        "question": "What is the James Webb Space Telescope and what are its key capabilities?",
        "explanation": "The James Webb Space Telescope is a large, infrared-optimized space observatory "
            "that was launched in 2021. It is designed to study the earliest galaxies in the universe,"
            " observe the formation of stars and planets, and explore the origins "
            "of our solar system, among other scientific objectives."
    },

    "artemis_program_info": {
        "image": "https://images-assets.nasa.gov/image/NHQ202211160002/NHQ202211160002~large.jpg"
            "?w=1920&h=1193&fit=clip&crop=faces%2Cfocalpoint",
        "question": "What is the Artemis program and what are its goals?",
        "explanation": "The Artemis program is NASA's initiative to return humans to the Moon, "
            "with the ultimate goal of establishing a sustainable presence on the lunar surface."
            " The program aims to land the first woman and the next man on the Moon by 2024 and to use the Moon"
            " as a stepping stone for future deep-space exploration, including potential missions to Mars."
    },

    "perseverance_rover_info": {
        "image": "https://science.nasa.gov/wp-content/uploads/2024/07/pia26344-2500x.jpg?w=2048&format=webp",
        "question": "What is the Perseverance rover and what is its mission on Mars?",
        "explanation": "The Perseverance rover is the latest Mars rover mission by NASA,"
            " launched in 2020. Its primary goals are to search for signs of ancient microbial life, "
            "characterize Mars' climate and geology, collect rock and soil samples for future return to Earth, "
            "and pave the way for human exploration of the Red Planet."
    },

    "parker_solar_probe_info": {
        "image": "https://science.nasa.gov/wp-content/uploads/2023/09/Parker_Solar_Probe_wisp-800x600-2.jpg?w=2048&format=webp",
        "question": "What is the Parker Solar Probe and what is its purpose?",
        "explanation": "The Parker Solar Probe is a NASA spacecraft launched in 2018 with the goal"
            " of studying the Sun and its corona, the outermost part of the Sun's atmosphere."
            " By making a series of close passes around the Sun, the probe aims to provide unprecedented"
            " insights into the solar wind, the Sun's magnetic fields, and the origins of solar energy."
    },

    "james_webb_telescope_launch_info": {
        "image": "https://live.staticflickr.com/65535/53389652523_77867aaf22_z.jpg",
        "question": "When was the James Webb Space Telescope launched and what was the launch process like?",
        "explanation": "The James Webb Space Telescope was launched on December 25, 2021, aboard "
        "an Ariane 5 rocket from the Guiana Space Center in French Guiana. The launch process was complex,"
        " as the telescope had to unfold and deploy its large mirror and sunshield in a carefully"
        " choreographed sequence after reaching orbit around the Sun at the second Lagrange point (C2L2)."
    }
}

help_img_url = 'https://media1.tenor.com/m/ozes7rBHiXcAAAAC/space-space-cat.gif'

HELPME = """
*/help* \- get all commands 
*/start* \- start message 
*/next* \- get random fact about space
*/cancel* \- cancel quiz or exit
*/rndimg* \- get random photo from NASA API
"""

# print(questions) 
# one line code to print beauty json 
# print(__import__('importlib').import_module('json').dumps(questions, indent=4))

# logging.debug(f"{bcolors.OKBLUE}ext start{bcolors.ENDC}")
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
