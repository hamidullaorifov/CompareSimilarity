import face_recognition

def get_face_embedding(image_path):
    
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    
    
    if len(face_locations) == 0:
        return None
    
    
    face_encodings = face_recognition.face_encodings(image, face_locations)
    return face_encodings[0] 

def calculate_similarity(embedding1, embedding2):
    
    if embedding1 is None or embedding2 is None:
        return None
    
    distance = face_recognition.face_distance([embedding1], embedding2)
    similarity_score = 1 - distance[0]
    return int(similarity_score*100)

# def main():
#     # Path to the images of the two people you want to compare
#     image_path_person1 = "path/to/person1.jpg"
#     image_path_person2 = "path/to/person2.jpg"
    
#     # Get the face embeddings for each person
#     embedding_person1 = get_face_embedding(image_path_person1)
#     embedding_person2 = get_face_embedding(image_path_person2)
    
#     if embedding_person1 is None or embedding_person2 is None:
#         print("Could not detect a face in one or both images.")
#         return
    
#     # Calculate the similarity score
#     similarity_score = calculate_similarity(embedding_person1, embedding_person2)
    
#     print(f"Similarity Score: {similarity_score:.2f}")