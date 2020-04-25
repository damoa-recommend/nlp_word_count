from flask import Flask
from app import get_recommendations, cosine_sim
import json

app = Flask(__name__)

@app.route("/")
def hello():               
  movie_name = "The Dark Knight Rises"            
  recommends = get_recommendations(movie_name, cosine_sim)
  return json.dumps(list(recommends))

if __name__ == "__main__":
  host_addr = "0.0.0.0"
  port_num = "8080"
  app.run(host=host_addr, port=port_num)