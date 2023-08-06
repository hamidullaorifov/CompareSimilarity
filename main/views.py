
from .serializers import RequestSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
import logging
from datetime import datetime
# from .utils import get_face_embedding,calculate_similarity




logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def write_log_file(message):
    with open('logs.txt','a') as f:
        f.write(f'{datetime.now()} | {message}\n')







from deepface import DeepFace
class CompareView(APIView):
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
    

    @swagger_auto_schema(request_body=RequestSerializer)
    def post(self, request, format=None):
        user = request.user
        data = request.data
        try:
            percentage = int(data.get('percentage'))
        except:
            raise ValidationError("Enter valid percentage")
        # Decode base64 images and save them as temporary files
        image1_base64 = data.get('image1', '')
        image2_base64 = data.get('image2', '')
        
        image1 = f'data:image/jpeg;base64,{image1_base64}'
        image2 = f'data:image/jpeg;base64,{image2_base64}'
        
        try:
            verification = DeepFace.verify(image1,image2)
            similarity = int(100*(1 - verification['distance']))
            if similarity >= percentage:
                response_data = {
                    'code':1,
                    'details':"The provided images belong to the same person.",
                    'result':'success',
                    'similarity':similarity
                    }
            else:
                response_data = {
                    'code':2,
                    'details':"The provided images do not belong to the same person.",
                    'result':'fail',
                    'similarity':similarity
                    }
        except ValueError:
            response_data = {
                'code':3,
                'details':"No Face in the Image",
                'result':'fail',
                'similarity':0
                }
            
        except Exception as e:
            response_data = {
                'code':4,
                'details':f"{e}",
                'result':'fail',
                'similarity':0
                }
        
        

        
        logger.info(f'request method: POST, username:{user.username},{response_data}')
        return Response(data=response_data)
    



































# class CompareView(APIView):
    # serializer_class = RequestSerializer
    # permission_classes = [IsAuthenticated]
    # parser_classes = (MultiPartParser,)

    # @swagger_auto_schema(request_body=RequestSerializer)
    # def post(self, request, format=None):
    #     user = request.user
    #     data = request.data

    #     # Decode base64 images and save them as temporary files
    #     image1_base64 = data.get('image1', '')
    #     image2_base64 = data.get('image2', '')


    #     if not image1_base64.startswith('data:image') or not image2_base64.startswith('data:image'):
    #         raise ValidationError("Invalid image format. Only base64-encoded images are supported.")


    #     image1 = self.decode_base64_and_save(image1_base64,'image1')
    #     image2 = self.decode_base64_and_save(image2_base64,'image2')

    #     # serializer = RequestSerializer(data=data)
    #     # if serializer.is_valid():
    #     #     print("valid")

    #     # Rest of your existing code...
    #     embedding_person1 = get_face_embedding(image1)
    #     embedding_person2 = get_face_embedding(image2)
    #     # ... (remaining code)
    #     if not embedding_person1 or not embedding_person2:
    #         response_data = {
    #             'code':3,
    #             'details':"No Face in the Image",
    #             'result':'fail'
    #             }
    #         logger.info(f'request method: POST, username:{user.username},{response_data}')
    #         return Response(data=response_data)
    #     similarity_score = calculate_similarity(embedding_person1, embedding_person2)
    #     try:
    #         percentage = int(data.get('percentage'))
    #     except:
    #         raise ValidationError("Enter valid percentage")
        
    #     if similarity_score >= percentage:
    #         response_data = {
    #             'code':1,
    #             'details':"The provided images belong to the same person.",
    #             'result':'success'
    #             }
    #         logger.info(f'request method: POST, username:{user.username},{response_data}')
    #         return Response(data={'message':'success'})
        

    #     response_data = {
    #             'code':2,
    #             'details':"The provided images do not belong to the same person.",
    #             'result':'fail'
    #             }
        
    #     logger.info(f'request method: POST, username:{user.username},{response_data}')
        



    #     # Clean up the temporary files
    #     self.cleanup_temporary_files(image1)
    #     self.cleanup_temporary_files(image2)
    #     return Response(data=response_data) 
    #     # The rest of your existing code...

    # def decode_base64_and_save(self, base64_string,name):
    #     try:
    #         # format, imgstr = base64_string.split(';base64,')
    #         # ext = format.split('/')[-1]
    #         ext = 'jpg'
    #         image = ContentFile(base64.b64decode(base64_string), name=f"temp{name}.{ext}")
    #         return image
    #     except Exception as e:
    #         raise ValidationError("Invalid base64 image data.")

    # def cleanup_temporary_files(self, image):
    #     if image and hasattr(image, 'path') and image.path:
    #         image.close()
    #         image.delete(save=False)


# class CompareView(APIView):
#     serializer_class = RequestSerializer
#     permission_classes = [IsAuthenticated]
#     parser_classes = (MultiPartParser,)
#     @swagger_auto_schema(request_body=RequestSerializer)
#     def post(self,request,format=None):
#         user = request.user
#         data = request.data
#         serializer = RequestSerializer(data=data)
#         if serializer.is_valid():
#             print("valid")
#         embedding_person1 = get_face_embedding(data.get('image1'))
#         embedding_person2 = get_face_embedding(data.get('image2'))

    
#         if embedding_person1 is None or embedding_person2 is None:
#             raise ValidationError("Choose valid files")
        
    

#         similarity_score = calculate_similarity(embedding_person1, embedding_person2)
#         percentage = data.get('percentage')

#         if similarity_score >= percentage:
#             logger.info(f'request method: POST, username:{user.username},status: success')
#             return Response(data={'message':'success'})
        


#             write_log_file(f'request method: POST, username:{user.username},status: fail')
#             logger.info(f'request method: POST, username:{user.username},status: fail')
#         return Response(data={'message':'fail'}) 