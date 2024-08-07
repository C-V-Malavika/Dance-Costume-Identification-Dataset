from rembg import remove
import cv2

input_path = 'Dataset_Test_with_Background/Bharatanatyam/Bharatanatyam-1.png'
output_path = 'Dataset_Test_without_Background/Bharatanatyam/Bharatanatyam-1.png'
    
input = cv2.imread(input_path)
output = remove(input)
cv2.imwrite(output_path, output)