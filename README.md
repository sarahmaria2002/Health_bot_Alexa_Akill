# Health Bot Alexa Skill

## Topic
**Amazon Alexa Skill – Health Bot: Personalized Voice-Enabled Health Monitoring Skill**

An Alexa skill that delights users by providing health-related information and assistance. The Health Bot Alexa skill helps users manage medication reminders, retrieve information about symptoms, find nearby hospitals, and identify potential causes of symptoms.

## Introduction
Amazon Alexa, developed by Amazon.com, is a virtual assistant system known for its capabilities in voice commands, digital streaming, and e-commerce. Alexa can perform a wide range of tasks such as setting alarms, streaming music, and providing real-time information. With "skills," users can extend Alexa’s functionality, such as weather programs and audio features.

## Definition
Alexa skills are akin to apps, designed to enhance Alexa's functionality. These skills enable users to interact with Alexa through voice commands for tasks like listening to music, checking the news, or more specialized functions.

## Scope
This skill includes:
- A Voice User Interface (VUI) compatible with any Alexa device.
- 2 custom APIs deployed on AWS.
- 1 external API integration.

## Help
This project is developed in Python.
Please edit the API files as needed. 
You can always edit the dialogues as well.
Refer the master branch for code.

## Objective
The Health Bot Alexa skill aims to:
1. **Medication Management**: Manage medication reminders.
2. **Symptom Information**: Provide accurate information on symptoms.
3. **Hospital Locator**: Find nearby hospitals or medical facilities.
4. **Potential Causes Identification**: Analyze symptoms to identify potential health issues.
5. **User Assistance**: Offer guidance on skill usage.
6. **Convenience**: Provide accessible health information through Alexa.
7. **User Engagement**: Enhance interaction with intuitive responses.

## Pros and Cons

### Pros
1. **Convenience**: Hands-free access to health-related information.
2. **User Engagement**: Increases user engagement with voice-assisted tech.
3. **Medication Management**: Effective reminder system.
4. **Symptom Information**: Quick access to symptoms information.
5. **Hospital Locator**: Assists in finding medical facilities.
6. **Potential Causes Identification**: Helps identify potential health issues.
7. **User Assistance**: Provides clear guidance and support.

### Cons
1. **Hearing Issues**: Accents or pronunciation may cause misunderstanding.
2. **Processing Time**: Potential slow response times.
3. **Internet Dependence**: Requires internet connectivity for external APIs.
4. **Accuracy**: Potential inaccuracies in symptom analysis.
5. **Privacy Concerns**: User data privacy concerns.
6. **Limited Scope**: Restricted to predefined intents and APIs.
7. **Technical Issues**: Potential server or API errors.
8. **Learning Curve**: Users may need time to adapt to the skill.

## System Requirements

| SI.No | Requirement                 | Definition |
|-------|-----------------------------|------------|
| 1     | Laptop or Amazon Alexa Device | For testing and running the skill. |
| 2     | Alexa Console Account or Amazon Developer Account | Access to create or modify skills. |
| 3     | Testing Emulator             | Built-in simulator for testing. |
| 4     | Coding Platform - VS Code    | Platform for coding and API testing. |
| 5     | Microphone/Keyboard          | For skill testing. |
| 6     | Internet Connection          | Required for API access and Alexa communication. |
| 7     | CLI                         | For deploying APIs from local to EC2 instance. |

## Technical Requirements

| SI.No | Requirement                 | Definition |
|-------|-----------------------------|------------|
| 1     | Amazon Alexa Device or Simulator | For testing the skill. |
| 2     | Amazon Skills Kit (ASK)       | Set of tools and documentation for building Alexa Skills. |
| 3     | Amazon Developer Console      | For generating, maintaining, and deploying skills. |
| 4     | Python                       | Programming language used for code development. |
| 5     | APIs and API Keys             | Required for accessing external APIs. |
| 6     | AWS Tools                    | For managing and creating Alexa skills. |
| 7     | AWS Lambda                   | Serverless computing service for running backend code. |
| 8     | HTTP Requests                | For making requests to external APIs. |
| 9     | AWS Console                  | To access EC2. |
| 10    | EC2 Instance                 | For deploying APIs on a server. |

## Skill Components

