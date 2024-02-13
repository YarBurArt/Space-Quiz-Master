TOKEN = "REPLACE_THE_KEY"
DB_URL = "mongodb://localhost:27017"

questions = {
    "quriosity_meaning": {
        "image": "https://fsmedia.imgix.net/af/04/5e/78/1e19/4018/a6b9"
                 "/4bd2a4f25d09/the-mars-opportunity-rover-in-this-"
                 "artist-rendering.png?rect=0%2C0%2C2038%2C1019"
                 "&auto=format%2Ccompress&dpr=2&w=650",
        "question": "the meaning of Opportunity's Mars rover mission?",
        "explanation": "here's an explanation\n https://science.nasa.gov/mission/mer-opportunity/"
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
