# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from typing import Text,Dict,Any,List
from rasa_sdk import Action, Tracker
import pandas as pd
import re
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionFQA(Action):

     def name(self) -> Text:
         return "action_faq"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

     #def ActionFetch(tracker: Tracker):
        dataframe = pd.read_csv('qna.csv')
        detected_intent = tracker.latest_message['intent'].get('name')
        #print("detected intent",tracker.latest_message['intent'].get('name'))
        answer = dataframe.loc[dataframe['intent'] == detected_intent]['Answer']
        print('answer',answer)
        print('answer item' , answer.item())
        dispatcher.utter_message(text= answer.item())

        return []

    
