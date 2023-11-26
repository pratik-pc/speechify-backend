
# SPEECHIFY

Speechify is a speech translation software developed in Python, designed to break down language barriers and enable seamless communication. Speechify empowers users to communicate effortlessly with people from different linguistic backgrounds.

## Software features

Speechify offers speech-to-speech translation, allowing users to speak naturally while the software translates their words into the chosen target language

Integration with Discord allowing users to stream translated audio to discord voice channel

## Software Interface

https://github.com/pratik-pc/speechify-backend/assets/33497322/97861eba-ba98-4a97-a102-5e7ab1ce6141

## Instructions

You can follow these instructions to setup the environment:

1. Clone this repo: `git clone https://github.com/pratik-pc/speechify-backend.git`
2. Run `pip install -r requirements.txt` in root directory
3. Create `.env` file and set the following variables
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION`
  - `S3_BUCKET_NAME`
  - `discord_token`
4. Run `flask run` in root directory
5. Run `python src\discord\websocket.py` & `python -m src.discord.discord_bot` in root directory
6. Speechify service is now running

## Related Repo

[Speechify GUI](https://github.com/pratik-pc/speechify)

## Need help or any suggestions?

Get in touch with me @ [twitter](https://twitter.com/Pratik24730644) or [linkedin](https://linkedin.com/in/pratik-chanda)
