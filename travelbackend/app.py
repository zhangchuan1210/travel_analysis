from flask import Flask
from config import Config
from extensions import db
def create_app():
# 初始化 Flask 应用和配置
  app = Flask(__name__)
  app.config.from_object(Config)

# 初始化数据库
  db.init_app(app)
# 注册控制器
#  from .controllers.hotspot import hotspot_blueprint
#  from .controllers.recommend import recommend_blueprint
#  from .controllers.tickets import tickets_blueprint
#  from .controllers.word_count import word_count_blueprint
  from controllers.travel_controller import scraper_bp

#  app.register_blueprint(hotspot_blueprint)
#  app.register_blueprint(recommend_blueprint)
#  app.register_blueprint(tickets_blueprint)
#  app.register_blueprint(word_count_blueprint)

  app.register_blueprint(scraper_bp)
  return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

