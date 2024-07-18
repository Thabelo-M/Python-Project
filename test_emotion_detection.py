from EmotionDetection import emotion_detector

def test_emotion(statement, expected_emotion):
    result = emotion_detector(statement)
    dominant_emotion = result['dominant_emotion']
    assert dominant_emotion == expected_emotion, f"Expected dominant emotion {expected_emotion}, but got {dominant_emotion}"

# Test cases
test_emotion("I am glad this happened", "joy")
test_emotion("I am really mad about this", "anger")
test_emotion("I feel disgusted just hearing about this", "disgust")
test_emotion("I am so sad about this", "sadness")
test_emotion("I am really afraid that this will happen", "fear")

print("All tests passed!")