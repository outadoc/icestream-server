from flask import Flask, abort, jsonify
from streamlink import NoPluginError, PluginError

from repository.live import InvalidServiceException, create_live
from repository.stream import get_stream_info

app = Flask(__name__)


@app.route('/api/v1/live/<service>/<channel>', methods=['GET'])
def get_live(service, channel):
    try:
        live = create_live(service, channel)
        streams = get_stream_info(live)
        if not streams:
            abort(404)
        return jsonify(streams)
    except InvalidServiceException:
        abort(400)
    except NoPluginError:
        abort(400)
    except PluginError:
        abort(500)


def create_app():
    return app


if __name__ == '__main__':
    app.run(debug=True)
