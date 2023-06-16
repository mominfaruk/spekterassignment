from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import pipeline
from setfit import SetFitModel


# Download from Hub and run inference
model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
# Run inference


@api_view(['POST'])
def analyze_sentiment(request):
    try:
        text = request.data.get('text')

        if text:
            # Perform sentiment analysis on the provided text
            result = model.predict([text])[0]

            # positie negative and neutral based on the result
            if result == 0:
                sentiment = "Negative"
            elif result == 1:
                sentiment = "Positive"
            else:
                sentiment = "Neutral"
              
            # Return the sentiment analysis result as a JSON response
            return Response({
                'sentiment': sentiment,
            })

        return Response({
            'error': 'Invalid request payload. "text" field is missing.'
        }, status=400)

    except Exception as e:
        return Response({
            'error': 'An error occurred while analyzing sentiment.'
        }, status=500)
