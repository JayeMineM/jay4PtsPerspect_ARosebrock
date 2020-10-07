def four_point_transform(image, pts): #Line_28
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts) #Line_31
	(tl, tr, br, bl) = rect #Line_32

	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left x-coordinates 
  # or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2)) #Line_37 #JayN# br(x,y)=(br[0],br[1]) 
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2)) #Line_38 #JayN# tl(x,y)=(tl[0],tl[1])
	maxWidth = max(int(widthA), int(widthB)) #Line_39
 
	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2)) #Line_44
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2)) #Line_45
	maxHeight = max(int(heightA), int(heightB)) #Line_46
 
	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left order
	# Line_53-57
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
 
	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst) #Line_60
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight)) #Line_61
 
	# return the warped image
	return warped #Line_64