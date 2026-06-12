import whisper
import json

model = whisper.load_model("large-v2")

result = model.transcribe(audio = "audio/14_Setting Alias In Git .mp3",
                          language = "hi",
                          task = "translate")

print(result)
# with open("output.json", "w") as f:
#     json.dump(f, result)