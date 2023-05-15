import numpy as np
import cv2

# Chessboard dimensions
chessboard_size = (9, 6)  # Number of inner corners (rows, columns)

# Criteria for corner detection
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Prepare object points
objp = np.zeros((np.prod(chessboard_size), 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

# Load the test image
img = cv2.imread('image3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find chessboard corners
ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

if ret:
    corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

    # Calibrate the camera using the detected corners
    obj_points = [objp]
    img_points = [corners]
    _, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

    # Print calibration results
    print("Camera matrix (K):")
    print(camera_matrix)
    print("Distortion coefficients:")
    print(dist_coeffs)

    # Pose estimation
    _, rvecs, tvecs = cv2.solvePnP(objp, corners, camera_matrix, dist_coeffs)
    rotation_matrix, _ = cv2.Rodrigues(rvecs)

    # AR overlay
    # Add your own code here to overlay your favorite number, character, etc.

    # Display the AR result
    cv2.imshow('AR Result', img)
    cv2.waitKey(0)
else:
    print("Chessboard corners not found in the image.")

cv2.destroyAllWindows()
