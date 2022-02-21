from main import *

# IMAGE ARUGMENTATION
# ///////////////////////////////////////////////////////////////
def letterbox(img, 
              new_shape=(640, 640), 
              color=(114, 114, 114), 
              auto=True, scaleFill=False, 
              scaleup=True):
    shape = img.shape[:2]  # current shape [height, width]当前范围的高和宽
    if isinstance(new_shape, int):#看看类型是不是int类型
        new_shape = (new_shape, new_shape)#这是进行了元组的合并，也就是有四个元素
    #scaleup = 按比例扩大的意思
    # Scale ratio (new / old)
    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
    if not scaleup:  # only scale down, do not scale up (for better test mAP)
        r = min(r, 1.0)

    # Compute padding （计算填充）
    ratio = r, r  # width, height ratios #宽度和高度分别的Ratio
    new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))#round是四舍五入
    dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding
    if auto:  # minimum rectangle
        dw, dh = np.mod(dw, 32), np.mod(dh, 32)  # wh padding
    elif scaleFill:  # stretch
        dw, dh = 0.0, 0.0
        new_unpad = (new_shape[1], new_shape[0])
        ratio = new_shape[1] / shape[1], new_shape[0] / shape[0]  # width, height ratios

    dw /= 2  # divide padding into 2 sides
    dh /= 2

    if shape[::-1] != new_unpad:  # resize
        img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_LINEAR)
    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
    return img, ratio, (dw, dh)
