import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "jokes-ubcy-d57743ed8e79.json"

import dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "jokes-ubcy"


def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result


def fetch_reply(query,session_id):
	response = detect_intent_from_text(query,session_id)
