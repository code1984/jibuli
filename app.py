import os
import base64
import replicate
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # 启用跨域，让前端可调用

# 设置 Replicate API token
REPLICATE_API_TOKEN = "r8_2fahtf0CqEwhotkW9dfhGdcrlDiZO4J0oY8uB"
replicate.Client(api_token=REPLICATE_API_TOKEN)

@app.route("/generate", methods=["POST"])
def generate():
    # 获取上传的图像和文本 prompt
    image_file = request.files.get("image")
    prompt = request.form.get("prompt", "")

    if not image_file or not prompt:
        return jsonify({"error": "Missing image or prompt"}), 400

    # 将图像转成 base64
    image_bytes = image_file.read()
    image_base64 = "data:image/png;base64," + base64.b64encode(image_bytes).decode("utf-8")

    # 调用 Replicate 模型
    try:
        output = replicate.run(
            "fofr/ipadapter:ded3c6ef27d131683b6fb5197fe57a654edaa91c7bb2e75fb767e80b16357d64",
            input={
                "image": image_base64,
                "prompt": prompt,
                "adapter_type": "ipadapter",
            }
        )
        return jsonify({"image_url": output[0]})
    except replicate.exceptions.ReplicateError as e:
        return jsonify({"error": str(e)}), 500

# 启动服务器
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)