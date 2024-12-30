from flask import Flask, Response

app = Flask(__name__)

# Correct file path to your MP4
file_path = r"D:\Movies\DC\hey.bin"

@app.route('/str')
def stream_video():
    def generate():
        with open(file_path, "rb") as video_file:
            chunk_size = 2000 * 2000  # 1MB chunks
            while chunk := video_file.read(chunk_size):
                yield chunk

    return Response(
        generate(),
        content_type="video/mp4",
        headers={
            "Content-Disposition": "inline; filename='video.mp4'",
        }
    )

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True, host='127.0.0.1', port=5000)
