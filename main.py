from flask import Flask, abort, jsonify

from repository.live import InvalidServiceException, create_live
from repository.stream import get_stream_info

app = Flask(__name__)


@app.route('/api/v1/live/<service>/<channel>', methods=['GET'])
def get_live(service, channel):
    try:
        live = create_live(service, channel)
        streams = get_stream_info(live)
        return jsonify(streams)
    except InvalidServiceException:
        abort(400)


def create_app():
    return app


if __name__ == '__main__':
    app.run(debug=True)
