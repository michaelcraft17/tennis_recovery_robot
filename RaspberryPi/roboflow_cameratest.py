import cv2
import inference
import threading
import time


image_path = 'image.jpg'

#Load the model and get a prediction
model = inference.get_model(model_id = "tennis_ball-c7buz/1", api_key="l9eXl0psjHcWXHpsevfs")
results = model.infer(image=image_path)

capture = cv2.VideoCapture(0)

# Calculate where the tennis ball is on the image
x = results[0].predictions[0].x
y = results[0].predictions[0].y
is_thread_running = False

def drawBoxesOnTennisBalls(frame, predictions, timestamp, color = (255, 0, 0), thickness = 2):
    for prediction in predictions:
        x = prediction.x
        y = prediction.y
        
        width = prediction.width
        height = prediction.height
        
        x_1 = (x + (width // 2)) // 1
        x_0 = (x - (width // 2)) // 1
        
        y_1 = (y + (width // 2)) // 1
        y_0 = (y - (width // 2)) // 1
        
        x_0 = int(x_0)
        x_1 = int(x_1)
        y_0 = int(y_0)
        y_1 = int(y_1)
        
        start_point = (x_0, y_0)
        end_point = (x_1, y_1)
        
        
        # Draw a box around the tennis ball on the image
        frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
        
    filepath = str(timestamp) + ".jpg"
    cv2.imwrite(filepath, frame)
    
    
    
def getModelResults(frame):
    global is_thread_running, thread_count
    is_thread_running = True
    
    
    ts = time.time() // 1
    print()
    print ("Start Model", ts)
    image_path = "frame.jpg"
    cv2.imwrite(image_path, frame)
    results = model.infer(image=image_path)
    
    predictions = results[0].predictions
    if predictions:
        print("Tennis Ball count", len(predictions))
        drawBoxesOnTennisBalls(frame, predictions, ts)
    else:
        print("No predictions made")
        
        
    time.sleep(3)
    print("Finished Model", ts)
    print()
    
    is_thread_running = False
    
    
        
while (True):
    ret, frame = capture.read()
    cv2.imshow('video screen', frame)
    cv2.imwrite("pic.jpg", frame)
     
    #print("is thread running;", is_thread_running)
    if(not is_thread_running):
        t = threading.Thread(target=getModelResults, args=(frame, ))
        t.start()
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


capture.release()
cv2.destroyAllWindows()




