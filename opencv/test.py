import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("カメラが見つかりません")
    exit()

while True:
  ret, frame = cap.read()
  if not ret:
    print("フレームの取得に失敗しました")
    break
  cv2.imshow('USB Camera', frame)
  y_c = 0
  m_c = 0
  w_c = 0
  w, h, _ = frame.shape
  for i in range(1,w,1):
    for j in range(1,h,1):
      b,g,r = frame[i,j]
    if r and g and  b >= 200:
      w_c = w_c + 1
    elif r and g >= 130:
      y_c = y_c + 1
    elif r and b >= 85:
      m_c = m_c + 1
  result = "yellow" if y_c>m_c else "magenta"
  if result == "magenta":
    y_c = y_c + w_c  
  else:
    m_c = m_c + w_c
  f_result = "yellow" if y_c>m_c else "magenta"
  print(f_result,f"yellow:{y_c}magenta:{m_c}")
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()