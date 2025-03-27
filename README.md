# Jibuli - Ghibli Style Image Generator

A web application that transforms your images into Ghibli-inspired artwork using AI.

## Features

- Upload your images and transform them into Ghibli style
- Add custom scene descriptions to guide the transformation
- Powered by Replicate's AI model

## Tech Stack

- **Backend**: Flask (Python)
- **AI Model**: fofr/ipadapter on Replicate

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your environment variables in `.env`:
   ```
   REPLICATE_API_TOKEN=your_token_here
   ```
4. Run the application:
   ```
   python app.py
   ```
   
## API Endpoints

- `POST /generate` - Generate a Ghibli-style image
  - Request: Multipart form with `image` file and `prompt` text
  - Response: JSON with `image_url` of the generated image

## License

MIT 