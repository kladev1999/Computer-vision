# Detect points that form a line
# lines = cv2.HoughLinesP(edge, 1, np.pi/180,255, minLineLength=10, maxLineGap=250)
# # Draw lines on the image
# for line in lines:
#     x1, y1, x2, y2 = line[0]
#     cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
# # Show result