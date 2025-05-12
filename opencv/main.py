import cv2
for ra in range(1,5):
  y_c = 0
  m_c = 0
  w_c = 0
  card = cv2.imread(f"pic{ra}.jpg")
  w, h, _ = card.shape
  for i in range(1,w,5):
    for j in range(1,h,5):
      b,g,r = card[i,j]
      if r and g and  b >= 200:
        w_c = w_c + 1
      elif r and g >= 200:
        y_c = y_c + 1
      elif r and b >=130:
        m_c = m_c + 1
  result = "Magenta" if m_c>=y_c else "Yellow"
  result_m = "ゴルフ" if m_c<=5000 else"テニス"
  result_y = "ゴルフ" if y_c<=5000 else"テニス"
  print(f"pic{ra}:{result}:{result_m if result=="Magenta" else result_y}")