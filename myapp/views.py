import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDataSerializer

class UserDataView(APIView):
    
    def post(self, request):
        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            
            name = serializer.validated_data['name']
            address = serializer.validated_data['address']
            contact = serializer.validated_data['contact']
            email = serializer.validated_data['email']

            try:
               
                SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
                SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'credentials.json')
                credentials = service_account.Credentials.from_service_account_file(
                    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

                service = build('sheets', 'v4', credentials=credentials)

                
                SPREADSHEET_ID = '1VPeMtJvutbxVIdGx2MuK2ubjkBH4De5Qum08P-I4Vq8'  
                RANGE_NAME = 'Sheet1!A:D'  

               
                values = [[name, address, contact, email]]
                body = {
                    'values': values
                }

                result = service.spreadsheets().values().append(
                    spreadsheetId=SPREADSHEET_ID,
                    range=RANGE_NAME,
                    valueInputOption='RAW',
                    body=body
                ).execute()

                return Response({"message": "Data added successfully!", "updatedCells": result.get('updates', {}).get('updatedCells')}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

