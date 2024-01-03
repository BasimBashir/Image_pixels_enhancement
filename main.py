# from skimage import io, filters, img_as_ubyte  # Import img_as_ubyte
#
# # Load your custom image "image1.jpg"
# image = io.imread("image1.jpg")
#
# # Apply the un-sharp mask filter with different parameters
# result_1 = filters.unsharp_mask(image, radius=1, amount=1)
# result_2 = filters.unsharp_mask(image, radius=5, amount=5)  # amount=2 original
# result_3 = filters.unsharp_mask(image, radius=20, amount=1)
#
# # Convert the images to uint8 format before saving
# result_1 = img_as_ubyte(result_1)
# result_2 = img_as_ubyte(result_2)
# result_3 = img_as_ubyte(result_3)
#
# # Save the original image
# io.imsave("original_image.jpg", image)
#
# # Save the enhanced images
# io.imsave("enhanced_image_1.jpg", result_1)
# io.imsave("enhanced_image_2.jpg", result_2)
# io.imsave("enhanced_image_3.jpg", result_3)


from skimage import io, filters
import cv2

# Open the video file
video_capture = cv2.VideoCapture("test_video.mov")

while True:
    ret, frame = video_capture.read()

    if not ret:
        break  # Break the loop when the video ends

    # Apply the un-sharp mask filter with different parameters
    result = filters.unsharp_mask(frame, radius=5, amount=5)  # You can adjust radius and amount

    # Show the processed frame
    cv2.imshow("Un-sharp Masked Frame", result)

    # Check for user input to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video object and close the OpenCV window
video_capture.release()
cv2.destroyAllWindows()

