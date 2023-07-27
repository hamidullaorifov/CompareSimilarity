
from .serializers import RequestSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
import logging
from .utils import get_face_embedding,calculate_similarity





logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class CompareView(APIView):
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)
    @swagger_auto_schema(request_body=RequestSerializer)
    def post(self,request,format=None):
        user = request.user
        data = request.data
        embedding_person1 = get_face_embedding(data.get('image1'))
        embedding_person2 = get_face_embedding(data.get('image2'))

    
        if embedding_person1 is None or embedding_person2 is None:
            raise ValidationError("Choose valid files")
        
    

        similarity_score = calculate_similarity(embedding_person1, embedding_person2)
        percentage = data.get('percentage')

        if similarity_score >= percentage:
            logger.info(f'request method: POST, username:{user.username},status: success')
            return Response(data={'message':'success'})
        



        logger.info(f'request method: POST, username:{user.username},status: fail')
        return Response(data={'message':'fail'}) 


