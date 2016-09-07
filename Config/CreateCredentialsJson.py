import json

# ADD YOUR CREDENTIALS IN HERE, ENSURE YOU ADD YOUR CREDENTIALS TO THE CORRECT
# REGION. USE CORRECT SYNTAX - SEE EXAMPLE BELOW:

# NLC = {
#     "url": "https://stream.watsonplatform.net/speech-to-text/api",
#     "password": "xxxxxxxxxxx",
#     "username": "xxxxxxxxxx-xxxxxxxxxxx-xxxxxxxxxx-xxxxxxxxxxx"
# }
# VR = {
#     "url": "https://gateway-a.watsonplatform.net/visual-recognition/api",
#     "api_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
#     "version": '2016-05-20'
# }

# Australia credentials
AusNLC = {
}
AusSpeechToText = {
}
AusVR = {
}
AusConversation = {
}
# US South credentials
USNLC = {
}
USConversation = {
}
USSpeechToText = {
}
USVR = {
}

#~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-~ ~-#
# DO NOT MODIFY CODE BELOW THIS LINE


Australia = {
"NLC": AusNLC,
"Conversation": AusConversation,
"SpeechToText": AusSpeechToText,
"VisualRecognition": AusVR
}
USSouth = {
"NLC": USNLC,
"Conversation": USConversation,
"SpeechToText": USSpeechToText,
"VisualRecognition": USVR
}

data = {}
data["region"] = {}
data["region"]["Australia"] = {}
data["region"]["US South"] = {}

data["region"]["Australia"] = Australia
data["region"]["US South"] = USSouth

with open('credentials.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)

with open('credentials.json') as outfile:
    print json.dumps(json.load(outfile), indent=2, sort_keys=True)

print "Credentials saved."
