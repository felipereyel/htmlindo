import flask
import forms
import flask_sock


def main() -> flask.Flask:
    app = flask.Flask(__name__)
    sock = flask_sock.Sock(app)

    @sock.route("/ws")
    def _ws(ws: flask_sock.Server):
        try:
            id = flask.request.args.get("id", "root")
            form = forms.find(id)
            if not form:
                return

            form.run(ws)
        finally:
            ws.close(message="Done")

    @app.get("/")
    def index():
        return flask.send_from_directory("statics", "index.html")

    app.run(host="0.0.0.0", port=5555)


if __name__ == "__main__":
    main()
