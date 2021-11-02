from flask import Flask, request
from flask_restful import Api, Resource, reqparse , abort

app = Flask(__name__)
api = Api(app)

videoPutArgs = reqparse.RequestParser()
videoPutArgs.add_argument("name", type=str, help="Name of the video is required", required=True)
videoPutArgs.add_argument("views", type=int, help="Views of the video is required", required=True)
videoPutArgs.add_argument("likes", type=int, help="Likes of the video is required", required=True)

videos = {}

def abort_if_video_id_does_not_exist(video_id):
    if video_id not in videos:
        abort(404 , message="video id is not valid...")

def abort_if_exist(video_id):
    if video_id in videos:
        abort(404 , message= 'video already exists with that ID...')



class video(Resource):
    def get(self, video_id):
        abort_if_video_id_does_not_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_exist(video_id)
        args = videoPutArgs.parse_args()
        videos[video_id] = args
        return videos[video_id] , 201

    def delete(self,video_id):
        abort_if_video_id_does_not_exist(video_id)
        del videos[video_id]
        return '',204


api.add_resource(video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
