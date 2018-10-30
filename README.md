# How to Use
1. Create a new IFTTT applet with "Webhook" as the trigger
2. Use a "Rich Notification" as the action service (or do what you want, but this is how I've set it up):
  - Title: `Snow Tomorrow!`
  - Message: `Might want to bring your laptop home! Here's the details: {{Value1}}`
3. Get the webhook URL by clicking the "Documentation" button on this page: https://ifttt.com/maker_webhooks
4. Get an API key from https://OpenWeatherMap.org
5. Create a new AWS Lambda python function and upload the snow_tmrw.zip (available in repo and in releases tab)
6. Enter the `OPEN_WEATHER_MAP_API_KEY` and `IFTTT_URL` env vars for the Lambda function
7. Setup whatever triggers you like for the lambda function. I like to use a CloudWatch cron job to run at 4pm on weekdays.
