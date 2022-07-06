# BookTrip chatbot
## Background
The BookTrip chatbot is a mock chatbot built on [AWS Lex V2](https://aws.amazon.com/lex/) as a learning exercise.

The intent is to build a chatbot which allows customers to book flights, hotel and rental car. A lambda function is used to improve the experience, for example by retaining the destination city from the booking of one service (intent) for prepopulating in the appropriate slot in other intents. Other examples include handling situations where a booking is requested for the past, a flight is requested with destination city the same as the origin city.

Some difficulty has been encountered, for example where sending a "Delegate" `dialogAction` response, the next action taken by the chatbot is not the action specified in the `proposedNextState`. Very frustrating.

## How to use it
Say hello, then have a conversation!
