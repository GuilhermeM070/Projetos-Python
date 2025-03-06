from flask import Flask, request, jsonify
from pytubefix import YouTube
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/download", methods=["POST"])
def download():
    data = request.json
    url = data.get("url")
    download_type = data.get("type")

    if not url:
        return jsonify({"error": "URL do vídeo é obrigatória."}), 400

    try:
        yt = YouTube(url)
        
        if download_type == "video":
            stream = yt.streams.get_highest_resolution()
        else:
            stream = yt.streams.get_audio_only()
        
        filename = stream.download(DOWNLOAD_FOLDER)
        download_link = f"http://localhost:5000/{filename}"

        return jsonify({
            "title": yt.title,
            "thumbnail": yt.thumbnail_url,
            "downloadLink": download_link
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
