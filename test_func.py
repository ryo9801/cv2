import cv2
def read(Yellow,Magenta,B_Yellow,L_Yellow,B_Magenta,L_Magenta,modecerecter):
  
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
    Y_c = 0
    M_c = 0
    W_c = 0
    w, h, _ = frame.shape
    for i in range(1,w,10):
      for j in range(1,h,10):
        b,g,r = frame[i,j]
        if not modecerecter :
          print(f"r={r}:g={g}:b={b}") #この値を基に引数Yellow,Magentaの値を決める
        if r and g >= Yellow:
          Y_c = Y_c + 1
        if g and b >= Magenta:
          M_c = M_c + 1
    result = "Yellow" if Y_c>M_c else "Magenta"
    F_result = None
    if result == "Magenta" :
      Y_c = 0  
    else : 
      M_c = 0
    if  L_Yellow < Y_c < B_Yellow :
      F_result = "L_Yellow" 
    elif B_Yellow < Y_c :
      F_result = "B_Yellow"
    if  L_Magenta <= M_c < B_Magenta:
      F_result = "L_Magenta"
    elif  B_Magenta < M_c :
      F_result ="B_Magenta"
    if modecerecter :
      print(result,f"Yellow:{Y_c}:Magenta:{M_c}")     
      print(F_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  cap.release()
  cv2.destroyAllWindows()