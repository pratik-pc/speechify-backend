from flask.views import MethodView

class Translation(MethodView):
  def get(self):
    return "Translation route"