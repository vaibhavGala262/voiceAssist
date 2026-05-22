# voiceAssist

Hindi + Telugu Voice Bot — single HTML file, zero backend needed.

- **STT**: Browser webkitSpeechRecognition (hi-IN)
- **AI**: Groq API (Llama 3.3 70B)
- **TTS**: Browser SpeechSynthesis

## Deploy on GitHub Pages

1. Push this repo to GitHub
2. Go to repo **Settings → Pages**
3. Under "Branch", select `main` / `root`
4. Save — your bot is live at `https://<user>.github.io/<repo>/`

No server, no build step. Just open the URL, paste your Groq API key, and use the mic.
