from .generic_detector import GenericFaceDetector, default_upsampling

class DLibFaceDetector(GenericFaceDetector):

  def __init__(self):
    import dlib
    self.detector = dlib.get_frontal_face_detector()

  # v1 without score. Deprecated
  # def detect_from_img_noscore(self, img, up_sample=default_upsampling):
  #   return [{
  #     "left": d.left(),
  #     "top": d.top(),
  #     "right": d.right(),
  #     "bottom": d.bottom()
  #   } for d in self.detector(img, up_sample)]

  def detect_from_img(self, img, up_sample=default_upsampling):
    dets, scores, idx = self.detector.run(img, up_sample, 0)
    return [{
      "left": d.left(),
      "top": d.top(),
      "right": d.right(),
      "bottom": d.bottom(),
      "score": scores[i]
    } for i, d in enumerate(dets)]
