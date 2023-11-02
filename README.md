# API for Symptom Logger

A microservice to communicate with my client endpoint using json, to receive symptom data and return a summary of that data.

Features:
- Activity Log
- Testing
- CI/CD github workflow to run tests on pull request

Creating a microservice for summarization allows me to update and improve it (like adding AI or using NLTK) without affecting the client app.
![Web Sequence Diagram](./slmicroservicewsd.png)