1. **LaunchRequestHandler**: Responds to the skill launch and provides an overview.
2. **AddMedicineIntentHandler**: Handles adding medication reminders.
3. **GetRemindersIntentHandler**: Retrieves all medication reminders.
4. **DeleteMedicineIntentHandler**: Deletes a medicine from the reminder list.
5. **GetCausesIntentHandler**: Identifies potential causes of symptoms.
6. **GetHospitalIntentHandler**: Finds nearby hospitals.
7. **GetSymptomsIntentHandler**: Retrieves symptoms for a given disease.
8. **HelpIntentHandler**: Provides guidance on interacting with the skill.
9. **ThankYouIntentHandler**: Handles user gratitude or session end.
10. **CancelAndStopIntentHandler**: Handles requests to cancel or stop interactions.
11. **FallbackIntentHandler**: Handles unmatched user input.
12. **SessionEndedRequestHandler**: Manages the end of a session.
13. **IntentReflectorHandler**: Reflects the intent triggered by the user.
14. **CatchAllExceptionHandler**: Handles unexpected errors.

## External Dependencies

| SI. No | Name                    | Definition                              | Endpoint URL |
|--------|-------------------------|------------------------------------------|--------------|
| 1      | FastAPI Endpoint 1      | Fetches symptom information.             | ADD THE URL |
| 2      | FastAPI Endpoint 2      | Provides data about nearby hospitals.    | ADD THE URL |
| 3      | Symptom Checker API     | Analyzes symptoms and identifies causes. | https://symptom-checker4.p.rapidapi.com/analyze |

## Methodology
1. Open Alexa Developer Console.
2. Navigate to your skill and go to the test tab.
3. Invoke the skill with a phrase like "Start" or "open health bot."
4. Alexa will greet and ask what to do.
5. Users can add/delete/show reminders, inquire about symptoms, find hospitals, or identify causes of symptoms.
6. Alexa provides responses based on user requests.
7. Alexa will ask if further assistance is needed or end the session.

## Sample Conversation Between User and Alexa

- User: open health bot Alexa: Welcome to Health Bot. How can I assist you today? You can add medicines to your reminders or ask for symptoms of diseases. 
- User: remind me about crocin at eight p.m. every day 
- Alexa: I've added crocin to your reminders. Is there anything else I can help you with? 
- User: add paracetamol at nine p.m. to my reminders 
- Alexa: I've added paracetamol to your reminders. Is there anything else I can help you with? 
- User: what are my reminders 
- Alexa: Your current reminders are: crocin, paracetamol. Is there anything else I can help you with? 
- User: remove crocin from my reminders 
- Alexa: I've removed crocin from your reminders. Is there anything else I can assist you with? 
- User: list my reminders 
- Alexa: Your current reminders are: paracetamol. Is there anything else I can help you with? 
- User: what are the symptoms of pneumonia 
- Alexa: The symptoms of pneumonia are high fever, chills, cough with phlegm, chest pain, difficulty breathing. Is there anything else I can assist you with? 
- User: what are the symptoms of arthritis 
- Alexa: The symptoms of arthritis are joint pain, stiffness, swelling, decreased range of motion. Is there anything else I can assist you with? 
- User: locate the nearest hospital 
- Alexa: Here are some hospitals you can visit: Global Hospitals, Sri Ramachandra Medical Centre, Frontier Lifeline Hospital. Is there anything else I can assist you with? 
- User: why am I having a severe headache 
- Alexa: The analysis is as follows: The potential causes are: Migraine, Tension headache, Cluster headache, Sinusitis, Brain tumor. Is there anything else I can help you with? 
- User: can you tell me the cause of skin rashes 
- Alexa: The analysis is as follows: The potential causes are: Contact dermatitis, Eczema, Psoriasis, Allergic reaction, Rosacea. Is there anything else I can help you with?
- User: no that's it 
- Alexa: You're welcome! Goodbye.


## References
1. [Wikipedia - Amazon Alexa](https://en.wikipedia.org/wiki/Amazon_Alexa)
2. [Amazon Alexa Skills Kit Documentation](https://developer.amazon.com/en-US/docs/alexa/ask-overviews/what-is-the-alexa-skills-kit.html)
3. [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
4. [FastAPI Documentation](https://fastapi.tiangolo.com/)
5. [Amazon Developer Console](https://developer.amazon.com/alexa/console/ask)
