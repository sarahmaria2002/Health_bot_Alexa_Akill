import ask_sdk_core.utils as ask_utils
import logging
import random
import requests
import boto3

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

medication_reminders = []

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speak_output = "Welcome to Health Bot. How can I assist you today? You can add medicines to your reminders or ask for symptoms of diseases."
        reprompt_output = "You can ask me questions about health or request information on specific topics."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_output)
                .response
        )

#add medicine to reminder
class AddMedicineIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AddMedicineIntent")(handler_input)

    def handle(self, handler_input):
        medicine = handler_input.request_envelope.request.intent.slots["medicine"].value
        medication_reminders.append(medicine)

        speak_output = f"I've added {medicine} to your reminders."
        reprompt_output = ".Is there anything else I can help you with?"
        speak_output = speak_output + reprompt_output
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_output)
                .response
        )


#delete medicine from reminders
class DeleteMedicineIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("DeleteMedicineIntent")(handler_input)

    def handle(self, handler_input):
        medicine = handler_input.request_envelope.request.intent.slots.get('medicine').value
        reprompt_output = "Is there anything else I can assist you with?"
        
        if medicine in medication_reminders:
            medication_reminders.remove(medicine)
            speak_output = f"I've removed {medicine} from your reminders."
        else:
            speak_output = f"{medicine} was not found in your reminders."
        
        speak_output += " " + reprompt_output
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_output)
                .response
        )
    
#to show all reminders
class GetRemindersIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("GetRemindersIntent")(handler_input)

    def handle(self, handler_input):
        reprompt_output = ".Is there anything else I can help you with?"
        
        if not medication_reminders:
            speak_output = "You don't have any reminders."
        else:
            reminders = ', '.join(medication_reminders)
            speak_output = f"Your current reminders are: {reminders}"

        speak_output = speak_output + reprompt_output
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_output)
                .response
        )

# #to say a disease and know its symptoms
class GetSymptomsIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("GetSymptomsIntent")(handler_input)

    def handle(self, handler_input):
        reprompt_output = ". Is there anything else I can assist you with?"
        disease = handler_input.request_envelope.request.intent.slots['disease'].value.lower()
        
        # Make HTTP GET request to FastAPI endpoint
	# Add your API URL
        fastapi_url = ""  
        response = requests.get(f"{fastapi_url}{disease}")
        
        if response.status_code == 200:
            data = response.json()
            if "symptoms" in data:
                speak_output = f"The symptoms of {disease} are {data['symptoms']}."
            else:
                speak_output = f"I'm sorry, I don't have information on {disease}."
        else:
            speak_output = "There was a problem retrieving information. Please try again later."
        
        speak_output = speak_output + reprompt_output
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_output)
                .response
        )

    
# to know nearby hospitals
class GetHospitalIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (
            handler_input.request_envelope.request.intent.name == "GetHospitalIntent" or
            handler_input.request_envelope.request.intent.name == "AMAZON.NavigateHomeIntent" or
            (handler_input.request_envelope.request.intent.name == "AMAZON.YesIntent" and
             'GetHospitalIntent' in handler_input.attributes_manager.session_attributes)
        )

    def handle(self, handler_input):
        try:
            # Make HTTP GET request to FastAPI endpoint
	    # Add your API URL
            api_url = ""
            response = requests.get(api_url)
            
            if response.status_code == 200:
                hospitals_data = response.json()
                
                # Get a random selection of 3 hospitals
                random_hospitals = random.sample(list(hospitals_data.keys()), k=min(3, len(hospitals_data)))
                
                # Construct the response
                speak_output = "Here are some hospitals you can visit:\n"
                for hospital_name in random_hospitals:
                    hospital_address = hospitals_data[hospital_name]
                    speak_output += f"{hospital_name}, located at {hospital_address}\n"
            else:
                speak_output = "There was a problem retrieving hospital information. Please try again later."
        except Exception as e:
            speak_output = "There was a problem processing your request. Please try again later."
            print(e)
        
        reprompt_output = ". Is there anything else I can assist you with?"
        speak_output += reprompt_output

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_output)
                .response
        )


#to say some some symptoms and know the potential causes / diseases
class GetCausesIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("GetCausesIntent")(handler_input)

    def handle(self, handler_input: HandlerInput):
        reprompt_output = "Is there anything else I can help you with?"

        speak_output = ""
        
        # Extract symptoms from the user input
        symptoms = handler_input.request_envelope.request.intent.slots.get("symptoms").value
        
        print("Extracted symptoms:", symptoms)  # Add this line for debugging
        
        # Define the API endpoint and headers
        url = "https://symptom-checker4.p.rapidapi.com/analyze"
        # Add your API key (go to RapidAPI and get the key for this API)
        headers ={
            'X-RapidAPI-Key': '',
            'X-RapidAPI-Host': 'symptom-checker4.p.rapidapi.com'
        }
        
        # Prepare the data payload
        data = {
            'symptoms': symptoms
        }
        
        try:
            # Make a POST request to the API
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            
            print("API Response:", result)  # Add this line for debugging
            
            # Extract potential causes from the API response
            potential_causes = result.get('potentialCauses', [])
            if potential_causes:
                potential_causes_str = ", ".join(potential_causes)
                speak_output += f"The potential causes are: {potential_causes_str}\n"
            
            speak_output = "The analysis is as follows:\n" + speak_output
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            speak_output = "There was an error fetching the data. Please try again later."

        # Construct the final response
        final_output = speak_output + " " + reprompt_output
        return (
            handler_input.response_builder
                .speak(final_output)
                .ask(reprompt_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "You can add medicines to your reminders or ask for symptoms of diseases. How can I assist you?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        speak_output = "Goodbye! Stay healthy and Thank you for using Health Bot."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Sorry, I couldn't understand that. How can I assist you?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

#stopping 
class ThankYouIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_intent_name("ThankYouIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.NoIntent")(handler_input))

    def handle(self, handler_input):
        speak_output = "You're welcome! Goodbye."
        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(True)  # End the session
                .response
        )

class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.response

class IntentReflectorHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )
    
    
class CatchAllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I couldn't understand that. Can you please repeat?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(AddMedicineIntentHandler())
sb.add_request_handler(GetRemindersIntentHandler())
sb.add_request_handler(DeleteMedicineIntentHandler())
sb.add_request_handler(GetCausesIntentHandler())
sb.add_request_handler(GetHospitalIntentHandler())
sb.add_request_handler(GetSymptomsIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(ThankYouIntentHandler())
sb.add_request_handler(CancelAndStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
